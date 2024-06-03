from django import forms

class NuevosFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    especialidad = forms.CharField(max_length=30)
    años_de_experiencia = forms.IntegerField()
    mail = forms.EmailField()