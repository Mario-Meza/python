"""
    keys() es un método en Python que devuelve una lista de las claves de un diccio-
    nario. Por ejemplo, si tenemos un diccionario llamado qmi_diccionariorcon claves
    qnombrer, qedadry qciudadr, podemos usar el método keys() para obtener una
    lista de estas claves:
"""

persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}

claves = persona.keys()
print(claves)