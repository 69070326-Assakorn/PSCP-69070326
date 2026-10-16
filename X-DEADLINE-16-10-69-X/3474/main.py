"""RESISTOR"""
digits = {
    "Black": 0,
    "Brown": 1,
    "Red": 2,
    "Orange": 3,
    "Yellow": 4,
    "Green": 5,
    "Blue": 6,
    "Purple": 7,
    "Grey": 8,
    "White": 9,
}
multipliers = {
    "Black": 1,
    "Brown": 10,
    "Red": 100,
    "Orange": 1000,
    "Yellow": 10000,
    "Green": 100000,
    "Blue": 1000000,
    "Purple": 10000000,
    "Gold": 0.1,
    "Silver": 0.01,
}
tolerances = {
    "Brown": 0.01,
    "Red": 0.02,
    "Green": 0.005,
    "Blue": 0.0025,
    "Purple": 0.0010,
    "Grey": 0.0005,
    "Gold": 0.05,
    "Silver": 0.10,
}
band1 = input()
band2 = input()
band3 = input()
band4 = input()

if (
    band1 in digits
    and band2 in digits
    and band3 in multipliers
    and band4 in tolerances
):
    BASE = (digits[band1] * 10 + digits[band2]) * multipliers[band3]
    LOWER = BASE * (1 - tolerances[band4])
    UPPER = BASE * (1 + tolerances[band4])
    print(f"{LOWER:.4f}")
    print(f"{UPPER:.4f}")
else:
    print("Error")
