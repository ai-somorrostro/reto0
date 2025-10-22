# Reto 0 - Grupo 5
## Integrantes
- Clemente Rodriguez
- Ibai Garcia
- Aritz Basarrate

## **[Landing page](https://ai-somorrostro.github.io/reto0)**
## En caso de que el requirements.txt de problemas, Posibles soluciones:
### Actualizar pip, setuptools y wheel
Estos son esenciales para instalar muchos paquetes, entra en tu entorno virtual y ejecutas este comando. Puedes actualizarlos así:

```bash
python -m pip install --upgrade pip setuptools wheel
```
## Actualizar paquetes del sistema
### En Linux/macOS:

```bash
sudo apt update && sudo apt upgrade
```
Esto puede instalar o actualizar librerías necesarias para compilar paquetes como lxml, psycopg2, etc. Hazlo fuera de tu entorno virtual.


# Guia de Instalación del proyecto
### Este repositorio contiene las imagenes de Grafana, InfluxDB y Node-red, si las tienes instaladas en tu maquina linux, desactivalas.
## Compatibilidad
 - Linux

## Paso 1
 - Nos descargamos el proyecto siguiendo la guia oficial de [Github](https://url-del-enlace.com), nos tiene que quedar tal que así:

    ![Arbol proyecto](recursos_readme/tree.png)

## Paso 2
 - En la terminal (ya sea en la propia maquina o atraves de ssh) nos desplazamos a la carpeta PIA.

    ![terminal_1](recursos_readme/terminal_1.png)

 - Dentro de esa carpeta, encontrarás un fichero llamado .env.example, entra dentro y quita los valores con corchetes(ej: VALOR_DE_ENTORNO=loquesea --> VALOR_DE_ENTORNO=) y rellenalo con tus valores seleccionados (recomendamos que se deje como esta).
 - Después, renombra el fechero de .env.example a .env y ya estaria.

## Paso 3
 - Despues, en esa misma terminal ejecutamos el siguiente comando, veremos como se empieza a descargar las imagenes y dependencias de todo lo que tiene que usar, tarda un poco:

    ![terminal_2](recursos_readme/terminal_2.png)

 - Si queremos desentendernos de lo que hace por detras le podemos añadir esto al comando:
    ```bash
    docker compose up --build -d
    ```
 - Este comando solo lo ejecutaremos la vez que nos descarguemos el proyecto, a partir de ahi tenemos las imagenes descargadas, si repetimos el mismo comando de arriba nos descargara otra vez las imagenes, por eso en futuras instancias ejecutamos el siguiente comando:
    ```bash
    docker compose up -d
    ```
## Paso 4
 - Despues de que se descargue y se despliegue todo podemos entrar dentro de la maquina y entrar a traves de un explorador web en los distintos servicios. Los usuarios y contraseñas de los distintos servicios son los siguientes:
     - Grafana
        - usuario: admin
        - contraseña: admin
     - Influxdb
        - usuario: cryptobro
        - contraseña: criptobro12345

## Paso 5
 - Una vez que hayamos hecho todo lo que queramos con los servicios, para apagarlos insertamos el siguiente comando:
    ```bash
    docker compose down
    ```
