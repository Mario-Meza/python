numeros = [1, 6, 2]

for numero in numeros:
    if numero % 2 == 0:
        print(f"El número {numero} es par")
        break
    else:
        print(f"El número {numero} es inpar")
else:
    print("No se encontró ningún número par")