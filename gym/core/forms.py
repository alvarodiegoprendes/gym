from django import forms
from .models import *

class Crear_gramaje(forms.Form):
    alimentos = forms.ModelMultipleChoiceField(queryset=Alimentos.objects.all(), widget=forms.CheckboxSelectMultiple)
    cantidad = forms.FloatField(label="cantidad",widget=forms.TextInput(attrs={'class': 'input'}),required= False) 