"""PICKTHEM"""
n = input()
listbefore = list(map(int, n.strip('[]').split(',')))
listnow = []
for i in listbefore:
    if not i % 2 or not i:
        listnow.append(i)
if not listnow:
    print("Nope")
else:
    for x in listnow:
        print(x)
