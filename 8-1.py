a = open('8.txt').read().split('\n')

r = {}

for x in a:
    b = x.split()[0]
    r[b] = 0

for x in a:
    c = x.split()
    c = [c[0], '+' if c[1]=='inc' else '-', c[2], "r['"+c[4]+"']", c[5], c[6]]
    exec("r['{0}'] = r['{0}'] {1} {2} if {3} {4} {5} else r['{0}']".format(*c))
    
print max([r[x] for x in r])