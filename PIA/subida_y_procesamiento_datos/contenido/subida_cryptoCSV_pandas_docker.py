#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
from influxdb_client import InfluxDBClient
import datetime

from nueva_token_influx import crear_token_escritura

token = crear_token_escritura()
influx_url = "http://influxdb:8086"
rawdata = pd.read_csv('cryptos_unidades_corregidas.csv')

rawdata['timestamp'] = pd.to_datetime(rawdata['timestamp'])
rawdata.set_index(rawdata['timestamp'], inplace = True)
del rawdata['timestamp']

client = InfluxDBClient(url = influx_url, token = token, org = "Cryptobro_Together_Strong")

write_client = client.write_api()

write_client.write("livemarket", record = rawdata, data_frame_measurement_name = "cryptocoins", data_frame_tag_columns=["name"])
print("Datos subidos a InfluxDB con éxito")





