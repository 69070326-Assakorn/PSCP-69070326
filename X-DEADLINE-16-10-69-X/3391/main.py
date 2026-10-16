"""MAGICCOINS"""
n = int(input())
totalF = 0
totalW = 0
totalE = 0

for _ in range(n):
    f1, w1, e1, f2, w2, e2 = map(int, input().split())
    totalF += max(f1, f2)
    totalW += max(w1, w2)
    totalE += max(e1, e2)

TOTAL = totalF + totalW + totalE
print(f"Total: {TOTAL}")
print(f"Fire: {totalF}")
print(f"Water: {totalW}")
print(f"Earth: {totalE}")

if totalF > totalW + totalE:
    print("Bonus: YES")
else:
    print("Bonus: NO")
