"""RABBIT"""
def main():
    """RABBIT"""
    row, column = map(int, input().split())
    RABBIT_R, RABBIT_C = map(int, input().split())
    n = int(input())

    grid = [[0] * column for _ in range(row)]

    for _ in range(n):
        INF_R, INF_C = map(int, input().split())
        for i in range(max(0, INF_R - 2), min(row, INF_R + 3)):
            for j in range(max(0, INF_C - 2), min(column, INF_C + 3)):
                DIST = max(abs(i - INF_R), abs(j - INF_C))
                if not DIST:
                    RISK = 100
                elif DIST == 1:
                    RISK = 60
                else:
                    RISK = 20
                if RISK > grid[i][j]:
                    grid[i][j] = RISK

    SAFE = 0
    for r in range(row):
        for c in range(column):
            if not grid[r][c]:
                SAFE += 1
    print(SAFE)
    print(f"{grid[RABBIT_R][RABBIT_C]}%")
main()
