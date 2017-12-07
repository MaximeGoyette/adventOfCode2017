import math

n = 361527
size = int(math.ceil(n**0.5))
d = [(0, 1), (-1, 0), (0, -1), (1, 0)]
cd = 0
l = 1
cl = 0
cc = (size//2+1, size//2)
a = [[0 for x in xrange(size+2)] for y in xrange(size+2)]
a[cc[0]][cc[1]] = 1

while True:
    value = sum(a[cc[0]-1][cc[1]-1:cc[1]+2] + a[cc[0]][cc[1]-1:cc[1]+2] + a[cc[0]+1][cc[1]-1:cc[1]+2])
    a[cc[0]][cc[1]] = value
    if value > n:
        print value
        break
    if cl == l:
        cl = 0
        cd = (cd + 1)%4
        if cd%2==0:
            l += 1

    cc = (cc[0] + d[cd][0], cc[1] + d[cd][1])
    cl += 1


