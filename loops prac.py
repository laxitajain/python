#!/usr/bin/env python
# coding: utf-8

# In[4]:


#1
def prime():
    for i in range(10,21):
        k=1
        for j in range(2,(i//2)+1):
            if i%j==0:
                k=0
        if k==1:
            print(i)
print(f"The prime numbers between 10 and 20 are:")
prime()


# In[7]:


#2
def perf(n):
    s=0
    for i in range(1,(n//2)+1):
        if n%i==0:
            s+=i
    if s==n:
        print(f"{n} is a perfect number!")
    else:
        print(f"{n} is not a perfect number.")
perf(6)


# In[9]:


#3
def prime(n,p):
    print(f"The prime numbers between {n} and {p} are: ")
    for i in range(n,p+1):
        k=1
        if i==1:
            continue
        if i==2 or i==3:
            print(i,end=" ")
            continue
        for j in range(2,(i//2)+1):
            if i%j==0:
                k=0
        if k==1:
            print(i,end=" ")
prime(1,50)


# In[15]:


#4
def pattern1(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print("\n")
n=int(input("Enter the number of rows:"))
pattern1(n)


# In[16]:


#5
def pattern1(n):
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print("*",end=" ")
        print("\n")
n=int(input("Enter the number of rows:"))
pattern1(n)


# In[ ]:




