# BDA - Big Data & Aplicado

## 1. Manipulación y Análisis de Datos

### Tarea 1: Cargar conjuntos de datos y aplicar transformaciones
**Descripción:**  
En primer lugar, accedimos a una página fiable que nos proporcionaba datos sobre el mercado financiero, nos descargamos los ficheros (stocks.csv y cryptocurrency.csv) y realizamos la limpieza de los ficheros para su corrercta subida de datos a influxDB. La primera subida fué a través de node-RED y la segunda a través de pandas.

**Herramientas utilizadas:**  
- Node-RED  
- Python (pandas)  
- InfluxDB
- Grafana  
---

### Tarea 2: Configurar flujos en Node-RED
**Descripción:**  
El primer archivo lo cargamos a través de Node-RED. Este flujo realiza la lectura de un archivo CSV con datos de acciones, los procesa y los envía a una base de datos **InfluxDB**.

- **timestamp:** Inicia el flujo automáticamente.  
- **stocks.csv:** Lee el archivo CSV con los datos bursátiles.  
- **csv:** Convierte el contenido del CSV en objetos JSON.  
- **function 3:** Transforma los datos en puntos para InfluxDB.  
- **subida a influx batch:** Envía los puntos a la base de datos InfluxDB.  

**Configuración de los flujos:**  
*(Describe cómo se estructuraron los nodos, conexiones, etc.)*

**Resultados / Comprobaciones:**  
*(Incluye capturas o resumen de los datos enviados correctamente.)*

---

### Tarea 3: Integración de APIs externas en Node-RED
**Descripción:**  
*(Indica qué APIs se integraron y con qué propósito.)*

**Configuración y conexión con InfluxDB:**  
*(Explica cómo los datos de la API llegan a InfluxDB.)*

**Resultados:**  
*(Describe los datos obtenidos y su utilidad.)*

---

### Tarea 4: Automatización del guardado de datos
**Descripción:**  
*(Explica cómo automatizaste el proceso de almacenamiento en InfluxDB.)*

**Herramientas y scripts utilizados:**  
*(Menciona scripts o flujos relevantes.)*

**Resultado final:**  
*(Describe cómo se logró la automatización completa.)*

---

## 2. Gestión de Series Temporales (InfluxDB)

### Tarea 1: Creación de buckets y estructura de datos
**Descripción:**  
*(Detalla los buckets creados y la estructura de los datos.)*

**Configuración:**  
- Bucket:  
- Measurement:  
- Fields:  
- Tags:  

**Resultado:**  
*(Comenta cómo se organizó la información.)*

---

### Tarea 2: Generación de tokens de lectura y escritura
**Descripción:**  
*(Explica cómo se gestionó la seguridad de acceso a los datos.)*

**Proceso:**  
*(Describe cómo se generaron los tokens y cómo se aplicaron.)*

**Resultado:**  
*(Incluye detalles de protección y validación.)*

---

### Tarea 3: Uso de tags para optimización
**Descripción:**  
*(Explica qué tags se usaron y por qué.)*

**Ejemplo de estructura:**  
```text
measurement,tag1=value1,tag2=value2 field1=...,field2=... timestamp
