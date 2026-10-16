"""Align"""
size = int(input())
position = input()
text = input()
space = size - len(text)

if position == "left":
    result = text + " " * space
elif position == "right":
    result = " " * space + text
else:
    left_space = (space + 1) // 2
    right_space = space // 2
    result = " " * left_space + text + " " * right_space
print(result)
