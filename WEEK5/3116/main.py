"""SCHOOL BUDGET"""
school = input().replace(" ", "")

n = len(school)

a = ord(school[0])
b = ord(school[-1])
x = []

for i in range(10):
    if i % 2 == 0:
        x.append((a + i) % n)
    else:
        x.append((b + i) % n)
        
x = [i % 10 for i in x]
print(*x[:6])
