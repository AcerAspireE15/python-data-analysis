
# coding: utf-8

# In[1]:


from pandas import Series
Series1 = Series([1, 2, 3, 4, 5])
Series2 = Series([100, 200, 300, 400, 500])
Series1 + Series2


# In[2]:


from pandas import Series
Series1 = Series([1, 2, 3, 4, 5])
Series2 = Series([100, 200, 300, 400, 500, 600, 700])
Series1 + Series2


# In[3]:


from pandas import Series
Series1 = Series([1, 2, 3, 4, 5])
Series2 = Series([100, 200, 300, 400, 500])
Series1 - Series2


# In[4]:


from pandas import Series
Series1 = Series([1, 2, 3, 4, 5])
Series2 = Series([100, 200, 300, 400, 500])
Series1 * Series2


# In[5]:


from pandas import Series
Series1 = Series([1, 2, 3, 4, 5])
Series2 = Series([100, 200, 300, 400, 500])
Series1 / Series2


# In[7]:


from pandas import DataFrame
data1 = {'Speed':[100, 103, 105],
         'Temp':[34, 23, 42]}
frame1 = DataFrame(data1)
frame1


# In[10]:


from pandas import DataFrame
data1 = {'Speed':[101, 113, 115],
         'Temp':[34, 23, 42],
         'Humidity':[45, 23, 58]
        }
frame2 = DataFrame(data1)
frame2


# In[11]:


frame1 + frame2


# In[12]:


Series2 = Series([100, 200 ,300], index=['Speed', 'Temp', 'Humidity'])
Series2 + frame2


# In[13]:


frame2 - Series2


# In[14]:


frame2 * Series2


# In[16]:


Series3 = Series([100, 200], index=['Speed', 'Temp'])
Series3 + frame2


# In[17]:


Series3 - frame2

