import numpy as np
import pandas as pd

# Fijar semilla para reproducibilidad
np.random.seed(42)

n_rows = 100
campaign_day = np.arange(1, n_rows + 1)

# 1. Generar datos base
ad_spend_base = np.random.randint(50, 5000, size=n_rows)
paid_sessions_base = ad_spend_base // 2 + np.random.randint(
    -15, 15, size=n_rows
)
paid_orders_base = (
    paid_sessions_base // 20 + np.random.randint(-2, 5, size=n_rows)
)
paid_orders_base = np.maximum(paid_orders_base, 0)
revenue_base = paid_orders_base * np.random.randint(30, 70, size=n_rows)
avg_fulfillment_cost_base = np.random.choice([8, 10, 12, 15], size=n_rows)

# Crear DataFrame convirtiendo todo a tipo 'object' (texto/mixto) desde el inicio
df = pd.DataFrame(
    {
        "campaign_day": campaign_day,
        "ad_spend": ad_spend_base.astype(object),
        "paid_sessions": paid_sessions_base.astype(object),
        "paid_orders": paid_orders_base.astype(object),
        "revenue": revenue_base.astype(object),
        "avg_fulfillment_cost": avg_fulfillment_cost_base.astype(object),
    }
)

# 2. Inyectar Errores Humanos Comunes (ahora sí aceptará textos y strings)

# A. Formato de texto con comas y símbolos
def format_currency_or_string(val):
  if pd.isna(val):
    return np.nan
  val_int = int(val)
  r = np.random.rand()
  if r < 0.3:
    return f"{val_int:,}"
  elif r < 0.45:
    return f"${val_int:,}"
  else:
    return str(val_int)


df["ad_spend"] = df["ad_spend"].apply(format_currency_or_string)
df["revenue"] = df["revenue"].apply(format_currency_or_string)

# B. Valores nulos (NaN) distribuidos aleatoriamente
mask_nan = np.random.rand(n_rows, len(df.columns)) < 0.04
for i, col in enumerate(df.columns):
  df.loc[mask_nan[:, i], col] = np.nan

# C. Errores de tipeo y strings de texto basura
typo_indices = np.random.choice(n_rows, 6, replace=False)
df.loc[typo_indices[0], "paid_sessions"] = "N/A"
df.loc[typo_indices[1], "ad_spend"] = "Error_dato"
df.loc[typo_indices[2], "paid_orders"] = "Pendiente"
df.loc[typo_indices[3], "revenue"] = "Sin registro"
df.loc[typo_indices[4], "avg_fulfillment_cost"] = "10.5 USD"
df.loc[typo_indices[5], "paid_sessions"] = "Indefinido"

# D. Valores negativos
neg_indices = np.random.choice(n_rows, 4, replace=False)
df.loc[neg_indices[0], "ad_spend"] = "-250"
df.loc[neg_indices[1], "paid_sessions"] = -15
df.loc[neg_indices[2], "revenue"] = "-1200"
df.loc[neg_indices[3], "paid_orders"] = -3

print(df.head(15))

df.to_csv("campaña_datos_sucios.csv", index=False, sep=";", encoding="utf-8")

print(
    "¡Archivo CSV guardado exitosamente en la carpeta de tu proyecto como"
    " 'campaña_datos_sucios.csv'!"
)