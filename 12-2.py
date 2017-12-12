a = open('12.txt').read()
a = a.split('\n')
a = [x.split(' <-> ') for x in a]
a = [(int(a[i][0]), map(int, a[i][1].split(', '))) for i in range(len(a))]

to_check = range(len(a))

groups = []

while len(to_check) > 0:
    l = [to_check[0]]
    current_group = []
    for x in l:
        try:
            to_check.remove(x)
        except:
            pass
        for y in a[x][1]:
            if y not in current_group:
                l += [y]
                current_group += [y]
    groups += [current_group]

print len(groups)