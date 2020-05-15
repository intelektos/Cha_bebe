from django import forms
from .models import Recado
#from django.core.mail import send_mail
#from django.conf import settings

class FormRecado(forms.ModelForm):
    class Meta:
        model = Recado
        fields = ['nome', 'sobrenome', 'email', 'mensagem']
