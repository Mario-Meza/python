# blog/models.py
# relación de uno a uno
from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.EmailField()

class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)


# relación de muchos a muchos
class Autor(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.EmailField()

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=30)

class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    etiquetas = models.ManyToManyField(Etiqueta)

# instalar app
# settings.py
INSTALLED_APPS = [
    'blog'
]