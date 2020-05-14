try:
    import Image
except ImportError:
    from PIL import Image
from django import forms
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from .models import Presente

class FormPresente(forms.ModelForm):
    class Meta:
        model = Presente
        fields = '__all__'

class AdminPresente(ModelAdmin):
    list_display = ('titulo',)
    list_filter = ('titulo',)
    search_fields = ('titulo',)
    form = FormPresente

    def save_model(self, request, obj, form, change):
        """Metodo declarado para criar miniatura da imagem depois de salvar"""
        super(AdminPresente, self).save_model(request, obj, form, change)

        if 'imagem' in form.changed_data:
            extensao = obj.imagem.name.split('.')[-1]
            obj.thumbnail = 'presentes/thumbnail/%s.%s'%(
               obj.id, extensao)

            miniatura = Image.open(obj.imagem.path)
            miniatura.thumbnail((100,100), Image.ANTIALIAS)
            miniatura.save(obj.thumbnail.path)

            obj.save()

admin.site.register(Presente, AdminPresente)


