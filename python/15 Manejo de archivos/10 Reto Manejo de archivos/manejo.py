# main.py

def registrar_gasto():
    fecha = input("Ingrese la fecha (DD/MM/YYYY): ")
    descripcion = input("Ingrese la descripción del gasto: ")
    cantidad = float(input("Ingrese la cantidad gastada: $"))

    with open("gastos_mensuales.txt", "a") as archivo:
        archivo.write(f"{fecha} - {descripcion} - ${cantidad}\n")
    print("Gasto registrado exitosamente.")

def mostrar_gastos():
    print("\nGastos Registrados:")
    try:
        with open("gastos_mensuales.txt", "r") as archivo:
            gastos = archivo.readlines()
            for gasto in gastos:
                print(gasto.strip())
    except FileNotFoundError:
        print("Aún no hay gastos registrados.")

def calcular_total_gastos():
    try:
        with open("gastos_mensuales.txt", "r") as archivo:
            gastos = archivo.readlines()
            total = sum(float(gasto.split("-")[-1].strip().replace("$", "")) for gasto in gastos)
            print(f"\nTotal de Gastos: ${total:.2f}")
    except FileNotFoundError:
        print("Aún no hay gastos registrados.")

# Programa Principal
while True:
    print("\n*** Registro de Gastos Mensuales ***")
    print("1. Registrar Nuevo Gasto")
    print("2. Mostrar Gastos Registrados")
    print("3. Calcular Total de Gastos")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        registrar_gasto()
    elif opcion == "2":
        mostrar_gastos()
    elif opcion == "3":
        calcular_total_gastos()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
