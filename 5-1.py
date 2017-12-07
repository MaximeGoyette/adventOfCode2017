a = open('5.txt').read()
a = a.split('\n')

a = map(int, a)

n = 0
i = 0

while i>=0 and i<len(a):
     a[i] += 1
     i += a[i] - 1
     n += 1

print n