# holamundo/models.py
from django.db import models

PROVINCIAS = (
    ('GR', 'Granada'),
    ('MD', 'Madrid')
)

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    provincia = models.CharField(max_length=2, choices=PROVINCIAS)

# settings.py
INSTALLED_APPS = [
    'holamundo'
]