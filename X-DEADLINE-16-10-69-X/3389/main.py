"""SMART TRASH COLLECTOR"""
time = int(input())
for _ in range(time):
    plastic, can, glass = map(float, input().split())
    total = plastic + can + glass

    if total > 50:
        ans = f"{total:.1f}, Overloaded"
        if plastic > 20:
            ans += ", Check Type Plastic"
        if can > 20:
            ans += ", Check Type Can"
        if glass > 20:
            ans += ", Check Type Glass"
        print(ans)

    else:
        ans = f"{total:.1f}"
        if plastic > 20:
            ans += ", Check Type Plastic"
        if can > 20:
            ans += ", Check Type Can"
        if glass > 20:
            ans += ", Check Type Glass"
        print(ans)
