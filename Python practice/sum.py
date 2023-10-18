a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))
sum=0
if a==b or b==c or c==a:
    sum=0
else:
    sum=a+b+c
print("SUM: ",sum)
