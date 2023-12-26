thislist=['orange','papaya','banana','guava','litchi']
#another list just to check for the other possibility (grape already present)
list2=['orange','grape','banana']
if 'grape' not in thislist:
    thislist.insert(len(thislist),'grape')
else: 
    print("Grape already present in the list.")
print(thislist)
if 'grape' not in list2:
    thislist.insert(len(list2),'grape')
else: 
    print("Grape already present in the list.")
print(list2)