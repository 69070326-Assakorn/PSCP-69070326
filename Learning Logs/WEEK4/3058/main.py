"""BrickBridge"""
a = int(input())
b = int(input())
bridge = int(input())

if b*5 >=bridge:
    use = bridge % 5
else:
    use = bridge - b*5

if use<=a:
    print(use)
else:
    print("-1")
