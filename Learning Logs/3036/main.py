"""CASTLE"""

import math

room = int(input())

# หาแถวของห้อง
row = math.ceil(math.sqrt(room))

answer = 0

while room > 1:

    # หาตำแหน่งของห้องในแถว
    position = room - (row - 1) ** 2

    # ขึ้นไปแถวบน
    if position % 2 == 0:
        room = (row - 1) ** 2 + position // 2
    else:
        room = (row - 1) ** 2 + (position + 1) // 2

    answer += 1

    # หาแถวใหม่หลังจากขึ้น
    row = math.ceil(math.sqrt(room))

print(answer)
