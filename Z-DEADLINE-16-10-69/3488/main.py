"""LIGHT-ROLLERCOASTER"""
def main():
    """LIGHT""" 
    n = int(input())
    covered = [0] * 360
    for _ in range(n):
        a, b = map(int, input().split())
        while a != b:
            covered[a] += 1
            a = (a + 1) % 360
    if all(x > 0 for x in covered):
        print(360)
    else:
        ans = 0
        cnt = 0
        for i in range(720):
            if covered[i % 360] > 0:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        print(min(ans, 360))
main()
