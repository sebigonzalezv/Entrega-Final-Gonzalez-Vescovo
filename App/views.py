from django.shortcuts import render
from .models import *
from .forms import *

# Views de las diferentes partes de la página web

def inicio(req):
    return render(req, "inicio.html", {})

def profesionales(req):
    return render(req, "profesionales.html", {})

def proyectos(req):
    return render(req, "proyectos.html", {})

def socios(req):
    return render(req, "socios.html", {})

def clientes(req):
    return render(req, "clientes.html", {})

# La view 'nuevos' será diferente si el request es del tipo POST o GET
# En caso de ser POST se están enviando datos a través del formulario
# En caso de ser GET se está intentando visualizar esa parte de la página web

def nuevos(req):

    if req.method == 'POST':
        miFormulario = NuevosFormulario(req.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            nuevo = Nuevo(nombre=data['nombre'], apellido=data['apellido'], especialidad=data['especialidad'], anos_de_experiencia=data['anos_de_experiencia'], mail=data['mail'])
            nuevo.save()
            return render(req, "respuestas.html", {"message": "¡Solicitud enviada con éxito!"})

        else:
            return render(req, "respuestas.html", {"message": "Datos inválidos, inténtelo nuevamente."})            

    else:
        miFormulario = NuevosFormulario()
        return render(req, "nuevos.html", {"miFormulario": miFormulario})

# Views de los resultados de la búsqueda con los formularios para las diferentes partes de la página web
# Uso de '__icontains' para hacer una búsqueda que no distinga entre mayúsculas y minúsculas y que permitan coincidencias parciales

def resultados_profesionales(req):

    if req.GET["especialidad"]:
        especialidad = req.GET["especialidad"]
        nombre = Profesional.objects.filter(especialidad__icontains=especialidad)
        apellido = Profesional.objects.filter(especialidad__icontains=especialidad)
        mail = Profesional.objects.filter(especialidad__icontains=especialidad)        
        return render(req, "resultados_profesionales.html", {"especialidad": especialidad, "nombre": nombre, "apellido": apellido, "mail": mail})       

    else:
        return render(req, "respuestas.html", {"message": "No completaste el formulario."})

def resultados_proyectos(req):

    if req.GET["nombre"]:
        nombre = req.GET["nombre"]
        ubicacion = Proyecto.objects.filter(nombre__icontains=nombre)
        tipo = Proyecto.objects.filter(nombre__icontains=nombre)
        fecha_ejecucion = Proyecto.objects.filter(nombre=nombre)
        return render(req, "resultados_proyectos.html", {"nombre": nombre, "ubicacion": ubicacion, "tipo": tipo, "fecha_ejecucion": fecha_ejecucion})       

    else:
        return render(req, "respuestas.html", {"message": "No completaste el formulario."})

def resultados_socios(req):

    if req.GET["empresa"]:
        empresa = req.GET["empresa"]
        especialidad = Socio.objects.filter(empresa__icontains=empresa)
        mail = Socio.objects.filter(empresa__icontains=empresa)
        return render(req, "resultados_socios.html", {"empresa": empresa, "especialidad": especialidad, "mail": mail})       

    else:
        return render(req, "respuestas.html", {"message": "No completaste el formulario."})

def resultados_clientes(req):

    if req.GET["empresa"]:
        empresa = req.GET["empresa"]
        especialidad = Cliente.objects.filter(empresa__icontains=empresa)
        mail = Cliente.objects.filter(empresa__icontains=empresa)
        return render(req, "resultados_clientes.html", {"empresa": empresa, "especialidad": especialidad, "mail": mail})       

    else:
        return render(req, "respuestas.html", {"message": "No completaste el formulario."})