def agregar_libro(libros, titulo, autor, año_publicacion):
    nuevo_libro = (titulo, autor, año_publicacion) #Se crea la tupla
    libros.append(nuevo_libro)
    print(f"\nLibro '{titulo}' agregado exitosamente.")

def mostrar_libros(libros):
    if not libros:
        print("No hay libros registrados.")
    else:
        print("\nLista de Libros:")
        for libro in libros:
            print(f"Título: {libro[0]}, Autor: {libro[1]}, Año de Publicación: {libro[2]}")

def buscar_libros_por_autor(libros, autor):
    libros_encontrados = [libro for libro in libros if libro[1] == autor]
    
    if not libros_encontrados:
        print(f"No hay libros del autor '{autor}'.")
    else:
        print(f"\nLibros del autor '{autor}':")
        for libro in libros_encontrados:
            print(f"Título: {libro[0]}, Año de Publicación: {libro[2]}")

def main():
    libros = []

    while True:
        print("\nGestor de Libros")
        print("1. Agregar libro")
        print("2. Mostrar libros")
        print("3. Buscar libros por autor")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            año_publicacion = input("Ingrese el año de publicación del libro: ")

            agregar_libro(libros, titulo, autor, año_publicacion)

        elif opcion == "2":
            mostrar_libros(libros)

        elif opcion == "3":
            autor_a_buscar = input("Ingrese el nombre del autor para buscar libros: ")
            buscar_libros_por_autor(libros, autor_a_buscar)

        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


main()
