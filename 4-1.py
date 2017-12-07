a = open('4.txt').read()
a = a.split('\n')

print sum([1 if len(x.split())==len(set(x.split())) else 0 for x in a])
