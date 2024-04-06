from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Cliente)
admin.site.register(models.Suscripcion)
admin.site.register(models.Alimentos)
admin.site.register(models.MedidasCorporales)
admin.site.register(models.Rutina)

