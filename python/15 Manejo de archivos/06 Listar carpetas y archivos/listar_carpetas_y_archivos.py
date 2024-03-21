import os

archivos_y_carpetas = os.listdir(".")

for nombre in archivos_y_carpetas:
    print(nombre)