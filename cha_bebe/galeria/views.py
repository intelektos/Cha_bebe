from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from .models import Album, Imagem

def index(request):
    template_name = 'index.html'
    albuns = Album.objects.all()
    context = {'albuns': albuns  }
    return render(request, template_name, context)

def album(request, slug):
	_album = get_object_or_404(Album, slug=slug)
	imagens = Imagem.objects.filter(album=_album)
	template_name = 'album.html'
	context = {'imagens': imagens}
	return render(request, template_name, context)

def imagem(request, slug):
	imagem = get_object_or_404(Imagem, slug=slug)
	template_name = 'imagem.html'
	context = {'imagem': imagem}
	return render(request, template_name, context)

