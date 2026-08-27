"""RABBIT EAT RAMEN"""
size, kind = input().split()
top = input()

if size == "S":
    if kind == "R":
        price = 60
    else:
        price = 80

elif size == "M":
    if kind == "R":
        price = 80
    else:
        price = 100

else:
    if kind == "R":
        price = 100
    else:
        price = 120

if top == "N":
    print(price)
else:
    t, num = top.split()
    num = int(num)

    if t == "P":
        price = price + 15 * num
    else:
        price = price + 10 * num
    print(price)
