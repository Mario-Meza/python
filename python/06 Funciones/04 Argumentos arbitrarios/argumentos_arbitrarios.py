"""
    - Son argumentos que se pasan como una funcion, pero que no se especifican en la definicion.
    - Estos argumentos se pasan como una tupla de argumentos, con un asterisco siguiente del nombre de la variable.
    (*nombres)
    - 
"""
def sumar(*numeros):
    suma = 0
    for num in numeros:
        suma += num
    print(f'La suma de {numeros} es {suma}')

suma1 = sumar(1,1,1,1,1,1,1,1)
suma2 = sumar(2,2,2,2)