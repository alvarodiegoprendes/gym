from django.urls import path
from . import views

urlpatterns = [
    #path( "<int:dia>", views.saludar_numero),
    #path( "<str:dia>", views.saludar),
    path( "alimentos/", views.mostrar_alimentos, name="alimentos"),
    path( "rutina/", views.mostrar_rutina, name="rutina")
    
]