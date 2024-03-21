"""
    - La recursividad es cuando una funcion se llama directamente asi misma o
      indirectamente para resolver un problema.
    - Cada llamada llamada recursiva reduce el problema original a un problema más pequeño
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1) # 1 * * 2 * 3 * 4 * 5 = 120
    
print(factorial(5))

# 1 x 2 x 3 x 4 x 5 = 120   5!

# 1 + 2 + 3 + 4 + ... + n = ?

def suma_de_naturales(n):
    if n == 1:
        return 1
    else:
        return n + suma_de_naturales(n-1)
    
print(suma_de_naturales(4))