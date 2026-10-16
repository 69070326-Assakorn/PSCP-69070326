"""BULLET"""
def main():
    """BULLET"""
    n = int(input())
    bullets = []

    for _ in range(n):
        x, y, d = map(int, input().split())
        bullets.append((x, y, d))
    found = False

    for tx in range(1000):
        for ty in range(1000):
            if all((tx - x)**2 + (ty - y)**2 == d**2
                   for x, y, d in bullets):
                print(tx, ty)
                found = True
                break
        if found:
            break
main()
