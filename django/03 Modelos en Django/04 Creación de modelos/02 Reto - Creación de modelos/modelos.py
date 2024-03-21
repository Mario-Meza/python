# alumnos/models.py
from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=200)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=300)
    curso = models.CharField(max_length=50)


class Profesor(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.EmailField()
    materia = models.CharField(max_length=100)



class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    creditos = models.IntegerField()


class Inscripcion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    asignaturas = models.ManyToManyField(Asignatura)

