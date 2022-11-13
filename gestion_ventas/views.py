from django.shortcuts import render, redirect
from gestion_ventas.models import Productos, Cliente

# Create your views here.

def ver_productos(request):
    productos = Productos.objects.all()
    return render(request, "ver_productos.html", {'productos': productos})

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
        return render(request, "comprar.html")