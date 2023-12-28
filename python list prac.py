#!/usr/bin/env python
# coding: utf-8

# In[2]:


#37
list=[1,2,-2,-9]
plist=[i for i in list if i>0]
print("The list of positive numbers is: ",plist)


# In[4]:


#38
list=[2,3,4,56,6]
count=0
for i in list: 
    if i%2==0: count+=1
print("The number of even numbers in the list is: ",count)


# In[6]:


#39
list=[2,3,4,5]
product=1
for i in list:
    product*=i
print("The product of all the numbers in the list is: ",product)


# In[8]:


#40
list=[2,90,3,120,6]
a=list[0]
for i in list:
    if i>a:
        a=i
print("The largest number in the list is: ",a)


# In[12]:


#41
list=[2,7,8,79,43,89]
a=list[0]
for i in list:
    if i>a:
        a=i
for j in list: 
    for i in list:
        if i<a and i>j:
            b=i
print("The second largest number in the list is: ",b)


# In[14]:


list=[2,7,8,79,43,89]
list.sort()
print(list[-2])


# In[3]:


a=[1,1,2,2,3]
for i in a:
    if a.count(i)==1:
        z=i
print(z)
        


# In[ ]:




