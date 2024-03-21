"""
- La función lambda en el código proporcionado define una función anónima que toma un argumento x y devuelve su cuadrado (es decir, x elevado al poder de 2). 
- La línea cuadrado = lambda x: x**2 asigna esta función anónima a la variable cuadrado. Ahora, cuadrado puede ser usada como cualquier otra función que toma un solo argumento y calcula su cuadrado.
- La línea print(cuadrado(5)) invoca la función cuadrado con el argumento 5. La función calcula el cuadrado de 5, que es 25, y luego imprime este valor.
"""

cuadrado = lambda x: x**2 #
print(cuadrado(5))

multiplicar = lambda x, y: x * y
print(multiplicar(5,7))