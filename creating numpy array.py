
# coding: utf-8

# In[1]:


import numpy as np

a = np.array([1,2,3,4,5])

a


# In[2]:


print(a)


# In[3]:


a = np.array([1,2,3,4])
print(a)


# In[4]:


a.reshape(2,2)


# In[5]:


import numpy as np

a = np.arange(24)

print(a)


# In[6]:


b = a.reshape(2,4,3)
print(b)


# In[7]:



x = np.zeros(5)
print(x)


# In[8]:


x = np.zeros(5,dtype=np.int)
print(x)

