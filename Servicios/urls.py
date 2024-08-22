from django.urls import path
from django.conf import settings
from . import views
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.servicios, name="Servicios"),
]