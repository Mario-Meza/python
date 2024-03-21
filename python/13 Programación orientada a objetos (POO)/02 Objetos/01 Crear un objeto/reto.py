"""
    Crea una clase llamada Libror que tenga dos atributos: título y autor. Agrega un
    método llamado qmostrar_informacionrque imprima el título y el autor del libro.
"""

class Libro:
    def mostrar_informacion(self, titulo, autor):
        print(f'Titulo: {titulo} Autor: {autor}')
        
libro_uno = Libro()
libro_uno.mostrar_informacion("Hola","Pablo cohelo")