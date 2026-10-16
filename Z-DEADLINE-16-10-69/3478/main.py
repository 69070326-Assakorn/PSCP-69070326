"""EASY HISTOGRAM"""
s = input()
count = {}
for ch in s:
    if ch.isalpha() and ch.isascii():
        count[ch] = count.get(ch, 0) + 1
for ch in sorted(count, key=lambda c: (c.lower(), c.isupper())):
    print(f"{ch} = {count[ch]}")
