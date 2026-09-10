"""CHRISTMAS LIGHTS"""
color , count = input().split()
count = int(count)
colors = ["Red", "Green", "Blue"]
start = {"R": 0, "G": 1, "B": 2}[color]

for i in range(count):
    print(colors[(start + i) % 3], end=" ")
