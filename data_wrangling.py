#!/usr/bin/env python
# coding: utf-8

# In[1]:


######################################data wrangling#########################################################


# In[2]:


#converting or mapping the data from one format into another

#It includes munging and data visualization
#Discovering 
#Structuring
#Cleaning
#Enrichment
#Validating
# In[3]:


#Need for data wrangling:
#Missing data
#Presence of noisy data
#Inconsistent data
#It helps to develope accurate model and prediction out of data


# In[4]:


#It prevents the data leakage


# In[5]:


##########################################Missing value detection####################################################


# In[6]:


###########df1.isnull().any() tells missing value is present or not


# In[7]:


####################################Missing Value Treatment##############################


# In[8]:


#Mean Imputation:   Replace the missing value with variable mean
#Median Imputation: Replace the missing value with variable median


# In[ ]:


####################################################Outlier value in dataset###################################################


# In[ ]:


#An outlier is a value that lies outside the usual observation of values


# In[16]:


#Detect any outlier in first column:
#import seaborn as sns
#sns.boxplot(x = df1 ['Assignment'])


# In[17]:


from sklearn.datasets import load_diabetes
dataset = load_diabetes()
dataset


# In[18]:


dataset.data


# In[19]:


dataset.target


# In[21]:


dataset['feature_names']


# In[22]:


import pandas as pd
import numpy as np


# In[23]:


df = pd.DataFrame(data=np.c_[dataset['data'],dataset['target']], columns = dataset['feature_names'] + ['target'])


# In[24]:


df


# In[26]:


df.isnull().any()       #is any null value


# In[27]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


for column in df:
    plt.figure()
    df.boxplot([column])
    


# In[28]:


#Data manipulation:
 #   Data manipulation involving perform some opeartion on the data in order to gather some specific information from the data
#Objects are python abstraction for data
#Data object in python : A data object is two dimensional data structure data is alligned in tabular fashion in rows and columns
 #   Different data objects are:
  #      head()
   #     tail()
    #    values()
     #   groupby()
      #  concatenation
       # merging
        


# In[30]:


import pandas as pd
import numpy as np
df = pd.Series(np.arange(1 , 51))
print(df.head(6))


# In[31]:


import pandas as pd
import numpy as np
df = pd.Series(np.arange(1 , 51))
print(df.tail(6))


# In[32]:


import pandas as pd
import numpy as np
df = pd.Series(np.arange(1 , 51))
print(df.values)                   #gives the actual values


# In[36]:


import pandas as pd
world_cup = {'Team' : ['Pakistan' , 'India' , 'UK' , 'Karachi' , 'Islamabad' , 'London'] , 'Rank' : [12 , 13 , 17 , 34 , 56 , 90] , 'Year' : [2013 , 2034 , 2098 , 2647 , 7833 , 9894]}
df = pd.DataFrame(world_cup)
print(df.groupby(['Team' , 'Rank']).groups)  #groupby is used to group the dataframe according to given condition


# In[37]:


#concate combines two or more data structure
import pandas as pd
world_cup = {'Team' : ['Pakistan' , 'India' , 'UK' , 'Karachi' , 'Islamabad' , 'London'] , 'Rank' : [12 , 13 , 17 , 34 , 56 , 90] , 'Year' : [2013 , 2034 , 2098 , 2647 , 7833 , 9894]}
country_cup = {'Team' : ['Pakistan' , 'India' , 'UK' , 'Karachi' , 'Islamabad' , 'London'] , 'Rank' : [12 , 13 , 17 , 34 , 56 , 90] , 'Year' : [2013 , 2034 , 2098 , 2647 , 7833 , 9894]}
df1 = pd.DataFrame(world_cup)
df2 = pd.DataFrame(country_cup)
print(pd.concat([df1 , df2] , axis = 1))   #axis = 1 : two datasets have been combined using column


# In[45]:


import pandas as pd
world_cup = {'Team' : ['Pakistan' , 'India' , 'UK' , 'Karachi' , 'Islamabad' , 'London'] , 'Rank' : [12 , 46 , 17 , 98 , 56 , 90] , 'Year' : [2013 , 2034 , 2098 , 2647 , 7833 , 9894]}
country_cup = {'Team' : ['Pakistan' , 'India' , 'UK' , 'Karachi' , 'Islamabad' , 'London'] , 'Rank' : [12 , 13 , 89 , 34 , 12 , 90] , 'Year' : [2013 , 2034 , 2098 , 2647 , 7833 , 9894]}
df1 = pd.DataFrame(world_cup)
df2 = pd.DataFrame(country_cup)
print(pd.merge(df1 , df2 , on = "Rank"))   # only merge same values


