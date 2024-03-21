"""
    pow() es una funcion incorporada en pthon que permite calcular la potencia de un numero.
    Esta funcion toma dos argumentos:
    > El primer argumento es el numero base
    > El segundo argumento es el exponente
"""
# Define una lista llamada listaNumeros con tres números enteros(elementos): 2, 3 y 4.
listaNumeros = [2,3,4]
# Inicia un bucle for que iterará sobre cada elemento de listaNumeros.
# En cada iteración del bucle, toma el elemento actual, que se refiere con la variable num
for num in listaNumeros:
    # Calcula la potencia de num elevado al cuadrado utilizando la función pow y almacena el resultado en la variable calcularPotencia.
    calcularPotencia = pow(num, 2)
    # Imprime el valor de calcularPotencia.
    print(calcularPotencia)