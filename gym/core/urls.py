from django.urls import path
from . import views

urlpatterns = [
    #path( "<int:dia>", views.saludar_numero),
    #path( "<str:dia>", views.saludar),
    path( "hola/", views.hola)
]