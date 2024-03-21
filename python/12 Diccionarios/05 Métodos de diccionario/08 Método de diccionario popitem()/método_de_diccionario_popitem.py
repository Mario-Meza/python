"""
El método popitem() elimina el último elemento insertado en el diccionario. 
En tu caso, siempre eliminará "año": 2023 y lo imprimirá, luego imprimirá el diccionario restante.
"""

tesla_model_3 = {
    "fabricante": "Tesla",
    "modelo": "Model 3",
    "año": 2023
}

elemento_eliminado = tesla_model_3.popitem()
print(elemento_eliminado)
print(tesla_model_3)