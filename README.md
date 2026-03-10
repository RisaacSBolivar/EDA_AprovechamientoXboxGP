<div align="center">
  <img src="Xbox_one_logo.png" alt="Xbox One Logo" width="300"/>
  <h1>Análisis de Xbox Game Pass: Rentabilidad y Uso (2022)</h1>
  
  [![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
  [![Jupyter Notebook](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)](https://jupyter.org/)
  [![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
  [![Matplotlib](https://img.shields.io/badge/Matplotlib-ffffff?style=flat&logo=matplotlib&logoColor=black)](https://matplotlib.org/)
</div>

<br>

Este proyecto evalúa el aprovechamiento del servicio **Xbox Game Pass** durante el año 2022. Su objetivo principal es analizar si los usuarios dedican su tiempo de juego a los títulos más populares y aclamados por la crítica, ayudando a determinar la rentabilidad y valor de la suscripción.

Se utilizan datos obtenidos de diversos datasets de **Kaggle**, que incluyen métricas de horas de juego y puntuaciones de **Metacritic**, plataforma reconocida mundialmente por promediar valoraciones tanto de prensa especializada como de jugadores.

---

## 🎯 Objetivo del Proyecto

Determinar el nivel de aprovechamiento del catálogo de Xbox Game Pass por parte de sus suscriptores:
- Hacer énfasis en los títulos populares dentro de la comunidad de jugadores.
- Explorar los patrones de comportamiento y la relación matemática/estadística que existe entre la popularidad de los juegos y su calidad percibida.

## 🛠️ Tecnologías y Herramientas

- **Lenguaje:** Python
- **Análisis y Manipulación de Datos:** `pandas`, `numpy`
- **Visualización de Datos:** `matplotlib`, `seaborn`
- **Entorno de Trabajo:** Jupyter Notebooks (`jupyter`)

---

## 📂 Estructura del Repositorio

El proyecto ha sido estructurado siguiendo buenas prácticas de procesos de ciencia de datos:

```text
📁 EDA_AprovechamientoXboxGP/
│
├── 📁 data/                  # Datasets brutos y procesados (.csv)
├── 📁 notebooks/             # Cuadernos Jupyter con los análisis por fases
│   ├── limpieza.ipynb               # Limpieza y estructuración inicial
│   ├── analisis_univariante.ipynb   # Variables categóricas y continuas individuales
│   ├── analisis_bivariante.ipynb    # Cruces de pares de variables
│   └── analisis_multivariante.ipynb # Análisis conjunto y correlaciones
│
├── 📁 src/
│   └── 📁 utils/             # Funciones auxiliares y constantes para gráficas y datos
│       ├── constants.py
│       └── funciones.py
│
├── main.ipynb                # Cuaderno principal que enlaza los hallazgos
├── memoria.pdf / .html       # Reporte final con explicaciones ejecutivas
├── README.md                 # Este documento
└── requirements.txt          # Dependencias necesarias
```

---

## 🚀 Instalación y Uso

Si deseas replicar este análisis de datos en tu entorno local:

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/TuUsuario/EDA_AprovechamientoXboxGP.git
   cd EDA_AprovechamientoXboxGP
   ```

2. **Crea un entorno virtual (Recomendado)**
   ```bash
   python -m venv venv
   # En Windows:
   .\venv\Scripts\activate
   # En macOS/Linux:
   source venv/bin/activate
   ```

3. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecuta Jupyter Notebook**
   ```bash
   jupyter notebook
   ```
   *Explora los archivos dentro de la carpeta `notebooks/`.*

---

## 📊 Fases del Análisis y Resultados Clave

1. **Exploración y Limpieza:** Preparación del dataset consolidando orígenes heterogéneos y manejando valores nulos.  
2. **Análisis Univariante y Bivariante:** Evaluación de la distribución de horas jugadas por tipo de juego, así como el contraste entre puntuaciones de usuarios en la plataforma Xbox y críticas de Metacritic.
3. **Análisis Multivariante:** Se examinaron las correlaciones subyacentes usando matrices de calor y diagramas de dispersión condicionados. Identificando que, aunque un juego sea aclamado en crítica, no siempre retiene al usuario en número de horas en la misma proporción.

> **💡 Conclusión:** La estrategia de Xbox Game Pass resulta atractiva ya que distribuye el tiempo de sus usuarios a través de una larga cola (long-tail) de juegos variados, y no depender exclusivamente del "top de Metacritic".

---

<div align="center">
  <b>Desarrollado con 🎮 y ☕ para el portafolio de análisis de datos.</b><br>
  <i>Si te resultó interesante, no dudes en dejar una ⭐.</i>
</div>
