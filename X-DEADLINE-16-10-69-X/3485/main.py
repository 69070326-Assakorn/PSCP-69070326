"""PASSWORDNOTSAME"""
def main():
    """PASSWORD"""
    n = int(input())
    nums = list(map(int, input().split()))[:n]
    result = sorted(x for x in nums if nums.count(x) == 1)
    print(*result)
main()
