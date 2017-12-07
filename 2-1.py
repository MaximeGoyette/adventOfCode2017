a = open('2.txt').read()

a = a.split('\n')

a = [map(int, x.split('\t')) for x in a]

print sum([max(x)-min(x) for x in a])