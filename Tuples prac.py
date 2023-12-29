#!/usr/bin/env python
# coding: utf-8

# In[28]:


#42
a=1,2,3,4
print("The tuple is:",a)


# In[29]:


#43
a=1,2,3,4,5,6,7,8,9,10,11
try:
    print("The 11th item is: ",a[10])
except IndexError:
    print("Index out of range")


# In[30]:


#44
a=1,2,3,4,5
print("The 2nd element from last is:",a[-2])
print("The negative indexing can also be used in via slicing:",a[-2:1:-1]) #negative indexing in slicing


# In[31]:


#45
a=1,2,3,4,5
print(*(i for i in range(len(a))))
print(*(i for i,_ in enumerate(a))) #another method, with enumerate function


# In[ ]:




