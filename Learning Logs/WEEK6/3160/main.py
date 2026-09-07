"""PRIME NUMBERS"""
start, end = map(int, input().split())
primes = []

for n in range(start, end + 1):
    prime = True
    for i in range(2, n):
        if not n % i:
            prime = False
            break
    if prime and n > 1:
        primes.append(n)
if len(primes) > 0:
    print(*primes)
print("Total primes:", len(primes))
