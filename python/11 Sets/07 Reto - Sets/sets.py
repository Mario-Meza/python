def main():
    # Libros en la biblioteca 1
    biblioteca1 = {"Harry Potter", "Cien años de soledad", "El Señor de los Anillos", "Código Da Vinci"}

    # Libros en la biblioteca 2
    biblioteca2 = {"Harry Potter", "Don Quijote", "Cien años de soledad", "Orgullo y prejuicio"}

    # Mostrar libros en cada biblioteca
    print("Libros en la Biblioteca 1:", biblioteca1)
    print("Libros en la Biblioteca 2:", biblioteca2)

    # Encontrar libros comunes en ambas bibliotecas
    libros_comunes = biblioteca1.intersection(biblioteca2)
    print("\nLibros comunes en ambas bibliotecas:", libros_comunes)

    # Encontrar libros únicos en cada biblioteca
    libros_unicos_biblioteca1 = biblioteca1.difference(biblioteca2)
    libros_unicos_biblioteca2 = biblioteca2.difference(biblioteca1)

    print("\nLibros únicos en la Biblioteca 1:", libros_unicos_biblioteca1)
    print("Libros únicos en la Biblioteca 2:", libros_unicos_biblioteca2)

    # Combinar ambas bibliotecas
    biblioteca_completa = biblioteca1.union(biblioteca2)
    print("\nLibros en la Biblioteca Completa:", biblioteca_completa)

    # Verificar si una biblioteca es subconjunto de la otra
    es_subconjunto = biblioteca1.issubset(biblioteca_completa)
    print("\n¿La Biblioteca 1 es un subconjunto de la Biblioteca Completa?", es_subconjunto)

    # Agregar un nuevo libro a ambas bibliotecas
    nuevo_libro = "El Principito"
    biblioteca1.add(nuevo_libro)
    biblioteca2.add(nuevo_libro)

    print(f"\nNuevo libro '{nuevo_libro}' agregado a ambas bibliotecas.")

    # Mostrar las bibliotecas actualizadas
    print("Libros en la Biblioteca 1:", biblioteca1)
    print("Libros en la Biblioteca 2:", biblioteca2)

main()
