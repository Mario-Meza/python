f = open('archivo.txt', 'w')
f.write('Hola, este es un archivo de prueba')
f.close()


f = open('archivo.txt', 'r')
contenido = f.read()
contenido_modificado = contenido + '\nAdios!'
f.write(contenido_modificado)
f.close()