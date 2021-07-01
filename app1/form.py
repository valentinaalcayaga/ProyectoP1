from django.forms import ModelForm
from .models import *


class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = ['rut', 'correo', 'nombre', 'asistencia', 'contraseña']
