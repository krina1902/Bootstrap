def max(l):
    max=l[0]
    for i in l:
        if i > max:
            max=i
    return max

def min(l):
    min=l[0]
    for i in l:
        if i < min:
            min = i
    return min

def sum(l):
    sum=0
    for i in l:
        sum=sum+i
    return sum

l=[1,2,3,4,5,6,7,8,0,101]
print(max(l))
print(min(l))
print(sum(l))