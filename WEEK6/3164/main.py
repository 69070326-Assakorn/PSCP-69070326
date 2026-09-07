"""SUM OF MUCH NUMBERS"""
def main():
    """SUM OF MUCH NUMBERS"""
    n = int(input())
    ans = []

    for _ in range(n):
        a = int(input())
        b = int(input())
        if a > b:
            ans.append(a)
        else:
            ans.append(b)

    if n <= 1:
        print(ans[0])
    else:
        print(" + ".join(map(str, ans)), "=", sum(ans))
main()
