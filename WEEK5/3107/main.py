"""BONUS"""
position, year, salary = input().split()

year = int(year)
salary = int(salary)

if position == "M":
    bonus = 1500
    if year <= 5:
        PERCENT = 6
    elif year <= 10:
        PERCENT = 8
    else:
        PERCENT = 10

elif position == "B":
    bonus = 1000
    if year <= 5:
        PERCENT = 5
    elif year <= 10:
        PERCENT = 6
    else:
        PERCENT = 7

else:
    bonus = 500
    if year <= 5:
        PERCENT = 4
    elif year <= 10:
        PERCENT = 5
    else:
        PERCENT = 6

bonus = bonus + (salary * PERCENT / 100)
print(int(bonus))
