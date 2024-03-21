# Ejercicio: Verificar la clasificación de edad

# Pedir al usuario que ingrese su edad
edad_str = input("Ingresa tu edad: ")

# Convertir la entrada a entero
edad = int(edad_str)

# Verificar la clasificación de edad
clasificacion = ""

if 0 <= edad < 12:
    clasificacion = "Niño"
elif 12 <= edad < 18:
    clasificacion = "Adolescente"
elif 18 <= edad < 65:
    clasificacion = "Adulto"
else:
    clasificacion = "Adulto Mayor"

# Imprimir la clasificación
print(f"Clasificación de edad: {clasificacion}")

# Utilizar match para una clasificación más detallada
match edad:
    case 0|1|2|3|4|5|6|7|8|9|10|11:
        print("¡Eres un niño pequeño!")
    case 12|13| 14 | 15 | 16 | 17:
        print("¡Estás en la etapa de la adolescencia!")
    case 18:
        print("¡Eres un adulto en plena edad laboral!")
    case _:
        print("¡Eres un adulto mayor y mereces respeto!")
