"""Suvarnabhumi Airport Parking"""
from math import ceil

IN = input().split(".")
OUT = input().split(".")

IN_second = int(IN[0]) * 3600 + int(IN[1]) * 60
OUT_second = int(OUT[0]) * 3600 + int(OUT[1]) * 60

IN_check = 0 <= int(IN[0]) <= 24 and 0 <= int(IN[1]) <= 60
OUT_check = 0 <= int(OUT[0]) <= 24 and 0 <= int(OUT[1]) <= 60

hour = (OUT_second - IN_second) / 3600

if hour > 0.25:
    hour = ceil(hour)
elif hour < 0:
    hour = -1
else:
    hour = 0

if 0 <= hour <= 24 and IN_check and OUT_check:
    match hour:
        case 0:
            print("FREE")
        case 1:
            print("25")
        case 2:
            print("50")
        case 3:
            print("80")
        case 4:
            print("110")
        case 5:
            print("145")
        case 6:
            print("180")
        case _:
            print("250")
else:
    print("ERROR")
