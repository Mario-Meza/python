"""
Crea un diccionario con 5 claves y 5 valores, luego imprime los valores usando el
método values()
"""

oscuridad = {
    "nombre": "Mago Oscuro",
    "tipo": "oscuridad",
    "atk": 1700,
    "def": 1700,
    "nivel": 4
}

print_clave = oscuridad.keys()
print_value = oscuridad.values()

print(print_clave)
print(print_value)