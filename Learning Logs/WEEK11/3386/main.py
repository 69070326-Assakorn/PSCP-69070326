"""DUPLICATE I"""
m = int(input())
n = int(input())
g1 = {input().strip() for _ in range(m)}
g2 = {input().strip() for _ in range(n)}

check = sorted(g1 & g2, key=int, reverse=True)
if not check:
    print("Nope")
else:
    for x in check:
        print(x)
