d={'salt':2,'tea':3,'banana':5, 'zoo':5} #dictionaries consist of key-value pairs. 
print(d)
d['heme']=6 #addition of a new elem
print(d)
print(d['tea'])
del d['salt']
print(d)
print(list(d)) #prints a list of all the keys in d
print(sorted(d)) #alphabetically sorted keys.
print('salt' in d)
print('banana' in d)
#another way to initialise a dictionary: (using the dict() keyword)
y=dict(mango=2,litchi=5)
print(y)
#dictionary comprehension
a={y:x**2 for x in (1,2,3) for y in ('you', 'me', 'i')} #here all the keys only have the value 3, because for duplicate keys, it considers the value which is last assigned to them
print(a)
z={1:2,1:3} #demonstration of duplicate keys
print(z)
print(z[1]) 