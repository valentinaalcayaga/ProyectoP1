from django.db import models


# Create your models here.

class Usuario(models.Model):
    correo = models.CharField(max_length=50, null=False, blank=False, primary_key=True, verbose_name="Ingrese correo")
    nombre = models.CharField(max_length=50, null=False, blank=False, verbose_name="Ingrese nombre completo")
    contraseña = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        abstract = True


class Administrador(Usuario):
    pass

    def __str__(self):
        return self.nombre


class Profesor(Usuario):
    curso = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nombre + " - " + self.curso


class Alumno(Usuario):
    notas = models.CharField(max_length=50, null=False, blank=False)
    asistencia = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nombre


class Asignatura(models.Model):
    codigo = models.CharField(max_length=5, null=False, blank=False, primary_key=True)
    nombreAsignatura = models.CharField(max_length=20, null=False, blank=False)

    profesor = models.ForeignKey(Profesor, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.codigo + " - " + self.nombreAsignatura + " - " + self.profesor.nombre


class Curso(models.Model):
    nombreCurso = models.CharField(max_length=10, null=False, blank=False, primary_key=True)
    alumnos = models.ForeignKey(Alumno, null=True, on_delete=models.SET_NULL)
