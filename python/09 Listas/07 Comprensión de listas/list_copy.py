"""
Si tenemos una lista de nuemros y queremos crear una nueva lista con el doble de cada numero.
    > En lugar de crear una nueva lista vacia y utilizar un for para recorrer la 
      lista original y agregar cada numero doble a la nueva lista, podemos simplificar todo copn una 
      compresnsion de listas
"""
lista_original = [1,2,3,4,5]
lista_doble = lista_original.copy()

print(lista_original == lista_doble)# imprimirá True porque los valores de lista_original y lista_copia son iguales, aunque sean dos objetos diferentes en memoria. 
print(lista_original is lista_doble)# imprimirá False porque lista_original y lista_copia no son el mismo objeto en memoria.



