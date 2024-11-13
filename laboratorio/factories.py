import factory
from .models import Laboratorio

class LaboratorioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Laboratorio  # Especifica el modelo al que se asociará esta factory

    # Definir los campos del modelo
    nombre = factory.Faker('word')  # Genera un nombre aleatorio
    valor_minimo = factory.Faker('random_number', digits=2)  # Genera un precio aleatorio
    fecha_de_creacion = factory.Faker('date_this_year')  # Genera una fecha aleatoria de este año
    fecha_de_actualizacion = factory.Faker('date_this_year')  # Genera una fecha aleatoria de este año