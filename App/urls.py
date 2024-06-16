from django.urls import path
from App.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('nuevos/', nuevos, name="Nuevos"),

    # CRUD de Profesionales
    path('lista-profesionales/', ProfesionalList.as_view(), name="ListaProfesionales"),
    path('detalle-profesionales/<pk>', ProfesionalDetail.as_view(), name="DetalleProfesional"),
    path('crear-profesionales/', ProfesionalCreate.as_view(), name="CrearProfesional"),
    path('actualizar-profesionales/<pk>', ProfesionalUpdate.as_view(), name="ActualizarProfesional"),
    path('eliminar-profesionales/<pk>', ProfesionalDelete.as_view(), name="EliminarProfesional"),
    # Buscar Profesionales
    path('resultados-profesionales/', resultados_profesionales, name="ResultadosProfesionales"),

    # CRUD de Proyectos
    path('lista-proyectos/', ProyectoList.as_view(), name="ListaProyectos"),
    path('detalle-proyectos/<pk>', ProyectoDetail.as_view(), name="DetalleProyecto"),
    path('crear-proyectos/', ProyectoCreate.as_view(), name="CrearProyecto"),
    path('actualizar-proyectos/<pk>', ProyectoUpdate.as_view(), name="ActualizarProyecto"),
    path('eliminar-proyectos/<pk>', ProyectoDelete.as_view(), name="EliminarProyecto"),
    # Buscar Proyectos
    path('resultados-proyectos/', resultados_proyectos, name="ResultadosProyectos"),

    # CRUD de Socios
    path('lista-socios/', SocioList.as_view(), name="ListaSocios"),
    path('detalle-socios/<pk>', SocioDetail.as_view(), name="DetalleSocio"),
    path('crear-socios/', SocioCreate.as_view(), name="CrearSocio"),
    path('actualizar-socios/<pk>', SocioUpdate.as_view(), name="ActualizarSocio"),
    path('eliminar-socios/<pk>', SocioDelete.as_view(), name="EliminarSocio"),
    # Buscar Socios
    path('resultados-socios/', resultados_socios, name="ResultadosSocios"),

    # CRUD de Clientes
    path('lista-clientes/', ClienteList.as_view(), name="ListaClientes"),
    path('detalle-clientes/<pk>', ClienteDetail.as_view(), name="DetalleCliente"),
    path('crear-clientes/', ClienteCreate.as_view(), name="CrearCliente"),
    path('actualizar-clientes/<pk>', ClienteUpdate.as_view(), name="ActualizarCliente"),
    path('eliminar-clientes/<pk>', ClienteDelete.as_view(), name="EliminarCliente"),
    # Buscar Clientes
    path('resultados-clientes/', resultados_clientes, name="ResultadosClientes"),
]