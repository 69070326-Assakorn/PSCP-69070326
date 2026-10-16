"""BUSSTOP I"""
p = int(input())
n = int(input())
bus = []
signs = {}
ans = 0

for i in range(n):
    num = list(map(int, input().split()))
    signs[num[0]] = num[1:]

for i in range(1,n+1):
    now = bus.count(i)
    ans += now
    while i in bus:
        bus.remove(i)
    if i in signs:
        for n in signs[i]:
            if n > i:
                if len(bus) < p:
                    bus.append(n)
                else:
                    break
print(ans)
