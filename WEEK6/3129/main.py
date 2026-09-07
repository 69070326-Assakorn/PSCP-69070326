"""COFFEE SHOP SALES"""
n = int(input())
price = []
total = 0
for i in range(n):
    price.append(int(input()))
    total += price[i]
print(total)
print(max(price))
print(min(price))
print(f"{total / n:.1f}")
