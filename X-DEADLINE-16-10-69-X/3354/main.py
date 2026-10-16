"""HINT"""
def main():
    """Find matching numbers."""
    a, x = input().split()
    b, y = input().split()
    c, z = input().split()

    for i in range(1000):
        n = f"{i:03d}"
        h, t, u = int(n[0]), int(n[1]), int(n[2])

        def check(v, op, k):
            """Check condition."""
            k = int(k)
            if op == "==":
                return v == k
            if op == "!=":
                return v != k
            if op == ">":
                return v > k
            if op == ">=":
                return v >= k
            if op == "<":
                return v < k
            if op == "<=":
                return v <= k
            return False

        if check(u, a, x) and check(t, b, y) and check(h, c, z):
            print(n)
main()
