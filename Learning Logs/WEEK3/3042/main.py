"""/10"""
n = int(input())
ans = []
for i in range(n, -1, -1):
    if not i % 10:
        ans.append(str(i))
print(" ".join(ans))
