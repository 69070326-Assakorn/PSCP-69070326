"""MOVIETICKET"""
n = int(input())
while n > 0:
    age, ticket = map(int, input().split())
    if age < 15:
        print(-1)
    elif ticket > n:
        print(-2)
    else:
        if age <= 22:
            PRICE = 120
        elif age >= 60:
            PRICE = 75
        else:
            PRICE = 150
        n -= ticket
        print(PRICE * ticket, n)
