"""
Generstor A starts with 679
Generator B starts with 771
"""

a = [679, 16807]
b = [771, 48271]

f = 2147483647

n = 0

for i in range(5000000):
    while True:
        a[0] = a[0]*a[1]%f
        if a[0]%4==0:
            break
    while True:
        b[0] = b[0]*b[1]%f
        if b[0]%8==0:
            break

    if bin(a[0])[-16:] == bin(b[0])[-16:]:
        n += 1

print n    

