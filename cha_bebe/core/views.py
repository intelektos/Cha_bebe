from django.shortcuts import render
import os
from django.conf import settings
from django.templatetags.static import static

def home(request):
	return render(request, 'home.html')

def galeria(request):
    path = settings.MEDIA_ROOT
    img_list = os.listdir(path + '/images')
    context = {'images' : img_list}
    return render(request, "galeria.html", context)
