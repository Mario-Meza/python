def calcular_promedio(lista_de_notas):
    """Calcula el rpomedio de una lista de notas.

    Args:
        lista_de_notas (list): lista de notas a promediar.

    Returns:
        float: Promedio de la lista de notas.
    """
    promedio = 0
    for nota in lista_de_notas:
        promedio += nota
    promedio /= len(lista_de_notas)
    return promedio