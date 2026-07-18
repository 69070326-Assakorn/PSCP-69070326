"""min(4)"""
count = int(input())
minimum = int(input())
count -= 1
while count > 0:
    x = int(input())
    if x < minimum:
        minimum = x
    count -= 1
print(minimum)
