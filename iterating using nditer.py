
# coding: utf-8

# In[28]:


import numpy as np

a = np.array([1,2,3,4])
b = np.array([10,20,30,40])
c = a * b
print(c)


# In[29]:


c = a + b
print(c)


# In[30]:


a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([1,2,3])
print(a)
print(b)


# In[31]:


print(a+b)


# In[32]:


a = np.arange(0,60,5)
a = a.reshape(3,4)
print(a)


# In[33]:


for x in np.nditer(a):
    print(x)


# In[34]:


for x in np.nditer(a):
    print(x + 5)

