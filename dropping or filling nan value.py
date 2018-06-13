
# coding: utf-8

# In[4]:


from pandas import Series
import numpy as np
ser = Series([1,2,3,4,np.nan],index=['a','b','c','d','e'])
ser


# In[6]:


ser = ser.dropna()


# In[7]:


ser


# In[10]:


from pandas import DataFrame
import numpy as np
data2 = {'Speed':[101, np.nan, 115],
         'Temp':[34, 23, 42],
         'Humidity':[4500, np.nan, 5800]
        }
frame2 = DataFrame(data2)

frame2


# In[11]:


frame2.dropna()


# In[12]:


frame2.fillna(20)

