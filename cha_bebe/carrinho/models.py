from django.db import models
from cha_bebe.presente.models import Presente

class ItemCarrinho(models.Model):
    id_carrinho = models.CharField(max_length=50)
    data_adicao = models.DateTimeField(auto_now_add=True)
    quantidade = models.IntegerField(default=1)
    presente = models.ForeignKey(Presente, on_delete=models.CASCADE, unique=False)

    class Meta:
        db_table = 'itens_carrinho'
        ordering = ['data_adicao']

    def total(self):
        return self.quantidade * self.presente.valor

    def name(self):
        return self.presente.titulo

    def preco(self):
        return self.presente.valor

    def get_absolute_url(self):
        return self.presente.get_absolute_url()

    def aumentar_quantidade(self, quantidade):
        self.quantidade = self.quantidade + int(quantidade)
        self.save()
