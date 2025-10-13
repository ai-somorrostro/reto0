FROM python:3.11-slim

WORKDIR /app

# Instala paquetes de Python
RUN pip install --no-cache-dir kaggle pandas influxdb-client
# Crear carpeta para credenciales (el archivo se montará desde el host)
RUN mkdir -p /root/.kaggle

# No copies kaggle.json aquí — se monta desde docker-compose
ENV KAGGLE_CONFIG_DIR=/root/.kaggle

CMD ["bash"]
