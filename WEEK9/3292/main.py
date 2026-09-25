"""ARROW"""
direction = input()
length = int(input())

for i, d in enumerate(direction):
    for row in range(length * 2 - 1):
        if d == "R":
            if row < length:
                print(" " * (row * 2) + "*" * (length - row))
            else:
                print(" " * ((length * 2 - 2 - row) * 2) + "*" * (row - length + 2))
        elif d == "L":
            if row < length:
                print(" " * (length - row - 1) + "*" * (length - row))
            else:
                print(" " * (row - length + 1) + "*" * (row - length + 2))
    if i != len(direction) - 1:
        print()
