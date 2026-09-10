"""HOTEL NO FLOOR 13"""
num = input()
KEY = list(map(int, num))

if KEY[0] > 5:
    A = 9
elif KEY[1] > 5:
    A = 10
elif KEY[2] > 5:
    A = 11
elif KEY[3] > 5:
    A = 12
elif KEY[4] > 5:
    A = 14
else:
    A = 13

if num == num[::-1]:
    if KEY[0] + KEY[4] > 5:
        B = 1
    elif KEY[1] * KEY[3] > 5:
        B = 2
    else:
        B = 0
else:
    if KEY[4] and KEY[0] // KEY[4] > 5:
        B = 1
    elif KEY[1] - KEY[4] > 5:
        B = 2
    else:
        B = 0

if sum(KEY) > 25:
    C = 1
elif KEY[0]*KEY[1]*KEY[2]*KEY[3]*KEY[4] > 55:
    C = 2
else:
    C = 0

ROOM = str(A) + str(B) + str(C)
print(ROOM)
