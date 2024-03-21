"""
    - Se refiere a la visivilidad de variables y funciones.
    - El ambito global se refiere a variables y funciones que estan en todos los ambitos.
    - Mientras que el ambito local se refiere a variables y funciones que solo estan disponibles dentro de un ambito especifico.

"""

var_global = 3

def suma():
    var_local = 5
    print(f"Variable global: {var_global} y variable local {var_local}")

suma()