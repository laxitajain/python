t=[]
choice='Y'
while choice.upper()=='Y':
    e=int(input("Enter the element: "))
    t.append(e)
    choice=input("Do you wish to enter another element?(Y/N): ")
    if choice.upper()!='Y' and choice.upper()!='N':
        print("Invalid input.")
        break
print("The entered list is,",t)
# another way (optimized):
t=[]
print("Enter items: ")
while True:
    item=input()
    if item.upper()=="STOP":
        break
    t.append(item)
print("The entered list is:",t)
    
