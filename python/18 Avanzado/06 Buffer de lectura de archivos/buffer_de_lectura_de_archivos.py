archivo = open('ejemplo.txt', 'r')

while True:
    data = archivo.read(1024)

    if not data:
        break

    print(data)

archivo.close()