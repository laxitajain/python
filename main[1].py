squares=[x**2 for x in range(10) ]
print(squares)
s=[(x,y) for x in [1,2,3] for y in [3,2,3] if x!=y]
print(s)
#equivalent to:
s=[]
for x in [1,2,3]:
    for y in [3,2,3]:
        if x!=y:
            s.append((x,y))
print(s)
vec = [[1,2,3], [4,5,6], [7,8,9]]
q=[elem for elem in vec]
print(q)
q=[num for elem in vec for num in elem]
print(q)
#equiv to:
s=[]
for elem in vec:
    for num in elem:
        s.append(num)
print(s)
from math import pi 
t=[(round(pi,i)) for i in range(1,6)]
print(t)
