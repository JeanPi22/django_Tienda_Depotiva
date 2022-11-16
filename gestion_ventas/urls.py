from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.ver_productos, name="ver_productos"),
    path('agregar_compra/', views.agregar_compra, name="agregar_compra"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

