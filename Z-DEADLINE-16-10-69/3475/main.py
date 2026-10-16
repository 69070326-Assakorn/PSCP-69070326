"""MUDDLED MENU"""
menu = []

while True:
    s = input().strip()
    if s == "DONE":
        break
    if s == "CLOSED":
        menu.clear()
        break
    if s == "SOMETHING'S WRONG":
        menu.clear()
        continue
    if s == "Can't do":
        if menu:
            menu.pop()
        continue
    if s.startswith("Can't do:"):
        food = s[len("Can't do:"):].strip()
        if food in menu:
            menu.remove(food)
        continue
    if " #" in s:
        food, order = s.rsplit(" #", 1)
        food = food.strip()
        if order == "N":
            menu.append(food)
        elif order.isdigit():
            pos = int(order) - 1
            menu.insert(min(pos, len(menu)), food)
print(f"Full Course: {menu} Reversed: {menu[::-1]}")
