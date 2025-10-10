#!/usr/bin/env python3
import docker
import sys

def pull_images(client, images):
    for image in images:
        try:
            print(f"🔄 Descargando {image} …")
            pulled = client.images.pull(image)
            print(f"✅ «{image}» descargada: {pulled.tags}")
        except docker.errors.APIError as e:
            print(f"❌ Error al descargar {image}: {e.explanation}")
        except Exception as e:
            print(f"❌ Error inesperado con {image}: {e}")

def main():
    # Lista de imágenes (con su repositorio y tag opcional)
    images = [
        "grafana/grafana:latest",
        "influxdb:latest",
        "nodered/node-red:latest"
    ]

    try:
        client = docker.from_env()
    except docker.errors.DockerException as e:
        print(f"❌ No se pudo conectar a Docker: {e}")
        sys.exit(1)

    pull_images(client, images)

if __name__ == "__main__":
    main()
