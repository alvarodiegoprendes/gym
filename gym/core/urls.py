from django.urls import include, path
from . import views

urlpatterns = [
    #path( "<int:dia>", views.saludar_numero),
    #path( "<str:dia>", views.saludar),
    path('crear_rutina/', views.crear_rutina, name="crear_rutina"),

    path('crear_actividad/', views.crear_actividad, name='crear_actividad'),
    path('crear_dieta/', views.crear_dieta, name='crear_dieta'),
    #path('asignar_gramajes/<int:dieta_id>/', views.asignar_gramajes, name='asignar_gramajes'),
    path('mostrar_alimentos/',views.mostrar_alimentos,name='mostrar_alimentos'),
    path('asignar_gramajes/', views.asignar_gramaje, name='asignar_gramajes'),
    path('mostrar_rutinas/',views.RutinaListView.as_view(),name='mostrar_rutinas'),


]