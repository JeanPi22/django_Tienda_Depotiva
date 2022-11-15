from django.urls import path
from . import views

urlpatterns = [
    path('inicio', views.Inicio, name="inicio"),
    path('', views.ver_productos, name="ver_productos")
]

