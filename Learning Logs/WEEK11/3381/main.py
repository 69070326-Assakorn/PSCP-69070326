"""POINT SORTING"""
t = int(input())
for _ in range(t):
    n = int(input())
    point = []
    for _ in range(n):
        x, y = map(int, input().split())
        point.append([x, y])
    point.sort(key=lambda pt:(pt[0]+pt[1],-pt[1]))
    for x, y in point:
        print(f"{x} {y}")
