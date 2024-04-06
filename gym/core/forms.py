from django import forms
from .models import *

class Crear_gramaje(forms.Form):
    alimentos = forms.ModelMultipleChoiceField(queryset=Alimentos.objects.all(), widget=forms.CheckboxSelectMultiple)
    cantidad = forms.CharField(label="cantidad", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))