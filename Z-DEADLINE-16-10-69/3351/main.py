"""RABBIT LANGUAGE"""
s = input().upper()
n = len(s)
if all(c in "IT" for c in s):
    print("unknown", n)
else:
    best = 0
    count = 0
    error = -1
    for i in range(n):
        c = s[i]
        if c not in "RABIT":
            error = i
            break
        if c == "A":
            if not i or s[i-1] not in "RA":
                error = i
                break
            count += 1
            best = max(best, count)
        else:
            count = 0
        if c == "R" and (i == n-1 or s[i+1] != "A"):
            error = i + 1 if i + 1 < n else i
            break
        if c == "B" and (i == n-1 or s[i+1] not in "IT"):
            error = i + 1 if i + 1 < n else i
            break
    if error != -1:
        print("no", error)
    else:
        print("yes", best)
    