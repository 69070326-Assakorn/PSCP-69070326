"""Calculator"""
n = int(input())
if n == 1:
    print(1)
else:
    count = 0
    for i in range(1, n + 1):
        count += len(str(i))
    print(count + n)
