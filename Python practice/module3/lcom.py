def com(l1,l2):
    for i in l1:
        for j in l2:
            if i==j:
                return True
            
            
l1=[1,2,3,4,5]
l2=[7,8,9,0,1,2]

print(com(l1,l2))