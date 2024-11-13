from django.db import models

class Laboratorio(models.Model):
  nombre = models.CharField(max_length=100)
  valor_minimo = models.DecimalField(max_digits=10, decimal_places=2)
  fecha_de_creacion = models.DateTimeField(auto_now_add=True)
  fecha_de_actualizacion = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = "laboratorios"
