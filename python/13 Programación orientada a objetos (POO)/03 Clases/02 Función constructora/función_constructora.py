"""_summary_
    Es un metodo especial que se invoca automaticamente al crear una nueva instancia de una clase.
        > Su proposito principal es inicializar los atributos de la nueva instancia con 
          valores preseterminados o especificos.
"""
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre_completo = f"{nombre} {apellido}" 
        self.edad = edad
    
    def saludar(self):
        print(f"Mi nombre es {self.nombre} y tengo {self.edad} años.")