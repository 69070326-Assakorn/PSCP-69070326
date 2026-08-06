"""EVEN,ODD"""
n1 = int(input())
n2 = int(input())
n3 = int(input())
even = 0
odd = 0
for i in [n1, n2, n3]:
    if not i % 2:
        even += 1
    else:
        odd += 1
print(even)
print(odd)
