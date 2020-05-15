from django.urls import include, path, re_path
from . import views

app_name = 'recado'
urlpatterns = [
    path('', views.recado, name='recado'),
    path('novo_recado', views.novo_recado, name='novo_recado'),
    path('salvo', views.salvo, name='salvo'),
]
