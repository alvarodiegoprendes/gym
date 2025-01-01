from cProfile import label
from dataclasses import field
from sys import prefix
from tkinter import Widget
from django import forms 
from .models import *

""" class Crear_gramaje(forms.Form):
    alimentos = forms.ModelMultipleChoiceField(queryset=Alimento.objects.all(), widget=forms.CheckboxSelectMultiple)
    cantidad = forms.CharField(label="cantidad", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}),required= False)  """

#funciona apara relacion many to many

""" class GramajeForm(forms.ModelForm):
    class Meta:
        model = Gramaje
        fields = ['alimentos','cantidad']
 """#funciona perfectamene crea un objeto gramaje con una referencia a alimentos y la cantidad respectiva a ese alimento


""" class GramajeForm(forms.ModelForm):
    class Meta:
        model = Gramaje
        fields = ['alimentos', 'cantidad'] """



class RutinaForm(forms.ModelForm):

    class Meta:
        model = Rutina
        exclude=('dias_descanso',)
    dias_entrenamiento = forms.MultipleChoiceField(
        choices=DIAS_SEMANA,
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )

class ActividadRutinaForm(forms.ModelForm):
    class Meta:
        model=Actividad
        fields=('rutina',)

class ActividadForm(forms.ModelForm):
    class Meta:
        model=Actividad
        fields=('duracion_ejercicio','repeticiones','tiempo_descanso','cantidad_series','peso','ejercicios','rutina')
        widgets={
            'ejercicios': forms.HiddenInput,
            'rutina': forms.HiddenInput,
        }

class DietaForm(forms.ModelForm):
    class Meta:
        model= Dieta
        fields=('__all__')


class GramajeDietaForm(forms.ModelForm):
    class Meta:
        model=Gramaje
        fields=('dietas',)
        
class GramajeForm(forms.ModelForm):
    class Meta:
        model= Gramaje
        fields= ('dietas','cantidad','alimentos','unidad',)
        widgets={
            'dietas': forms.HiddenInput,
            'alimentos': forms.HiddenInput,
        }



        
