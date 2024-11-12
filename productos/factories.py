import factory
from .models import Producto

class ProductoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Producto  # Especifica el modelo al que se asociará esta factory

    # Definir los campos del modelo
    nombre = factory.Faker('word')  # Genera un nombre aleatorio
    descripcion = factory.Faker('text')  # Genera una descripción aleatoria
    precio = factory.Faker('random_number', digits=5)  # Genera un precio aleatorio
    stock = factory.Faker('random_number', digits=3)  # Genera un stock aleatorio
    fecha_creacion = factory.Faker('date_this_year')  # Genera una fecha aleatoria de este año
    fecha_actualizacion = factory.Faker('date_this_year')  # Genera una fecha aleatoria de este año