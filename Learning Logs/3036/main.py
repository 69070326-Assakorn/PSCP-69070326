"""CASTLE"""
import math
room = int(input())
row = math.ceil(math.sqrt(room))
answer = 0
while room > 1:
    position = room - (row - 1) ** 2
    if position % 2 == 0:
        room = (row - 1) ** 2 + position // 2
    else:
        room = (row - 1) ** 2 + (position + 1) // 2
    answer += 1
    row = math.ceil(math.sqrt(room))
print(answer)
