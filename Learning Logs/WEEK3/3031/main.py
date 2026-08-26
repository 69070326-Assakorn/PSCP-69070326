"""INK"""
import math
s, n = map(int, input().split())
PI = 3.1416
while n:
    x, y = map(int, input().split())
    print(math.ceil(PI * (x * x + y * y) / s))
    n -= 1
