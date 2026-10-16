"""CUTECAT CUTEFOX"""
n = int(input())

cat = {}
fox = {}
names = set()

for _ in range(n):
    s = input().strip()
    s = s.replace("{", "").replace("}", "")
    a = s.split(":")

    x = a[0].strip().strip('"').strip("'")
    y = a[1].strip().strip('"').strip("'")

    if x[:3] in ("Cat", "Fox") and x[3:].isdigit():
        code = x
        name = y
    else:
        name = x
        code = y

    names.add(name)
    num = int(code[3:])

    if code.startswith("Cat"):
        cat[num] = (name, code)
    elif code.startswith("Fox"):
        fox[num] = (name, code)

if 1 not in cat and "Garfield" not in names:
    cat[1] = ("Garfield", "Cat01")

if 1 not in fox and "Fubuki" not in names:
    fox[1] = ("Fubuki", "Fox01")

print("Cat :", len(cat))
print("Fox :", len(fox))

for i in sorted(cat):
    name, code = cat[i]
    print(name, ":", code)

for i in sorted(fox):
    name, code = fox[i]
    print(name, ":", code)
