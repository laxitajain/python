a=[2,1,21]
e=[]
n=int(input("Enter the number of items you wish to enter: "))
for i in range(n):
    t=int(input())
    e.append(t) 
print(e) 
a[len(a):]=e #e is an iterable here (list/set/tuple,etc.) this syntax is equivalent to the a.extend(iterable) feature.
print(a)
