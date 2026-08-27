"""EXPRESS"""
a, b = input().split()
kg = float(input())

if a == "BKK" and b == "CNX":
    print(f"{10 + 30 * kg:.2f}")
elif a == "CNX" and b == "UBP":
    print(f"{15 + 40 * kg:.2f}")
elif a == "UBP" and b == "BKK":
    print(f"{20 + 40 * kg:.2f}")
elif a == "BKK" and b == "PKT":
    print(f"{25 + 50 * kg:.2f}")
elif a == "PKT" and b == "CNX":
    print(f"{30 + 60 * kg:.2f}")
elif a == "UBP" and b == "PKT":
    print(f"{40 + 70 * kg:.2f}")
else:
    print("Error")
