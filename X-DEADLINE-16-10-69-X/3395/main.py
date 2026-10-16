"""QUEUE"""
n = int(input().split()[0])
h = list(map(int, input().split()))
customers = list(map(int, input().split()))
prefix = [0] * n
current = 0

for i in range(n):
    prefix[i] = current
    if h[i] > current:
        current = h[i]

for pos in customers:
    idx = pos - 1
    front = prefix[idx]
    chair = front - h[idx] + 1
    if chair < 0:
        chair = 0
    print(chair)
