"""CARD"""
x = input().upper()
rank = x[:-1]
suit = x[-1]

if rank == 'A':
    rank = 'ace'
elif rank == 'J':
    rank = 'jack'
elif rank == 'Q':
    rank = 'queen'
elif rank == 'K':
    rank = 'king'

if suit == 'D':
    suit = 'diamonds'
elif suit == 'H':
    suit = 'hearts'
elif suit == 'S':
    suit = 'spades'
else:
    suit = 'clubs'

print(rank, 'of', suit)
