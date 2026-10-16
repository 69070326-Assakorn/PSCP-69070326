"""DIFFERENCE"""
a = int(input())
b = int(input())
setA = set()
setB = set()

for _ in range(a):
    setA.add(int(input()))
for _ in range(b):
    setB.add(int(input()))
ans = sorted(setA - setB)
print(*ans)
