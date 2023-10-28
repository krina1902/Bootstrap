#factorial

# n=int(input("enter n:"))
# fact=1
# for i in range (1,n+1):
#     fact=fact*i
# print(fact)

################################################
s="krina antala"
n={}
for i in s:
   if i in n:
       n[i]+=1
   else:
       n[i]=1
print(n)