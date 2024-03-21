"""
    Los dobles paréntesis en startswith(('j', 's')) se utilizan para pasar una 
    tupla de valores a la función startswith(). Esto permite que la función 
    compruebe si la cadena comienza con cualquiera de los valores en la tupla, 
    en este caso, 'j' o 's'. Sin los dobles paréntesis, sólo se pasaría un solo 
    valor a startswith().
"""
lista = ["perro","sapo", "sabana", "sofa","java","tallador","jabon","rabano"]

lista_doble = [letra for letra in lista if letra.startswith(('j','s'))]
print(lista_doble)