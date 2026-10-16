"""TEAM"""
N, M = map(int, input().split())
if not (1 <= N <= 10 and 1 <= M <= 20):
    print("Data Incorrect")
else:
    total = 0
    teams = []
    for i in range(N):
        scores = list(map(int, input().split()))

        if len(scores) != M or any(x < 0 or x > 100 for x in scores):
            print("Data Incorrect")
            break
        teams.append(scores)
        total += sum(scores)

    else:
        for i, scores in enumerate(teams, start=1):
            avg = sum(scores) / M
            maximum = max(scores)
            print(f"Team {i}: Average = {avg:.2f}, Max = {maximum}")
        print(f"Total Score of All Teams = {total}")
