from django.shortcuts import render, redirect
from gestion_ventas.models import Productos, Cliente
from django.http import HttpResponse

# Create your views here.  

def ver_productos(request):
    productos = Productos.objects.all()
    return render(request, "ver_productos.html", {'productos': productos})


def agregar_compra(request):
    if request.method == "POST":
        nombre_apellido = request.POST["nombre_apellido"]
        correo = request.POST["correo"]
        direccion = request.POST["direccion"]
        departamento = request.POST["departamento"]
        ciudad = request.POST["ciudad"]
        telefono = request.POST["telefono"]
        data = Cliente(nombre_apellido=nombre_apellido, correo=correo, direccion=direccion, departamento=departamento,
        ciudad=ciudad, telefono=telefono)
        data.save()
        return redirect("ver_productos")
    else:
        return render(request, "comprar_producto.html")