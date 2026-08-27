"""PRICE&PROMOTION"""
a, b, c = map(int, input().split())

total = a * 25 + b * 40 + c * 55
count = a + b + c

if count >= 3:
    total = total * 90 // 100
print(total)
