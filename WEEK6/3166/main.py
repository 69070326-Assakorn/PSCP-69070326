"""PASS OR FAIL & AVG"""
def main():
    """PASS OR FAIL & AVG"""
    n = int(input())
    score = []
    for _ in range(n):
        score.append(int(input()))
    total = sum(score)
    average = total / n

    if average >= 60 and all(s >= 50 for s in score):
        print(f"{average:.1f}")
        print("PASS")
    else:
        print(f"{average:.1f}")
        print("FAIL")
main()
