s = "Python is the best Programming. Python is high-level programming language."
s1 = s.split()
print(s1)
count=0
i=0
while i<len(s1):
    count=0
    for j in s1:
        if s1[i]==j:
            count = count + 1
    print(s1[i],":",count)
    i=i+1