class Animal:
    def __init__(self, nombre, especie, edad):
        self.especie = especie
        self.edad = edad
        self.nombre = nombre
        
    def hablar(self):
        pass
    
    def moverse(self):
        pass
    
    def describirme(self):
        print(f"Soy un Animal de especie {self.especie} y soy de tipo {type(self).__name__}")

class Perro(Animal):
    def __init__(self, nombre, especie, edad, dueño):
        super().__init__(nombre, especie, edad)
        self.dueño = dueño
    
    def descripcion(self):
        print(f"Soy un Animal de especie {self.especie}, mi dueño es {self.dueño} y soy de tipo {type(self).__name__}")

        

animal = Perro("Perro", "Mamifero", 7,"Luis")
animal.descripcion()
