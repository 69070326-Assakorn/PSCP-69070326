"""Arcade of Time: Store Check"""
def main():
    """CHECK"""
    num, _ = map(int, input().split())
    shops = []

    for _ in range(num):
        start, stop = map(int, input().split())
        shops.append((start, stop))

    times = list(map(int, input().split()))

    for t in times:
        count = 0
        for start, stop in shops:
            if start <= t < stop:
                count += 1

        print(count, end=" ")
main()
