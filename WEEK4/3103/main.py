"""AEIOU LOOP"""
n = int(input())
for i in range(n):
    letter = input()
    count = 0
    for alphabet in letter:
        if alphabet in "aeiouAEIOU":
            count += 1
    print(count)
