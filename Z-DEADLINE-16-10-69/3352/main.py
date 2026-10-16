"""LastStand"""
a = input().strip("[]").split(",")
for i in a:
    print(int(i) % 10)
