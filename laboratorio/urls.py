from django.urls import path
from . import views

urlpatterns = [
    path('laboratorios', views.ListadoLaboratorio, name='laboratorios'),
    path('laboratorios/crear', views.crear_laboratorio, name='crear_laboratorio'),
]
