"""Castle"""
num = int(input())
floor = 1
maxnum = 1

while maxnum < num:
    floor += 1
    maxnum = floor**2

MINNUM = (floor - 1) ** 2 + 1

if not (MINNUM - num) % 2:
    print((floor - 1) * 2)
else:
    print((floor - 1) * 2 - 1)
