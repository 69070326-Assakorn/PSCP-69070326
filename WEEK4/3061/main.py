"""PASS/FAIL"""
midterm = int(input())
final = int(input())
score = midterm + final
print(score)
if score >= 50:
    print("pass")
else:
    print("fail")
