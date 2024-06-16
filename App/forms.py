from django import forms

# Formulario para enviar información a la Base de Datos (nuevos)

class NuevosFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    especialidad = forms.CharField(max_length=30)
    experiencia = forms.IntegerField()
    mail = forms.EmailField()