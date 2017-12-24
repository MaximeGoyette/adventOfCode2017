a = open('24.txt').read()

c = [tuple(map(int , x.split('/'))) for x in  a.split('\n')]

b = {}

m = 0

while True:
    s = [(0, 0)]

    a = c[:]

    while True:
        n = len(a)
        for x in a:
            if s[-1][1] in x:
                if b.get(tuple(s + [x]), None) == None and x[0] == s[-1][1]:
                    s.append(x)
                    a.remove(x)
                elif b.get(tuple(s + [x[::-1]]), None) == None and x[1] == s[-1][1]:
                    s.append(x[::-1])
                    a.remove(x)
                
        if len(a) == n:
            break

    if s == [(0, 0)]:
        break
    else:
        b[tuple(s)] = sum(map(sum, s))
        m = max([m, len(s)])

v = filter(lambda x: len(x) == m, b)

print max([b[x] for x in v])