a = [0]

current = 0

jump = 303

for i in range(1, 2018):
    current = (current + jump)%len(a)
    a.insert(current + 1, i)
    current += 1

print a[a.index(2017) + 1]