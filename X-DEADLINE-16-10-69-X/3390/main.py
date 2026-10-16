"""ARRAY 2D"""
array = []
errorrow = -1
errorcolumn = -1

for _ in range(5):
    array.append(list(map(int, input().split())))

for i in range(5):
    if sum(array[i]) % 2:
        errorrow = i
        break

for r in range(5):
    SUM = 0
    for n in range(5):
        SUM += array[n][r]
    if SUM % 2:
        errorcolumn = r
        break
print(f"{errorrow} {errorcolumn}")
