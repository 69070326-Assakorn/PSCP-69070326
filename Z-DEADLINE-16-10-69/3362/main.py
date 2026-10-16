"""DESTINY"""
a = input().strip()
b = input().strip()

if len(a) < len(b):
    a, b = b, a

b += a[len(b):]

result = ""
for c in b:
    if c.lower() in "love":
        result += "w"
    else:
        result += "$"

longest = 0
current = 0

for c in result:
    if c == "w":
        current += 1
        longest = max(longest, current)
    else:
        current = 0

if longest % 2 == 1:
    result += str(longest)
elif longest < 2:
    result += "#"

print(result)