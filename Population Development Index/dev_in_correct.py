
# coding: utf-8

# In[68]:


import numpy as np
import pandas as pd
import math


# In[2]:


data = pd.read_csv("population_census_data.csv")


# In[4]:


data.head()


# In[14]:


m = data.shape[0]
n = data.shape[1]
bias = np.ones(m)
bias = pd.DataFrame(bias)


# In[17]:


n


# In[54]:


X = pd.concat([bias,data.iloc[:,0:6]],axis=1)


# In[55]:


X


# In[18]:


def dev_in(features):
    w = pd.DataFrame(np.random.randint(1,6,7))
    
    h = 
    
    


# In[56]:


w = pd.DataFrame(np.random.randint(1,6,7))


# In[57]:


w


# In[58]:


X = X.values
# X = pd.DataFrame(X)
# X = X.as_matrix()
# type(X)


# In[59]:


type(X)


# In[50]:


w = pd.DataFrame(np.random.randint(1,6,7))
w = w.as_matrix()


# In[51]:


type(w)


# In[95]:


h = np.log(X).dot(w)
# h = X.dot(w)


# In[96]:


# np.log(h)
h


# In[97]:


def sigmoid(hyp):
    di = 1/(1+np.exp(-hyp))
    return di
    


# In[98]:


dev_i = sigmoid(h)


# In[99]:


dev_i


# In[72]:


type(h)


# In[76]:


np.exp(-h)


# In[ ]:


h = w[]

