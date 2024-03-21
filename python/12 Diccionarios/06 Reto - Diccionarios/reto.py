# agregar tarea
def add_task(tareas, descripcion, estado, fecha_vencimiento=None):
    nueva_tarea = {
        "descripcion": descripcion,
        "estado": estado,
        "vencimiento": fecha_vencimiento
        }
    
    #agrega un nuevo elemento al diccionario tareas con la clave descripcion y el valor nueva_tarea.
    tareas[descripcion] = nueva_tarea 
    #Pintamos la descripcion con un mensaje de exito
    print(f'\nTarea: "{descripcion}" se agrego con exito')


def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas registradas.")
    else:
        print("\nLista de Tareas:")
        for descripcion, tarea in tareas.items():
            print(f"Descripción: {tarea['descripcion']}, Estado: {tarea['estado']}, Fecha de Vencimiento: {tarea['vencimiento']}")

def completar_tarea(tareas, descripcion):
    tarea = tareas.get(descripcion)

    if tarea:
        tarea["estado"] = "completada"
        print(f"\nTarea '{descripcion}' completada.")
    else:
        print(f"No se encontró la tarea '{descripcion}'.")

def eliminar_ultima_tarea(tareas):
    if not tareas:
        print("No hay tareas para eliminar")
    else:
        descripcion, tarea = tareas.popitem()
        print(f"\nÚltima tarea '{descripcion}' eliminada.")

def main():
    tareas_pendientes = {}

    while True:
        print("\nGestor de Tareas Pendientes")
        print("1- Agregar Tarea")
        print("2- Mostrar tareas")
        print("3- Completar tarea")
        print("4- Eliminar tarea")
        print("5-salir")

        opcion = input("Seleccione una opcion (1-5): ") 
        
        if opcion == "1":
            descripcion = input("Ingrese la descripcion de la tarea: ")
            estado = "pendiente"
            fecha_vencimiento = input("Ingrese la fecha de vencimiento: ")

            add_task(tareas_pendientes, descripcion, estado, fecha_vencimiento)
        
        elif opcion == "2":
            mostrar_tareas(tareas_pendientes)
        elif opcion == "3":
            descripcion = input("Ingrese la descripcion de la tarea: ")
            completar_tarea(tareas_pendientes, descripcion)
        elif opcion == "4":
            eliminar_ultima_tarea(tareas_pendientes)
        elif opcion == "5":
            print("Saliendo del programa. Hasta luego")
            break
        else:
            print("Opcion no valida. Intente de nuevo")

main()    




