# leer registros
from blog.models import Autor

Autor.objects.all()

# leer atributo
Autor.objects.all()[0].nombre

# leer un registro
autor = Autor.objects.get(pk=1)

# leer atributo
autor.nombre 

# leer modelo relacionado
autor = Autor.objects.get(nombre="Juan")
autor.blog_set.all()
autor.blog_set.count()

# blog/models.py
from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.EmailField()

    # mejora visual
    def __str__(self):
        return f"{self.id} {self.nombre} {self.email}"