"""test"""
n = int(input())

scores = [0] * n

for i in range(n):
    scores[i] = int(input())

max_score = max(scores)
top_count = scores.count(max_score)

print(max_score)
print(top_count)
