"""Inflation"""
money = int(float(input()) * 100)
year = int(input())
for moneyy in range(year):
    money = money*10381//10000
moneyy = money//100
dot = money%100
print(f"{moneyy}.{dot:02d}")
