"""ATM"""
money = int(input())

if 100 <= money <=20000 and not money % 100:
    for bill in [1000, 500, 100]:
        count = money // bill
        money %= bill
        if count>0:
            print(f"{bill} = {count}")
else:
    print("ERROR")
