from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, re_path
from . import views

app_name = 'galeria'
urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^(?P<slug>[\w_-]+)/$', views.album, name='album'),
    re_path(r'^imagem/(?P<slug>[\w_-]+)/$', views.imagem, name='imagem'),
]


