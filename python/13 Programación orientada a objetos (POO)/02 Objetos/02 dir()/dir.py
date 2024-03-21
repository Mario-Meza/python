"""_summary_
    Es una funcion que devuelve una lista de los nombres de los atributos y metodos de un objeto.
    Es util para eplorar los atributos y metodos de un objeto y obtener informacion del objeto.
    Tiene como proposito listar los atributos y metodos validso asociados a un objeto en python
    > Sin argumentos: Cuando se llama a dir() sin especificar un objeto, devuelve una lista de los nombres definidos en el ámbito actual de tu programa.
    > Con un objeto:Cuando pasas un objeto a dir(), intenta devolver una lista de sus atributos y métodos. Estos incluyen:
        - Atributos propios del objeto.
        - Atributos y métodos heredados de sus clases padre.
        - Funciones y atributos integrados de Python a los que el objeto tiene acceso.
"""
import math
print(dir(math))  # Salida: ['acos', 'asin', 'atan', 'ceil', 'cos', ...]
