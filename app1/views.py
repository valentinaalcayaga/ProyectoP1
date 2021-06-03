from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app1.models import Alumno


def Ejemplo(request):
    return render(request, "home.html")


def Ejemplo2(request):
    return render(request, 'nuevo.html')


def listaAlumnos(request):
    datos = {'listaAlumnos': Alumno.objects.all()}
    return render(request, 'alumno.html', datos)
