l = range(256)
a = eval('[' + open('10.txt').read() + ']')
c = 0
skip = 0

for x in a:
    sub = []
    for i in range(x):
        sub += [l[(c + i)%len(l)]]
    sub.reverse()
    for i in range(x):
        l[(c + i)%len(l)] = sub[i]
    c = (c + x + skip)%len(l)
    skip += 1

print l[0] * l[1]