from cha_bebe.carrinho.models import ItemCarrinho # cart.models import CartItem
from cha_bebe.presente.models import Presente #ecomstore.catalog.models import Product
from cha_bebe import settings

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Max

from datetime import datetime, timedelta
import decimal
import random

CARRINHO_ID_SESSION_KEY = 'id_carrinho'

def _id_carrinho(request):
    if request.session.get(CARRINHO_ID_SESSION_KEY,'') == '':
        request.session[CARRINHO_ID_SESSION_KEY] = _gerar_id_carrinho()
    return request.session[CARRINHO_ID_SESSION_KEY]

def _gerar_id_carrinho():
    """ função para gerar ID de carrinhos aleatórios  """
    id_carrinho = ''
    caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
    id_carrinho_length = 50
    for y in range(id_carrinho_length):
        id_carrinho += caracteres[random.randint(0, len(caracteres)-1)]
    return id_carrinho

def get_itens_carrinho(request): #get
    """ return all items from the current user's cart """
    return ItemCarrinho.objects.filter(id_carrinho=_id_carrinho(request))

def adicionar_ao_carrinho(request):  #add_to_cart
    """ function that takes a POST request and adds a product instance to the current customer's shopping cart """
    postdata = request.POST.copy()
    # get presente slug from post data, return blank if empty
    presente_slug = postdata.get('presente_slug','')
    # get quantity added, return 1 if empty
    quantidade = postdata.get('quantidade',1)
    # fetch the product or return a missing page error
    p = get_object_or_404(Presente, slug=presente_slug)
    #get products in cart
    carrinho_presentes = get_itens_carrinho(request) #cart_products = get_cart_items(request)
    presente_no_carrinho = False #product_in_cart = False
    # check to see if item is already in cart
    for item in carrinho_presentes: #for cart_item in cart_products:
        if item.presente.id  == p.id:
            # update the quantity if found
            item.aumentar_quantidade(quantidade) #augment_quantity(quantity)
            presente_no_carrinho = True
    if not presente_no_carrinho:
        # create and save a new cart item
        ci = ItemCarrinho()
        ci.presente = p
        ci.quantidade = quantidade
        ci.id_carrinho = _id_carrinho(request)
        ci.save()

def get_single_item(request, item_id):
    return get_object_or_404(ItemCarrinho, id=item_id, cart_id=_id_carrinho(request))

# update quantity for single item
def atualizar_carrinho(request): #update_cart
    """ function takes a POST request that updates the quantity for single product instance in the
    current customer's shopping cart

    """
    postdata = request.POST.copy()
    item_id = postdata['item_id']
    quantidade = postdata['quantidade']
    item = get_single_item(request, item_id) #cart_item
    if item:
        if int(quantidade) > 0:
            item.quantidade = int(quantidade)
            item.save()
        else:
            remover_do_carrinho(request)

# remove a single item from cart
def remover_do_carrinho(request):
    """ function that takes a POST request removes a single product instance from the current customer's
    shopping cart
    """
    postdata = request.POST.copy()
    item_id = postdata['item_id']
    item = get_single_item(request, item_id)
    if item:
        item.delete()

def subtotal_carrinho(request):
    """ gets the subtotal for the current shopping cart """
    total_carrinho = decimal.Decimal('0.00') #cart_total
    presentes_carrinho = get_itens_carrinho(request)
    for item in presentes_carrinho:
        total_carrinho += item.presente.valor * item.quantidade
    return total_carrinho

# returns the total number of items in the user's cart
def contar_itens_carrinho(request): #cart_distinct_item_count
    return get_itens_carrinho(request).count()

def esta_vazio(request): #is_empty
    return contar_itens_carrinho(request) == 0

def esvaziar_carrinho(request): #empty_cart
    """ empties the shopping cart of the current customer """
    carrinho_usuario = get_itens_carrinho(request) #user_cart
    carrinho_usuario.delete()

def remover_itens_antigos(): #remove_old_cart_items
    """ 1. calculate date of 90 days ago (or session lifespan)
    2. create a list of cart IDs that haven't been modified
    3. delete those CartItem instances

    """
    print("Removendo carrinho antigos")
    remove_before = datetime.now() + timedelta(days=-settings.SESSION_COOKIE_DAYS)
    cart_ids = []
    old_items = ItemCarrinho.objects.values('id_carrinho').annotate(last_change=Max('data_adicao')).filter(last_change__lt=remove_before).order_by()
    for item in old_items:
        cart_ids.append(item['id_carrinho'])
    to_remove = ItemCarrinho.objects.filter(cart_id__in=cart_ids)
    to_remove.delete()
    print(str(len(cart_ids)) + " carrinhos removidos")


