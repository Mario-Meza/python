alumno = {
    "nombre": "Jose",
    "apellidos": "Ramirez Lopez",
    "edad": 27,
    "pais": "México",
    "ciudad": "CDMX",
    "rfc":"DFDGFS334FD"
}

boorar_elemento = alumno.pop('nombre')
for c, v in alumno.items():
    print(f'{c}: {v}')