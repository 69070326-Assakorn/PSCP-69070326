"""3nPlus1"""
n = int(input())

while n:
    count = 1
    while n != 1:
        if not n % 2:
            n = n // 2
        else:
            n = n * 3 + 1
        count += 1

    print(count)
    n = int(input())
