"""exchange number"""
Num1 = int(input())
symbol = input()
NUM2 = int(str(Num1)[::-1])
if 10 <= Num1 <= 99:
    if symbol == "+":
        total = Num1 + NUM2
        print(Num1,"+",NUM2,"=",total)
    elif symbol == "*":
        total = Num1 * NUM2
        print(Num1,"*",NUM2,"=",total)
