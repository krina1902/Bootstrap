s=input("enter s: ")

if len(s)<2:
    print(s)
else:
    print(s[:2]+s[-2:])