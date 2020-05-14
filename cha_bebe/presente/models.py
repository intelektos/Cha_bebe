from django.db import models
from django.urls import reverse
from datetime import datetime
from django.db.models import signals
from django.template.defaultfilters import slugify
from cha_bebe.utils.signals_comuns import slug_pre_save


class Presente(models.Model):
    class Meta:
        ordering = ('titulo',)

    titulo = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    descricao = models.TextField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    imagem = models.ImageField(
        null=True,
        blank=True,
        upload_to='presentes/imagens',
        )
    thumbnail = models.ImageField(
        null=True,
        blank=True,
        upload_to='presentes/thumbnail',
        )

    def __unicode__(self):
        return self.titulo

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('presente:detalhe', args=[str(self.slug)])


signals.pre_save.connect(slug_pre_save, sender=Presente)
