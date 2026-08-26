"""Temperature"""
T = float(input())
have = input()
want = input()
if have == "C" and want == "F":
    print(f"{T * 9 / 5 + 32:.2f}")
elif have == "F" and want == "C":
    print(f"{(T - 32) * 5 / 9:.2f}")
elif have == "C" and want == "K":
    print(f"{T + 273.15:.2f}")
elif have == "K" and want == "C":
    print(f"{T - 273.15:.2f}")
elif have == "C" and want == "R":
    print(f"{(T + 273.15) * 9 / 5:.2f}")
elif have == "R" and want == "C":
    print(f"{T * 5 / 9 - 273.15:.2f}")
elif have == "F" and want == "K":
    print(f"{(T - 32) * 5 / 9 + 273.15:.2f}")
elif have == "K" and want == "F":
    print(f"{(T - 273.15) * 9 / 5 + 32:.2f}")
elif have == "F" and want == "R":
    print(f"{T + 459.67:.2f}")
elif have == "R" and want == "F":
    print(f"{T - 459.67:.2f}")
elif have == "K" and want == "R":
    print(f"{T * 9 / 5:.2f}")
elif have == "R" and want == "K":
    print(f"{T * 5 / 9:.2f}")
else:
    print(f"{T:.2f}")
