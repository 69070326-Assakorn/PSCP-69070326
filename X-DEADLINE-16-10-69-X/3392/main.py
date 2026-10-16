"""ARRAY HAHE"""
array = [0] * 50

for i in range(3):
    array[i] = int(input())
    print(f"Input number {i + 1} stored.")

while True:
    menu = int(input())
    if not menu:
        break
    if menu == 1:
        print(f"Original order: {array[0]} {array[1]} {array[2]}")
    elif menu == 2:
        desc = sorted(array[:3], reverse=True)
        print(f"Descending order: {desc[0]} {desc[1]} {desc[2]}")
    elif menu == 3:
        asc = sorted(array[:3])
        print(f"Ascending order: {asc[0]} {asc[1]} {asc[2]}")
