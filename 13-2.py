a = open('13.txt').read().split('\n')
a = [map(int, x.split(': ')) for x in a]

firewall = [0 for x in range(max(zip(*a)[0]) + 1)]

for x in a:
    firewall[x[0]] = x[1]

def is_safe(firewall, delay):
    for i in range(len(firewall)):
        if firewall[i] > 0 and (delay + i)%(2*(firewall[i] - 1)) == 0:
            return False

    return True

n = 0
while not is_safe(firewall, n):
    n += 1

print n