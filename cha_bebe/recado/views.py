from django.shortcuts import render, redirect
from .models import Recado
from .forms import FormRecado

def recado(request):
    template_name = 'recados.html'
    recados = Recado.objects.filter(aprovado=True)

    context = {'recados': recados}
    return render(request, template_name, context)

def novo_recado(request):
    template_name = 'novo_recado.html'
    if request.method == 'POST':
        form = FormRecado(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recado:salvo')

    else:
        form = FormRecado()
    context = {
        'form': form
    }
    return render(request, template_name, context)

def salvo(request):
    return render(request, 'salvo.html')
