import os
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# === Ruta base: carpeta del proyecto (donde está ESTE .py) ===
BASE_DIR = Path(__file__).resolve().parent
CHARTS_DIR = BASE_DIR / "assets" / "images" / "charts"

# Crear carpeta si no existe
CHARTS_DIR.mkdir(parents=True, exist_ok=True)
print(f"Guardando gráficas en: {CHARTS_DIR}")

# ---------- Estilo compartido: acorde a la identidad negro/dorado/blanco del sitio ----------
# Fondo transparente para que la tarjeta del sitio se vea a través (funciona en claro y oscuro).
# El dorado se usa solo como acento sobre el dato relevante; el resto queda en un gris cálido neutro.
GOLD = "#b8922a"
NEUTRAL = "#a99a78"
TEXT = "#8a7a5a"
FIGSIZE = (6, 4)
DPI = 200

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.size": 10.5,
    "text.color": TEXT,
    "axes.edgecolor": TEXT,
    "axes.labelcolor": TEXT,
    "xtick.color": TEXT,
    "ytick.color": TEXT,
    "axes.titlesize": 13,
    "axes.titleweight": "bold",
    "axes.titlecolor": "#4a4030",
    "savefig.transparent": True,
})


def style_axes(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_alpha(.4)
    ax.spines["bottom"].set_alpha(.4)
    ax.tick_params(length=0)
    ax.yaxis.grid(True, color=TEXT, alpha=.18, linewidth=.7)
    ax.set_axisbelow(True)


# ---------- 1) CPL antes vs después ----------
data_cpl = {
    "mes": ["Ene", "Feb", "Mar", "Abr", "May", "Jun"],
    "cpl_antes":  [75, 72, 68, 62, 58, 55],
    "cpl_despues":[55, 52, 50, 48, 46, 45],
}
df_cpl = pd.DataFrame(data_cpl)

fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
ax.plot(df_cpl["mes"], df_cpl["cpl_antes"], marker="o", markersize=5,
        linewidth=2, linestyle="--", color=NEUTRAL, label="Antes")
ax.plot(df_cpl["mes"], df_cpl["cpl_despues"], marker="o", markersize=6,
        linewidth=2.4, color=GOLD, label="Después")
ax.set_title("Evolución del CPL por mes")
ax.set_xlabel("Mes")
ax.set_ylabel("CPL ($)")
ax.legend(frameon=False, loc="upper right")
style_axes(ax)
fig.tight_layout()

output1 = CHARTS_DIR / "cpl_evolucion.png"
fig.savefig(output1, bbox_inches="tight", pad_inches=.18)
plt.close(fig)
print(f"✔ Gráfica guardada: {output1.name}")

# ---------- 2) ROAS por campaña ----------
data_roas = {
    "campaña": ["Curso masaje", "Wellness spa", "Reel ofertas"],
    "roas":    [4.2, 2.1, 5.1],
}
df_roas = pd.DataFrame(data_roas)
colors_roas = [GOLD if v == df_roas["roas"].max() else NEUTRAL for v in df_roas["roas"]]

fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
bars = ax.bar(df_roas["campaña"], df_roas["roas"], color=colors_roas, width=.56)
ax.bar_label(bars, labels=[f"{v}x" for v in df_roas["roas"]], padding=4,
             color="#4a4030", fontsize=10, fontweight="bold")
ax.set_title("ROAS por campaña")
ax.set_ylabel("ROAS (veces)")
ax.set_ylim(0, max(df_roas["roas"]) * 1.22)
style_axes(ax)
fig.tight_layout()

output2 = CHARTS_DIR / "roas_campanas.png"
fig.savefig(output2, bbox_inches="tight", pad_inches=.18)
plt.close(fig)
print(f"✔ Gráfica guardada: {output2.name}")

# ---------- 3) CTR por dispositivo ----------
data_ctr = {
    "dispositivo": ["Móvil", "Escritorio"],
    "ctr":         [4.5, 2.3],
}
df_ctr = pd.DataFrame(data_ctr)
colors_ctr = [GOLD if v == df_ctr["ctr"].max() else NEUTRAL for v in df_ctr["ctr"]]

fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
bars = ax.bar(df_ctr["dispositivo"], df_ctr["ctr"], color=colors_ctr, width=.42)
ax.bar_label(bars, labels=[f"{v}%" for v in df_ctr["ctr"]], padding=4,
             color="#4a4030", fontsize=10, fontweight="bold")
ax.set_title("CTR por dispositivo")
ax.set_ylabel("CTR (%)")
ax.set_ylim(0, max(df_ctr["ctr"]) * 1.22)
style_axes(ax)
fig.tight_layout()

output3 = CHARTS_DIR / "ctr_dispositivos.png"
fig.savefig(output3, bbox_inches="tight", pad_inches=.18)
plt.close(fig)
print(f"✔ Gráfica guardada: {output3.name}")

print("\nListo: abre assets/images/charts/ y deberías ver las 3 imágenes .png")