# In[ ]:


#Merging is performed using database joins whereas concatenation combines two or more dataframe and havingt no relationship


# In[ ]:


#Different types of joins:
#Joins are used to combine records from two or more tables in a database
#A join always locates related column values in the two tables
#left join
#right join
#inner join
#Full outer join


# In[42]:


#Left join:
#Returns all the rows from left table , even if there are no matches in the right table


# In[43]:


import pandas as pd
world_cup = {'Team' : ['Pakistan' , 'India' , 'UK' , 'Karachi' , 'Islamabad' , 'London'] , 'Rank' : [12 , 13 , 56 , 34 , 56 , 90] , 'Year' : [2013 , 2034 , 2098 , 2647 , 7833 , 9894]}
country_cup = {'Team' : ['Pakistan' , 'India' , 'UK' , 'Karachi' , 'Islamabad' , 'London'] , 'Rank' : [12 , 90 , 17 , 38 , 56 , 90] , 'Year' : [2013 , 2034 , 2098 , 2647 , 7833 , 9894]}
df1 = pd.DataFrame(world_cup)
df2 = pd.DataFrame(country_cup)
print(pd.merge(df1 , df2 , on = "Year" , how = 'left'))


# In[46]:


#Right join
#Perserves the unmatched rows from the second table joining them with the NULL in the shape of first table


# In[54]:


import pandas as pd
world_cup = {'Team' : ['Pakistan' , 'India' , 'UK' , 'Karachi' , 'Islamabad' , 'London'] , 'Rank' : [12 , 13 , 56 , 34 , 56 , 90] , 'Year' : [2013 , 2034 , 2098 , 2647 , 7833 , 9894]}
country_cup = {'Team' : ['Pakistan' , 'India' , 'UK' , 'Karachi' , 'Islamabad' , 'London'] , 'Rank' : [12 , 90 , 17 , 38 , 56 , 90] , 'Year' : [2013 , 2034 , 2098 , 2647 , 7833 , 9894]}
df1 = pd.DataFrame(world_cup)
df2 = pd.DataFrame(country_cup)
print(pd.merge(df1 , df2 , on = "Rank" ,how = 'right'))


# #Inner join : Select all rows from both participating table if there is a match between the columns 
# 

# In[53]:


import pandas as pd
world_cup = {'Team' : ['Pakistan' , 'India' , 'UK' , 'Karachi' , 'Islamabad' , 'London'] , 'Rank' : [127 , 139 , 561 , 34 , 569 , 902] , 'Year' : [2013 , 2034 , 2098 , 2647 , 7833 , 9894]}
country_cup = {'Team' : ['Pakistan' , 'India' , 'UK' , 'Karachi' , 'Islamabad' , 'London'] , 'Rank' : [124 , 90 , 17 , 384 , 562 , 903] , 'Year' : [2013 , 2034 , 2098 , 2647 , 7833 , 9894]}
df1 = pd.DataFrame(world_cup)
df2 = pd.DataFrame(country_cup)
print(pd.merge(df1 , df2 , on = "Rank" , how = 'inner'))


# In[56]:


#Full outer join
#Returns all the records when there is a match in either left (table1) or right (table2) table records 


# In[57]:


import pandas as pd
world_cup = {'Team' : ['Pakistan' , 'India' , 'UK' , 'Karachi' , 'Islamabad' , 'London'] , 'Rank' : [127 , 139 , 561 , 34 , 569 , 902] , 'Year' : [2013 , 2034 , 2098 , 2647 , 7833 , 9894]}
country_cup = {'Team' : ['Pakistan' , 'India' , 'UK' , 'Karachi' , 'Islamabad' , 'London'] , 'Rank' : [124 , 90 , 17 , 384 , 562 , 903] , 'Year' : [2013 , 2034 , 2098 , 2647 , 7833 , 9894]}
df1 = pd.DataFrame(world_cup)
df2 = pd.DataFrame(country_cup)
print(pd.merge(df1 , df2 , on = "Rank" , how = 'outer'))


# In[ ]:




