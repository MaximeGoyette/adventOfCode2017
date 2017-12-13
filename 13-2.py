a = open('13.txt').read().split('\n')
a = [map(int, x.split(': ')) for x in a]

firewall = [0 for x in range(max(zip(*a)[0]) + 1)]

for x in a:
    firewall[x[0]] = x[1]

def is_safe(firewall, delay):
    pico = delay
    pos = 0

    while pos < len(firewall):
        if firewall[pos] > 0 and pico%(2*(firewall[pos] - 1)) == 0:
            return False
        pico += 1
        pos += 1

    return True

n = 0
while not is_safe(firewall, n):
    n += 1

print n