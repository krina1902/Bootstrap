l=[1,2,1.1,"abc",True,0,False,7,8]
# l.append(5)
# print(len(l))
# print(l.count(1))
l.pop()
l1=l.copy()
# print(l1)
l.extend(l1)
l.reverse()
l.remove(1.1)
print(l.index(False))
l.insert(2,234)
l.pop(3) #index
l.pop()
print(l)

for i in l:
    print(i)
    
print(2 in l)
