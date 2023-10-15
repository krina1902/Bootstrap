#  0  1  2     3     4  5  6   7    8     9       10    11
l=[1,2,"abc","def",True,0,1.1,3.4,False,"java","auto","php"]
#  2 1   0      9   8   7  6    5   4    3       2     1
a=l.copy()
print(l[-12:-1:1])#[1,.....,"auto"]
print(l[:-12:5])#[]


'''
print(l[-15::90])#[1]
print(l[-12::90])#[1]
print(l[:-13])#[]
print(l[-12:-2:2])#[1, 'abc', True, 1.1, False]
print(l[-12:-2:-2])#[]
print(l[::-6])#["php",0]
print(l[::-1])
a.reverse() 
print(a)
print("#"*60)
print(l[:2])#[1,2]
print(l[1:4:5])#[2]
print(l[3::3])#["def",1.1,"java"]
print(l[:14:10])#[1,"auto"]
print(l[::14])#[1]
print(l[1:14:1])#[2,.......,"php"]
print(len(l))
'''