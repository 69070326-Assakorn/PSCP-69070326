"""FOURDIRECTIONS"""
arrows = {
    'U': [
        "  *   ",
        " ***  ",
        "* * * ",
        "  *   ",
        "  *   "
    ],
    'D': [
        "  *   ",
        "  *   ",
        "* * * ",
        " ***  ",
        "  *   "
    ],
    'L': [
        "  *   ",
        " *    ",
        "***** ",
        " *    ",
        "  *   " 
    ],
    'R': [
        "  *   ",
        "   *  ",
        "***** ",
        "   *  ",
        "  *   "
    ]
}

s = input()
s = [arrows[c] for c in s]
for i in range(5):
    print("".join(row[i] for row in s))
