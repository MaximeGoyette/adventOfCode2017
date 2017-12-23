a = open('20.txt').read()
a = a.split('\n')
a = [x.split(', ') for x in a]
a = [[map(int, y.split('<')[1].split('>')[0].split(',')) for y in x] for x in a]

def abs_vec(a):
    return [abs(x) for x in a]

m = (0, a[0])

for i in range(len(a)):
    if sum(abs_vec(a[i][2])) < sum(abs_vec(m[1][2])):
        m = (i, a[i])

print m[0]
