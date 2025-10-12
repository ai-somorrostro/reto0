#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
from influxdb_client import InfluxDBClient
import datetime


# In[7]:


rawdata = pd.read_csv('cryptos_unidades_corregidas.csv')
display(rawdata)


# In[8]:


rawdata['timestamp'] = pd.to_datetime(rawdata['timestamp'])
rawdata.set_index(rawdata['timestamp'], inplace = True)
del rawdata['timestamp']


# In[9]:


display(rawdata)


# In[10]:


my_token = 'mi_token_super_seguro'


# In[11]:


client = InfluxDBClient(url = "http://localhost:8086", token = my_token, org = "Cryptobro_Together_Strong")


# In[12]:


write_client = client.write_api()


# In[13]:


write_client.write("livemarket", record = rawdata, data_frame_measurement_name = "cryptocoins", data_frame_tag_columns=["name"])


# In[ ]:




