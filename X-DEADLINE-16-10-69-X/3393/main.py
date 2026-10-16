"""CAVE EXPLORER"""
n = int(input())
cave = list(map(int, input().split()))
cmds = input().strip()
code = cave.index(1)
chest = cave.index(2)

for cmd in cmds:
    if cmd == "R":
        if code + 1 < n:
            code += 1
    elif cmd == "L":
        if code - 1 >= 0:
            code -= 1
    if code == chest:
        break
MAP = [0] * n
MAP[code] = 1
if code != chest:
    MAP[chest] = 2
print(*MAP)
