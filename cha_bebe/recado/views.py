from django.shortcuts import render
from .models import Recado

def recado(request):
    template_name = 'recados.html'
    albuns = Album.objects.all()
    context = {'albuns': albuns  }
    return render(request, template_name, context)
