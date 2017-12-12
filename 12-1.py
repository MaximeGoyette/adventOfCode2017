a = open('12.txt').read()
a = a.split('\n')
a = [x.split(' <-> ') for x in a]
a = [(int(a[i][0]), map(int, a[i][1].split(', '))) for i in range(len(a))]

to_check = [0]
group = []

for x in to_check:
    for y in a[x][1]:
        if y not in group:
            to_check += [y]
            group += [y]

print len(group)