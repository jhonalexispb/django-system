# forms.py
from django import forms

class PrincipioActivoForm(forms.Form):
    nombrePrincipioActivo = forms.CharField(max_length=255, min_length=1, required=True)
    concentracion = forms.CharField(max_length=20, required=False)
