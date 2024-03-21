class Calculadora:
    def __init__(self):
        self.operaciones_realizadas = []

    def registrar_operacion(self, operacion):
        self.operaciones_realizadas.append(operacion)

    def generar_operaciones(self):
        for operacion in self.operaciones_realizadas:
            yield operacion

    @staticmethod
    def _validar_numeros(*args):
        for num in args:
            if not isinstance(num, (int, float)):
                raise ValueError("Todos los argumentos deben ser números.")

    def suma(self, *args):
        self._validar_numeros(*args)
        resultado = sum(args)
        self.registrar_operacion(f"Suma: {args} = {resultado}")
        return resultado

    def resta(self, a, b):
        self._validar_numeros(a, b)
        resultado = a - b
        self.registrar_operacion(f"Resta: {a} - {b} = {resultado}")
        return resultado

    def multiplicacion(self, *args):
        self._validar_numeros(*args)
        resultado = 1
        for num in args:
            resultado *= num
        self.registrar_operacion(f"Multiplicación: {args} = {resultado}")
        return resultado

    def division(self, a, b):
        self._validar_numeros(a, b)
        if b == 0:
            raise ValueError("No se puede dividir por cero.")
        resultado = a / b
        self.registrar_operacion(f"División: {a} / {b} = {resultado}")
        return resultado


# Decorador para registrar operaciones
def registrar_operacion(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        calculadora.registrar_operacion(f"{func.__name__.capitalize()}: {args} = {resultado}")
        return resultado
    return wrapper


# Uso de la calculadora con decoradores
calculadora = Calculadora()

@registrar_operacion
def potencia(a, b):
    return a ** b

@registrar_operacion
def operacion_personalizada(x, y, z):
    return (x + y) * z

# Realizar algunas operaciones
calculadora.suma(3, 5)
calculadora.resta(10, 3)
calculadora.multiplicacion(2, 4, 6)
calculadora.division(8, 2)
potencia(2, 3)
operacion_personalizada(1, 2, 3)

# Mostrar operaciones registradas
print("\nOperaciones Registradas:")
for operacion in calculadora.generar_operaciones():
    print(operacion)
