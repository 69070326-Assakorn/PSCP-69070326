"""PADTHAI"""
need = {
    "Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp",
    "Bean Sprouts", "Noodle", "Chives", "Lime",
    "Egg", "Oil", "Peanuts"
}

taste = {"Sweet", "Sour", "Salty"}

ingredient = set()
while True:
    add = input().strip()
    if add == "Cook":
        break
    ingredient.add(add)

flavor = set()
while True:
    add = input().strip()
    if add == "End":
        break
    flavor.add(add)

if not ingredient.issubset(need):
    print("This is not Pad Thai!!!")
elif ingredient != need:
    print("This is bad!")
elif flavor == taste:
    print("Delicious!")
else:
    print("Not Bad...")
