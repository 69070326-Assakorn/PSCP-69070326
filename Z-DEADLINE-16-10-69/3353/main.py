"""PickThemAgain"""
numbers = list(map(int, input().split()))
found = False
for n in reversed(numbers):
    if not n % 3 or not n % 5:
        print(n)
        found = True
if not found:
    print("Nope")
