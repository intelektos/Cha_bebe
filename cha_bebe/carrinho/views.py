from django.shortcuts import render, get_object_or_404
from cha_bebe.carrinho import carrinho
from django.template import RequestContext
from django.http import HttpResponseRedirect
#from ecomstore.checkout import checkout
from cha_bebe import settings

""" def album(request, slug):
	_album = get_object_or_404(Album, slug=slug)
	imagens = Imagem.objects.filter(album=_album)
	template_name = 'album.html'
	context = {'imagens': imagens}
	return render(request, template_name, context) 
	"""

def carrinho(request):
    template_name="carrinho.html"
    contagem = carrinho.contar_itens_carrinho(request)
    context = {'contagem': contagem}
    return render(request, template_name, context)
    """
    
    if request.method == 'POST':
        postdata = request.POST.copy()
        if postdata['submit'] == 'Remove':
            carrinho.remover_do_carrinho(request)
        if postdata['submit'] == 'Update':
            carrinho.atualizar_carrinho(request)
        if postdata['submit'] == 'Checkout':
#            checkout_url = checkout.get_checkout_url(request)
            return HttpResponseRedirect(checkout_url)
    itens = carrinho.get_itens_carrinho(request)
    page_title = 'Carrinho de Presentes'
    subtotal = carrinho.subtotal_carrinho(request)
    return render(request, template_name, RequestContext(request))
    """


