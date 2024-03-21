"""
    difference() es una función de Python que devuelve la diferencia entre dos conjun-
    tos. Esta función devuelve un conjunto con los elementos que están en el primer
    conjunto, pero no en el segundo.
"""
conjunto_1 = {1, 2, 3, 4, 5}
conjunto_2 = {3, 4, 5, 6, 7}

resultado = conjunto_1.difference(conjunto_2)

print(resultado)