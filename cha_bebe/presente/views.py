from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from .models import Presente

def presente(request):
    template_name = 'presente.html'
    presentes = Presente.objects.all()
    context = {'presentes': presentes}
    return render(request, template_name, context)

def detalhe(request, slug):
	presente = get_object_or_404(Presente, slug=slug)
	template_name = 'detalhe.html'
	context = {'presente': presente}
	return render(request, template_name, context)
