from django.db import models
from datetime import datetime

class Recado(models.Model):
    nome = models.CharField('Nome', max_length=50)
    sobrenome = models.CharField('Sobrenome', max_length=50)
    email = models.EmailField('E-mail')
    mensagem = models.TextField('Mensagem')
    aprovado = models.BooleanField(default=False)
    data_inclusao = models.DateTimeField(auto_now_add=True)

    @property
    def nome_completo(self):
        return '%s %s' % (self.nome, self.sobrenome)
