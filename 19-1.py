a = open('19.txt').read()

d = {'down': (1, 0), 'up': (-1, 0), 'left': (0, -1), 'right': (0, 1)}
cd = 'down'

a = [list(x) for x in a.split('\n')]

for i in range(len(a[0])):
    if a[0][i] == '|':
        cc = (0, i)

path = []

n = 1

while True:
    next_c = (cc[0] + d[cd][0], cc[1] + d[cd][1])
    if next_c[0] >= 0 and next_c[0] < len(a) and next_c[1] >= 0 and next_c[1] < len(a[0]):
        cc = next_c
    else:
        break
    if not a[cc[0]][cc[1]] in ['+', ' ', '-', '|']:
        path.append(a[cc[0]][cc[1]])
    elif a[cc[0]][cc[1]] == '+':
        if cd == 'down' or cd == 'up':
            if a[cc[0]][cc[1] - 1] != ' ':
                cd = 'left'
            else:
                cd = 'right'
        else:
            if a[cc[0] - 1][cc[1]] != ' ':
                cd = 'up'
            else:
                cd = 'down'
    n += 1
    if cc == (5, 67):
        break

print ''.join(path)