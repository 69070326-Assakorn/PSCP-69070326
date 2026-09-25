"""RIGHT ARROW"""
k = int(input())
n = int(input())
mid = n // 2
for i in range(n):
    spaces = abs(mid - i)
    print(" " * (mid - spaces) + "*" * k)
