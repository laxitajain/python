a=[2,1,21]
a.insert(0,2) #inserts an element 2 before the 0th index element.
print(a)
a.insert(len(a),2) #inserts 2 before len(a), i.e. at the end. equivalent to a.append(2)
print(a)
a.remove(2) #removes the first element from the list whose value is equal to 2
print(a)
a.pop(2)
print(a)
print(a.pop())
print(a)
a.clear()
print(a)
a=[2,4,5,6,4,6,7,4,8]
print(a.index(4))
print(a.index(4,2))
print(a.index(4,5,8))
print(a.count(4))
print(a)
c=a.copy() # returns a shallow copy of a.  equivalent to a[:]
print(c)
print(a.sort()) #methods like insert, remove or sort that only modify the list have no return value printed – they return the default None. 1 This is a design principle for all mutable data structures in Python.
print(a) #
