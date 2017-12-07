from itertools import permutations

a = open('2.txt').read()
a = a.split('\n')
a = [map(int, x.split('\t')) for x in a]

total = 0

for x in a:
    for y in permutations(x, 2):
        if y[0]%y[1]==0:
            total += y[0]//y[1]

print total
