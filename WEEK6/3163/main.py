"""Export products"""
def main():
    """Export products"""
    n = int(input())
    total = 0
    even = 0
    odd = 0

    for _ in range(n):
        price = int(input())
        total += price
        if not price % 2:
            even += 1
        else:
            odd += 1

    print("SUM", total)
    print("EVEN", even)
    print("ODD", odd)
main()
