from django.db import models

# Create your models here.

class Profesional(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=30)
    años_de_experiencia = models.IntegerField()
    mail = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"
    
    class Meta():
        verbose_name_plural = 'Profesionales'

class Proyecto(models.Model):
    nombre = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=30)
    tipo = models.CharField(max_length=60)
    fecha_ejecucion = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.ubicacion} - {self.fecha_ejecucion}"
    
    class Meta():
        ordering = ('fecha_ejecucion', 'nombre', 'ubicacion', 'tipo')
        unique_together = ('nombre', 'ubicacion')

class Socio(models.Model):
    empresa = models.CharField(max_length=30, unique=True)
    especialidad = models.CharField(max_length=30)
    mail = models.EmailField()

    def __str__(self):
        return f"{self.empresa} - {self.especialidad}"

class Cliente(models.Model):
    empresa = models.CharField(max_length=30, unique=True)
    especialidad = models.CharField(max_length=30)
    mail = models.EmailField()

    def __str__(self):
        return f"{self.empresa} - {self.especialidad}"

class Nuevo(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=30)
    años_de_experiencia = models.IntegerField()
    mail = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"