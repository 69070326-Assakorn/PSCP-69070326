"""RABBIT LOVE BUU"""
s = input()
ans = 0
for i, char in enumerate(s):
    if char.lower() == 'b':
        n = 0
        j = i + 1
        while j < len(s) and s[j].lower() == 'u':
            n += 1
            j += 1
        ans = max(ans, n)
if ans >= 2:
    print("Yes", ans)
elif 'b' in s.lower():
    i = s.lower().index('b')
    print(s[:i+1] + 'U' * (len(s)-i-1))
else:
    print(('BUU' * len(s))[:len(s)])
