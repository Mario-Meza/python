# filtrar
from blog.models import Autor
Autor.objects.filter(nombre="Juan")

# filtro avanzado
from holamundo.models import Producto

Producto(cantidad=99).save()
Producto(cantidad=101).save()
Producto.objects.all()

Producto.objects.filter(cantidad__gt=100)[0].cantidad
Producto.objects.filter(cantidad__lt=100)[0].cantidad