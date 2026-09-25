"""BIGFRAME"""
def main():
    """BIGFRAME"""
    lines = []
    for _ in range(5):
        lines.append(input())
    width = max(len(line) for line in lines) + 4
    print("*" * width)

    for line in lines:
        print("* " + line + " " * (width - len(line) - 3) + "*")
    print("*" * width)
main()