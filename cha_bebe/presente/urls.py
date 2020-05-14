from django.urls import include, path, re_path
from . import views

app_name = 'presente'
urlpatterns = [
    path('', views.presente, name='presente'),
    re_path(r'^(?P<slug>[\w_-]+)/$', views.detalhe, name='detalhe'),
]
