"""SEND"""
n, s = map(int, input().split())
send = [0] * (n + 1)

for i in range(1, n + 1):
    send[i] = int(input())
passed = set()
now = s
while now and now not in passed:
    passed.add(now)
    now = send[now]
print(len(passed))
