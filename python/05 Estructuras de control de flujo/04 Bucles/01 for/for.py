lista = [1, 2, 3, 4, 5]
diccionario = {
    "nombre": "mario",
    "edad": 28,
    "estado":"hidalgo",
    "cp":42220
}
tupla = ("jose", 21, "cancer")

# iterar sobre una lista
print("___Lista___")
for elemento in diccionario:
    print(elemento)

# iterar sobre un diccionario
print("___Diccionario___")
for k,v in diccionario.items():
    print(f'{k}: {v}')

# iterar sobre una tupla
print("___Tupla___")
for tup in tupla:
    print(tup)