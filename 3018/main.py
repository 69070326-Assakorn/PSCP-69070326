"""Rectangle Area"""
x1, y1, w1, h1 = map(int, input().split())
x2, y2, w2, h2 = map(int, input().split())

left = max(x1, x2)
right = min(x1 + w1, x2 + w2)
bottom = max(y1, y2)
top = min(y1 + h1, y2 + h2)

if right <= left or top <= bottom:

    print("no overlapping")
else:
    print((right - left) * (top - bottom))
