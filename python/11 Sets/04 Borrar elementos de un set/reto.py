"""
    Crea un set con los números del 1 al 10, luego borra los números impares del set.
"""
# Crea un set con los números del 1 al 10
mi_set = {1,2,3,4,5,6,7,8,9,10}

# Crea una copia del set para iterar sobre él
# Esto es necesario porque no puedes cambiar un set mientras lo estás iterando
copia_set = mi_set.copy()

for num in copia_set:
     # Si el número es impar, bórralo del set original
    if num % 2 != 0:
        mi_set.remove(num)

print(mi_set)