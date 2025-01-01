from django.db import models
import datetime

from django.urls import reverse_lazy

# Create your models here.

GENDER_CHOICES = (("male", "MALE"), ("female", "FEMALE"))
TIPO_EJERCICIO = (("fuera", "fuerza"),("cardio","cardio"),("elasticidad","elasticidad"))

class Suscripcion(models.Model):
    fecha_inscripcion = models.DateField (blank=False, null=True)
    fecha_vencimiento = models.DateField (blank=False, null=True)
    importe = models.FloatField(default=0)
    pago = models.FloatField(default=0)

    def __str__(self):
        return str(self.fecha_inscripcion)


class MedidaCorporal(models.Model):
    altura = models.FloatField(default=0,blank=True)
    peso = models.FloatField(default=0,blank=True)
    fecha_medicion = models.DateField (blank=True, null=True)
    porcentaje_grasa = models.FloatField (blank=True, null=True)


class Area(models.Model):
    nombre = models.CharField(blank=True)
    objetivo = models.CharField(blank=True)
    direccion = models.CharField(blank=True)
    descripcion = models.CharField(blank=True)

    def __str__(self):
        return self.nombre


class Ejercicios(models.Model):
    area = models.ForeignKey(
        Area,  on_delete=models.PROTECT, blank=True, null=True
    )
    nombre = models.CharField(blank=False)
    zona_muscular = models.CharField(blank=True)
    equipo_necesario = models.CharField(blank=True)
    foto = models.ImageField(upload_to="static/gym/img",
                             default="static/gym/fotos/cliente.png", blank=True, null=True,)
    tipo_de_ejercicio = models.CharField(blank=True, choices= TIPO_EJERCICIO)  # fuerza, cardio, elasticidad etc
    descripcion = models.CharField(blank=False)

    def __str__(self):
        return self.nombre

    
DIAS_SEMANA = [
    ('LUN', 'Lunes'),
    ('MAR', 'Martes'),
    ('MIE', 'Miércoles'),
    ('JUE', 'Jueves'),
    ('VIE', 'Viernes'),
    ('SAB', 'Sábado'),
    ('DOM', 'Domingo'),
]

class Rutina(models.Model):
    nombre = models.CharField(blank=False)
    dias_entrenamiento = models.CharField(blank=True)
    dias_descanso=models.CharField(blank=True)
    duracion_rutina = models.DurationField(default=datetime.timedelta(days=30), blank=True)
    
    # duracion_ejercicio= models.DurationField
    # repeticiones=models.IntegerField
    # tiempo_descanso=models.DurationField
    # cantidad_series=models.IntegerField
    # peso=models.FloatField
    def __str__(self):
        return self.nombre
    


class Alimento(models.Model):

    nombre = models.CharField(max_length=200, blank=False)
#    especie = models.CharField(max_length=10, blank=False, null=True)
    calorias = models.FloatField(default=0)
    proteinas = models.FloatField(default=0)
    carbohidratos = models.FloatField(default=0)
    grasas = models.FloatField(default=0)

    def __str__(self):
        return self.nombre


class Dieta(models.Model):
   # lista_alimentos=models.ForeignKey(
   #     Gramaje, related_name="dieta", on_delete=models.PROTECT, blank=False, null=True
    # )

    # lista_alimentos=models.ManyToManyField(Gramaje)
    
    #usuario= models.foreinkey(usuario)
    nombre_dieta = models.CharField(max_length=10, blank=False)
    descripcion = models.CharField(max_length=10, blank=False)
    proposito = models.CharField(max_length=10, blank=False)
    fecha_inicio = models.DateField (blank=False, null=True)
    fecha_final = models.DateField (blank=False, null=True)
    duracion = models.DurationField(default=datetime.timedelta(days=30))

    def __str__(self):
        return self.nombre_dieta


class Gramaje(models.Model):

    alimentos = models.ForeignKey(
        Alimento, on_delete=models.PROTECT, blank=False, null=False
    )
    dietas = models.ForeignKey(
        Dieta, on_delete=models.CASCADE, blank= False, null=False
    )

    cantidad = models.FloatField(default=0)
    UNIDAD_CHOICES = [
           ('kg', 'Kilogramos'),
           ('lb', 'Libras'),
           ('g', 'Gramos'),
           # Agrega más unidades si es necesario
       ]
    unidad = models.CharField(max_length=2, choices=UNIDAD_CHOICES, default='g')

    def __str__(self) -> str:
        return self.alimentos.nombre
""" class Gramaje(models.Model):
    alimentos = models.ManyToManyField(Alimentos)
    cantidad = models.FloatField(default=0)

    def set(self, cantidad):
        self.cantidad = cantidad
        self.save() """  # para cuando es relacion many to many


class Records(models.Model):
    ejercicio = models.ForeignKey(
        Ejercicios, on_delete=models.PROTECT, blank=False, null=True
    )
    fecha = models.DateField
    repeticiones = models.IntegerField(default=0)
    peso_alcanzado = models.FloatField(default=0)


class Actividad(models.Model):
    rutina = models.ForeignKey(
        Rutina, on_delete=models.PROTECT, blank=False
    )
    ejercicios = models.ForeignKey(
        Ejercicios, on_delete=models.PROTECT, blank=False
    )
    duracion_ejercicio = models.TimeField(blank=True,null=True, default=datetime.time(0, 0, 0))
    repeticiones = models.IntegerField(blank=True,default=0)
    tiempo_descanso = models.TimeField(blank=True,null=True, default=datetime.time(0, 0, 0))
    cantidad_series = models.IntegerField(blank=True,default=0)
    peso = models.FloatField(blank=True,default=0)
    def __str__(self):

        return self.ejercicios.nombre

