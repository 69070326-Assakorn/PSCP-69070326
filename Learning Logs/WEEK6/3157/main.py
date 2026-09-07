"""GAME POINTS"""
n = int(input())
points = 0
for _ in range(n):
    point = input()
    if point == "+":
        points += 10
    elif point == "-":
        points -= 5
print(points)
