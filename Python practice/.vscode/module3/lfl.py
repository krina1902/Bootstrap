
l=["abcd","acfca","12321","ab","going","L","KK"]
count=0
for i in l:
    if len(i)>1 and i[0]==i[-1]:
        count = count + 1
print(count)