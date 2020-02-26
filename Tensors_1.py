#!/usr/bin/env python
# coding: utf-8

# # Tensors 

# In[2]:


import torch


# In[3]:


## zeros()
w = torch.zeros(4,3)


# In[4]:


w.size()


# In[ ]:





# ## size() and shape

# In[5]:


w.shape


# In[ ]:





# In[ ]:





# ## randn() and randn_like()

# In[7]:


w = torch.randn(4,3)
w


# In[8]:


t = torch.randn_like(w)
t


# In[ ]:





# ## fill_()

# In[10]:


w.fill_(1)


# In[ ]:





# In[ ]:





# ## view()

# In[12]:


w.view(3,4)


# In[13]:


w.view(3,-1)


# In[ ]:





# ## numpy()

# In[14]:


w.numpy()


# In[ ]:





# In[ ]:




