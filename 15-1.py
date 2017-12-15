"""
Generator A starts with 679
Generator B starts with 771
"""

a = [679, 16807]
b = [771, 48271]

f = 2147483647

n = 0

for i in range(40000000):
    a[0] = a[0]*a[1]%f
    b[0] = b[0]*b[1]%f

    if bin(a[0])[-16:] == bin(b[0])[-16:]:
        n += 1

print n    

