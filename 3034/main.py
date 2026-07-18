"""Passenger pod"""
n, k = map(int, input().split())
total = n
line = [0] * k

while n > 0:
    row = int(input())
    line[row - 1] += 1
    n -= 1
rounds = min(line)
print(total - rounds * k)
