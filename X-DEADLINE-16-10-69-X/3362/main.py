"""DESTINY"""
name1 = input()
name2 = input()
len1 = len(name1)
len2 = len(name2)

if len1 < len2:
    difference = len2 - len1
    name1 += "".join(name1[i % len1] for i in range(difference))
elif len2 < len1:
    difference = len1 - len2
    name2 += "".join(name2[i % len2] for i in range(difference))

LOVE = "loveLOVE"
talisman = []

for i, c in enumerate(name1):
    if c in LOVE or name2[i] in LOVE:
        talisman.append("w")
    else:
        talisman.append("$")
RESULT = "".join(talisman)
TOTAL = RESULT.count("w")
RESULT = "".join(talisman)
TOTAL = RESULT.count("w")

if TOTAL % 2:
    MAX = 0
    CURRENT = 0
    for c in RESULT:
        if c == "w":
            CURRENT += 1
            if CURRENT > MAX:
                MAX = CURRENT
        else:
            CURRENT = 0
    RESULT += str(MAX)
else:
    if "ww" not in RESULT:
        RESULT += "#"

print(RESULT)
