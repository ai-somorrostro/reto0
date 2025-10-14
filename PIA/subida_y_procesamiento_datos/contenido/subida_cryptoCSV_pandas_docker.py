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

    # Verificar que el archivo existe
    csv_path = "/app/contenido/cryptos_unidades_corregidas.csv"
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"❌ No se encontró el archivo CSV en: {csv_path}")

    # Cargar datos
    rawdata = pd.read_csv(csv_path)
    rawdata['timestamp'] = pd.to_datetime(rawdata['timestamp'])
    rawdata.set_index(rawdata['timestamp'], inplace=True)
    del rawdata['timestamp']

    # Conectar a InfluxDB
    client = InfluxDBClient(url=influx_url, token=token, org=org)
    write_client = client.write_api(write_options=SYNCHRONOUS)

    # Subir datos
    write_client.write(bucket=bucket,
                       record=rawdata,
                       data_frame_measurement_name="cryptocoins",
                       data_frame_tag_columns=["name"])

    print("✅ Datos subidos a InfluxDB con éxito")

except Exception as e:
    print(f"❌ Error durante la subida de datos: {e}")
