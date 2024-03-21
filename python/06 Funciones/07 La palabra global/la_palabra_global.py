"""
    -La palabra global se utiliza para ahcer referencia a una variable global en el ambito actual de una funcion.
     Cuando se declara una variable dentro de una funcion,esta se considera como una variable local solo esta disponible dentro de la funcion.

"""
variableGlobal1 = 4
variableGlobal2 = 3

def data():
    global variableGlobal1 # colocammos la palabra resertvada global antes de la variable si deseamos acceder a ella  mmodificarla.Si no hacemos esto creara una copia
    global variableGlobal2

    variableGlobal1 = 20
    variableGlobal2 = 20

    variableLocal1 = 3
    variableLocal2 = 3

    return variableGlobal1 + variableGlobal2


sumar = data()
print(sumar)
