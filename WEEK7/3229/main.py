"""GAME SCORE ONLINE"""
SCORE = int(input())
BONUS = int(input())
DAY = int(input())
SUM = SCORE + BONUS
if DAY >= 3:
    SUM *= 1.5
if SUM >= 1500:
    RANK = "5"
elif SUM >= 1000:
    RANK = "4"
elif SUM >= 500:
    RANK = "3"
elif SUM >= 200:
    RANK = "2"
else:
    RANK = "1"
if RANK == "5" and DAY >= 7:
    CODE = "99"
elif RANK == "4" and BONUS > 300:
    CODE = "88"
else:
    CODE = "0"
print(int(SUM))
print(RANK)
print(CODE)
