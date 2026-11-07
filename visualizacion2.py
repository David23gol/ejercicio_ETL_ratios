import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Cargar el DataFrame limpio y con ratios desde el CSV
df = pd.read_csv("campaña_datos_limpios.csv", sep=";")

# 2. Calcular métricas financieras adicionales para el análisis
# Costo total de cumplimiento = paid_orders * avg_fulfillment_cost
df["total_fulfillment_cost"] = df["paid_orders"] * df["avg_fulfillment_cost"]

# Rentabilidad Neta = Revenue - (Gasto de Publicidad + Costo de Cumplimiento)
df["net_profit"] = df["revenue"] - (df["ad_spend"] + df["total_fulfillment_cost"])

# 3. Configurar el estilo visual de los gráficos
sns.set_theme(style="whitegrid")  # Fondo limpio con cuadrícula
fig, axes = plt.subplots(
    nrows=2, ncols=1, figsize=(12, 10), sharex=True
)  # Dos paneles compartiendo el eje X (días)

# --- GRÁFICO SUPERIOR: Impacto de la Publicidad vs Ingresos ---
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

# --- GRÁFICO INFERIOR: Rentabilidad Neta Diaria ---
# Barras azules para ganancias positivas, naranjas/rojas para pérdidas
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

# 4. Ajustar diseño, guardar la imagen en alta calidad y mostrar
plt.tight_layout()

# Guardar antes de mostrar para evitar imágenes en blanco
plt.savefig(
    "impacto_campana_rentabilidad.png", dpi=300, bbox_inches="tight"
)

print(
    "¡Gráfico generado y guardado exitosamente como"
    " 'impacto_campana_rentabilidad.png'!"
)

plt.show()