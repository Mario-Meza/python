try:
    x = 5 / 0
except ZeroDivisionError:
    print("No se puede dividir un número para cero")
finally:
    print("Se ejecutará siempre")