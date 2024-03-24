from typing import Any
from django.db import models


# Create your models here.

GENDER_CHOICES = (("male", "MALE"), ("female", "FEMALE"))

class Suscripcion(models.Model):
    fecha_inscripcion=models.DateField(blank=True, null=True)
    fecha_vencimiento=models.DateField(blank=True, null=True)
    importe=models.FloatField(default=0)
    pago=models.FloatField(default=0)
    def __str__(self):
        return str(self.fecha_inscripcion)
    
class MedidasCorporales(models.Model):
    altura= models.FloatField(default=0)
    peso= models.FloatField(default=0)
    fecha_medicion= models.DateField
    porcentaje_grasa= models.FloatField

class Area(models.Model):
    nombre=models.CharField(max_length=10, blank=True, null=True)
    objetivo=models.CharField(max_length=10, blank=True, null=True)
    direccion=models.CharField(max_length=10, blank=True, null=True)
    descripcion = models.CharField(max_length=10, blank=True, null=True)
    def __str__(self):
        return self.nombre
    

class Ejercicios(models.Model):
    area=models.ForeignKey(
        Area, related_name="ejercicios", on_delete=models.PROTECT, blank=True, null=True
    )
    nombre= models.CharField(max_length=10, blank=True, null=True)
    zona_muscular= models.CharField(max_length=10, blank=True, null=True)
    equipo_necesario=models.CharField(max_length=10, blank=True, null=True)
    foto=models.ImageField(upload_to="athletes/pics",default="athletes/athlete_default_photo.png",blank=True,null=True,
    )
    tipo_de_ejercicio=models.CharField(max_length=10, blank=True, null=True) #fuerza, cardio, elasticidad etc
    descripcion=models.CharField(max_length=10, blank=True, null=True)
    def __str__(self):
        return self.nombre


class Rutina(models.Model):
    lista_ejercicios=models.ForeignKey(
        Ejercicios, related_name="rutina", on_delete=models.PROTECT, blank=True, null=True
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

    nombre= models.CharField(max_length=200, blank=True, null=True)
#    especie = models.CharField(max_length=10, blank=True, null=True)
    calorias= models.FloatField(default=0)
    proteinas= models.FloatField(default=0)
    carbohidratos= models.FloatField(default=0)
    grasas= models.FloatField(default=0)
 #   "calorias": "106.0",
 #   "proteinas": "2.2",
  #  "carbohidratos": "24.0",
  #  "grasas": "0.1"
    def __str__(self):
        return self.nombre

class Gramaje(models.Model):
    alimentos=models.ForeignKey(
        Alimentos, related_name="gramaje", on_delete=models.PROTECT, blank=True, null=True
    )
    cantidad=models.FloatField(default=0)

class Dieta(models.Model):
    lista_alimentos=models.ForeignKey(
        Gramaje, related_name="dieta", on_delete=models.PROTECT, blank=True, null=True        
    )
    nombre_dieta=models.CharField(max_length=10, blank=True, null=True)
    descripcion=models.CharField (max_length=10, blank=True, null=True)
    proposito=models.CharField(max_length=10, blank=True, null=True)
    fecha_inicio= models.DateField
    fecha_final= models.DateField
    duracion= models.DurationField
    def __str__(self):
        return self.nombre_dieta

class Records(models.Model):
    ejercicio=models.ForeignKey(
        Ejercicios, related_name="records", on_delete=models.PROTECT, blank=True, null=True
    )    
    fecha= models.DateField
    repeticiones= models.IntegerField(default=0)
    peso_alcanzado= models.FloatField(default=0)

class Actividad(models.Model):
    rutina=models.ForeignKey(
        Rutina, related_name="actividad", on_delete=models.PROTECT, blank=True, null=True
    )
    ejercicios=models.ForeignKey(
        Ejercicios, related_name="actividad", on_delete=models.PROTECT, blank=True, null=True
    )
    dieta= models.ForeignKey(
        Dieta, related_name="actividad", on_delete=models.PROTECT, blank=True, null=True     
    )
    dias_entrenamiento=models.DateField
    dias_descanso=models.DateField
    duracion_ejercicio= models.DurationField
    repeticiones=models.IntegerField(default=0)
    tiempo_descanso=models.DurationField
    cantidad_series=models.IntegerField(default=0)
    peso=models.FloatField(default=0)


class Cliente(models.Model):
    entrenador=models.ForeignKey(
        'self', related_name="cliente", on_delete=models.PROTECT, blank=True, null=True 
    )
    rutina= models.ForeignKey(
        Rutina, related_name="cliente", on_delete=models.PROTECT, blank=True, null=True
    )
    suscripcion=models.ForeignKey(
        Suscripcion, related_name="cliente", on_delete=models.PROTECT, blank=True, null=True
    )
    medidas_corporales= models.ForeignKey(
        MedidasCorporales, related_name="cliente", on_delete=models.PROTECT, blank=True, null=True
    )
    nombre= models.CharField(max_length=10, blank=True, null=True)
    edad= models.IntegerField(default=0)
    genero = models.CharField(max_length=30 ,choices=GENDER_CHOICES)
    foto= models.ImageField(upload_to="media/foto/",default="cliente.png",blank=True,null=True,
    )
    
    def __str__(self):
        return self.nombre + " " + str(self.suscripcion.fecha_vencimiento)