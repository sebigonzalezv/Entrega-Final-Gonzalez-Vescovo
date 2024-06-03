from django.urls import path
from App.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('profesionales/', profesionales, name="Profesionales"), 
    path('proyectos/', proyectos, name="Proyectos"),
    path('socios/', socios, name="Socios"),
    path('clientes/', clientes, name="Clientes"),
    path('nuevos/', nuevos, name="Nuevos"),
    path('resultados-profesionales/', resultados_profesionales, name="ResultadosProfesionales"),
    path('resultados-proyectos/', resultados_proyectos, name="ResultadosProyectos"),
    path('resultados-socios/', resultados_socios, name="ResultadosSocios"),
    path('resultados-clientes/', resultados_clientes, name="ResultadosClientes"),
]