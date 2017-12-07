a = open('4.txt').read()
a = a.split('\n')

total = 0

for x in a:
    x = x.split()
    if (len(x) == len(set([''.join(sorted(y)) for y in x]))):
        total += 1

print total