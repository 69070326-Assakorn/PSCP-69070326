"""Cyan's Password"""
name = input()
sur = input()
age = input()
if len(name)>=5 and len(sur) >= 5 :
    password = name[:2]+sur[-1]+age[-1]
    print(password)
else :
    password = name[:1]+age+sur[-1]
    print(password)
