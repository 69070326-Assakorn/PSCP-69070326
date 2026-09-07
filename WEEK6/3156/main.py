"""CONAN"""
s = input()
k = int(input())
ans = ""

for c in s:
    ans += chr((ord(c) - ord('a') + k) % 26 + ord('a'))
print(ans)
