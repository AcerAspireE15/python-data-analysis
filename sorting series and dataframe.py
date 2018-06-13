
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


# In[18]:


Ser = Series([3,7,1,4,7,2],index=[2,7,3,5,9,1])
Ser


# In[20]:


Ser.sort_index()


# In[21]:


data2 = {'Speed':[101, 113, 115],
         'Temp':[34, 23, 42],
         'Humidity':[45, 23, 58]
        }
frame2 = DataFrame(data2)

frame2


# In[22]:


frame2 = frame2.reindex([2,1,0])


# In[23]:


frame2


# In[25]:


frame2.sort_index()


# In[27]:


frame2 = frame2.reindex(columns=['Speed','Humidity','Temp'])
frame2


# In[31]:


frame2.sort_index(axis=1,ascending=False)


# In[32]:


frame2.sort_index(axis=1)

