from django.urls import path

from app1.views import *

urlpatterns = [
    path('', Ejemplo),

    path('cursos/', listaCursos, name='cursos'),

    path('alumno/', listaAlumnos, name='alumno'),

    path('agregarAlumnos/', agregarAlumnos, name='agregarAlumnos'),

    path('editarAlumnos/<rut_alumno>', editarAlumnos, name='editarAlumnos'),

]
