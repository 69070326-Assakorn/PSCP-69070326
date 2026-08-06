"""AEIOU LOOP"""
n = int(input())
count = 0
for letter in range(n):
    letter = input()
    if letter in ["A", "E", "I", "O", "U"]:
        count += 1
print(count)
