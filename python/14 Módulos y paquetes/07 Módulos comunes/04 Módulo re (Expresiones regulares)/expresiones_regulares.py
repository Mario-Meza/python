import re

texto = "Alamo alerta adios aviso canción"
expresion_regular = r'\ba\w*'
resultados = re.findall(expresion_regular, texto)

print(resultados)

