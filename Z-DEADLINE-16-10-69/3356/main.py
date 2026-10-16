"""BUS"""
n = int(input())
m = int(input())
x = int(input())

for r in range(n - 1, -1, -1):
    row = []
    for c in range(m):
        seat = c * n + r + 1
        if seat == x:
            row.append("XX")
        else:
            row.append(f"{seat:02d}")
    print(" ".join(row))
    if not r % 2 and r:
        print()
