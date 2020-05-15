from django import forms
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from .models import Recado

class AdminRecado(ModelAdmin):
    list_display = ('nome_completo','email', 'aprovado')
    search_fields = ('nome','sobrenome', 'aprovado')

admin.site.register(Recado, AdminRecado)
