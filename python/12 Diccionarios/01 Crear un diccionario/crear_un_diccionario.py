alumno = {
    "nombre": "Jose",
    "apellidos": "Ramirez Lopez",
    "edad": 27,
    "pais": "México",
    "ciudad": "CDMX",
    "rfc":"DFDGFS334FD"
}

#Acceder a la clave "nombre"
ver_nombre = alumno["nombre"]
print("1- El valor de nombre es", ver_nombre)

#modificar edad
modificar_edad = alumno["edad"] = 34
print("2- Edad modificada", modificar_edad)

contador = 1
for c,v in alumno.items():
    print(f'{contador}> {c}: {v}')
    contador += 1