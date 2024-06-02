from django.db import models

# Create your models here.

class Profesionales(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=30)
    años_experiencia = models.IntegerField()
    mail = models.EmailField()

class Proyectos(models.Model):
    nombre = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=30)
    tipo = models.CharField(max_length=60)
    fecha_ejecucion = models.IntegerField()

class Socios(models.Model):
    empresa = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=30)
    mail = models.EmailField()

class Clientes(models.Model):
    empresa = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=30)
    mail = models.EmailField()




