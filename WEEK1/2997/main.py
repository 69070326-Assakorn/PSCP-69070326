"""ELO"""
RA = float(input())
RB = float(input())
P = input()

EB = 1/(1+(10**((RA-RB)/400)))
EA = 1/(1+(10**((RB-RA)/400)))

if P == "B":
    print(f"{EB:.2f}")
elif P == "A":
    print(f"{EA:.2f}")
