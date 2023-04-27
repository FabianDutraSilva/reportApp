from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('reportes/', views.reportes),
    path('reporte/', views.reporte),
    path('reporte/<int:id>', views.reporte),
    path('equipos/', views.equipos),
    path('equipo/', views.equipo),
    path('equipo/<int:id>', views.equipo),
    path('confirmar_borrar_reporte/<int:id>', views.confirmar_borrar_reporte),
    path('confirmar_borrar_equipo/<int:id>', views.confirmar_borrar_equipo),
    path('borrar_reporte/<int:id>', views.borrar_reporte),
    path('borrar_equipo/<int:id>', views.borrar_equipo),
    path('login/', views.loginPage),
    path('logout/', views.logoutPage),
    path('registro/', views.registro)
]