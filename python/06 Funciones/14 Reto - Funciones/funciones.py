# Funcion suma cuadrados
def suma_cuadrados_numeros_pares(lista):
    suma = 0
    for num in lista:
        if num % 2 == 0:
            suma += num ** 2
    return suma

# Funcion suma cubos
def suma_cubos_numeros_impares(lista):
    suma = 0
    for num in lista:
        if num % 2 != 0:
            suma += num ** 3
    return suma

def operaciones_combinadas(lista, func_par, func_impar):

    # Ámbito global
    resultado_par = func_par(lista)
    resultado_impar = func_impar(lista)

    return resultado_par, resultado_impar

# Lista de números para probar el programa
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Llamada a la función principal
resultado_cuadrados, resultado_cubos = operaciones_combinadas(
    numeros, 
    suma_cuadrados_numeros_pares, 
    suma_cubos_numeros_impares
)

# Imprimir resultados
print("Suma de cuadrados de números pares:", resultado_cuadrados)
print("Suma de cubos de números impares:", resultado_cubos)
