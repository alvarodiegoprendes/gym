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

class Entrenador(models.Model):
    nombre=models.CharField
    genero=models.CharField(choices= GENDER_CHOICES)
    lista_atletas= models.ForeignKey(
        Atleta, related_name="results", on_delete=models.PROTECT, blank=True, null=True
    )
    horario=models.DateTimeField
    foto=models.ImageField

class Ejercicios(models.Model):
    nombre= models.CharField
    zona_muscular= models.CharField
    equipo_necesario=models.CharField
    area=models.CharField
    foto=models.ImageField
    tipo_de_ejercicio=models.CharField #fuerza, cardio, elasticidad etc
    descripcion=models.CharField


class Rutina(models.Model):
    dias_entrenamiento=models.DateField
    dias_descanso=models.DateField
    ejercicios=models.ForeignKey(
        Ejercicios, related_name="results", on_delete=models.PROTECT, blank=True, null=True
    )
    duracion_rutina=models.DurationField
    duracion_ejercicio= models.DurationField
    repeticiones=models.IntegerField
    tiempo_descanso=models.DurationField
    cantidad_series=models.IntegerField

class Alimentos(models.Model):
    pass

class Dieta(models.Model):
    nombre_dieta=models.CharField
    descripcion=models.CharField 
    proposito=models.CharField
    lista_alimentos=models.CharField #debe ser importado de la clase alimento
    cantidad=models.FloatField
    fecha_inicio= models.DateField
    fecha_final= models.DateField
    duracion= models.DurationField(fecha_final-fecha_inicio)
    

class Records(models.Model):
    fecha= models.DateField
    ejercicio=models.ForeignKey(
        Ejercicios, related_name="results", on_delete=models.PROTECT, blank=True, null=True
    )
    repeticiones= models.IntegerField
    peso_alcanzado= models.FloatField

class Atleta(models.Model):
    nombre= models.CharField
    edad= models.IntegerField
    genero = models.CharField(choices=GENDER_CHOICES)
    foto= models.ImageField
    rutina= models.ForeignKey(
        Rutina, related_name="results", on_delete=models.PROTECT, blank=True, null=True
    )
    entrenador= models.ForeignKey(
        Entrenador, related_name="results", on_delete=models.PROTECT, blank=True, null=True
    )
    suscripcion=models.ForeignKey(
        Suscripcion, related_name="results", on_delete=models.PROTECT, blank=True, null=True
    )
    medidas_corporales= models.ForeignKey(
        MedidasCorporales, related_name="results", on_delete=models.PROTECT, blank=True, null=True
    )