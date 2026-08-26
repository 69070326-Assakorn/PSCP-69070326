"""A-E-I-O-U"""
text = input().lower()
for x in "aeiou":
    if text.count(x) > 0:
        print(x,":",text.count(x))
