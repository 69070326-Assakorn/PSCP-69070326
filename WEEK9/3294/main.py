"""TEACHING SCHEDULE"""
N = int(input())
A = int(input())
total = N * A

if not total:
    print("No teaching")
else:
    hours = total // 60
    minutes = total % 60
    if hours > 0 and minutes > 0:
        print(f"{hours} hours {minutes} minute")
    elif hours > 0:
        print(f"{hours} hours")
    else:
        print(f"{minutes} minute")
