from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

# View del inicio de la página web
def inicio(req):
    return render(req, "inicio.html", {})

# CRUD de Profesionales
class ProfesionalList(ListView):
    model = Profesional
    template_name = "profesional_list.html"
    context_object_name = "profesionales"
class ProfesionalDetail(DetailView):
    model = Profesional
    template_name = "profesional_detail.html"
    context_object_name = "profesional"
class ProfesionalCreate(CreateView):
    model = Profesional
    template_name = "profesional_create.html"
    fields = ('__all__')
    success_url = "/app/lista-profesionales"
class ProfesionalUpdate(UpdateView):
    model = Profesional
    template_name = "profesional_update.html"
    fields = ('__all__')
    success_url = "/app/lista-profesionales"
    context_object_name = "profesional"
class ProfesionalDelete(DeleteView):
    model = Profesional
    template_name = "profesional_delete.html"
    success_url = "/app/lista-profesionales"
    context_object_name = "profesional"

# CRUD de Proyectos
class ProyectoList(ListView):
    model = Proyecto
    template_name = "proyecto_list.html"
    context_object_name = "proyectos"
class ProyectoDetail(DetailView):
    model = Proyecto
    template_name = "proyecto_detail.html"
    context_object_name = "proyecto"
class ProyectoCreate(CreateView):
    model = Proyecto
    template_name = "proyecto_create.html"
    fields = ('__all__')
    success_url = "/app/lista-proyectos"
class ProyectoUpdate(UpdateView):
    model = Proyecto
    template_name = "proyecto_update.html"
    fields = ('__all__')
    success_url = "/app/lista-proyectos"
    context_object_name = "proyecto"
class ProyectoDelete(DeleteView):
    model = Proyecto
    template_name = "proyecto_delete.html"
    success_url = "/app/lista-proyectos"
    context_object_name = "proyecto"

# CRUD de Socios
class SocioList(ListView):
    model = Socio
    template_name = "socio_list.html"
    context_object_name = "socios"
class SocioDetail(DetailView):
    model = Socio
    template_name = "socio_detail.html"
    context_object_name = "socio"
class SocioCreate(CreateView):
    model = Socio
    template_name = "socio_create.html"
    fields = ('__all__')
    success_url = "/app/lista-socios"
class SocioUpdate(UpdateView):
    model = Socio
    template_name = "socio_update.html"
    fields = ('__all__')
    success_url = "/app/lista-socios"
    context_object_name = "socio"
class SocioDelete(DeleteView):
    model = Socio
    template_name = "socio_delete.html"
    success_url = "/app/lista-socios"
    context_object_name = "socio"

# CRUD de Clientes
class ClienteList(ListView):
    model = Cliente
    template_name = "cliente_list.html"
    context_object_name = "clientes"
class ClienteDetail(DetailView):
    model = Cliente
    template_name = "cliente_detail.html"
    context_object_name = "cliente"
class ClienteCreate(CreateView):
    model = Cliente
    template_name = "cliente_create.html"
    fields = ('__all__')
    success_url = "/app/lista-clientes"
class ClienteUpdate(UpdateView):
    model = Cliente
    template_name = "cliente_update.html"
    fields = ('__all__')
    success_url = "/app/lista-clientes"
    context_object_name = "cliente"
class ClienteDelete(DeleteView):
    model = Cliente
    template_name = "cliente_delete.html"
    success_url = "/app/lista-clientes"
    context_object_name = "cliente"

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
        return render(req, "profesional_result.html", {"especialidad": especialidad, "nombre": nombre, "apellido": apellido, "mail": mail})       
    else:
        return render(req, "respuestas.html", {"message": "No completaste el formulario."})

def resultados_proyectos(req):
    if req.GET["nombre"]:
        nombre = req.GET["nombre"]
        ubicacion = Proyecto.objects.filter(nombre__icontains=nombre)
        tipo = Proyecto.objects.filter(nombre__icontains=nombre)
        fecha_ejecucion = Proyecto.objects.filter(nombre=nombre)
        return render(req, "proyecto_result.html", {"nombre": nombre, "ubicacion": ubicacion, "tipo": tipo, "fecha_ejecucion": fecha_ejecucion})       
    else:
        return render(req, "respuestas.html", {"message": "No completaste el formulario."})

def resultados_socios(req):
    if req.GET["especialidad"]:
        especialidad = req.GET["especialidad"]
        empresa = Socio.objects.filter(especialidad__icontains=especialidad)
        mail = Socio.objects.filter(especialidad__icontains=especialidad)
        return render(req, "socio_result.html", {"empresa": empresa, "especialidad": especialidad, "mail": mail})       
    else:
        return render(req, "respuestas.html", {"message": "No completaste el formulario."})

def resultados_clientes(req):
    if req.GET["especialidad"]:
        especialidad = req.GET["especialidad"]
        empresa = Cliente.objects.filter(especialidad__icontains=especialidad)
        mail = Cliente.objects.filter(especialidad__icontains=especialidad)
        return render(req, "cliente_result.html", {"empresa": empresa, "especialidad": especialidad, "mail": mail})       
    else:
        return render(req, "respuestas.html", {"message": "No completaste el formulario."})