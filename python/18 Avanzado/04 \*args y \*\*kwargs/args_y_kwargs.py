def sueldo(*args, **kwargs):
    total_sueldo = 0
    for arg in args:
        total_sueldo += arg
    for key, value in kwargs.items():
        total_sueldo += value
    return total_sueldo

print(sueldo(1000, 2000, 3000, juan=5000, pedro=8000))