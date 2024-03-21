def mostrar_menu():
    print("\nCRUD de Usuarios")
    print("1. Agregar usuario")
    print("2. Mostrar usuarios")
    print("3. Actualizar usuario")
    print("4. Borrar usuario")
    print("5. Salir")

def agregar_usuario(usuarios):
    nombre = input("Ingrese el nombre del usuario: ")
    usuarios.append(nombre)
    print(f"\nUsuario '{nombre}' agregado exitosamente.")

def mostrar_usuarios(usuarios):
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        print(usuarios)


def actualizar_usuario(usuarios):
    nombre_a_actualizar = input("Ingrese el nombre del usuario a actualizar: ")

    if nombre_a_actualizar in usuarios:
        nuevo_nombre = input("Ingrese el nuevo nombre (o presione Enter para mantener el actual): ")
        
        if nuevo_nombre:
            usuarios[usuarios.index(nombre_a_actualizar)] = nuevo_nombre

        print(f"\nUsuario '{nombre_a_actualizar}' actualizado exitosamente.")
    else:
        print(f"No se encontró el usuario '{nombre_a_actualizar}'.")

def borrar_usuario(usuarios):
    nombre_a_borrar = input("Ingrese el nombre del usuario a borrar: ")

    if nombre_a_borrar in usuarios:
        usuarios.remove(nombre_a_borrar)
        print(f"\nUsuario '{nombre_a_borrar}' borrado exitosamente.")
    else:
        print(f"No se encontró el usuario '{nombre_a_borrar}'.")

def main():
    usuarios = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            agregar_usuario(usuarios)
        elif opcion == "2":
            mostrar_usuarios(usuarios)
        elif opcion == "3":
            actualizar_usuario(usuarios)
        elif opcion == "4":
            borrar_usuario(usuarios)
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

main()
