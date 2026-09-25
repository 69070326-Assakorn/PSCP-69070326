"""FLOWER BED"""
L, N = map(int, input().split())
d = 1
while N > d:
    N -= d
    d += 1
print((d + L - 1) // L)
