"""LAPPING"""
n, k = map(int, input().split())
times = [int(input()) for _ in range(n)]
s_min = min(times)
target = k * s_min
finalists = 0
for s in times:
    if (k - 1) * s < target:
        finalists += 1
print(finalists)
