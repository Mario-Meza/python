def es_maor_de_edad(edad):
    assert edad >= 18, "La persona no es mayor de edad"
edad = 17

try:
    es_maor_de_edad(edad)
except AssertionError as error:
    print(error)
else:
    print("Eres mayor de edad")