from django.shortcuts import render, HttpResponse
from Servicios.models import Servicio

# Create your views here.
def home(request):
    return render(request, "ProyectoWebApp/home.html")

def tienda(request):
    return render(request, "ProyectoWebApp/tienda.html")

def contacto(request):
    return render(request, "ProyectoWebApp/contacto.html")