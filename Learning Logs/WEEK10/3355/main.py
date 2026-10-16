"""SHORTEN"""
def main():
    """SHORTEN"""
    ALL = []
    while True:
        number = int(input())
        if number == -1:
            break
        ALL.append(number)

    SUM = []
    start = 0
    while start < len(ALL):
        stop = start
        while stop + 1 < len(ALL) and ALL[stop + 1] == ALL[stop] + 1:
            stop += 1
        SUM.append(f"{ALL[start]}-{ALL[stop]}" if stop > start else str(ALL[start]))
        start = stop + 1
    print(", ".join(SUM))
main()
