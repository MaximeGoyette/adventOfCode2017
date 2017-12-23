a = open('22.txt').read()

a = a.split('\n')

cc = (len(a)//2, len(a[0])//2)

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cd = 0

points = {}

n = 0

for y in range(len(a)):
    for x in range(len(a[0])):
        if a[y][x] == '#':
            points[(y, x)] = 'i'

for i in range(10000):
    if points.get(cc, None) == 'i':
        cd += 1
        del points[cc]
    else:
        cd -= 1
        points[cc] = 'i'
        n += 1
    cd %= len(d)
    cc = (cc[0] + d[cd][0], cc[1] + d[cd][1])

print n