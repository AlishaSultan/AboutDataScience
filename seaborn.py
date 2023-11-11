#!/usr/bin/env python
# coding: utf-8

# In[1]:


# loading data .csv file


# In[2]:


#df.to_csv()  why? you should make a local copy as u can run ths risk of losing the data when u shut down your python compiler.
#load the data into csv file


# In[3]:


# .xlsx is the extension of excel file 


# In[4]:


#df = pandas.read_excel(".xlsx")


# In[5]:


#load the data into excel file
#df.to_excel()


# In[6]:


#Data exploration techniques:
#Dimensionality check-----------------df.shape
#type of dataset----------------------type(df)-----see column type------df['chas'].dtype
#slicing and indexing---------------- df.iloc [a:b , x:y] x represent start index of column and y represent end index of column and a represent first index of row and b represent last index of row
#Identifying unique elements--------- df['column name'].unique()
#value extraction ------------------df['column name'].values()
#Feature mean-------------------- df.mean()
#Feature median ----------------df.median()
#Feature mode ---------------- df.mode(axis = 0) #axis = 0 represent the columns   axis = 1 (calculate mode over the rows)


# In[7]:


#Heatmap:
#A heat map is a type of graph that uses color the way a bar graph uses the height and width for data visualisation


# In[9]:


#plotting heatmap using seaborn

#define correlation between the matrices given as the columns 

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv("D:/ESS/lec/diabetes.csv")
correlations = df.corr()
sns.heatmap(data = correlations , square = True , cmap = "bwr")  
#cmap---for color
plt.yticks(rotation = 0)
plt.xticks(rotation=90)

#red blocks shows the column of x and y axis that have a maximum correlation and blue cells shows the minimum correlation between the columns and other color represent the 1 and 0. 0 means maximum correlation and 1 means minimum correlation 


# In[10]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# In[11]:


df = pd.read_csv("D:/ESS/lec/diabetes.csv")


# In[12]:


correlations = df.corr()


# In[14]:


sns.heatmap(data = correlations , square = True , cmap = "bwr")
plt.yticks(rotation = 0)
plt.xticks(rotation = 90)


# sns.heatmap(data = correlations , square = True , cmap = "bwr")

# In[ ]:




