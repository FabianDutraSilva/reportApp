from django.db import models

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
        return self.nombre

class Activo(models.Model):
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
        return self.nombre

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
        return self.nombre + ' ' + self.apellido

class Causa(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    causa = models.CharField(max_length=50)
    def __str__(self):
        return self.causa

class Tipo(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=50)
    def __str__(self):
        return self.tipo

class Reporte(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    ubicacion = models.CharField(max_length=200)
    equipo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    causa = models.CharField(max_length=200)
    rrhh = models.CharField(max_length=200)
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    def __str__(self):
        return self.reporte