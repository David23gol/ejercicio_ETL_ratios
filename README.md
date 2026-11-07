# 🚀 Pipeline ETL & Análisis de Ratios Financieros

Pipeline de ingeniería de datos modular desarrollado en **Python** para la extracción, limpieza, transformación, cálculo de ratios financieros y carga automatizada (`Load`) hacia una base de datos relacional **MySQL**.

---

## 🛠️ Stack Tecnológico y Librerías
* **Lenguaje:** Python 
* **Manipulación de Datos:** Pandas, NumPy
* **Conexión y Base de Datos:** SQLAlchemy, PyMySQL, MySQL
* **Seguridad:** Python-Dotenv (`.env`) para la gestión de credenciales
* **Control de Versiones:** Git & GitHub

---

## 📂 Estructura del Proyecto

El repositorio está modularizado siguiendo buenas prácticas de arquitectura de datos:

```text
ejercicio_ETL_ratios/
│
├── .env                  # Variables de entorno (Credenciales ocultas - Excluido en .gitignore)
├── .gitignore            # Archivos excluidos del control de versiones
├── campaña_datos_sucios.csv   # Dataset de origen con anomalías
├── campaña_datos_limpios.csv  # Dataset procesado y saneado
├── crear_df.py           # Script de inicialización y generación de datos
├── limpieza.py           # Fase Transform: Limpieza de nulos, duplicados y tipos de datos
├── ratios.py             # Cálculo de métricas financieras (ROI, ROAS, conversión)
├── exportar_mysql.py     # Fase Load: Carga relacional blindada hacia MySQL
├── visualizacion.py      # Generación de reportes gráficos iniciales
└── visualizacion2.py     # Gráficos avanzados y análisis visual de métricas