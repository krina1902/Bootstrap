l=[1,2,3,4,5,6,7,8,9]
l1=[6,7,8,0]
count=0
for i in l:
    if i in l1:
        count=count+1
if count==len(l1):
    print("true")
else:
    print("false")