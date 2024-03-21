class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"Hola, soy un animal llamado {self.nombre}")

animal = Animal("Fido")
animal2 = Animal("Fido2")
animal3 = Animal("Fido3")
animal4 = Animal("Fido4")