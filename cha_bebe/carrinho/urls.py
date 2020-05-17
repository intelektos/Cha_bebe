from django.urls import include, path, re_path
from . import views

app_name = 'carrinho'
urlpatterns = [
    path('', views.carrinho, name='carrinho'),
]
