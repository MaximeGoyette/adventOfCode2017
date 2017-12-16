initial = list('abcdefghijklmnop')

p = initial[:]

a = open('16.txt').read()
a = a.split(',')
a = [(x[0], x[1:]) for x in a]

def spin(a, n):
    return a[-n:] + a[:-n]

def exchange(a, A, B):
    c = a[int(A)]
    a[int(A)] = a[int(B)]
    a[int(B)] = c
    return a

def partners(a, A, B):
    i1 = a.index(A)
    i2 = a.index(B)
    return exchange(a, i1, i2)

def dance(a, p):
    for x in a:
        if x[0] == 's':
            p = spin(p, int(x[1]))
        elif x[0] == 'x':
            p = exchange(p, *x[1].split('/'))
        elif x[0] == 'p':
            p = partners(p, *x[1].split('/'))
    return p

n = 0

while True:
    p = dance(a, p)
    n += 1
    if p == initial:
        break

for i in range(1000000000%n):
    p = dance(a, p)

print ''.join(p)