#60
tuple1=(2,"happy","classroom",3.5)
print(tuple1)
#61
tuple2=(2,32,21,89)
print("The largest element of the tuple is:",max(tuple2))
#62
tuple3=2,3,3,4,5
print("The sum of the elements in the tuple is:",sum(tuple3))
#63
nums=input("Enter the comma-seperated numbers: ")
list1=nums.split(",")
tuple1=tuple(list1)
print(f"The list is: {list1}, and the tuple is: {tuple1}")