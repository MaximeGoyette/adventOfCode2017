key = 'vbqugkhl'

def knot_hash(a):
    l = range(256)
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

    return ''.join(d)

total = 0

for i in range(128):
    h = knot_hash('{}-{}'.format(key, i))
    row = ''.join(['{0:0{1}b}'.format(int(x, 16),4) for x in h])
    total += row.count('1')

print total