from django.shortcuts import render
from gestion_ventas.models import Productos

# Create your views here.

def ver_productos(request):
    productos = Productos.objects.all()
    return render(request, "ver_productos.html", {'productos': productos})
