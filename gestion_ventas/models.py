from django.db import models

# Create your models here.

class Productos(models.Model):
    nombre = models.CharField(max_length=30)
    costo = models.IntegerField(default=0)
    cantidad_stock = models.IntegerField(default=0)
    imagen = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre_apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    direccion = models.CharField(max_length=50)
    departamento = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)
    telefono = models.CharField(max_length=15)
    producto = models.ForeignKey(Productos, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre_apellido

