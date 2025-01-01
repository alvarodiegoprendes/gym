from urllib import request
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.


""" def mostrar_alimentos(request):
    if request.method == 'POST':
        form = Crear_gramaje(request.POST)
        if form.is_valid():
            alimentos_seleccionados = form.cleaned_data['alimentos']
            cantidades = request.POST.getlist('cantidad')

            # Verificar si la cantidad de alimentos seleccionados coincide con la cantidad de cantidades ingresadas
            if len(alimentos_seleccionados) != len(cantidades):
                # Manejar el caso de error aquí, si es necesario
                pass

            else:
                # Crear un objeto Gramaje
                nueva_rutina = Gramaje.objects.create()

                # Asociar cada alimento seleccionado con su respectiva cantidad al objeto Gramaje
                for alimento, cantidad in zip(alimentos_seleccionados, cantidades):
                    nueva_rutina.alimentos.add(alimento, through_defaults={'cantidad': cantidad})

                form = Crear_gramaje()
                return render(request, 'alimentos.html', {'alimentos': form})  # Reemplaza 'ruta_hacia_otra_pagina' con la URL a la que quieres redirigir

    else:  # Si el request.method es 'GET'
        form = Crear_gramaje()

    return render(request, 'alimentos.html', {'alimentos': form}) """

# funciona pero con relacion many to many

@login_required(login_url='login')
def crear_rutina(request):
    if not request.user.es_entrenador:
        messages.error(request, 'Usted no tiene permisos para acceder a esta pagina')
        return redirect('mostrar_cuenta')
    
    if request.method == 'GET':
        rutinaform = RutinaForm() 
        contexto = {'rutinaform': rutinaform}
        return render(request, 'core/crear_rutina.html', contexto)

    elif request.method == 'POST':
        rutina = RutinaForm(request.POST)
        dias_entrenamiento = request.POST.getlist('dias_entrenamiento')
        key_dias_semana = [key for key, valor in DIAS_SEMANA]

        dias_descanso = [dia for dia in key_dias_semana if dia not in dias_entrenamiento]
        if rutina.is_valid():
            messages.success(request, "sus datos se han recibido correctamente")
            nueva_rutina = rutina.save(commit=False)
            nueva_rutina.dias_descanso = dias_descanso
            nueva_rutina.save()
            return redirect('crear_actividad')
        else:
            messages.error(request, "sus datos no son validos")
            return redirect('crear_rutina')
    else:
        return HttpResponse('el metodo no es ni post ni get')


""" def crear_actividad(request):
    if request.method=='GET':
                
        conjunto_form = ConjuntoForm()
        ejercicioss = Ejercicios.objects.all()
        actividad_form_list = []
        
        for ejercicio in ejercicioss:
            actividad_form_instance = conjunto_form.actividadform(prefix=ejercicio.nombre.replace(' ', '_'),)
 
           # actividad_form_list.append((ejercicio, actividad_form_instance[actividad_form_instance.total_form_count()-1]))
            actividad_form_list.append((ejercicio, actividad_form_instance))

        contexto={'conjunto_form':conjunto_form,
                  'actividad_form':actividad_form_list,
                  }
        print(contexto)

        return render(request,'core/crear_actividad.html',contexto) """

