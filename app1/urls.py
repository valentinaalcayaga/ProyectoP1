from django.urls import path

from app1.views import *




urlpatterns = [
    path('', Ejemplo, name='Ejemplo'),

    path('asignaturas/', listaAsignaturas, name='asignaturas'),

    path('alumno/', listaAlumnos, name='alumno'),

    path('agregarAlumnos/', agregarAlumnos, name='agregarAlumnos'),

    path('editarAlumnos/<rut_alumno>', editarAlumnos, name='editarAlumnos'),

    path('eliminarAlumnos/<rut_alumno>', eliminarAlumnos, name='eliminarAlumnos'),

    path('notas/', listaNotas, name='notas'),

    path('registroUsuarios/', registro_usuarios1, name='registro1'),

    path('asistencia/', listaAsistencia, name='asistencia'),

]
