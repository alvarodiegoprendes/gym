from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
# Create your views here.

""" 
dias_semanas={
    "lunes":"dia de pecho",
    "martes": "dia de hombro",
    "miercoles": "dia de pierna"
}

def saludar_numero (request,dia):
    lista_dias_semanas=list(dias_semanas.keys())

    if dia>0 and dia<=len(lista_dias_semanas):

        rutina_int=lista_dias_semanas[dia-1]

        return HttpResponseRedirect("/core/"+rutina_int)
    else:
        return HttpResponse("no hay rutina para ese dia")

def saludar(request,dia):
    try:
        rutina=dias_semanas[dia]  
    except: 
        rutina="no hay rutina"
    rutina_html= f"<h2>{rutina}</h2>"
    return HttpResponse(rutina_html) """


def mostrar_alimentos(request):
    if request.method == 'GET':
        return render(request, 'alimentos.html', {
            'alimentos': Crear_gramaje()
        })
    else:
        Gramaje.objects.create(
            alimentos=request.POST['alimentos'],
            cantidad=request.POST['cantidad'],

        ) 
        return render(request, 'alimentos.html', {
            'alimentos': Crear_gramaje()
        })



def mostrar_rutina(request):
    rutina = Rutina.objects.all()
    return render(request, 'rutina.html', {'rutina': rutina})
