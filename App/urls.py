from django.urls import path
from App.views import inicio, profesionales, proyectos, socios, clientes

urlpatterns = [
    path('', inicio),
    path('profesionales/', profesionales), 
    path('proyectos/', proyectos),
    path('socios/', socios),
    path('clientes/', clientes),
]