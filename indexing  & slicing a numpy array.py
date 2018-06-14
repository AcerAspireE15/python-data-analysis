
# coding: utf-8

# In[2]:


import numpy as np

a = np.arange(10)

print(a)


# In[4]:


s = slice(2,7,2)
print(a[s])


# In[5]:


print(a)


# In[6]:


b = a[2:7:2]
print(b)


# In[7]:


print(a[2:])


# In[8]:


print(a[2:5])


# In[9]:


a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)


# In[10]:


print(a[1:])


# In[13]:


print(a[1:2])


# In[14]:


print(a[2:])


# In[15]:


print(a)


# In[17]:


b = a[[0,1,2],[0,1,0]]
print(b)


# In[19]:


x = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
print(x)


# In[25]:


row = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])
y = x[row,cols]
print(y)


# In[26]:


print(x)

print(x[x>5])
# In[27]:


print(x[x>5])

