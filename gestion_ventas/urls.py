from django.urls import path
from . import views

urlpatterns = [
    path('inicio', views.Inicio, name="inicio"),
    path('', views.ver_productos, name="ver_productos"),
    path('comprar', views.agregar_compra, name="comprar"),
    path('form_compra', views.form_compra, name="form_compra")
]

