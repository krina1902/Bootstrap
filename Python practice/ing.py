s=input("enter s: ")

if len(s)<3:
    print(s)
elif s[-3:]=="ing":
    print(s+"ly")
else:
    print(s+"ing")