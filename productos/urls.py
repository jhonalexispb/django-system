from django.urls import path
from . import views

urlpatterns = [
    path('productos', views.ListadoProducto, name='productos'),
    path('productos/crear', views.crear_producto, name='crear_producto'),
]