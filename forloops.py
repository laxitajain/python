#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1
fruits=["apple","banana","mango","orange","guava"]
for i in fruits:
    print(i,end=" ")
    


# In[2]:


#2
cars=["Mercedes","BMW","Jaguar","Audi","Bughati"]
for i in cars:
    if i=="Audi":
        break
    print(i,end=" ")
    


# In[3]:


#3
fruits=["apple","banana","mango","orange","guava"]
for i in fruits:
    if i=="banana":
        continue
    print(i,end=" ")


# In[10]:


#4
fruits={"apple":"red","orange":"orange","banana":"yellow"}
for i,j in fruits.items():
    print(i,":",j,end=" ")


# In[11]:


#5
a=34
b=10
if a<b:
    pass
else:
    print(a)


# In[ ]:




