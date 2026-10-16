"""TUPLE'S SAD LIFE"""
x = tuple(input().split())
y = input()
num = x.index(y)
side = x.count(y)
for _ in range(side):
    print(*(str(num)*side))
