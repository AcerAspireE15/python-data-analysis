
# coding: utf-8

# In[39]:


import numpy as np
from matplotlib import pyplot as plt

x = np.arange(1,11)
y = 4*x + 10
plt.title('This is the title')
plt.xlabel("This is x label")
plt.ylabel("This is y label")
plt.plot(x,y)
plt.show()

