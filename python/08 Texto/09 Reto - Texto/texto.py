def procesar_texto(texto):
    # Imprimir la longitud del texto
    print(f"Longitud del texto: {len(texto)} caracteres")

    # Reemplazar todas las ocurrencias de 'Python' con 'C++'
    texto = texto.replace('python', 'Python')
    print(f"Texto modificado (reemplazando 'python' con 'Python'):\n{texto}")

    # Encontrar la posición de la primera aparición de la palabra 'desafiante'
    posicion = texto.find('desafiante')
    if posicion != -1:
        print(f"La palabra 'desafiante' comienza en la posición {posicion}")
    else:
        print("La palabra 'desafiante' no se encuentra en el texto")

    # Eliminar espacios en blanco al principio y al final del texto
    texto = texto.strip()
    print(f"Texto sin espacios en blanco al principio y al final:\n{texto}")

    # Dividir el texto en una lista de palabras
    palabras = texto.split()
    print("Lista de palabras en el texto:")
    for palabra in palabras:
        print(palabra)

    # Verificar si el texto comienza con la palabra 'Este'
    if texto.startswith('Este'):
        print("El texto comienza con 'Este'")
    else:
        print("El texto no comienza con 'Este'")

# Texto de ejemplo
texto_ejemplo = """Este es un texto de ejemplo.
python es un lenguaje de programación desafiante y poderoso.
"""

# Procesar el texto
procesar_texto(texto_ejemplo)
