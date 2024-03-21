archivo = open("archivo.txt", "r")

archivo.seek(6)

contenido = archivo.read()

print(contenido)

archivo.close()