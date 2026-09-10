"""VOWEL COUNT"""
word = input()
VOWELS = "aeiouAEIOU"
count = 0
for letter in word:
    if letter in VOWELS:
        count += 1
print(count)
