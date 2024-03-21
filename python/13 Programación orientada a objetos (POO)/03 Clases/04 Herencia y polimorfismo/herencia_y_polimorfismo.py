"""
La herencia es un mmecanismo que permite a una clase heredar los atributos  metodos de otra clase.
,simplificando el proceso de desarrollo.

El Polimorfismo en Python es una característica que permite a una clase comportar-
se de manera diferente dependiendo de la situación. Esto significa que una clase
puede definir métodos con el mismo nombre, pero con diferentes parámetros
"""
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"Hola, soy un animal llamado {self.nombre}")

class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def hablar(self):
        print("Woof, soy un perro y me llamo", self.nombre)

fido = Perro("Fido")
fido.hablar()  