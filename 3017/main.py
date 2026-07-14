"""BILL"""

price = float(input())
service = price * 0.1

if service <= 50:
    service = 50

elif service >= 1000:
    service = 1000

vat =  (price + service) *0.07
print(f"{(price + service + vat):.2f}")
