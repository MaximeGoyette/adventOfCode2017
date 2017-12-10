l = range(256)
a = open('10.txt').read()
a = [ord(x) for x in a]
a += [17, 31, 73, 47, 23]
c = 0
skip = 0

for n in range(64):
    for x in a:
        sub = []
        for i in range(x):
            sub += [l[(c + i)%len(l)]]
        sub.reverse()
        for i in range(x):
            l[(c + i)%len(l)] = sub[i]
        c = (c + x + skip)%len(l)
        skip += 1

d = []
for n in range(16):
    d += [reduce(lambda x, y: x^y, l[n*16:n*16+16])]

d = map(lambda x: chr(x).encode('hex'), d)

print ''.join(d)