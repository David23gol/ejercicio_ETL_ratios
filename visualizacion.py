"""Script de Visualización (graficar_campana.py)
Asegúrate de tener instaladas las librerías (pip install matplotlib seaborn) y ejecuta el siguiente código después de depurar tus datos:"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# --- SUPONIENDO QUE YA TIENES TU DATAFRAME LIMPIO (df) ---
# (Ejemplo rápido de simulación limpia para que el script corra directo si lo pruebas)
np.random.seed(42)
n = 100
df = pd.DataFrame(
    {
        "campaign_day": np.arange(1, n + 1),
        "ad_spend": np.random.randint(100, 3000, size=n),
        "paid_orders": np.random.randint(5, 100, size=n),
        "revenue": np.random.randint(300, 8000, size=n),
        "avg_fulfillment_cost": 10,
    }
)

# 1. CÁLCULO DE MÉTRICAS Y RENTABILIDAD
# Costo total de cumplimiento = paid_orders * avg_fulfillment_cost
df["total_fulfillment_cost"] = df["paid_orders"] * df["avg_fulfillment_cost"]

# Rentabilidad Neta = Revenue - (Gasto de Publicidad + Costo de Cumplimiento)
df["net_profit"] = df["revenue"] - (df["ad_spend"] + df["total_fulfillment_cost"])

# 2. CONFIGURACIÓN DEL ESTILO DE LOS GRÁFICOS
sns.set_theme(style="whitegrid")  # Fondo limpio con cuadrícula
fig, axes = plt.subplots(
    nrows=2, ncols=1, figsize=(12, 10), sharex=True
)  # Dos gráficos compartiendo el eje X (días)

# --- GRÁFICO 1: Impacto de la Publicidad vs Ventas (Líneas de tiempo) ---
sns.lineplot(
    data=df,
    x="campaign_day",
    y="revenue",
    ax=axes[0],
    color="green",
    linewidth=2.5,
    label="Ingresos (Revenue)",
)
sns.lineplot(
    data=df,
    x="campaign_day",
    y="ad_spend",
    ax=axes[0],
    color="crimson",
    linewidth=2.5,
    label="Inversión Publicitaria (Ad Spend)",
)
axes[0].set_title(
    "Impacto de la Publicidad Pagada vs. Ingresos por Día",
    fontsize=14,
    fontweight="bold",
)
axes[0].set_ylabel("Monto ($)", fontsize=12)
axes[0].legend(loc="upper left")

# --- GRÁFICO 2: Rentabilidad Neta Diaria (Barras / Área) ---
# Usamos un mapa de colores condicional: azul si hay ganancias, rojo si hay pérdidas
colors = np.where(df["net_profit"] >= 0, "royalblue", "darkorange")
axes[1].bar(
    df["campaign_day"],
    df["net_profit"],
    color=colors,
    alpha=0.85,
    edgecolor="black",
    linewidth=0.5,
)
axes[1].axhline(0, color="black", linestyle="--", linewidth=1)  # Línea de equilibrio en 0
axes[1].set_title(
    "Rentabilidad Neta Diaria [Revenue - (Publicidad + Logística)]",
    fontsize=14,
    fontweight="bold",
)
axes[1].set_xlabel("Día de Campaña (campaign_day)", fontsize=12)
axes[1].set_ylabel("Beneficio Neto ($)", fontsize=12)

# Ajustar diseño automáticamente para que no se solapen los textos
plt.tight_layout()

# Mostrar la ventana interactiva con el gráfico
plt.show()
# 1. Cargar el DataFrame limpio
import pandas as pd

# 1. Cargar el DataFrame limpio
df = pd.read_csv("campaña_datos_limpios.csv", sep=";")

# 2. Recalcular las métricas financieras en el script de análisis
df["total_fulfillment_cost"] = df["paid_orders"] * df["avg_fulfillment_cost"]
df["net_profit"] = df["revenue"] - (df["ad_spend"] + df["total_fulfillment_cost"])

# 3. Filtrar exclusivamente los días con rentabilidad negativa
dias_negativos = df[df["net_profit"] < 0].sort_values(by="net_profit", ascending=True)

# 4. Mostrar los días críticos y sus variables principales
print(f"Total de días con pérdidas en la campaña: {len(dias_negativos)}")
print("\n--- DETALLE DE LOS DÍAS CON PÉRDIDAS NETAS ---")
print(
    dias_negativos[
        [
            "campaign_day",
            "ad_spend",
            "revenue",
            "paid_sessions",
            "paid_orders",
            "net_profit",
        ]
    ]
)