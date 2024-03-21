"""
    Crea una tupla con los nombres de los meses del año y luego imprímelos en orden
    alfabético.
"""
meses_del_año = ("enero","febreo","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre ")
contador = 1
for m in meses_del_año:
    print(contador, "-" ,m)
    contador += 1