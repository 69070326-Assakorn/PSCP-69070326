"""Milk"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
milk = d // a

if not b:
    print(milk)
else:
    caps = milk
    while caps >= b:
        t = caps // b
        milk += t * c
        caps = caps % b + t * c
    print(milk)
