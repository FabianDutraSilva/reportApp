from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ubicacion(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    clasificacion1 = models.CharField(max_length=200)
    clasificacion2 = models.CharField(max_length=200)
    centroCosto = models.CharField(max_length=200)
    prioridad = models.CharField(max_length=200)
    parteDe = models.CharField(max_length=200)
    def __str__(self):
        return str(self.nombre)

class Equipo(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    serie = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    centroCosto = models.CharField(max_length=200)
    prioridad = models.CharField(max_length=200)
    parteDe = models.CharField(max_length=200)
    def __str__(self):
        return str(self.nombre)

class Rrhh(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    nominal = models.PositiveSmallIntegerField()
    extra = models.PositiveSmallIntegerField()
    def __str__(self):
        return str(self.nombre + ' ' + self.apellido)

class Causa(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    causa = models.CharField(max_length=50)
    def __str__(self):
        return str(self.causa)

class Tipo(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=50)
    def __str__(self):
        return str(self.tipo)

class Reporte(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200)
    equipo = models.CharField(max_length=200)
    clase = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    descripcion = models.TextField()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return str(self.descripcion)
