def test(a,n):
    t=0
    for i in range(len(a)):
        if n==a[i]:
            t=1
            break
    if t==1:
        print("Item exists")
    else:
        print("Item doesn't exist")
o=int(input("Enter the number of items: "))
print("Enter the items: ")
t=[]
for j in range(o):
    e=int(input())
    t.append(e)
k=int(input("Enter the item you wish to search: "))
test(t,k)