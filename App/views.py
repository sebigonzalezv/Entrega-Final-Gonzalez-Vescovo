from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def inicio(req):
    return HttpResponse("Pantalla inicio")

def profesionales(req):
    return HttpResponse("Pantalla profesionales")

def proyectos(req):
    return HttpResponse("Pantalla proyectos")

def socios(req):
    return HttpResponse("Pantalla socios")

def clientes(req):
    return HttpResponse("Pantalla clientes")