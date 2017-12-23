from sympy.ntheory import isprime

a = 1
b = c = d = e = f = g = h = 0

b = 108100
c = 125100

while True:
    if not isprime(b):
        h += 1
    
    if b == c:
        break
    
    b += 17

print h