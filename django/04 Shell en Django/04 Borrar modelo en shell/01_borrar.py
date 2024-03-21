from blog.models import Autor

autor = Autor.objects.filter(nombre="Pedro")[0]
autor.blog_set.create(titulo="¿Qué es JavaScript?", contenido="Este blog describe JavaScript")
autor.blog_set.all()

autor.delete()

# borrar todo
Autor.objects.delete()