"""
ara acceder a los elementos de una lista en Python, se utiliza el índice de cada
elemento. El índice de un elemento es su posición en la lista, comenzando desde 0.

La segunda instrucción print(mi_lista[1:3]) imprime una sublista de mi_lista que
incluye los elementos desde el índice 1 hasta el índice 3, sin incluir el elemento
en el índice 3. Por lo tanto, imprime [2, 3], que son los elementos en los índices 
1 y 2.
"""
mi_lista = [1,2,3,4]
print(mi_lista[0])# Accede al primer elemento
print(mi_lista[1:3])# Accede a un rango desde el indice 1 hasta el indice 3 / sin incluir el elemento en el indice 3
print(mi_lista[:3])# Accede a un rango desde el indice 0 hasta el indice 3/ sin incluir el elemento en el indice 3
print(mi_lista[-2])# Accede a un elemento desde el final
print(mi_lista[-4])