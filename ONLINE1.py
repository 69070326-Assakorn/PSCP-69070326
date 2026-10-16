"""GCD_N"""
import math

def main():
    """GCD_N"""
    n = int(input())
    result = 0

    for _ in range(n):
        number = int(input())
        result = math.gcd(result, number)
    print(result)
main()
