from django.db import models
from django.contrib.auth.models import User

# Modelos relacionados la proyecto

class Profesional(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    anos_de_experiencia = models.IntegerField(verbose_name="Años de experiencia")
    mail = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"
    
    class Meta():
        verbose_name_plural = 'Profesionales'

class Proyecto(models.Model):
    nombre = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
    tipo = models.CharField(max_length=100)
    fecha_ejecucion = models.IntegerField(verbose_name="Fecha de ejecución")
    imagen = models.ImageField(upload_to='proyectos', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.ubicacion} - {self.fecha_ejecucion}"
    
    class Meta():
        ordering = ('fecha_ejecucion', 'nombre', 'ubicacion', 'tipo')
        unique_together = ('nombre', 'ubicacion')

class Socio(models.Model):
    empresa = models.CharField(max_length=50, unique=True)
    especialidad = models.CharField(max_length=50)
    mail = models.EmailField()

    def __str__(self):
        return f"{self.empresa} - {self.especialidad}"

class Cliente(models.Model):
    empresa = models.CharField(max_length=50, unique=True)
    especialidad = models.CharField(max_length=50)
    mail = models.EmailField()

    def __str__(self):
        return f"{self.empresa} - {self.especialidad}"

class Nuevo(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    anos_de_experiencia = models.IntegerField()
    mail = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null=True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"