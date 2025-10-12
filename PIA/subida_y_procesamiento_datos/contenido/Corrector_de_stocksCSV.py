#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1. IMPORTAR LIBRERÍAS
import pandas as pd
import numpy as np
import datetime
import os

# In[ ]:


try:
    rawdata = pd.read_csv("stocks.csv")
    print("Archivo 'stocks.csv' cargado exitosamente.")
except FileNotFoundError:
    print("Error: No se encontró el archivo 'stocks.csv'.")
    print("Asegúrate de que el archivo está en la misma carpeta que el cuaderno o usa la ruta completa.")
    # Detenemos la ejecución si no se encuentra el archivo
    # Puedes comentar la siguiente línea si prefieres que continúe
    raise


# In[ ]:


def convertir_volumen(volumen_str):
    # Si el dato no es de tipo string, lo devolvemos tal cual para evitar errores
    if not isinstance(volumen_str, str):
        return volumen_str

    # Estandarizamos el texto: quitamos espacios y lo ponemos en mayúsculas
    volumen_str = volumen_str.strip().upper()

    try:
        if 'M' in volumen_str:
            # Si tiene 'M', quitamos la 'M' y multiplicamos por 1 millón
            return float(volumen_str.replace('M', '')) * 1_000_000
        elif 'K' in volumen_str:
            # Si tiene 'K', quitamos la 'K' y multiplicamos por 1 mil
            return float(volumen_str.replace('K', '')) * 1_000
        else:
            # Si no tiene ni 'M' ni 'K', solo lo convertimos a número
            return float(volumen_str)
    except (ValueError, TypeError):
        # Si algo falla en la conversión (ej: texto vacío), devolvemos None
        return None


# In[ ]:


# Columna 'vol_': Usamos la función que acabamos de crear
rawdata['vol_'] = rawdata['vol_'].apply(convertir_volumen)

# Columna 'chg_%': Quitamos el '%'
rawdata['chg_%'] = rawdata['chg_%'].astype(str).str.replace('%', '')

# Lista de todas las columnas que deben ser numéricas
columnas_a_convertir = ['last', 'high', 'low', 'chg_', 'chg_%', 'vol_']

for columna in columnas_a_convertir:
    # Convertimos cada columna a número. Si hay algún error, se convierte en NaN (nulo)
    rawdata[columna] = pd.to_numeric(rawdata[columna], errors='coerce')

# Opcional pero muy recomendado: Reemplazamos cualquier valor nulo (NaN) que haya quedado por 0
rawdata.fillna(0, inplace=True)


# In[ ]:

file_path = "stocks_unidades_corregidas.csv"

# Verifica si el archivo existe
if os.path.exists(file_path):
    df_antiguo = pd.read_csv(file_path)
    df_antiguo.to_csv("stocks_unidades_corregidas_old.csv", index=True)
    
# Este paso es para guardar el dataframe con los cambios como un CSV
rawdata.to_csv("stocks_unidades_corregidas.csv", index=False)
print("Archivo 'stocks_unidades_corregidas.csv' creado exitosamente.")
