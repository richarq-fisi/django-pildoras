from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static

from ProyectoWebApp import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('tienda', views.tienda, name="Tienda"),
    path('contacto', views.contacto, name="Contacto")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)