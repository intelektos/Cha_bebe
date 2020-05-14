from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
#from .core import urls

urlpatterns = [
    path('', include('cha_bebe.core.urls',namespace="core")),
    path('galeria', include('cha_bebe.galeria.urls', namespace='galeria')),
    path('presente', include('cha_bebe.presente.urls', namespace='presente')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
