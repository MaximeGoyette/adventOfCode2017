from sys import argv

a = argv[1]

total = 0
jump = len(a)//2

for i in range(len(a)):
    if a[i] == a[(i + jump)%len(a)]:
        total += int(a[i])

print total