
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

