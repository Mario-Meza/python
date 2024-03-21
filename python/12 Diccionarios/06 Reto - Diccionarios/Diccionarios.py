def agregar_tarea(tareas, descripcion, estado, fecha_vencimiento=None):
    nueva_tarea = {"descripcion": descripcion, "estado": estado, "fecha_vencimiento": fecha_vencimiento}
    tareas[descripcion] = nueva_tarea
    print(f"\nTarea '{descripcion}' agregada exitosamente.")

def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas registradas.")
    else:
        print("\nLista de Tareas:")
        for descripcion, tarea in tareas.items():
            print(f"Descripción: {tarea['descripcion']}, Estado: {tarea['estado']}, Fecha de Vencimiento: {tarea['fecha_vencimiento']}")

def completar_tarea(tareas, descripcion):
    tarea = tareas.get(descripcion)

    if tarea:
        tarea["estado"] = "Completada"
        print(f"\nTarea '{descripcion}' completada.")
    else:
        print(f"No se encontró la tarea '{descripcion}'.")

def eliminar_ultima_tarea(tareas):
    if not tareas:
        print("No hay tareas para eliminar.")
    else:
        descripcion, tarea = tareas.popitem()
        print(f"\nÚltima tarea '{descripcion}' eliminada.")

def main():
    tareas_pendientes = {}

    while True:
        print("\nGestor de Tareas Pendientes")
        print("1. Agregar Tarea")
        print("2. Mostrar Tareas")
        print("3. Completar Tarea")
        print("4. Eliminar Última Tarea")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            estado = "Pendiente"
            fecha_vencimiento = input("Ingrese la fecha de vencimiento (o presione Enter si no hay fecha): ")

            agregar_tarea(tareas_pendientes, descripcion, estado, fecha_vencimiento)

        elif opcion == "2":
            mostrar_tareas(tareas_pendientes)

        elif opcion == "3":
            descripcion = input("Ingrese la descripción de la tarea a completar: ")
            completar_tarea(tareas_pendientes, descripcion)

        elif opcion == "4":
            eliminar_ultima_tarea(tareas_pendientes)

        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
main()
