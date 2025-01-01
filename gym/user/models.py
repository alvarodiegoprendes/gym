from django.contrib.auth.models import AbstractUser
from core.models import *
from django.db import models
# Create your models here.


GENDER_CHOICES = (("male", "MALE"), ("female", "FEMALE"))


class Cuenta(AbstractUser):
    entrenador = models.ForeignKey(
        'self', on_delete=models.PROTECT, blank=True, null=True
    )
    rutina = models.ForeignKey(
        Actividad, on_delete=models.PROTECT, blank=True, null=True
    )
    suscripcion = models.ForeignKey(
        Suscripcion, on_delete=models.PROTECT, blank=True, null=True
    )
    medidas_corporales = models.ForeignKey(
        MedidaCorporal, on_delete=models.PROTECT, blank=True, null=True
    )
    es_entrenador = models.BooleanField(default=False)
    edad = models.IntegerField(default=0)
    genero = models.CharField(max_length=30, choices=GENDER_CHOICES)
    foto = models.ImageField(upload_to="static/gym/fotos/", default="static/gym/fotos/cliente.png", blank=False, null=True,)

    def __str__(self):
        return self.username