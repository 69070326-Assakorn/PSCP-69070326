"""Coke"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if not b :
    print(a*d)
else:
    price = 0
    caps = 0
    count = 0
    while count < d:
        if caps >= b:
            caps -= b
            price += c
        else:
            price += a
        caps += 1
        count += 1
    print(price)
