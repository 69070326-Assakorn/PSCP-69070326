"""gift"""
r, h, g = map(float, input().split())
width = h + 2 * r
length = 2 * 3.14 * r + g
print(f"{width:.2f} {length:.2f}")
