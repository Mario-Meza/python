"""
Crea un diccionario con algunas claves y valores, luego usa setdefault() para obtener
el valor de una clave específica.
"""
persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}

valor = persona.setdefault("Pais", "España")
print(persona)