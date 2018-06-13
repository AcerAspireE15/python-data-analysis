
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


# In[18]:


new_frame = DataFrame(data, columns = ['Name','Age','Salary','Profile'])


# In[19]:


new_frame


# In[20]:


new_frame['Salary']


# In[24]:


new_frame.ix[2]

