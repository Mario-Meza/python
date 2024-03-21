# Operadores aritméticos
a = 10
b = 3

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
potencia = a ** b
modulo = a % b

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print(f"Potencia: {potencia}")
print(f"Módulo: {modulo}")

# Operadores de asignación
x = 5
x += 3  # equivalente a x = x + 3
y = 8
y *= 2  # equivalente a y = y * 2

print(f"x después de la asignación: {x}")
print(f"y después de la asignación: {y}")

# Operadores de comparación
num1 = 10
num2 = 20

igual = num1 == num2
diferente = num1 != num2
mayor_que = num1 > num2
menor_que = num1 < num2
mayor_o_igual = num1 >= num2
menor_o_igual = num1 <= num2

print(f"Igual: {igual}")
print(f"Diferente: {diferente}")
print(f"Mayor que: {mayor_que}")
print(f"Menor que: {menor_que}")
print(f"Mayor o igual que: {mayor_o_igual}")
print(f"Menor o igual que: {menor_o_igual}")

# Operadores lógicos
condicion_1 = True
condicion_2 = False

and_logico = condicion_1 and condicion_2
or_logico = condicion_1 or condicion_2
not_logico = not condicion_1

print(f"AND lógico: {and_logico}")
print(f"OR lógico: {or_logico}")
print(f"NOT lógico: {not_logico}")

# Operadores de membresía
lista = [1, 2, 3, 4, 5]

in_lista = 3 in lista
not_in_lista = 6 not in lista

print(f"¿3 está en la lista? {in_lista}")
print(f"¿6 no está en la lista? {not_in_lista}")

# Operadores de identidad
cadena_1 = "Hola"
cadena_2 = "Hola"

is_identico = cadena_1 is cadena_2
is_not_identico = cadena_1 is not cadena_2

print(f"¿Identidad? {is_identico}")
print(f"¿No identidad? {is_not_identico}")

# Operadores de bits
bitwise_and = a & b
bitwise_or = a | b
bitwise_xor = a ^ b
bitwise_not = ~a
left_shift = a << 1
right_shift = a >> 1

print(f"Bitwise AND: {bitwise_and}")
print(f"Bitwise OR: {bitwise_or}")
print(f"Bitwise XOR: {bitwise_xor}")
print(f"Bitwise NOT: {bitwise_not}")
print(f"Left Shift: {left_shift}")
print(f"Right Shift: {right_shift}")
