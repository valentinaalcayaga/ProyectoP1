from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from gunicorn.config import User

from .models import *


class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = ['rut', 'correo', 'nombre', 'asistencia', 'contraseña']


