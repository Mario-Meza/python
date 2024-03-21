def mi_generador(n):
    for i in range(n):
        yield i**2

generador_cuadrados = mi_generador(5)

print(next(generador_cuadrados))
print(next(generador_cuadrados))
print(next(generador_cuadrados))
print(next(generador_cuadrados))
print(next(generador_cuadrados))
print(next(generador_cuadrados))