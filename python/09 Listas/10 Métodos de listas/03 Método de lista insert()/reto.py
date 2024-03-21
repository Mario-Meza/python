"""
    Crea una lista con 5 elementos y usa la función insert() para insertar un elemento
    en una posición específica.

    > El método insert() en Python no reemplaza el elemento en la posición dada, 
      sino que desplaza ese elemento y todos los elementos siguientes a la 
      derecha. En tu caso, estás insertando el número 100 en la posición 9 de la 
      lista.
"""
lista = [1,2,3,4,5,6,7,8,9,10]

lista.insert(9, 100)
print(lista[9])
print(lista)