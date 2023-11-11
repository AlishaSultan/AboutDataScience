#!/usr/bin/env python
# coding: utf-8

# In[1]:


#data visualization ploting libraries:
#matplotlib python 2d ploting library
#vispy
#pygal
#bokeh
#folium
#seaborn
#networkx


# In[2]:


import numpy as np


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


from matplotlib import style


# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


randomnumber = np.random.rand(10)


# In[7]:


print(randomnumber)


# In[15]:


style.use('ggplot')
plt.plot(randomnumber , 'g' , label = 'line one' , linewidth = 2)
plt.xlabel('Range')
plt.ylabel("Numbers")
plt.title("First Plot")
plt.legend()
plt.show()


# In[16]:


cause = 'chronic' , 'cough' , 'asthma' , 'hypertension' , 'sepsis' , 'others'
percentile = [62 , 45 , 12 , 6 , 32 , 90]


# In[20]:


#set the pie chart plot properties
#set figure size
plt.figure(figsize = (10 , 10))
explode = (0 , 0 , 0 , 0 , 0 , 0.05)
#set pie chart properties
plt.pie(percentile , labels = cause , explode = explode , autopct = '%1.1f%%' , startangle = 70)
plt.axis('equal')
plt.title("OHIO state - 2012 : Leading cause of death")
plt.show()


# In[ ]:





# In[ ]:




