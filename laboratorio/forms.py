from django import forms
from .models import Laboratorio

class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = ['nombre', 'valor_minimo']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del laboratorio'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor minimo de venta'}),
        }
