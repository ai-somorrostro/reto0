#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
import datetime
import os

from nueva_token_influx import crear_token_escritura

try:
    # Crear token de escritura
    token = crear_token_escritura()
    influx_url = "http://influxdb:8086"
    org = "Cryptobro_Together_Strong"
    bucket = "livemarket"

    # Verificar que el archivo nuevo existe
    csv_path = "/app/contenido/cryptos_unidades_corregidas.csv"
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"❌ No se encontró el archivo CSV en: {csv_path}")

    # Cargar datos nuevos
    rawdata = pd.read_csv(csv_path)
    rawdata['timestamp'] = pd.to_datetime(rawdata['timestamp'])
    rawdata.set_index(rawdata['timestamp'], inplace=True)
    del rawdata['timestamp']

    # Conectar a InfluxDB
    client = InfluxDBClient(url=influx_url, token=token, org=org)
    write_client = client.write_api(write_options=SYNCHRONOUS)

    # Ruta del archivo viejo
    csv_path_old = "/app/contenido/cryptos_unidades_corregidas_old.csv"

    if os.path.exists(csv_path_old):
        # Cargar datos viejos
        rawdata_old = pd.read_csv(csv_path_old)
        rawdata_old['timestamp'] = pd.to_datetime(rawdata_old['timestamp'])
        rawdata_old.set_index(rawdata_old['timestamp'], inplace=True)
        del rawdata_old['timestamp']

        # Comparar los DataFrames
        diferencias = rawdata.compare(rawdata_old)

        # Subir solo las diferencias
        write_client.write(bucket=bucket,
                           record=diferencias,
                           data_frame_measurement_name="cryptocoins",
                           data_frame_tag_columns=["name"])

        print("✅ Diferencias subidas a InfluxDB con éxito")
    else:
        # No hay archivo viejo, subir el CSV nuevo completo
        write_client.write(bucket=bucket,
                           record=rawdata,
                           data_frame_measurement_name="cryptocoins",
                           data_frame_tag_columns=["name"])

        print("📥 No se encontró archivo viejo. Se subió el CSV nuevo completo a InfluxDB")

except Exception as e:
    print(f"❌ Error durante la subida de datos: {e}")
