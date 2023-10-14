s=input("Enter String: ")

lower=0
upper=0
space=0
char=0
num=0
for i in s:
    if i.isalpha():
        char+=1
    if i.islower():
        lower+=1
    elif i.isspace():
        space+=1
    if i.isupper():
        upper+=1
    elif i.isnumeric():
        num+=1
print("Total char: ",char)
print("Total lower: ",lower)
print("Total space: ",space)
print("Total upper: ",upper)
print("Total num: ",num)
