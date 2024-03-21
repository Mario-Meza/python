f = open("archivo.txt", "r")

print(f.tell())

linea = f.readline()

print(f.tell())

f.close()