"""GUESS ROLL THE DICE"""
guess = int(input())
dice = int(input())
if guess not in range(1, 7) or dice not in range(1, 7):
    print("Invalid")
else:
    if guess == dice:
        print("Correct!")
    else:
        print("Wrong!")
