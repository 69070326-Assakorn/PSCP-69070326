"""PASSING UNDER THE BRIDGE"""
def main():
    """PASSING UNDER THE BRIDGE"""
    _, N = map(int, input().split())
    events = []

    for _ in range(N):
        A, B = map(int, input().split())
        events.append((A, 1))
        events.append((B, -1))

    events.sort()
    current = 0
    answer = 0

    for _, change in events:
        current += change
        answer = max(answer, current)
    print(answer)
main()
