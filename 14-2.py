key = 'vbqugkhl'

def knot_hash(a):
    l = range(256)
    a = [ord(x) for x in a]
    a += [17, 31, 73, 47, 23]
    c = 0
    skip = 0

    for n in range(64):
        for x in a:
            sub = []
            for i in range(x):
                sub += [l[(c + i)%len(l)]]
            sub.reverse()
            for i in range(x):
                l[(c + i)%len(l)] = sub[i]
            c = (c + x + skip)%len(l)
            skip += 1

    d = []
    for n in range(16):
        d += [reduce(lambda x, y: x^y, l[n*16:n*16+16])]

    d = map(lambda x: chr(x).encode('hex'), d)

    return ''.join(d)

grid = []

for i in range(128):
    h = knot_hash('{}-{}'.format(key, i))
    row = ''.join(['{0:0{1}b}'.format(int(x, 16),4) for x in h])
    grid += [[int(x) for x in row]]

used = []

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == 1:
            used.append((y, x))

regions = 0

while len(used) > 0:
    to_check = [used[0]]
    used.remove(to_check[0])
    for x in to_check:
        if (x[0], x[1] - 1) in used and x[1] >= 1 and grid[x[0]][x[1] - 1] == 1:
            used.remove((x[0], x[1] - 1))
            to_check.append((x[0], x[1] - 1))
        if (x[0], x[1] + 1) in used and x[1] < len(grid[0]) - 1 and grid[x[0]][x[1] + 1] == 1:
            used.remove((x[0], x[1] + 1))
            to_check.append((x[0], x[1] + 1))
        if (x[0] - 1, x[1]) in used and x[0] >= 1 and grid[x[0] - 1][x[1]] == 1:
            used.remove((x[0] - 1, x[1]))
            to_check.append((x[0] - 1, x[1]))
        if (x[0] + 1, x[1]) in used and x[0] < len(grid) - 1 and grid[x[0] + 1][x[1]] == 1:
            used.remove((x[0] + 1, x[1]))
            to_check.append((x[0] + 1, x[1]))
        grid[x[0]][x[1]] = 0
    regions += 1

print regions