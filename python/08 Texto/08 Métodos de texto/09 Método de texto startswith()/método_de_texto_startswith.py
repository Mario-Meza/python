"""
startswith() es un método de texto que permite verificar si una cadena de texto co-
mienza con una subcadena específica. Este método devuelve un valor booleano
(True o False).
"""
def found_word(word):
    encontrar_palabra = word.startswith("Mexico")

    return encontrar_palabra

resultado_busqueda = found_word("Hola Mexico desde Hidalgo")
print(resultado_busqueda)

def count_word(counts):
    contador_palabra = len(counts)
    encontar_palabra = found_word(counts)

    return f"La palabra tiene {contador_palabra} y encontrar la palabra es {encontar_palabra}"

resultado_contador = count_word("Mexico")
print(resultado_contador)
    
