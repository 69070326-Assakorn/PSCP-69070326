"""Distance 3D"""
from math import sqrt

x1, y1, z1 = map(int, input().split())
x2, y2, z2 = map(int, input().split())

distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)

print(f"{distance:.2f}")
