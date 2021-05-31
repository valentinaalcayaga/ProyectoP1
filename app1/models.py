from django.db import models

# Create your models here.

class Usuario (models.Model):
    correo = models.CharField(max_length=50, null=False, blank=False, primary_key=True, verbose_name= "Ingrese correo")
    nombre = models.CharField(max_length=50, null=False, blank=False, verbose_name= "Ingrese nombre completo")
    contraseña = models.CharField(max_length=50, null=False, blank=False)



class Administrador (models.Model):
    correo = models.ForeignKey(Usuario, null=True, on_delete=models.SET_NULL)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    contraseña = models.CharField(max_length=50, null=False, blank=False)


class Profesor (models.Model):
    correo = models.ForeignKey(Usuario, null=True, on_delete=models.SET_NULL)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    contraseña = models.CharField(max_length=50, null=False, blank=False)

    curso = models.CharField(max_length=50, null=False, blank=False)
    asignatura = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return (self.nombre + " - " + self.curso)


class Alumno (models.Model):
    correo = models.ForeignKey(Usuario, null=True, on_delete=models.SET_NULL)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    notas = models.CharField(max_length=50, null=False, blank=False)
    asistencia = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return (self.nombre + " - " + self.nombrecurso)


class Asignatura(models.Model):
    codigo = models.CharField(max_length=5, null=False, blank=False, primary_key=True)
    nombre = models.CharField(max_length=20, null=False, blank=False)

    profesor = models.ForeignKey(Profesor, null= True, on_delete= models.SET_NULL() )

    def __str__(self):
        return (self.codigo + " - " + self.nombre + " - " + self.profesor.nombre)



class Curso (models.Model):
    nombrecurso = models.CharField(max_length=10, null=False, blank=False, primary_key=True)

    alumnos =  models.ForeignKey(Alumno, null= True, on_delete= models.SET_NULL() )


