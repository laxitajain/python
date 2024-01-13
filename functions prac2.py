#1
def circleinfo(r):
    print(f"The area of the circle is {3.14*r*r}.")
    print(f"The perimeter of the circle is {3.14*2*r}.")
circleinfo(7.0)
#2
def absl(n):
    if n<0:
        n=-n
    return n
n=int(input("Enter the number: "))
print(f"The absolute value of n is {absl(n)}")
#3
def even(n):
    if n%2==0:
        return True
    return False
n=int(input("Enter a number: "))
if even(n):
    print("It's even!")
else:
    print("It's odd!")
#4
def check(n,p):
    if n.upper()==p.upper():
        return True
    return False
n=input("Enter string 1: ")
p=input("Enter string 2: ")
if check(n,p):
    print("Equal!")
else:
    print("Not equal!")
#5
def convert(c):
    return ((9*c)/5)+32
c=int(input ("Enter temp in C: "))
print(f"Temp in F is: {convert(c)}")




