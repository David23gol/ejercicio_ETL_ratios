import numpy as np
import pandas as pd

# 1. Cargar los datos del CSV sucio en la variable

# --- TU CÁLCULO DE RATIOS ---
# Calcular PCVR (porcentaje de conversión de sesiones a órdenes pagadas)
"""campaña_limpia_df["pcvr"] = 100 * (campaña_limpia_df["paid_orders"] / campaña_limpia_df["paid_sessions"])"""

# Opcional: Manejar divisiones por cero (donde paid_sessions era 0, el resultado será inf o NaN)
"""campaña_limpia_df["pcvr"] = campaña_limpia_df["pcvr"].replace([np.inf, -np.inf], np.nan).fillna(0)

# Visualizar el resultado final con la nueva columna
print(campaña_limpia_df[["campaign_day", "paid_sessions", "paid_orders", "pcvr"]].head(15))"""
campaña_limpia_df["pcvr"] = (
    100
    * (
        campaña_limpia_df["paid_orders"] / campaña_limpia_df["paid_sessions"]
    )
).fillna(0)
