#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import datetime
import os

# In[2]:
# Ruta absoluta al directorio donde está este script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta completa al CSV
csv_path = os.path.join(script_dir, "cryptocurrency.csv")

rawdata = pd.read_csv(csv_path)


# In[3]:


rawdata.set_index(rawdata['timestamp'], inplace = True)


# In[4]:


del rawdata['timestamp']


# In[5]:


def convertir_valor(valor):
    if pd.isna(valor):
        return np.nan

    s = str(valor).strip()
    # quitar símbolos comunes
    s = s.replace("$", "").replace(",", "").replace("%", "").replace("T", "").strip()

    # valores no válidos
    if s in ("", "-", "—", "N/A", "na", "NA"):
        return np.nan

    # procesar sufijos
    if "B" in s:
        return float(s.replace("B", "")) * 1000   # Billions → millones
    elif "M" in s:
        return float(s.replace("M", ""))          # Millions → millones
    elif "K" in s:
        return float(s.replace("K", "")) / 1000   # Thousands → millones
    elif "T" in s:
        return float(s.replace("T", "")) * 1000000   # Trillions → trillones
    else:
        return float(s)   # número normal o porcentaje ya limpio

def limpiar_dataframe(df):
    df_limpio = df.copy()
    for col in df_limpio.columns:
        try:
            df_limpio[col] = df_limpio[col].apply(convertir_valor)
        except Exception:
            # si la columna no es convertible (ej. texto puro como "name" o "symbol"),
            # simplemente la dejamos igual
            pass
    return df_limpio


# In[7]:

csv_path_save = os.path.join(script_dir, "cryptos_unidades_corregidas.csv")

df_limpio = limpiar_dataframe(rawdata)
df_limpio.to_csv(csv_path_save, index=True)

# In[ ]:




