# funciones suma cuadrados
def suma_cuadrados_numeros_pares(lista):
    suma = 0
    for num in lista:
        if num % 2 == 0:
            suma += num ** 2
    return suma

# funcion_cubos_numeros_pares
def suma_cubos_numeros_inpares(lista):
    suma = 0
    for num in lista:
        if num % 2 != 0:
            suma += num ** 3
    return suma

# suma operaciones combinadas
def operaciones_combinadas(lista, function_pares, function_inpares):
    """
    Esta función calcula la suma total de una lista de números, utilizando las funciones "function_pares" y "function_impares".
    Parámetros:
        lista (list): Una lista de números.
        function_pares (function): Función que calcula la suma de los cuadrados de los números pares.
        function_impares (function): Función que calcula la suma de los cubos de los números impares.
    Retorno:
        int: La suma total de la lista.
    """

    func_pares = function_pares(lista)
    func_inpares = function_inpares(lista)

    return func_pares, func_inpares

# Lista de numeros para probar el programa
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Llamada a la funcion principal
resultado_cuadrados, resultado_cubos = operaciones_combinadas(
    numeros, 
    suma_cuadrados_numeros_pares,
    suma_cubos_numeros_inpares
)

print("Suma de cuadrado de numeros pares: ", resultado_cuadrados)
print("Suma de cubos de numeros inapres: ", resultado_cubos)



