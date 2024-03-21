"""
    Una funcion anidada es una funcion defeinida dentro de otra funcion.
    Significa que la funcion interna esta disponible en el ambito local de la funcion externa 
    pero no esta disponible fuera de ella.
"""

def function1():
    contadroSuma = 0

    def function2(lista = [1,2,3,4,5]):
        nonlocal contadroSuma
        for num in lista:
            contadroSuma += num
        print(f'El resultado de la suma de los numeros de la lista es {contadroSuma}')

    
    function2()

function1()

        

    

