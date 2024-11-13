import factory
from .models import PrincipioActivo

class PrincipioActivoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PrincipioActivo  # Especifica el modelo al que se asociará esta factory

    # Definir los campos del modelo
    nombre = factory.Faker('word')  # Genera un nombre aleatorio
    concentracion = factory.Faker('random_number', digits=2)  # Genera un precio aleatorio
    fecha_de_creacion = factory.Faker('date_this_year')  # Genera una fecha aleatoria de este año
    fecha_de_actualizacion = factory.Faker('date_this_year')  # Genera una fecha aleatoria de este año