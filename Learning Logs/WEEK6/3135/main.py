"""GIFTS AND THIEF"""
N, K, T = map(int, input().split())
player = 1
count = 0

while True:
    if player == T:
        count += 1
        break
    if player == 1 and count:
        break
    player = (player + K) % N
    count += 1
print(count)