@login_required(login_url='login')
def crear_actividad(request):
    if not request.user.es_entrenador:
        messages.error(request,'Usted no tiene permisos para acceder a esta pagina')
        return redirect('mostrar_cuenta')
    if request.method=='GET':
                
        rutinaform=ActividadRutinaForm
        actividadform=ActividadForm
        ejercicios = Ejercicios.objects.all()
        actividad_form_list = []
        
        for ejercicio in ejercicios:
            actividad_form_instance = actividadform(prefix=ejercicio.id)
 
            actividad_form_list.append((ejercicio, actividad_form_instance))

        contexto={'rutina_form':rutinaform,
                  'actividad_form':actividad_form_list,
                  }
       # print(contexto)

        return render(request,'core/crear_actividad.html',contexto)
    
    elif request.method == 'POST':
        ejercicios = Ejercicios.objects.all()
        rutinaform = ActividadRutinaForm(request.POST)
       #actividadform_lista = []

        if rutinaform.is_valid():

            for ejercicio in ejercicios:
                
                peso = request.POST.get(f'{ejercicio.id}-peso')
                repeticiones = request.POST.get(f'{ejercicio.id}-repeticiones',)
                cantidad_series = request.POST.get(f'{ejercicio.id}-cantidad_series')
                tiempo_descanso = request.POST.get(f'{ejercicio.id}-tiempo_descanso')
                duracion_ejercicio = request.POST.get(f'{ejercicio.id}-duracion_ejercicio')
                
               # actividad = Actividad(peso=peso, repeticiones=repeticiones, cantidad_series=cantidad_series, tiempo_descanso=tiempo_descanso, duracion_ejercicio=duracion_ejercicio,ejercicios=Ejercicios.objects.get(nombre=ejercicio),rutina=Rutina.objects.get(nombre=rutinaform.cleaned_data['rutina']))
                actividad = ActividadForm(data={
                    'peso': peso,
                    'repeticiones': repeticiones,
                    'cantidad_series': cantidad_series,
                    'tiempo_descanso': tiempo_descanso,
                    'duracion_ejercicio': duracion_ejercicio,
                    'ejercicios': Ejercicios.objects.get(id=ejercicio.id),
                    'rutina': Rutina.objects.get(nombre=rutinaform.cleaned_data['rutina'])
                })

                if actividad.is_valid():
                    actividad.save()
                else:
                    messages.error(request,"sus datos no son validos")
                    return redirect('crear_actividad')

            messages.success(request, "Sus datos se han guardado correctamente")
            return redirect('crear_rutina')
        else:
            messages.error(request,"sus datos no son validos")
            return redirect('crear_actividad')
    else:
        return HttpResponse('el metodo no es ni post ni get')
""" 
            actividadform = ActividadForm(request.POST, prefix=ejercicio.nombre.replace(' ', '_'))
            actividadform_lista.append(actividadform)
         
        if rutinaform.is_valid():


            for actividadform in actividadform_lista:
                if actividadform.is_valid():
                    actividad = actividadform.save(commit=False)
                    actividad.rutina = Rutina.objects.get(nombre=rutinaform.cleaned_data['rutina'])
                    actividad.ejercicios = Ejercicios.objects.get(nombre=actividadform.prefix.replace('_', ' '))
                    actividad.save()
 """


    

@login_required(login_url='login')    
def crear_dieta(request):
    if not request.user.es_entrenador:
        messages.error(request,'Usted no tiene permisos para acceder a esta pagina')
        return redirect('mostrar_cuenta')
    if request.method == 'GET':
        dietaform = DietaForm()

        contexto = {'dietaform': dietaform}

        return render(request, 'core/crear_dieta.html', contexto)
    
    elif request.method == 'POST':
        dieta = DietaForm(request.POST)

        if dieta.is_valid():
            messages.success(request,"sus datos se han recibido correctamente")
            dieta.save()
            return redirect('asignar_gramajes')
        
        else:
            messages.error(request,"sus datos no son validos")
            return redirect('crear_dieta')
    else:
        return HttpResponse('el metodo no es ni post ni get')
