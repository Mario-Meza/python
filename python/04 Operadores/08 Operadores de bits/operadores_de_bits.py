a = 0b10101010
b = 0b11001100
c = a & b # 0b10001000

print(bin(c))

a = 0b10101010
b = 0b11001100
c = a | b # 0b11101110

print(bin(c))

a = 0b10101010
b = 0b11001100
c = a ^ b # 0b01100110

print(bin(c))

a = 0b10101010
b = a >> 2 # 0b00101010

print(bin(b))

a = 0b10101010
b = a << 2 # 0b1010101000

print(bin(b))

print(0b1101 & 0b1010)