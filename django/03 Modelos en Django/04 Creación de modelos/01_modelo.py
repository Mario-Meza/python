# modelo
from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()


# choices
PROVINCIAS = (
    ('GR', 'Granada'),
    ('MD', 'Madrid')
)

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    provincia = models.CharField(max_length=2, choices=PROVINCIAS)