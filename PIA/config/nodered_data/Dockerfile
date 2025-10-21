# 🐳 Base image: Node-RED oficial
FROM nodered/node-red:latest

# 👤 Cambia a usuario root para instalar paquetes
USER root

# 📦 Instala el nodo de InfluxDB
RUN npm install --unsafe-perm node-red-contrib-influxdb

# 🔒 Regresa al usuario node-red
USER node-red

CMD ["bash"]