# Tipos de datos y variables
numero_entero = 10
numero_decimal = 3.14
texto = "Hola, Python!"
booleano = True

# Cambios de valores y asignación de valores en las variables
numero_entero = 20
texto = "Hola, Academia X"

# Listas
lista_numeros = [1, 2, 3, 4, 5]
lista_textos = ["manzana", "banana", "cereza"]

# Tuplas
tupla_colores = ("rojo", "verde", "azul")

# Rangos
rango_numeros = range(1, 5)

# Diccionarios
diccionario_frutas = {"manzana": 3, "banana": 5, "cereza": 2}

# Conjuntos con set y frozenset
conjunto_1 = set([1, 2, 3, 4, 5])
conjunto_2 = frozenset([2, 4, 6, 8, 10])

# Nonetype
valor_nulo = None

# F-strings
producto = "Laptop"
precio = 1000
mensaje = f"El producto: {producto} tiene un precio de {precio} USD."

# Type
tipo_numero = type(numero_entero)
tipo_texto = type(texto)

# Imprimir resultados
print("Numero entero:", numero_entero)
print("Numero decimal:", numero_decimal)
print("Texto:", texto)
print("Booleano:", booleano)

print("\nListas:")
print(lista_numeros)
print(lista_textos)

print("\nTupla de colores:", tupla_colores)

print("\nRango de numeros:", list(rango_numeros))

print("\nDiccionario de frutas:", diccionario_frutas)

print("\nConjunto 1:", conjunto_1)
print("Conjunto 2:", conjunto_2)

print("\nValor nulo:", valor_nulo)

print("\nF-string:")
print(mensaje)

print("\nTipos:")
print("Tipo de numero entero:", tipo_numero)
print("Tipo de texto:", tipo_texto)
