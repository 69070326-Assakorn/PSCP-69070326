"""BIRD"""
N = int(input())
H = list(map(int, input().split()))
ans = 0

for i in range(N):
    left_ok = (not i or H[i] > H[i - 1])
    right_ok = (i == N - 1 or H[i] > H[i + 1])

    if left_ok and right_ok:
        ans += 1
print(ans)
