from django.db import models

class PrincipioActivo(models.Model):
    nombre = models.CharField(max_length=100)
    concentracion = models.CharField(max_length=20)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    fecha_de_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'principios_activos'