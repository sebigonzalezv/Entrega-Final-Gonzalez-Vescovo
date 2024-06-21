from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

# View del inicio de la página web
def inicio(req):
    try:
        avatar = Avatar.objects.get(user=req.user.id)
        return render(req, "inicio.html", {"url": avatar.imagen.url})
    except:
        return render(req, "inicio.html")

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

# View del Login de la página web
def login_view(req):
    
    if req.method == 'POST':
        miFormulario = AuthenticationForm(req, data=req.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]
            user = authenticate(username=usuario, password=psw)

            if user:
                login(req, user)
                return render(req, "respuestas.html", {"message": f"Bienvenido/a, {usuario}!"}) 
            
            else:
                return render(req, "respuestas.html", {"message": "Datos incorrectos."})                  

        else:
            return render(req, "respuestas.html", {"message": "Datos inválidos."})              

    else:
        miFormulario = AuthenticationForm()
        return render(req, "login.html", {"miFormulario": miFormulario})

# View del Registro de la página web
def register(req):
    
    if req.method == 'POST':
        miFormulario = UserCreationForm(req.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data["username"]
            miFormulario.save()
            return render(req, "respuestas.html", {"message": f"Usuario {usuario} creado con éxito!"})                  

        else:
            return render(req, "respuestas.html", {"message": "Datos inválidos."})              

    else:
        miFormulario = UserCreationForm()
        return render(req, "register.html", {"miFormulario": miFormulario})

# View para editar el perfil del usuario
@login_required
def edit(req):
    usuario = req.user

    if req.method == 'POST':
        miFormulario = UserEditForm(req.POST, instance=req.user)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])
            usuario.save()
            return render(req, "respuestas.html", {"message": "Datos actualizados con éxito."})  

        else:
            return render(req, "edit.html", {"miFormulario": miFormulario})            

    else:
        miFormulario = UserEditForm(instance=req.user)
        return render(req, "edit.html", {"miFormulario": miFormulario})

# View para agregar un avatar
@login_required
def add_avatar(req):
    
    if req.method == 'POST':
        miFormulario = AvatarFormulario(req.POST, req.FILES)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            avatar = Avatar(user=req.user, imagen=data["imagen"])
            avatar.save()
            return render(req, "respuestas.html", {"message": "Avatar cargado con éxito."})  

        else:
            return render(req, "respuestas.html", {"message": "Datos inválidos."})            

    else:
        miFormulario = AvatarFormulario()
        return render(req, "add_avatar.html", {"miFormulario": miFormulario})