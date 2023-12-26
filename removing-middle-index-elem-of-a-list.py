n=int(input("Enter the number of items: "))
print("Enter the items: ")
list1=[]
for i in range(n):
    item=int(input())
    list1.append(item)
if n%2==0:
    list1[n//2-1:n//2+1]=[]
else:
    list1[n//2:n//2+1]=[]
print(list1)
