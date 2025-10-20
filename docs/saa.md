# SAA - Sistemas de Aprendizaje Automático

## Introducción
En esta asignatura se ha trabajado la **carga, exploración y visualización de datos** mediante librerías de Python, enfocándose en la comprensión, análisis y comunicación visual de la información.  
El objetivo principal ha sido **desarrollar habilidades en el manejo de datasets reales**, su representación gráfica y la interpretación de patrones relevantes para la toma de decisiones.

---

## 1️. Carga de Datos (Pandas)

### Tarea: Cargar archivos de datos en diferentes formatos
**Descripción:**  
*(Explica los tipos de datos cargados: CSV, Excel, JSON, SQL Server, etc., y su procedencia.)*

**Objetivo:**  
Asegurar la correcta lectura de los datos, sin errores de formato, usando la librería **pandas**.

**Formatos utilizados:**  
- [ ] CSV  
- [ ] Excel  
- [ ] JSON  
- [ ] SQL Server *(máxima puntuación si los datos se generaron directamente desde SQL Server)*  

**Ejemplo de código:**
```python
import pandas as pd
import pyodbc

# Ejemplo de carga desde SQL Server
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=servidor;DATABASE=bd;UID=usuario;PWD=contraseña')
df = pd.read_sql('SELECT * FROM tabla_datos', conn)

# Ejemplo de carga desde CSV
df_csv = pd.read_csv('data/dataset.csv')

## 2️. Curso de Visualización de Datos (Seaborn)

### 🎓 Curso: "Tutorial Seaborn desde cero" (Codificando Bits)

**Descripción:**  
Se visualizó el curso de YouTube “TUTORIAL SEABORN DESDE CERO”, con una duración aproximada de **38 minutos**, orientado al uso de **Seaborn** para mejorar la calidad y personalización de las gráficas en Python.

**Enlace al curso:**  
🔗 [Tutorial Seaborn desde Cero - Codificando Bits](https://www.youtube.com/) *(añadir enlace completo si se dispone)*

**Aprendizajes clave:**
- Creación de gráficos estadísticos con `seaborn`.  
- Personalización de colores, estilos y temas.  
- Representación de distribuciones y relaciones entre variables.  
- Integración de Seaborn con Matplotlib.  

**Evidencia:**  
*(Puedes incluir una captura del curso completado o del certificado, si se solicita.)*

---

## 3️. Explicación del Ejercicio de Visualización

### 🧠 Ejercicio:
**“Visualización: Explicación de gráficas y su uso” (Classroom)**

**Descripción:**  
*(Resume los puntos principales del ejercicio: tipos de gráficas explicadas, utilidad de cada una, y cómo ayudan en el análisis de datos.)*

**Contenido tratado:**
- Importancia de elegir el gráfico adecuado según el tipo de dato.  
- Comparación entre gráficos de barras, líneas y dispersión.  
- Interpretación de los resultados visuales.  

**Resultado:**  
*(Incluye ejemplos o reflexiones sobre qué tipo de gráfico consideras más útil para tu dataset.)*

---

## 4️. Visualización de Datos (Matplotlib y Seaborn)

### 🧮 Generación de Visualizaciones

**Ejemplos de visualizaciones:**
- Gráfico de barras  
- Gráfico de líneas  
- Diagrama de dispersión  
- Histograma  
- Mapa de calor  

---

### 🧩 Ejemplo de código:
```python
# Gráfico de dispersión con Seaborn
sns.scatterplot(data=df, x='variable_x', y='variable_y', hue='categoria')
plt.title('Relación entre variable_x y variable_y')
plt.show()

## 🧾 Resultado

*(Incluye descripciones de los gráficos creados, qué información muestran y por qué son relevantes para el análisis.)*

**Por ejemplo:**
- El **gráfico de barras** permitió comparar los valores promedio por categoría.  
- El **diagrama de dispersión** ayudó a identificar correlaciones entre variables.  
- El **mapa de calor** reveló relaciones de dependencia y posibles patrones de agrupación.  

---

## 5️⃣ Análisis y Reflexión sobre la Visualización de Datos

### 📘 Concepto General
La **visualización de datos** es la representación gráfica de la información para facilitar la comprensión de grandes volúmenes de datos.  
A través de gráficos, tablas y dashboards, se pueden identificar **tendencias, patrones y valores atípicos** de forma rápida y efectiva.

---

### 💡 Aplicación en Big Data
En el contexto de los **Big Data**, las herramientas de visualización son esenciales para transformar datos complejos en información útil que facilite la **toma de decisiones basada en datos**.

---

## 📈 Tipos Comunes de Visualizaciones de Datos

### 🔹 Formatos generales
- Gráficos  
- Tablas  
- Mapas  
- Infografías  
- Dashboards  

---

### 🔸 Ejemplos específicos

| Tipo de visualización | Descripción breve |
|-----------------------|------------------|
| Gráfico de área | Muestra la evolución de una variable a lo largo del tiempo. |
| Gráfico de barras | Compara valores categóricos o cuantitativos. |
| Diagrama de caja y bigotes | Detecta valores atípicos y distribuciones. |
| Gráfico de burbujas / nubes | Representa tres dimensiones: posición, tamaño y color. |
| Mapa de calor | Visualiza correlaciones o densidades en una matriz de datos. |
| Histograma | Muestra la distribución de frecuencias de una variable. |
| Gráfico de dispersión (2D o 3D) | Analiza la relación entre dos o más variables. |
| Gráfico de árbol radial / treemap | Representa jerarquías y proporciones. |
| Mapa de distribución de puntos | Indica localizaciones geográficas o eventos. |
| Escala de tiempo / Gantt | Muestra tareas o eventos en secuencia temporal. |

*(Puedes añadir ejemplos de los gráficos que creaste en tu proyecto o reto.)*

---

## 🔍 Datos Relevantes y Justificación

**Selección de datos para análisis posterior:**  
*(Describe qué columnas o variables te resultaron más interesantes para explorar en profundidad y por qué.)*

**Ejemplo:**  
> “Seleccioné las variables `temperatura_media` y `consumo_energético` para estudiar su relación, ya que podrían mostrar patrones estacionales útiles para la predicción.”

**Defensa de la selección:**  
*(Explica brevemente cómo la visualización de esos datos puede aportar valor o servir en un contexto real de análisis.)*

---

## 🧾 Conclusiones

- La carga y tratamiento de datos con **pandas** permite trabajar de forma eficiente con múltiples formatos.  
- Las librerías **Matplotlib** y **Seaborn** son herramientas clave para explorar y comunicar información visualmente.  
- La correcta elección del tipo de gráfico mejora la comprensión de los datos y ayuda en la toma de decisiones.  
- La visualización no solo representa los datos, sino que también permite **descubrir información oculta** y **validar hipótesis analíticas**.  

---

## 📚 Referencias

- Curso: *“Tutorial Seaborn desde Cero”* - Codificando Bits  
- Librerías: [Pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/)  
- Documentación de Python: [https://docs.python.org/3/](https://docs.python.org/3/)

