# forms.py
from django import forms

class PrincipioActivoForm(forms.Form):
    nombre = forms.CharField(max_length=255, required=True, error_messages={'required': 'Este campo es obligatorio.'})
    concentracion = forms.FloatField(min_value=0.1, required=False, error_messages={'invalid': 'Debe ser un número válido.', 'min_value': 'La concentración debe ser mayor que 0.'})

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre.strip():  # Validación adicional: no permitir nombres vacíos
            raise forms.ValidationError('El nombre no puede estar vacío.')
        return nombre

    def clean_concentracion(self):
        concentracion = self.cleaned_data.get('concentracion')
        if concentracion is not None and concentracion <= 0:
            raise forms.ValidationError('La concentración debe ser mayor que 0.')
        return concentracion