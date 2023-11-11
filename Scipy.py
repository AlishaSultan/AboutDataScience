#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Scipy libraries:
#Cluster (handles clustering algorithm)
#Constants(perform mathematical equations)
#fftpack(Compute discrete fourier transform routines)
#integrate(Solves mathmatical sequence or series)
#spatial(is used to problems related to graphs)
#interplot(Creates new data points)
#I/O reads and write from and to several file formats
#linalg(solve linear algebra problems)
#ndimage(Processes multidimensional images)
#odr(Handles explicit and implicit functions)
#optimize(optimizes performance)
#signal(processes and transfer information in different formats)
#Sparse(Is a sparse matrix package)
#Weave(Integrates C and C++)
#Stats(Has statistical distribution and functions)
#Special(is used to retrieve other special functions)


# In[2]:


import numpy as np
from scipy import linalg


# In[3]:


Variable_for_X = np.array([[1 ,1] , [4 , 9]])


# In[4]:


Variable_for_Y = np.array([30 , 150])


# In[5]:


linalg.solve(Variable_for_X , Variable_for_Y )


# In[ ]:




