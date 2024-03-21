texto = "Hola mi nombre es Mario"

for word in texto.split():
    cantidad_palabras = len(word)

print(f'La cadena de texto "{texto}" contiene '
      f'{cantidad_palabras} palabras y lo puedes ver de esta forma:'
      f'{texto.split()}') 

