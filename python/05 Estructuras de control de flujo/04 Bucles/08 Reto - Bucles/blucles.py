# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Límite para la suma
limite_suma = 15

# Inicializar la variable resultado
resultado_suma = 0

# Bucle for para iterar sobre la lista de números
for numero in numeros:
    # Ignorar números impares
    if numero % 2 != 0:
        continue

    # Salir del bucle si la suma supera el límite
    if resultado_suma > limite_suma:
        break

    # Sumar el número par al resultado
    resultado_suma += numero

# Imprimir el resultado
print(f"La suma de números pares hasta {limite_suma} es: {resultado_suma}")
