"""ELECRIC USING"""
from decimal import Decimal, ROUND_HALF_UP
N = int(input())
if N <= 10:
    electricity = N * 5
elif N <= 50:
    electricity = 10 * 5 + (N - 10) * 7
elif N <= 100:
    electricity = 10 * 5 + 40 * 7 + (N - 50) * 10
elif N <= 200:
    electricity = 10 * 5 + 40 * 7 + 50 * 10 + (N - 100) * 12
else:
    electricity = 10 * 5 + 40 * 7 + 50 * 10 + 100 * 12 + (N - 200) * 15

ft = Decimal(N) * Decimal("0.50")
vat = Decimal(electricity) * Decimal("0.07")
total = Decimal(electricity) + ft + vat
total = total.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
print(total)
