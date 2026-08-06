"""LEAP YEAR"""
year = int(input())
if year < 1582:
    if not year % 4:
        print("yes")
    elif year == 1500:
        print("yes")
    else:
        print("no")
else:
    if not year % 4 and (year % 100 or not year % 400 ):
        print("yes")
    else:
        print("no")
