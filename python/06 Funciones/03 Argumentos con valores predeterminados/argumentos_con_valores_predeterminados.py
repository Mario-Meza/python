"""
    1- Son argumentos con valores predeterminados son aquellos que se asignan a una funcion cuando se llama asi misma sin especificar un valor para el argummento.
    2- Esto significa que si una función tiene un argumento con un valor prede-
       terminado, el usuario no necesita especificar un valor para ese argumento cuando
       llama a la función.
    """
def saludar(nombre="mario"):
    print(f'Hola {nombre}')
    
nombre1 = saludar()
#print(nombre1)