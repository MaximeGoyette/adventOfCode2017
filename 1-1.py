a = open('1.txt').read()

total = 0
jump = 1

for i in range(len(a)):
    if a[i] == a[(i + jump)%len(a)]:
        total += int(a[i])

print total