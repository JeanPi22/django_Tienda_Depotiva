from django.shortcuts import render, redirect
from gestion_ventas.models import Productos, Cliente
from django.http import HttpResponse

# Create your views here.      

def Inicio(request):
    return render(request, "inicio.html")


def ver_productos(request):
    productos = Productos.objects.all()
    return render(request, "ver_productos.html", {'productos': productos})


def form_compra(request):
    return render(request, "comprar_producto.html")


def agregar_compra(request):
    if request.method == "POST":
        nombre_apellido = request.POST["nombre"]
        correo = request.POST["categoria"]
        direccion = request.POST["costo"]
        departamento = request.POST["stock"]
        ciudad = request.POST["descripcion"]
        telefono = request.POST["descripcion"]
        data = Cliente(nombre_apellido=nombre_apellido, correo=correo, direccion=direccion, departamento=departamento,
        ciudad=ciudad, telefono=telefono)
        data.save()
        return redirect("/ver_productos/")
    else:
        return render(request, "comprar_producto.html")


