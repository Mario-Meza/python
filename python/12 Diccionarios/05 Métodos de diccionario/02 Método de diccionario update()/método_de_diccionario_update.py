"""
    Update() es una función de Python que se utiliza para actualizar los valores de un
    diccionario. Esta función toma dos argumentos: un diccionario y una secuencia de
    pares clave-valor. Esta función actualiza el diccionario con los pares clave-valor es-
    pecificados.
"""
alumno = {
    "nombre": "Jose",
    "apellidos": "Ramirez Lopez",
    "edad": 27,
    "pais": "México",
    "ciudad": "CDMX",
    "rfc":"DFDGFS334FD",
    "estudios": "Universidad"
}

alumno.update({"name":"Mario"})
print(alumno)