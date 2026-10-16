"""PIG"""
n = int(input())
w = list(map(int, input().split()))
ans = []

for i in range(0, 2 * n, 2):
    ans.append(max(w[i], w[i + 1]))
if n == 1:
    print(ans[0])
else:
    print(" + ".join(map(str, ans)), "=", sum(ans))
