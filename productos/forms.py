from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del producto', 'rows': 4}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio del producto'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Stock disponible'}),
        }

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio <= 0:
            raise forms.ValidationError("El precio debe ser un número positivo.")
        return precio