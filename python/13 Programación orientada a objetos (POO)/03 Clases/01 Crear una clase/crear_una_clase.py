class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print(f"Mi nombre es {self.nombre} y tengo {self.edad} años.")

persona = Persona("Juan", 20)
persona.saludar()

persona2 = Persona("José", 18)
persona2.saludar()