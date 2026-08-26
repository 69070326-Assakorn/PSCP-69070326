"""SEASON"""
month = int(input())
day = int(input())

if month in [1, 2, 3]:
    season = "winter"
elif month in [4, 5, 6]:
    season = "spring"
elif month in [7, 8, 9]:
    season = "summer"
else:
    season = "fall"
if day >= 21 and month in [3, 6, 9, 12]:
    if season == "winter":
        season = "spring"
    elif season == "spring":
        season = "summer"
    elif season == "summer":
        season = "fall"
    else:
        season = "winter"
print(season)
