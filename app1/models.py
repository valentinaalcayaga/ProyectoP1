from django.db import models


# Create your models here.

class Usuario(models.Model):
    rut = models.CharField(max_length=12, null=False, blank=False, primary_key=True, verbose_name="Ingrese rut sin -")
    correo = models.CharField(max_length=50, null=False, blank=False, verbose_name="Ingrese correo")
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
    pass

    def __str__(self):
        return self.nombre


class Asignatura(models.Model):
    codigo = models.CharField(max_length=5, null=False, blank=False, primary_key=True)
    nombreAsignatura = models.CharField(max_length=20, null=False, blank=False)
    profesor = models.ForeignKey(Profesor, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.codigo + " - " + self.nombreAsignatura + " - " + self.profesor.nombre



class Notas(models.Model):
    PRUEBA = '01'
    CONTROL = '02'
    TALLER = '03'
    DIAGNOSTICO = '04'

    EVALUACIONES_CHOICES = [
        (PRUEBA, 'Prueba'),
        (CONTROL, 'Control'),
        (TALLER, 'Taller'),
        (DIAGNOSTICO, 'Diagnostico'),
    ]

    alumno = models.ForeignKey(Alumno, null=True, on_delete=models.SET_NULL, verbose_name='Alumno')
    asignatura = models.ForeignKey(Asignatura, null=True, on_delete=models.SET_NULL, verbose_name='Asignatura')
    evaluacion = models.CharField(max_length=15, blank=True, null=True, verbose_name='Evaluación',
                                  choices=EVALUACIONES_CHOICES, default=None)
    nota_1 = models.FloatField(blank=True, null=True, verbose_name='Nota 1')
    nota_2 = models.FloatField(blank=True, null=True, verbose_name='Nota 2')
    nota_3 = models.FloatField(blank=True, null=True, verbose_name='Nota 3')
    nota_4 = models.FloatField(blank=True, null=True, verbose_name='Nota 4')
    nota_5 = models.FloatField(blank=True, null=True, verbose_name='Nota 5')
    nota_6 = models.FloatField(blank=True, null=True, verbose_name='Nota 6')
    promedio = models.FloatField(blank=True, null=True, verbose_name='Promedio')

    def __str__(self):
        return self.alumno.rut + " - " + self.alumno.nombre + " - " + self.evaluacion


class Curso(models.Model):
    nombreCurso = models.CharField(max_length=10, null=False, blank=False, primary_key=True)
    alumnos = models.ForeignKey(Alumno, null=True, on_delete=models.SET_NULL)

class Asistencia(models.Model):
    fecha = models.DateTimeField(primary_key= True, blank=False, verbose_name='Fecha')
    opasistir = [("1", "presente"), ("2", "ausente")]
    asistir = models.CharField(max_length=20, blank=False, null=True, choices=opasistir, verbose_name='Asistencia')
    alumno = models.ForeignKey(Alumno, null=True, on_delete=models.SET_NULL, verbose_name='Alumno')
    asignatura = models.ForeignKey(Asignatura, null=True, on_delete=models.SET_NULL, verbose_name='Asignatura')