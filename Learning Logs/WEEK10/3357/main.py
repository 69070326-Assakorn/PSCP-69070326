"""GIRAFFE"""
n = int(input())
h = [int(input()) for _ in range(n)]
count = 0

for i in range(n):
    END = True
    if i > 0 and h[i] < h[i - 1]:
        END = False
    if i < n - 1 and h[i] < h[i + 1]:
        END = False
    if END:
        count += 1
print(count)
