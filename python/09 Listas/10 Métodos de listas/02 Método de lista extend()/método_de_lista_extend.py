"""
    extend() permite agregar elementos a una lista existente.Por ejemplo, si tenemos una lista llamada
    lista_1 con los elementos [1,2,3] ,podemos usar este metodo para
    agreagr elementos [4,5,6] a la lista
"""
lista_1 = [1,2,3,4,5]
lista_2 = [6,7,8,9,10]

lista_1.extend(lista_2)
print(lista_1)
