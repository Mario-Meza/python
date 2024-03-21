#Clase empleado
class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Salario Base: ${self.salario_base}"

class Gerente(Empleado):
    def __init__(self, nombre, salario_base, bono):
        super().__init__(nombre, salario_base)
        self.bono = bono

    def calcular_salario(self):
        salario_total = super().calcular_salario() + self.bono
        return salario_total

    def mostrar_informacion(self):
        return f"Gerente - {super().mostrar_informacion()}, Bono: ${self.bono}"

class Programador(Empleado):
    def __init__(self, nombre, salario_base, lenguaje):
        super().__init__(nombre, salario_base)
        self.lenguaje = lenguaje

    def mostrar_informacion(self):
        return f"Programador - {super().mostrar_informacion()}, Lenguaje: {self.lenguaje}"

# Ejemplo de uso
empleado1 = Empleado("Juan Pérez", 50000)
gerente1 = Gerente("Ana Gómez", 70000, 10000)
programador1 = Programador("Carlos Rodriguez", 60000, "Python")

empleados = [empleado1, gerente1, programador1]

for empleado in empleados:
    print(empleado.mostrar_informacion())
    print(f"Salario Total: ${empleado.calcular_salario()}\n---\n")
