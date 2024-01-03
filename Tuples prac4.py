#64
set1={1,2,3,4}
print(set1)
#65
set1={1,2,3,4}
for i in set1:
    if i==3:
        print(i)
#66
set1={1,2,3,4,5}
i=5
if i in set1:
    print(f"{i} exists in the set!")
else:
    print(f"{i} does not exist in the set!")
#67
set1={1,2,3,4,5}
set1.remove(3)
set1.add(6)
print(set1)