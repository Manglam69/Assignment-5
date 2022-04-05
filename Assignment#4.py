#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_csv('youtube_dataset.csv',encoding='cp1252')
df.head()


# In[3]:


type(df)


# In[4]:


df.shape


# In[5]:


#Subset_function
def subset_data(data,first_row,last_row):
    
    subset=data.iloc[first_row:last_row]
    
    return subset.to_csv('Top_{}.csv'.format(last_row),encoding='cp1252')


# In[6]:


#Exporting csv file for top 1000 rows
subset_data(df,0,1000)


# In[42]:


#Function to find out distribution of channeltype
def plot_channel_dist(first_row,last_row):
    sns.set_style("whitegrid")
    fig=sns.displot(df['channeltype'].iloc[first_row:last_row],height=5,aspect=3)
    
    return fig


# In[47]:


#Calling the function for top 1000 rows
plot_channel_dist(0,1000)


# In[41]:


sns.set_style("whitegrid")
sns.displot(df['channeltype'].iloc[0:1000],height=5,aspect=3)


# In[12]:


type(df3)


# In[13]:


df3


# In[ ]:




