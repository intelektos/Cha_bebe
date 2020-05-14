from django.urls import include, path, re_path
from . import views

app_name = 'recado'
urlpatterns = [
    path('', views.recado, name='recado'),
]
