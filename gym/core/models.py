from typing import Any
from django.db import models

# Create your models here.

GENDER_CHOICES = (("male", "MALE"), ("female", "FEMALE"))

class Suscripcion(models.Model):
    fecha_inscripcion=models.DateField
    fecha_vencimiento=models.DateField
    importe=models.FloatField
    pago=models.FloatField

class MedidasCorporales(models.Model):
    altura= models.FloatField
    peso= models.FloatField
    fecha_medicion= models.DateField
    porcentaje_grasa= models.FloatField

class Area(models.Model):
    nombre=models.CharField
    objetivo=models.CharField
    direccion=models.CharField
    

class Ejercicios(models.Model):
    area=models.ForeignKey(
        Area, related_name="results", on_delete=models.PROTECT, blank=True, null=True
    )
    nombre= models.CharField
    zona_muscular= models.CharField
    equipo_necesario=models.CharField
    foto=models.ImageField
    tipo_de_ejercicio=models.CharField #fuerza, cardio, elasticidad etc
    descripcion=models.CharField


class Rutina(models.Model):
    lista_ejercicios=models.ForeignKey(
        Ejercicios, related_name="results", on_delete=models.PROTECT, blank=True, null=True
    )
    # dias_entrenamiento=models.DateField
    # dias_descanso=models.DateField
    duracion_rutina=models.DurationField
    # duracion_ejercicio= models.DurationField
    # repeticiones=models.IntegerField
    # tiempo_descanso=models.DurationField
    # cantidad_series=models.IntegerField
    # peso=models.FloatField


class Alimentos(models.Model):
    pass

class Gramaje(models.Model):
    alimentos=models.ForeignKey(
        Alimentos, related_name="results", on_delete=models.PROTECT, blank=True, null=True
    )
    cantidad=models.FloatField

class Dieta(models.Model):
    lista_alimentos=models.ForeignKey(
        Gramaje, related_name="results", on_delete=models.PROTECT, blank=True, null=True        
    )
    nombre_dieta=models.CharField
    descripcion=models.CharField 
    proposito=models.CharField
    fecha_inicio= models.DateField
    fecha_final= models.DateField
    duracion= models.DurationField(fecha_final-fecha_inicio)

class Records(models.Model):
    ejercicio=models.ForeignKey(
        Ejercicios, related_name="results", on_delete=models.PROTECT, blank=True, null=True
    )    
    fecha= models.DateField
    repeticiones= models.IntegerField
    peso_alcanzado= models.FloatField

class Actividad(models.Model):
    rutina=models.ForeignKey(
        Rutina, related_name="results", on_delete=models.PROTECT, blank=True, null=True
    )
    ejercicios=models.ForeignKey(
        Ejercicios, related_name="results", on_delete=models.PROTECT, blank=True, null=True
    )
    dieta= models.ForeignKey(
        Dieta, related_name="results", on_delete=models.PROTECT, blank=True, null=True     
    )
    dias_entrenamiento=models.DateField
    dias_descanso=models.DateField
    duracion_actividad=models.DurationField
    duracion_ejercicio= models.DurationField
    repeticiones=models.IntegerField
    tiempo_descanso=models.DurationField
    cantidad_series=models.IntegerField
    peso=models.FloatField

class Cliente(models.Model):
    entrenador=models.ForeignKey(
        'self', related_name="results", on_delete=models.PROTECT, blank=True, null=True 
    )
    rutina= models.ForeignKey(
        Rutina, related_name="results", on_delete=models.PROTECT, blank=True, null=True
    )
    suscripcion=models.ForeignKey(
        Suscripcion, related_name="results", on_delete=models.PROTECT, blank=True, null=True
    )
    medidas_corporales= models.ForeignKey(
        MedidasCorporales, related_name="results", on_delete=models.PROTECT, blank=True, null=True
    )
    nombre= models.CharField
    edad= models.IntegerField
    genero = models.CharField(choices=GENDER_CHOICES)
    foto= models.ImageField
