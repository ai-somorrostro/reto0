import time
import subprocess

def ejecutar_tareas():
    print("Ejecutando flujo de descarga...")
    subprocess.run(["python", "contenido/descargar_dataset.py"])
    subprocess.run(["python", "contenido/Corrector_de_cryptosCSV.py"])
    subprocess.run(["python", "contenido/Corrector_de_stocksCSV.py"])
    subprocess.run(["python", "contenido/subida_cryptoCSV_pandas_docker.py"])
    print("Tareas completadas.")

# Ejecutar cada 30 minutos
while True:
    ejecutar_tareas()
    print("Esperando 10 minutos...")
    time.sleep(600)  # 1800 segundos = 30 minutos
