#!/usr/bin/env python
# coding: utf-8

# In[12]:


#56
tuple1=1,2,3,4
tuple1=tuple(tuple1[i] for i in range(len(tuple1)-1,-1,-1)) #method1, using constructor
print(f"The reversed tuple is: {tuple1}")


# In[13]:


#56
tuple1=1,2,3,4
tuple1=tuple1[::-1] #method2, using slicing
print(f"The reversed tuple is: {tuple1}")


# In[14]:


#57
tuple1=(1,2,3)*4
print(f"The tuple created with repetition is: {tuple1}")


# In[7]:


#58
tuple1=(1,2,3,4) #packing
a,b,c,d=tuple1 #unpacking
print(a)
print(b)
print(c)
print(d)


# In[11]:


#59
tuple1=6,7,8,3,5
print("The smallest element is:",min(tuple1))


# In[ ]:




