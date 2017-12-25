p = 0

a = {}

state = 'A'

for i in range(12399302):

    if state == 'A':
        if a.get(p, 0) == 0:
            a[p] = 1
            p += 1
            state = 'B'
        else:
            del a[p]
            p += 1
            state = 'C'

    elif state == 'B':
        if a.get(p, 0) == 0:
            p -= 1
            state = 'A'
        else:
            del a[p]
            p += 1
            state = 'D'

    elif state == 'C':
        if a.get(p, 0) == 0:
            a[p] = 1
            p += 1
            state = 'D'
        else:
            a[p] = 1
            p += 1
            state = 'A'

    elif state == 'D':
        if a.get(p, 0) == 0:
            a[p] = 1
            p -= 1
            state = 'E'
        else:
            del a[p]
            p -= 1
            state = 'D'
        
    elif state == 'E':
        if a.get(p, 0) == 0:
            a[p] = 1
            p += 1
            state = 'F'
        else:
            a[p] = 1
            p -= 1
            state = 'B'

    elif state == 'F':
        if a.get(p, 0) == 0:
            a[p] = 1
            p += 1
            state = 'A'
        else:
            a[p] = 1
            p += 1
            state = 'E'

print len([x for x in a if a[x] == 1])