"""TAXI"""
distance = int(input())

if not distance:
    print(0)
elif distance <= 1:
    print(35)
elif distance <= 10:
    print(35 + (distance - 1) * 5)
else:
    print(35 + 9 * 5 + (distance - 10) * 8)
