"""SurprisingVote"""
total = float(input())
maximum = float(input())
others = total - maximum
minimum = max(0, others - maximum)
if maximum - minimum > 2:
    print("Surprising")
else:
    print("Not surprising")
