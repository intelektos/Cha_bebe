from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
    path('galeria', views.galeria, name='galeria'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



