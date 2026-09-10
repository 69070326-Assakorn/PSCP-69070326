"""BABY FROG JUMP"""
x, y = map(int, input().split())
SUM = 0
count = 0

while SUM < y and x > 0:
    SUM += x
    count += 1
    x -= 2

if SUM >= y:
    print(count)
else:
    print(-1)
