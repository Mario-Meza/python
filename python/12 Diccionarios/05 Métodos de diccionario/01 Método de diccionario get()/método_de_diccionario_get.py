"""
    get() es un método de diccionario en Python que devuelve el valor de una clave
    específica. Si la clave no existe, devuelve un valor predeterminado.
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

valor = alumno.get('nombre')
print(valor)

valor2 = alumno.get('edades', 'No existe')
print(valor2)