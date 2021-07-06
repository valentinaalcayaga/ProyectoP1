from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from app1.form import *
from app1.models import *


def Ejemplo(request):
    return render(request, "home.html")


def listaCursos(request):
    datos = {'listaCursos': Curso.objects.all()}
    return render(request, 'cursos.html', datos)


def listaAlumnos(request):
    datos = {'listaAlumnos': Alumno.objects.all()}
    return render(request, 'alumno.html', datos)


def agregarAlumnos(request):
    if request.method == "POST":
        formulario = AlumnoForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('alumno')

    else:
        formulario = AlumnoForm()

    datos = {'form': formulario, }
    return render(request, 'agregarAlumnos.html', datos)


def editarAlumnos(request, rut_alumno):
    alumno = Alumno.objects.get(rut=rut_alumno)

    if request.method == "POST":
        formulario = AlumnoForm(request.POST, instance=alumno)

        if formulario.is_valid():
            formulario.save()
            return redirect('alumno')

    else:
        formulario = AlumnoForm(instance=alumno)

    datos = {'form': formulario}
    return render(request, 'editarAlumnos.html', datos)


def eliminarAlumnos(request, rut_alumno):
    alumno = Alumno.objects.get(rut=rut_alumno)
    alumno.delete()
    return redirect('alumno')


def listaNotas(request):
    datos = {'listaNotas': Notas.objects.all()}
    return render(request, 'notas.html', datos)
