try:
    # Solicitar al usuario que ingrese dos números
    numerador = float(input("Ingrese el numerador: "))
    denominador = float(input("Ingrese el denominador: "))

    # Realizar la división y mostrar el resultado
    resultado = numerador / denominador
    print(f"Resultado de la división: {resultado}")

except ValueError:
    print("Por favor, ingrese números válidos.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except Exception as e:
    print(f"Error inesperado: {e}")
finally:
    print("Termino del programa.")
