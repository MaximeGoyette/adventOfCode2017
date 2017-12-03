import math

n = 21
size = int(math.ceil(n**0.5))
d = [(0, 1), (-1, 0), (0, -1), (1, 0)]
cd = 0
l = 1
cl = 0
cc = (size//2, size//2 - 1)
a = [[0 for x in xrange(size)] for y in xrange(size)]
a[cc[0]][cc[1]] = 1

for i in xrange(1, size**2 + 1):
    value = i
    a[cc[0]][cc[1]] = value

    if cl == l:
        cl = 0
        cd = (cd + 1)%4
        if cd%2==0:
            l += 1

    cc = (cc[0] + d[cd][0], cc[1] + d[cd][1])
    cl += 1

def find_v(a, v):
    for i in range(len(a)):
        if v in a[i]:
            return (a[i].index(v), i)

c1 = find_v(a, n)
c2 = find_v(a, 1)

print abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])