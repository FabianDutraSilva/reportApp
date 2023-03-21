from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('lista/', views.lista),
    path('reporte/<int:id>', views.reporte),
    path('reporte/', views.reporte)
]