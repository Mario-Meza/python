def decimal_a_binario(numero):
    return bin(numero)[2:]

def decimal_a_octal(numero):
    return oct(numero)[2:]

def decimal_a_hexadecimal(numero):
    return hex(numero)[2:]

def menu_conversion():
    print("1. Convertir a binario")
    print("2. Convertir a octal")
    print("3. Convertir a hexadecimal")
    print("4. Salir")

def convertir_numero():
    while True:
        try:
            numero_decimal = int(input("Ingrese un número decimal: "))
            return numero_decimal
        except ValueError:
            print("Error: Ingrese un número válido.")

def main():
    while True:
        menu_conversion()
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            numero_decimal = convertir_numero()
            print(f"Binario: {decimal_a_binario(numero_decimal)}")
        elif opcion == "2":
            numero_decimal = convertir_numero()
            print(f"Octal: {decimal_a_octal(numero_decimal)}")
        elif opcion == "3":
            numero_decimal = convertir_numero()
            print(f"Hexadecimal: {decimal_a_hexadecimal(numero_decimal)}")
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
