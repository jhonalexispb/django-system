from django.urls import path
from . import views

urlpatterns = [
    path('principios_activos', views.ListadoPrincipiosActivos, name='principios_activos'),
    path('principios_activos/crear', views.crear_principio_activo, name='crear_principios_activos'),
]