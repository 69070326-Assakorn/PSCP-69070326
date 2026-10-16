"""PSCP_P02"""
n = input()
ans = 0
for x in n:
    if x != '0':
        if not ans:
            ans = int(x)
        else:
            ans *= int(x)
print(ans)
