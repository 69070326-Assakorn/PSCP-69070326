"""barb wire fence"""
wide,long,layer = map(int, input().split())
price = int(input())
total = 2 * (wide + long) * layer
cost = total * price
print(total)
print(cost)
