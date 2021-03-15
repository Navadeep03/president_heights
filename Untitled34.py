#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data= pd.read_csv(r'N:\Tony Stark Data\Innovites\Book3.csv')


# In[3]:


data.head(10)


# In[4]:


import numpy as  np


# In[5]:


height = np.array(data["height(cm)"])


# In[6]:


print(height)


# In[7]:


print("Mean of heights =", height.mean())
print("Standard Deviation of height =", height.std())
print("Minimum height =", height.min())
print("Maximum height =", height.max())


# In[8]:


print("25th percentile =", np.percentile(height, 25))
print("Median =", np.median(height))
print("75th percentile =", np.percentile(height, 75))


# In[9]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


# In[10]:


plt.hist(height)
plt.title("Height Distribution of Presidents of USA")
plt.xlabel("height(cm)")
plt.ylabel("Number")
plt.show()


# In[ ]:




