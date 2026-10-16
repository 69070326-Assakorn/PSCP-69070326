"""DEMONSLAYER"""
DEMON = [
    ["Spider Demon", 1],
    ["Swamp Demon", 2],
    ["Arrow Demon", 1],
    ["Hand Demon", 2],
    ["Drum Demon", 3],
    ["Mugen Train", 2],
    ["Upper Moon", 3],
]

KILL = 0
TOTAL = 0

while KILL < 5:
    NAME, WEAKNESS = DEMON.pop(0)
    print(NAME)
    KILLED_THIS_ROUND = False
    for _ in range(2):
        ATTACK = int(input())
        TOTAL += 1
        if ATTACK == WEAKNESS:
            print("kill")
            KILL += 1
            KILLED_THIS_ROUND = True
            break
    if not KILLED_THIS_ROUND:
        print("back")
        DEMON.append([NAME, WEAKNESS])
print(TOTAL)
