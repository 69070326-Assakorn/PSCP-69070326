"""Birthday"""
from datetime import date
y1 = int(input())
m1 = int(input())
d1 = int(input())
y2 = int(input())
m2 = int(input())
d2 = int(input())

p1 = date(y1, m1, d1)
p2 = date(y2, m2, d2)

if p1 < p2:
    FIRST = 1
    diff = (p2 - p1).days
else:
    FIRST = 2
    diff = (p1 - p2).days

if diff <= 7:
    print(0)
else:
    print(FIRST)
