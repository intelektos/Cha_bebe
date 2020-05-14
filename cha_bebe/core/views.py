from django.shortcuts import render
import os
from django.conf import settings
from django.templatetags.static import static

def home(request):
	return render(request, 'home.html')

def sobre(request):
	return render(request, 'sobre.html')
