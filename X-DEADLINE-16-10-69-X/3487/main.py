"""LIGHT BULB"""
def main():
    """LIGHT"""
    n = int(input())
    lists = []
    for _ in range(n):
        lists.append(int(input()))
    lists.sort()

    TOTAL = 0
    left = 0
    for HEIGHT in lists:
        left += HEIGHT
        TOTAL += left * 2
    print(TOTAL)
main()
