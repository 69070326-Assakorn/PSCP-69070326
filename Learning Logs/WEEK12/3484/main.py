"""ROBOT"""
a = input().split()
n = int(a[0])
p = float(a[1])

grid = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    grid.append(row)

for r in range(n):
    count = 0
    points = 0
    for x in grid[r]:
        if x > 0:
            count += 1
        points += x
    print(*grid[r], count, points)

collumn_count = []
collumn_points = []

for c in range(n):
    count = 0
    points = 0
    for r in range(n):
        x = grid[r][c]
        if x > 0:
            count += 1
        points += x
    collumn_count.append(count)
    collumn_points.append(points)

print(*collumn_count)
print(*collumn_points)

total_tiles = sum(collumn_count)
total_points = sum(collumn_points)
fine = total_points * p

print(f"{total_tiles} {total_points} {fine:.2f}")
