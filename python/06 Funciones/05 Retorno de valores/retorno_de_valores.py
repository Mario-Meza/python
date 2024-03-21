"""
    - El retorno de valores es una forma de devolver un resultado de una funcion.Esto significa que una funcion puede devolver un valor
      que puede ser usado por el programa que la llamo.
"""
def numeros(num1, num2):
    if num1 > num2:
        return f'{num1} es mayor'
    elif num2 > num1:
        return f'{num2} es mayor'
    else:
        return f'son iguales'
    
result = numeros(7, 7)
print(result)