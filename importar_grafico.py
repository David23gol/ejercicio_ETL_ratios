"""Para guardar cualquier gráfico generado con Matplotlib como un archivo de imagen directamente desde tu script de Python, debes utilizar la función .plt.savefig()

El secreto clave: El orden importa
Debes colocar la línea para guardar siempre antes de . Si ejecutas  primero, Matplotlib vacía el lienzo de la figura y, al intentar guardarla después, obtendrás un archivo de imagen totalmente en blanco.plt.show()plt.show()

Ejemplo práctico de uso:"""
#plt.savefig("grafico_impacto_publicidad.png", dpi=300, bbox_inches="tight")

import matplotlib.pyplot as plt

# ... (todo tu código de configuración de los gráficos y datos) ...

# Ajustar diseño automáticamente
plt.tight_layout()

# 1. GUARDAR LA IMAGEN ANTES DE MOSTRARLA
plt.savefig(
    "impacto_campana_rentabilidad.png",  # Nombre y extensión del archivo
    dpi=300,  # Alta resolución (ideal para informes o presentaciones)
    bbox_inches="tight",  # Evita que las etiquetas o títulos queden cortados en los bordes
)

# 2. MOSTRAR LA GRÁFICA EN PANTALLA
plt.show()