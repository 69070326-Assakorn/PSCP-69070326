"""LIFE BALANCE"""
def main():
    """LIFE BALANCE"""
    n = int(input())
    long = 0
    short = 0
    for _ in range(n):
        h = int(input())
        if h > 18:
            long += 1
        else:
            short += 1
    ans = n + max(0, long - 1 - short)
    print(ans)
main()
