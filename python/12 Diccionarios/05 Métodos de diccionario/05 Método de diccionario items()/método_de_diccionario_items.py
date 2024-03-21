"""
   items() es un método de diccionario en Python que devuelve una lista de tuplas,
   donde cada tupla contiene una clave y su valor correspondiente. 
"""
persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}

for k,v in persona.items():
    print(f'{k}: {v}')