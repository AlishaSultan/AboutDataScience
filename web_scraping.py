#!/usr/bin/env python
# coding: utf-8

# In[1]:


#web scrapping
#extracting information from the websites
#parser
#parser is a basic tool to interpret or render information from a web document


# In[4]:


#import required libraries
from bs4 import BeautifulSoup
import requests


# In[5]:


#url for web scraping
url = "https://www.simplilearn.com/"


# In[6]:


#access the url with request object
result = requests.get(url)
#scrape the web page content
webpage = result.content
#create a soup object for parsing web page using html parser
sl_soup = BeautifulSoup(webpage , 'html.parser')  #sl_soup is the soup object created for parsing web page using html parser


# In[7]:


#close the result object
result.close()


# In[9]:


#view the content of soup object
sl_soup.contents


# In[12]:


print(sl_soup.prettify())


# In[13]:


#view the head of soup object
print(sl_soup.head)


# In[14]:


#view the title of web page
sl_soup.title


# In[16]:


#find all the links present on the web page
for href in sl_soup.findAll('a' , href = True):
    print(href['href'])


# In[ ]:


# Key Takeaways:
#numpy: numpy can manipulate the data using various array shape manipulation techniques
#Scipy: has built_in package that help in handling the scientific domain
#matplotlib: is a visualization tool that uses a low level graph plotting library built in python
#scikit is a powerful machine learning python library for data analysis and information extraction
#pandas can load or explode data in a variety of formats

