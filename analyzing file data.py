
# coding: utf-8

# In[2]:


import pandas 
data_frame = pandas.read_csv("Book.csv")
data_frame


# In[3]:


data_frame = data_frame.drop([1])
data_frame


# In[5]:


data_frame = data_frame.drop('product_name',axis=1)
data_frame


# In[8]:


data_frame.sort_values(by='produc_price')


# In[10]:


data_frame.sum(numeric_only=True)

