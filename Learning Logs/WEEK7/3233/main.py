"""LOTTERY"""
a = input().split()
b = input().split()

x, y = a
p, q = b

if x == p and y == q:
    print(1000000)
elif y == q:
    print(100000)
elif x == p and y[-3:] == q[-3:]:
    print(2000)
elif x == p and y[-2:] == q[-2:]:
    print(1000)
elif y[-3:] == q[-3:]:
    print(200)
elif y[-2:] == q[-2:]:
    print(100)
elif x == p:
    print(20)
else:
    print(0)
