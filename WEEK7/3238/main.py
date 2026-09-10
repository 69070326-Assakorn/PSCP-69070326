"""ELON MUSK"""
X, K = map(str, input().split())
NUM = int(X)
CHAR = ord(K)

if K == "#":
    for i in range(NUM):
        ANS = ""
        for b in range(NUM):
            if i == b or b+i == (NUM - 1):
                ANS += K
            else:
                ANS += "-"
        print(ANS)

else:
    if not NUM % 2:
        NUM1 = NUM // 2
        for i in range(NUM):
            ANS = ""
            for b in range(NUM):
                if i == b or b+i == (NUM - 1):
                    if i <= ((NUM + 1)/2)-1 and CHAR+(NUM1-i) <= 126:
                        ANS += chr((CHAR+NUM1) - i)
                    elif i > ((NUM + 1)/2)-1 and (CHAR+i)-(NUM1 + 1) <= 126:
                        ANS += chr((CHAR-NUM1) + i)
                    else:
                        ANS += "-"
                else:
                    ANS += "-"
            print(ANS)
    else:
        NUM1 = (NUM-1) // 2
        for i in range(NUM):
            ANS = ""
            for b in range(NUM):
                if i == b or b+i == (NUM - 1):
                    if i <= ((NUM + 1)/2)-1 and CHAR+(NUM1-i) <= 126:
                        ANS += chr(CHAR+(NUM1-i))
                    elif i > ((NUM + 1)/2)-1 and (CHAR+i)-NUM1 <= 126:
                        ANS += chr((CHAR+i)-NUM1)
                    else:
                        ANS += "-"
                else:
                    ANS += "-"
            print(ANS)
