x = 10

try:
    numero = input("Ingrese un numero: ")
    parse_num = int(numero)
    result = x / parse_num
except ValueError as ve:
    print(f'Valor no valido {ve}')
except ZeroDivisionError as zde:
    print(f'No se puede dividir un valor para 0 { zde}')
else:
    print(f'{result}')