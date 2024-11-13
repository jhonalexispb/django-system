from django import forms
from .models import Laboratorio

class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = ['nombre', 'valor_minimo']

    def clean_valor_minimo(self):
        valor_minimo = self.cleaned_data.get('valor_minimo')
        if valor_minimo <= 0:
            raise forms.ValidationError("El valor minimo debe ser un número positivo.")
        return valor_minimo
