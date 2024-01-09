#1
for i in range(6):
    print(i)
#2
x=int(input("Enter the base: "))
y=int(input("Enter the exponent: "))
p=1
for i in range(0,y):
    p=p*x
print(p)
a=int(input("Enter the base: "))
b=int(input("Enter the exponent: "))
p=1
i=0
while(i<b):
    p=p*a
    i+=1
print(p)
#3
list1=[1,2,3,4,5]
for i in list1:
    print(i**3,end=" ")

