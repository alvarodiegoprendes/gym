from bson import is_valid
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
# Create your views here.
# accounts/views.py

def inicio(request):
    
    return render(request,'cuenta/inicio.html')

def gym_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' Bienvenido/a {username} !!')
            return redirect('mostrar_cuenta')
        else:
            messages.error(request, 'Cuenta o password incorrecto, realice el login correctamente')
    form = AuthenticationForm()
    return render(request, 'cuenta/login.html', {'form': form})

@login_required(login_url='login')
def mostrar_cuenta(request):
    usuario = request.user
    contexto = {
        'usuario': usuario,
    }
    return render(request, 'cuenta/cuenta_usuario.html', contexto)

def gym_registrarse(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            messages.success(request, f'Tu cuenta fue creada con éxito! Ya te podes loguear en el sistema.')
            return redirect('login')
    else:
        form = RegistrarUsuarioForm()
    return render(request, 'cuenta/registrarse.html', {'form': form})


@login_required(login_url='login')
def editar_cuenta(request):

    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST, instance=request.user)
        medidas_form = MedidaCorporalForm(request.POST, instance=request.user.medidas_corporales)

        if form.is_valid() and medidas_form.is_valid():
            medidas = medidas_form.save()  # Guardar las medidas corporales
            cuenta = form.save(commit=False)  # No guardar aún la cuenta
            cuenta.medidas_corporales = medidas  # Asignar las medidas corporales al usuario
            cuenta.save()  # Ahora guardar la cuenta
            messages.success(request, 'Tu cuenta fue editada con éxito!')
            return redirect('mostrar_cuenta')
        else:
            messages.error(request, 'Hubo un error al actualizar sus datos')
    else:
        form = EditarUsuarioForm(instance=request.user)
        medidas_form = MedidaCorporalForm(instance=request.user.medidas_corporales)
    
    contexto = {
        'form': form,
        'medidas_form': medidas_form,  # Asegúrate de pasar el formulario de medidas al contexto
    }
    return render(request, 'cuenta/editar_cuenta.html', contexto)
@login_required(login_url='login')
def gym_logout(request):
    logout(request)
    return redirect('inicio')