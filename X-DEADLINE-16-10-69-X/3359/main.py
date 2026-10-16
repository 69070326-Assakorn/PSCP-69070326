"""CUPS"""
def main():
    """CUPS"""
    n = int(input())
    count = {}
    for _ in range(n):
        size = int(input())
        if size in count:
            count[size] += 1
        else:
            count[size] = 1
    print(max(count.values()))
main()
