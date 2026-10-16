"""SELL CAR"""
def main():
    """SELL"""
    N = int(input())
    cars = []
    for _ in range(N):
        P, V = map(int, input().split())
        cars.append((P, V))

    cars.sort(reverse=True)
    max_v = 0
    ans = 0

    for P, V in reversed(cars):
        if V < max_v:
            ans += 1
        max_v = max(max_v, V)
    print(ans)
main()
