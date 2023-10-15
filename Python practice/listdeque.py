# deque = first in first out
# stack = first in last out
#################deque#####################################
from _collections import deque
l=deque([])
l.append(10)
print(list(l))
l.append(20)
print(list(l))
l.append(30)
print(list(l))

l.popleft()
print(list(l))
l.popleft()
print(list(l))
l.popleft()
print(list(l))

#######################stack##########################
a=[]
a.append(10)
print(a)
a.append(20)
print(a)
a.append(30)
print(a)
a.pop()
print(a)
a.pop()
print(a)
a.pop()
print(a)
