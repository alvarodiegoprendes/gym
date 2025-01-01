from django.contrib import admin
from . import models
from user import models



# Register your models here.

class AlimentoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['nombre', 'calorias',
                    'proteinas', 'carbohidratos', 'grasas']



admin.site.register(models.Suscripcion)
admin.site.register(models.Alimento,AlimentoAdmin)
admin.site.register(models.MedidaCorporal)
admin.site.register(models.Rutina)
admin.site.register(models.Gramaje)
admin.site.register(models.Dieta)
admin.site.register(models.Area)
admin.site.register(models.Ejercicios)
admin.site.register(models.Actividad)


class AdministracionGym(admin.AdminSite):
    site_header = 'Administracion Gym'
    site_title = 'Administracion superuser'
    index_title= 'Administracion del sitio'

administracion_gym=AdministracionGym(name='gym')
administracion_gym.register(models.Suscripcion)
administracion_gym.register(models.Alimento,AlimentoAdmin)
administracion_gym.register(models.MedidaCorporal)
administracion_gym.register(models.Rutina)
administracion_gym.register(models.Gramaje)
administracion_gym.register(models.Dieta)
administracion_gym.register(models.Area)
administracion_gym.register(models.Ejercicios)
administracion_gym.register(models.Actividad)
administracion_gym.register(models.Cuenta)