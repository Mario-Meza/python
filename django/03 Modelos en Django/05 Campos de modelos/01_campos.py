# app/models.py
from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=50)

class Producto(models.Model):
    cantidad = models.IntegerField()

class Publicacion(models.Model):
    fechapublicacion = models.DateField()