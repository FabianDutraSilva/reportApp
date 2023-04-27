from django.urls import path
from . import views

urlpatterns = [
    path('', views.routes),
    path('reportes/', views.reportes),
    path('reporte/<int:id>', views.reporte)
]
