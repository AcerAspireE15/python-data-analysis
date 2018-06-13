
# coding: utf-8

# In[11]:


data = {'Name':['John', 'Tim', 'Rob'], 
        'Age':[34, 23, 42],
        'Salary':[4500, 2300, 5800]
       }


# In[12]:


from pandas import DataFrame

frame = DataFrame(data)


# In[13]:


frame


# In[14]:


frame


# In[16]:


new_frame = DataFrame(data, columns = ['Age','Name','Salary'])


# In[17]:


new_frame


# In[33]:


new_frame = DataFrame(data, columns = ['Name','Age','Salary'])


# In[34]:


new_frame


# In[35]:


new_frame['Salary']


# In[36]:


new_frame.ix[2]


# In[37]:


new_frame['Profile']='Doctor'


# In[38]:


new_frame


# In[39]:


new_frame['Education']='MS'


# In[40]:


new_frame


# In[41]:


# transpose

new_frame = new_frame.T


# In[42]:


new_frame


# In[43]:


new_frame = new_frame.T


# In[44]:


new_frame


# In[47]:


from pandas import Series

obj = Series([100,200,300,400,500], index=['d','a','b','e','c'])


# In[48]:


obj


# In[51]:


obj


# In[62]:


obj = obj.reindex(['a','b','c','d','e'])
obj
                   


# In[60]:


from pandas import Series

obj = Series([100,200,300,400,500], index=['d','a','b','e','c'])

obj


# In[61]:


obj = obj.reindex(['a','b','c','d','e'])
obj


# In[63]:


data = {'Name':['John', 'Tim', 'Rob'], 
        'Age':[34, 23, 42],
        'Salary':[4500, 2300, 5800]
       }
frame = DataFrame(data)
frame


# In[64]:


frame = frame.reindex([0,2,1])
frame


# In[65]:


frame = frame.reindex([1,2,0])
frame


# In[67]:


fileds = ['Age','Name','Salary']
frame = frame.reindex(columns=fileds)
frame

