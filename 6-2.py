a = "14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4".split('\t')

a = map(int, a)

c = []
n = 0

def get_max(a):
    m = (0, 0)
    for i in range(len(a)):
        if a[i] > m[1]:
            m = (i, a[i])
    return m

while True:
    if ''.join(map(str, a)) in c:
        print len(c)-c.index(''.join(map(str, a)))
        break
    c += [''.join(map(str, a))]
    x = get_max(a)
    a[x[0]] = 0
    for i in range(1, x[1]+1):
        a[(x[0]+i)%len(a)] += 1
    n += 1
