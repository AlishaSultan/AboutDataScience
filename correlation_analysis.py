#!/usr/bin/env python
# coding: utf-8

# In[1]:


###################################Find correlation #########################################################
###################################correlation analysis######################################################

import pandas as pd


# In[2]:


df = pd.read_csv("D:/ESS/lec/diabetes.csv")


# In[3]:


df


# In[5]:


df[['Pregnancies' , 'BloodPressure']].groupby(['BloodPressure']).describe().unstack()


# In[6]:


df[['Pregnancies' , 'BloodPressure']].corr()


# In[ ]:




