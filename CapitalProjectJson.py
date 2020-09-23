#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
with open('cgcapitalprojects_img.geojson', 'r') as projects:
     capitalprojects = json.load(projects)


# In[2]:


capitalprojects


# In[3]:


with open('cgcapitalprojects_img.geojson', 'r') as projects:
    print(json.dumps(json.load(projects), indent=4))


# In[ ]:




