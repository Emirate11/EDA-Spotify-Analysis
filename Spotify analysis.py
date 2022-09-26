#!/usr/bin/env python
# coding: utf-8

# ## EDA Analysis on Nigerian spotify dataset

# Spotify is a Swedish audio streaming and media services provider founded in April 2006. It is the world's largest music streaming service provider and has over 381 million monthly active users, which also includes 172 million paid subscribers.
# 
# Here, We'll be exploring and quantify data about music and drawing valuable insights.
# 
# Perform an exploratory data analysis (EDA) and data visualization project using data from Spotify using Python.

# ### Import neccessary libraries

# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ### Load Dataset

# In[6]:


ssong = pd.read_csv("nigerian_spotify_songs1.csv")
ssong.head()


# ### Checking for null values
# ##### We can see that there are no null values in the dataset

# In[7]:


ssong.info()


# In[8]:


ssong.describe()


# In[9]:


ssong.boxplot()


# In[10]:


ssong.isnull().sum()


# ### Visualizing Top five artist by popuparity

# we can see that Burna Boy is clearly the most popular artist

# In[20]:


ssong.groupby(["artist"])["popularity"].max().sort_values(ascending = False).head(5).plot(kind = "bar", ylabel = "popularity", title = "Artist by popuparity")


# with DJ Tunez being the most popular artist on average

# In[21]:


ssong.groupby(["artist"])["popularity"].mean().sort_values(ascending = False).head(5).plot(kind = "bar",ylabel = "popularity", title = "Artist by popuparity (Average)")


# With African Giant being the most popular album by the artist Burna Boy

# In[22]:


ssong.groupby(["album"])["popularity"].max().sort_values(ascending = False).head(5).plot(kind = "bar",ylabel = "popularity", title = "Album by popuparity")


# Most popular album by average is clearly Kontrol

# In[14]:


ssong.groupby(["album"])["popularity"].mean().sort_values(ascending = False).head(5).plot(kind = "bar")


# In[15]:


ssong["release_date"]


# In[16]:


ssong.groupby(["album"])["artist"].value_counts().head(20)


# In[ ]:





# In[17]:


ssong.groupby(["artist"])["album"].value_counts().sort_values(ascending = False).head(20)


# In[18]:


ssong.groupby(["artist"])["album"].value_counts()


# The most popular song name is clearly "On the Low" by artist Burna Boy

# In[19]:


ssong.groupby(["name"])["popularity"].max().sort_values(ascending = False).head(5).plot(kind = "bar")


# In[ ]:




