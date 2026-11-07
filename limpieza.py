import os
import numpy as np
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Cargar las variables secretas del archivo .env
load_dotenv()

# 1. Cargar los datos del CSV sucio en la variable
campaña_datos_sucios_df = pd.read_csv("campaña_datos_sucios.csv", sep=";")
print(campaña_datos_sucios_df.head(15))

def limpiar_datos(df: pd.DataFrame) -> pd.DataFrame:
  columnas_a_limpiar = [
      "ad_spend",
      "paid_sessions",
      "paid_orders",
      "revenue",
      "avg_fulfillment_cost",
  ]
  for columna in columnas_a_limpiar:
    df[columna] = pd.to_numeric(
        df[columna].astype(str).str.replace(r"[^\d.-]", "", regex=True),
        errors="coerce",
    ).clip(lower=0)
  return df
#Rutina ETL de Sanitización Numérica Masiva en Pandas: Elimina caracteres basura/símbolos mediante Regex, coacciona tipos de texto inválidos a NaN sin romper el flujo, y aplica un límite inferior (clip) para evitar valores negativos en métricas de negocio.

campaña_limpia_df = limpiar_datos(campaña_datos_sucios_df)
print(campaña_limpia_df.head(15))

campaña_limpia_df["pcvr"] = (
    100
    * (
        campaña_limpia_df["paid_orders"] / campaña_limpia_df["paid_sessions"]
    )
).fillna(0)

campaña_limpia_df["pcvr"] = campaña_limpia_df["pcvr"].replace([np.inf, -np.inf], np.nan).fillna(0)
#Limpia los errores matemáticos de división por cero transformando los infinitos () en nulos (), y luego reemplaza dichos nulos por 0 para evitar fallos en los gráficos o en los cálculos posteriores."infNaN0

campaña_limpia_df["cpo"] = (
        campaña_limpia_df["ad_spend"] / campaña_limpia_df["paid_orders"]
)
print(campaña_limpia_df.head(15))
campaña_limpia_df.to_csv(
    "campaña_datos_limpios.csv", index=False, sep=";", encoding="utf-8"
)

print(
    "¡Archivo guardado exitosamente como 'campaña_datos_limpios.csv' en la"
    " raíz del proyecto!"
)

print(campaña_limpia_df.head(15))
import matplotlib.pyplot as plt
import seaborn as sns
print(
    campaña_limpia_df[
        ["campaign_day", "paid_sessions", "paid_orders", "pcvr", "cpo"]
    ].head(15)
)

# 2. Guardar el DataFrame limpio y con ratios en un nuevo archivo CSV
campaña_limpia_df.to_csv(
    "campaña_datos_limpios.csv", index=False, sep=";", encoding="utf-8"
)

print(
    "\n¡Éxito! El DataFrame depurado y con ratios se guardó como"
    " 'campaña_datos_limpios.csv'.")

import os
import numpy as np
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Cargar las variables secretas del archivo .env
load_dotenv()

# 1. Cargar el DataFrame limpio desde el CSV procesado
df = pd.read_csv("campaña_datos_limpios.csv", sep=";")

# 2. Recalcular las métricas financieras por seguridad
df["total_fulfillment_cost"] = df["paid_orders"] * df["avg_fulfillment_cost"]
df["net_profit"] = df["revenue"] - (
    df["ad_spend"] + df["total_fulfillment_cost"]
)

# Limpiar valores infinitos para evitar errores en MySQL
df.replace([np.inf, -np.inf], None, inplace=True)

# 3. Leer las credenciales de forma segura desde el entorno
usuario = os.getenv("DB_USER")
contraseña = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
puerto = os.getenv("DB_PORT")
nombre_db = os.getenv("DB_NAME")

# Crear la cadena de conexión optimizada
cadena_conexion = (
    f"mysql+pymysql://{usuario}:{contraseña}@{host}:{puerto}/{nombre_db}"
)
engine = create_engine(cadena_conexion)

# 4. FASE LOAD: Volcar el DataFrame en la tabla SQL relacional
nombre_tabla = "tb_campana_ventas"
df.to_sql(nombre_tabla, con=engine, if_exists="replace", index=False)

print("==================================================")
print("      FASE LOAD COMPLETADA EXITOSAMENTE           ")
print("==================================================")
