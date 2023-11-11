#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Scikit is a powerful machine learning python library used for data analysis and information extraction
#Efficient tools to identify and organize problems(supervised and unsupervised learning)
#Free and open datasets


# In[2]:


import pandas as pd


# In[4]:


df = pd.read_csv("D:/ESS/lec/tips_dataset.csv")


# In[5]:


print(df)


# In[6]:


#view top 5 records
df.head(5)


# In[8]:


#view the dataset size
df.size


# In[9]:


#view the shape of dataset
df.shape


# In[11]:


#view the columns of dataset
df.columns


# In[14]:


#create a feature object from column
X_features = df[['tip' , 'sex' , 'smoker' , 'day' , 'time' , 'size']]


# In[15]:


#view feature object
X_features


# In[16]:


#create target_object
Y_feature = df[['total_bill']]


# In[17]:


Y_feature


# In[20]:


#view feature object shape
X_features.shape


# In[21]:


#view target object shape
Y_feature.shape


# In[25]:


#split test and train dataset
from sklearn.model_selection import train_test_split
X_train ,  X_test , y_train , y_test = train_test_split(X_features , Y_feature , random_state = 1) 


# In[26]:


#view the shape of test and train dataset
X_train.shape


# In[27]:


X_test.shape


# In[28]:


y_train.shape


# In[29]:


y_test.shape


# In[36]:


from sklearn.linear_model import LinearRegression
linReg = LinearRegression()
linReg.fit(X_train , y_train)


# In[ ]:


#print intercept and coeficient
print linreg.intercept_
print linreg.coef_

#pred

y_pred = linreg.predict(x_test)


#mean square error
from sklearn import metrics
import numpy as np

print np.sqrt(metrics.mean_squared_error(y_test , y_pred))

