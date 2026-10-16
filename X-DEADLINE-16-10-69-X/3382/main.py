"""DAY09-9_02-BACKWARD"""
lists = []
while True:
    char = input()
    if char == "NULL":
        break
    lists.append(char)
for idx, _ in enumerate(lists):
    print(lists[(idx*-1)-1])
