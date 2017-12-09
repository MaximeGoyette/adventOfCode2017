a = open('9.txt').read()

b = ''

i = 0
while i < len(a):
    if a[i] == '!':
        i += 1
    else:
        b += a[i]
    i += 1

c = ''

i = 0
while i < len(b):
    if b[i] == '<':
        while b[i] != '>':
            i += 1
    else:
        c += b[i]
    i += 1

d = []

i = 0
n = 1
while i < len(c):
    if c[i] == '{':
        n += 1
    elif c[i] == '}':
        n -= 1
        d += [n]
    i += 1

print sum(d)