@login_required(login_url='login')
def asignar_gramaje(request):
    if not request.user.es_entrenador:
        messages.error(request,'Usted no tiene permisos para acceder a esta pagina')
        return redirect('mostrar_cuenta')
    if request.method == 'GET':
        gramajedietaform = GramajeDietaForm
        gramajeform = GramajeForm 
        alimento_gramaje_lista=[]
        alimentos=request.GET.get('busqueda_alimento')

        if alimentos:
            alimentos=Alimento.objects.filter(nombre__icontains=alimentos).order_by('nombre')
            if not alimentos:
                messages.error(request,'no fue encontrado ningun alimento con ese nombre')
            for alimento in alimentos:
                gramajeform_instance= gramajeform(prefix=alimento.id)
                alimento_gramaje_lista.append((alimento,gramajeform_instance))
        else:

            alimentos=Alimento.objects.all().order_by('nombre')
            for alimento in alimentos:
                gramajeform_instance= gramajeform(prefix=alimento.id)
                alimento_gramaje_lista.append((alimento,gramajeform_instance))

        contexto = {
            'gramajedietaform':gramajedietaform,
            'alimento_gramaje_lista':alimento_gramaje_lista,

        }

        return render(request, 'core/asignar_gramajes.html', contexto)

    elif request.method == 'POST':

        alimentos=Alimento.objects.all()
        gramajedietaform = GramajeDietaForm(request.POST)

        if 'cantidad' in request.POST:

            if gramajedietaform.is_valid():

                for alimento in alimentos:
                    cantidad = request.POST.get(f'{alimento.id}-cantidad','0')
                    unidad = request.POST.get(f'{alimento.id}-unidad')

                    if cantidad !='0':
                        gramajeform=GramajeForm(data={
                            'cantidad': cantidad,
                            'unidad': unidad,
                            'alimentos': Alimento.objects.get(id=alimento.id),
                            'dietas': Dieta.objects.get(nombre_dieta=gramajedietaform.cleaned_data['dietas']),
                        })

                        if gramajeform.is_valid():
                            gramajeform.save()   
                        else:
                            messages.error(request,"sus datos no son validos")
                            return redirect('asignar_gramajes')
                messages.success(request,'sus datos han sido guardados')
                return redirect('crear_dieta')
            else:
                messages.error(request,'sus datos no son validos')
                return redirect('asignar_gramajes')
        else:
            messages.error(request,'no envio ningun dato para ser guardado')
            return redirect('asignar_gramajes')
    else:
        return HttpResponse('el metodo no es soportado ya que no es ni get ni post')

@login_required(login_url='login')
def mostrar_alimentos(request):
    # si se usara el metodo GET en vez de el POST no abria que escribir los if ya que la informacion siempre se manda mediante un GET quedaria todo en una linea. request.GET.get('busqueda_alimento','')) aqui hay que pasar como segundo parametro un contexto vacio a la funcion get() ya que el metodo GET puede no estar enviando niguna informacion
    # alimento = Alimento.objects.filter(nombre__contains= request.GET.get('busqueda_alimento','')).order_by('nombre')
    # contexto = {'alimentos': alimento}
    # return render(request, 'core/mostrar_alimentos.html', contexto)

    if request.method == 'POST':

        alimento = Alimento.objects.filter(nombre__icontains=request.POST['busqueda_alimento']).order_by('nombre')
        alimento3 = Alimento.objects.get(id=1)

        gramaje_alimentos = alimento3.gramaje_set.all()
        
        contexto = {'alimentos': alimento,
                    'gramaje_alimentos': gramaje_alimentos}
        

        return render(request, 'core/mostrar_alimentos.html', contexto)

    elif request.method == 'GET':

        alimento = Alimento.objects.all().order_by('nombre')

        alimento3 = Alimento.objects.get(id=1)

        gramaje_alimentos = alimento3.gramaje_set.all()

        contexto = {'alimentos': alimento,
                    'gramaje_alimentos': gramaje_alimentos}

        return render(request, 'core/mostrar_alimentos.html', contexto)
    else:
        return HttpResponse("el metodo introducido no es ni POST ni GET ")

class RutinaListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    login_url = 'login'
    model = Rutina
    template_name = "core/mostrar_rutina.html"
    context_object_name = 'lista_rutina'

    def test_func(self):
        return self.request.user.es_entrenador

    def handle_no_permission(self):
        messages.error(self.request, 'Usted no tiene permisos para acceder a esta pagina')
        return redirect('mostrar_cuenta')



""" def asignar_gramajes(request, dieta_id):
    dieta = get_object_or_404(Dieta, id=dieta_id)
    if request.method == 'POST':
        form = GramajeForm(request.POST)
        if form.is_valid():
            gramaje = form.save(commit=False)
            gramaje.dieta = dieta
            gramaje.save()
            return render(request, 'core/asignar_gramajes.html', {'form': form, 'dieta': dieta})  # Permanece en la misma página para asignar más gramajes
    else:
        form = GramajeForm()
    return render(request, 'core/asignar_gramajes.html', {'form': form, 'dieta': dieta })
"""


