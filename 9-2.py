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
g = False
n = 0
while i < len(b):
    if b[i] == '>':
        g = False
    if g:
        n += 1
    if b[i] == '<':
        g = True
    i += 1

print n