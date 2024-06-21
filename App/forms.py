from django import forms
from .models import Avatar
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


# Formulario para enviar información a la Base de Datos (nuevos)
class NuevosFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    especialidad = forms.CharField(max_length=30)
    experiencia = forms.IntegerField()
    mail = forms.EmailField()

# Formulario para editar el perfil de usuario
class UserEditForm(UserChangeForm):  
    
    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )
    
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

    def clean_password2(self):
        print(self.cleaned_data)
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2

# Formulario para agregar un avatar
class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ("imagen", )