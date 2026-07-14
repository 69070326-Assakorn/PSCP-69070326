"""Primary Color"""
color1 = input().lower()
color2 = input().lower()
if (color1 == "red" and color2 == "yellow") or (color1 == "yellow" and color2 == "red") :
    print("Orange")
elif (color1 == "blue" and color2 == "yellow") or (color1 == "yellow" and color2 == "blue") :
    print("Green")
elif (color1 == "blue" and color2 == "red") or (color1 == "red" and color2 == "blue") :
    print("Violet")
elif (color1 == "red" and color2 == "red"):
    print("Red")
elif (color1 == "yellow" and color2 == "yellow"):
    print("Yellow")
elif (color1 == "blue" and color2 == "blue"):
    print("Blue")
else :
    print("Error")
