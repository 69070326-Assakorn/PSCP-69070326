"""CUPS"""
from bisect import bisect_left
import sys
data = list(map(int, sys.stdin.read().split()))
n = data[0]
cups = data[1:n + 1]
stacks = []
for cup in cups:
    i = bisect_left(stacks, cup)
    if i == len(stacks):
        stacks.append(cup)
    else:
        stacks[i] = cup
print(len(stacks))
