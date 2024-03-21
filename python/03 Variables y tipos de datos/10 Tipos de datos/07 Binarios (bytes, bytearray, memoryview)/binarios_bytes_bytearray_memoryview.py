mi_secuencia_de_bytes = b'Hola mundo'
print(mi_secuencia_de_bytes)

mi_bytearray = bytearray(b'Hola mundo')
mi_bytearray[0] = ord('C')
print(mi_bytearray)

mi_memoryview = memoryview(b'Hola mundo')
# mi_memoryview[0] = ord('C')
print(mi_memoryview)