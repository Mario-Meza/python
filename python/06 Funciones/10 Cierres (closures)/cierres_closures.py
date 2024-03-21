def funcion_externa():
    mensaje = "Hola"

    def funcion_interna():
        print(mensaje)

    return funcion_interna

mi_funcion = funcion_externa()
mi_funcion()