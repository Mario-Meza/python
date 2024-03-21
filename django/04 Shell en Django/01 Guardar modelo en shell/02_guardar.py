# guardar modelo
from blog.models import Autor

autor = Autor(nombre="Tu nombre", email="tuemail@gmail.com")
autor.save()

autor = Autor(nombre="Pedro", email="otroemail@gmail.com")
autor.save()

autor = Autor(nombre="Juan", email="juan@gmail.com")
autor.save()

# guardar modelo relacionado
from blog.models import Blog

blog = Blog(titulo="¿Qué es HTML?", contenido="Este blog describe HTML", autor=autor)
blog.save()

# alternativa
autor.blog_set.create(titulo="¿Qué es CSS?", contenido="Este blog describe CSS")