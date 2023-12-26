a={1,2,3,4,5} #sets can be declared either with {} or with set()
print(a)
x=set('asdhjhk') #creates a set with all the letters as indiv. elements
print(x)
b=set(a) #also creates a set 
print(b)
y=set() #creates an empty set, empty {} can't be used to create an empty set. they create an empty dictionary.
print(y)
print(type(y))
p={2,3,4,5}
q={4,5,6,7}
r=p-q 
print(p-q) #elems in p but not in q
print(r)
print(p|q) #similar to pUq (union of two sets) , returns elems in p or q or both
print(p&q) #similar to p intersection q, returns elems in both p and pUq
print(p^q) #similar to symm. diff. of p and q, returns elems in p or in q, but not in both. 
#all the above operations can be similarly applied to str type sets.

#set comprehension
a={x for x in 'ajkkjk' if x!='a'and x!='b'}
print(a)
c={x for x in a}
print(c)
d={x for x in 'safaf' if x not in 'af'}
print(d)
#eliminates duplicate members
a={1,1,2}
print(a)
