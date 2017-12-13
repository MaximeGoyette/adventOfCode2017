a = open('13.txt').read().split('\n')
a = [map(int, x.split(': ')) for x in a]

firewall = [0 for x in range(max(zip(*a)[0]) + 1)]

for x in a:
    firewall[x[0]] = x[1]

def get_severity(firewall):
    pico = 0
    severity = 0

    while pico < len(firewall):
        if firewall[pico] > 0 and pico%(2*(firewall[pico] - 1)) == 0:
            severity += firewall[pico] * pico
        pico += 1

    return severity 

print get_severity(firewall)