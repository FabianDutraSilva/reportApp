from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('incidentes/', views.incidentes),
    path('reporte/<int:id>', views.reporte),
    path('reporte/', views.reporte),
    path('equipos/', views.equipos),
    path('agregar-equipo/', views.agregar_equipo),
    path('agregar-equipo/<int:id>', views.agregar_equipo)
]