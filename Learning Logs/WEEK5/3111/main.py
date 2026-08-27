"""SCHOOL COOPERATIVE"""
from decimal import Decimal, ROUND_HALF_UP
def main():
    """SCHOOL COOPERATIVE"""
    member = input()
    n = int(input())
    total = Decimal(0)

    for _ in range(n):
        total += Decimal(input())

    if member == "Y":
        total = total * Decimal("0.95")
    elif total >= Decimal("500"):
        total = total * Decimal("0.97")
    print(total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
main()
