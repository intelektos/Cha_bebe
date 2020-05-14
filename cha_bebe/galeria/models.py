from django.db import models
from django.urls import reverse
from datetime import datetime
from django.db.models import signals
from cha_bebe.utils.signals_comuns import slug_pre_save

class Album(models.Model):
    class Meta:
        ordering = ('titulo',)

    titulo = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    capa = models.ImageField(
        null=True,
        blank=True,
        upload_to='galeria/capa',
        )

    def __unicode__(self):
        return self.titulo

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('galeria:album', args=[str(self.slug)])


class Imagem(models.Model):
    class Meta:
        ordering = ('album','titulo',)

    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    descricao = models.TextField(blank=True, null=True)
    original = models.ImageField(
        null=True,
        blank=True,
        upload_to='galeria/original',
        )
    thumbnail = models.ImageField(
        null=True,
        blank=True,
        upload_to='galeria/thumbnail',
        )
    publicacao = models.DateTimeField(default=datetime.now, blank=True)

    def __unicode__(self):
        return self.titulo

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('galeria:imagem', args=[str(self.slug)])


signals.pre_save.connect(slug_pre_save, sender=Album)
signals.pre_save.connect(slug_pre_save, sender=Imagem)

