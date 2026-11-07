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