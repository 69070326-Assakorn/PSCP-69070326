"""AR TIKTOK"""
r, x, y = map(int, input().split())

distance = x * x + y * y
radius = r * r

if distance < radius:
    print("IN")
elif distance == radius:
    print("ON")
else:
    print("OUT")
