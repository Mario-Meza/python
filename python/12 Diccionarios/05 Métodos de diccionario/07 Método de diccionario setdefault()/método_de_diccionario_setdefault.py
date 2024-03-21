"""
    setdefault() es un método de diccionario en Python que devuelve el valor de una
    clave específica. Si la clave no existe, el método crea la clave con el valor predeter-
    minado especificado.
"""
auto = { "fabricante": "Tesla" }

valor = auto.setdefault("fabricantes", "Tesla1")
print(auto)
