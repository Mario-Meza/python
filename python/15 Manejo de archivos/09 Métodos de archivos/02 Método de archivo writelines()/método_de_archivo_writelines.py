f = open("archivo.txt", "w")

lines = ["Línea 1\n", "Línea 2\n", "Línea 3\n",]
f.writelines(lines)

f.close()