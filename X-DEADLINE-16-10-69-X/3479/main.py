"""NAME OF CARD"""
card = input().strip().upper()
rank = card[:-1]
suit = card[-1]

if rank == "A":
    RANK = "Ace"
elif rank == "J":
    RANK = "Jack"
elif rank == "Q":
    RANK = "Queen"
elif rank == "K":
    RANK = "King"
else:
    RANK = rank

if suit == "D":
    SUIT = "Diamonds"
elif suit == "H":
    SUIT = "Hearts"
elif suit == "S":
    SUIT = "Spades"
else:
    SUIT = "Clubs"

print(RANK + " of " + SUIT)
