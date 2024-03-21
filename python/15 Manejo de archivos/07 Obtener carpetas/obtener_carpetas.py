import os

carpetas = [item for item in os.listdir(".") if os.path.isdir(item)]

for carpeta in carpetas:
    print(carpeta)