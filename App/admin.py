from django.contrib import admin
from .models import *

# Registro de los modelos en el panel de administración

admin.site.register(Profesional)
admin.site.register(Proyecto)
admin.site.register(Socio)
admin.site.register(Cliente)
admin.site.register(Nuevo)
admin.site.register(Avatar)