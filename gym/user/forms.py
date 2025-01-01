from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms


class MedidaCorporalForm(forms.ModelForm):
    class Meta:
        model = MedidaCorporal
        fields = '__all__'  


class RegistrarUsuarioForm(UserCreationForm):
    medidas_corporales = MedidaCorporalForm() 

    class Meta:
        model = Cuenta
        fields = ['username','email','first_name','last_name', 'password1', 'password2', 'edad', 'genero', 'foto']

class EditarUsuarioForm(forms.ModelForm):
    medidas_corporales = MedidaCorporalForm()  

    class Meta:
        model = Cuenta
        fields = ['username','email','first_name','last_name', 'edad', 'genero', 'foto']

