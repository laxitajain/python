n=int(input("Enter the number: "))
k=1
if n==1 or n==0:
    print("Neither Prime nor Composite")
if n==2 or n==3:
    print("Prime!")
for i in range(2,(n//2)+1):
    if n%i==0:
        k=0
        break
if k==1:
    print("Prime!")
else:
    print("Not Prime!")
 
