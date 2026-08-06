"""safe"""
Alphabet = input()
Num = input()
if Alphabet == "H" and Num == "4567" :
    print("safe unlocked")
elif Alphabet == "H" and Num != "4567" :
    print("safe locked - change digit")
elif Alphabet != "H" and Num == "4567" :
    print("safe locked - change char")
else :
    print("safe locked")
