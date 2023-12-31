#!/usr/bin/env python
# coding: utf-8

# In[2]:


#51
tuple1=1,
print(tuple1)


# In[3]:


#52
tuple1=1,2,3,4
list1=list(tuple1)
list1.remove(3)
tuple1=tuple(list1)
print(tuple1)


# In[4]:


#53
tuple1=1,2,3,4
tuple2=5,6,7,8
tuple3=tuple1+tuple2
print(tuple3)


# In[7]:


#54
tuple1=tuple(x**2 for x in range(5)) #constructor with the argument as a generator
tuple2=(tuple1) #constructor with the argument as another tuple
print(tuple1)
print(tuple2)


# In[8]:


#55
tuple1=1,2,6,7,8,6,9,6
print(tuple1.count(6))


# In[ ]:




