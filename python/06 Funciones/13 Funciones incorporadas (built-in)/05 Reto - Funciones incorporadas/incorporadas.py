"""FORMA 1
    si la intención es que la función trabaje con argumentos pasados al momento de ser llamada,
    entonces las variables deben definirse fuera de la función.
"""
def imprimirListaDePalabras(listaDePalabras, longitudMinima):
    for palabra in listaDePalabras:
        if len(palabra) > longitudMinima:
            print(f'Palabra "{palabra}" tiene una longitud superior a {longitudMinima}')
                
palabras = ["perro","comentarios","computadora","casa","audifonos"]
longitudMinimaDeseada = 7

imprimirListaDePalabras(palabras, longitudMinimaDeseada)

"""FORMA 2
    Si las variables están definidas dentro de la función,
    entonces no es necesario pasar argumentos y la función no debería definir parámetros:
"""
def imprimirListaDePalabras():
    palabras = ["perro","comentarios","computadora","casa","audifonos"]
    longitudMinimaDeseada = 7
    
    for palabra in palabras:
        if len(palabra) > longitudMinimaDeseada:
            print(f'Palabra "{palabra}" tiene una longitud superior a {longitudMinimaDeseada}')
                

imprimirListaDePalabras()
