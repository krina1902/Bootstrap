l=1,2,3,4,5,6,7,8,9,0
print(tuple(l))

t=(1,1.1,2,3,"tops","python")
print("tops" in t)
print(1.2 in t)
print(len(t))
print(t[::-1])


l = [(5, 2, 3), (4, 7, 6), (8, 9, 6)]
print([t[:-1] + (10,) for t in l]) 

a=[(),(1,2),("tops"),(3,4,5,6),(),("")]
for i in a:
    if len(i)==0:
        a.remove(i)
print(a)


l=[("k",1),("r",2),("i",3),("n",4),("a",5)]

print(*l)
print(list(zip(*l)))
