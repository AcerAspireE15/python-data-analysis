
# coding: utf-8

# In[1]:


import numpy as np
x = np.linspace(10,20,5)
print(x)


# In[2]:


import numpy as np
x = np.linspace(10,20,5, endpoint=False)
print(x)


# In[3]:


a = np.logspace(1.0,2.0,num=10)
print(a)


# In[4]:


a = np.logspace(1.0,2.0,num=10,base=2)
print(a)

