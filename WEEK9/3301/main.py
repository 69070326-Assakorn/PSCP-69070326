"""BOX"""
W, L, M, N = map(int, input().split())
answer = W * L

for A in range(M, N + 1):
    remain_W = W % A
    remain_L = L % A
    waste = remain_W * remain_L
    if waste < answer:
        answer = waste
print(answer)
