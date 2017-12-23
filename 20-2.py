a = """p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>"""

a = open('20.txt').read()
a = a.split('\n')
a = [x.split(', ') for x in a]
a = [[map(int, y.split('<')[1].split('>')[0].split(',')) for y in x] for x in a]

def add_vectors(a, b):
    return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]

def next_vector(a):
    ac = a[2]
    v = add_vectors(ac, a[1])
    p = add_vectors(v, a[0])
    return [p, v, ac]

while True:
    for x in a:
        n = len(filter(lambda y: y[0] == x[0], a))
        if n > 1:
            a = filter(lambda y: y[0] != x[0], a)
    for i in range(len(a)):
        a[i] = next_vector(a[i])

    print len(a)