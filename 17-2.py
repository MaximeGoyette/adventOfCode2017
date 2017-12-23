current = 0

jump = 303

answer = None

for i in range(1, 50000001):
    current = (current + jump)%i
    if current == 0:
        answer = i
    current += 1

print answer