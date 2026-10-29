"""
Módulo 5 — Curso GeoMapIA (SELPER Colombia)
Aplicación Web: GeoAnalizador Agrícola y Ambiental en Python (Streamlit + PyDeck 3D + Plotly)
Generada mediante el Prompt 5.1 del PROMPT_PLAYBOOK.md
"""

from pathlib import Path
import pandas as pd
import pydeck as pdk
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="GeoAnalizador SELPER — Streamlit + IA",
    page_icon="🛰️",
    layout="wide",
)

st.title("🛰️🌾 GeoAnalizador Agrícola y Ambiental SELPER Colombia")
st.caption("Módulo 5 del Curso GeoMapIA • Sube un archivo CSV con coordenadas o explora los lotes de muestreo por defecto.")

# 1. Carga de datos (por defecto o subidos por el usuario)
DEFAULT_CSV = Path(__file__).resolve().parents[2] / "data" / "muestreo_agro_campo.csv"

st.sidebar.header("📂 1. Fuente de Datos")
uploaded_file = st.sidebar.file_uploader("Sube tu CSV (con columnas latitud y longitud)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv(DEFAULT_CSV)

# Filtros en la barra lateral
st.sidebar.header("🎛️ 2. Filtros Territoriales")
regiones = ["Todas"] + sorted(df["region"].dropna().unique().tolist())
region_sel = st.sidebar.selectbox("Región Natural:", regiones)

cultivos = sorted(df["cultivo"].dropna().unique().tolist())
cultivos_sel = st.sidebar.multiselect("Cultivos:", cultivos, default=cultivos)

variable_3d = st.sidebar.selectbox(
    "Variable para altura de columnas 3D:",
    ["rendimiento_ton_ha", "altitud_msnm", "humedad_suelo_pct", "ndvi"],
)

# Aplicar filtros
df_f = df[df["cultivo"].isin(cultivos_sel)].copy()
if region_sel != "Todas":
    df_f = df_f[df_f["region"] == region_sel]

# 2. Fila de KPIs
c1, c2, c3, c4 = st.columns(4)
c1.metric("Lotes Monitoreados", len(df_f))
c2.metric("NDVI Promedio", f"{df_f['ndvi'].mean():.2f}" if len(df_f) else "0.00")
c3.metric("Humedad de Suelo Media", f"{df_f['humedad_suelo_pct'].mean():.1f}%" if len(df_f) else "0%")
c4.metric("Altitud Media (m s.n.m.)", f"{int(df_f['altitud_msnm'].mean())} m" if len(df_f) else "0 m")

# 3. Pestañas de Visualización
tab1, tab2, tab3 = st.tabs([
    "🧊 Mapa 3D de Columnas (PyDeck)",
    "🗺️ Mapa Satelital / 2D",
    "📈 Gráficos y Descarga CSV",
])

with tab1:
    st.subheader(f"Extrusión 3D por `{variable_3d}`")
    if len(df_f) > 0:
        df_f["elevation_scaled"] = df_f[variable_3d] * (50000 if variable_3d == "ndvi" else 1500)
        layer_3d = pdk.Layer(
            "ColumnLayer",
            data=df_f,
            get_position=["longitud", "latitud"],
            get_elevation="elevation_scaled",
            elevation_scale=1,
            radius=14000,
            get_fill_color="[16, 185, 129, 200]",
            pickable=True,
            auto_highlight=True,
        )
        view_state = pdk.ViewState(
            latitude=float(df_f["latitud"].mean()),
            longitude=float(df_f["longitud"].mean()),
            zoom=5.3,
            pitch=45,
        )
        st.pydeck_chart(
            pdk.Deck(
                layers=[layer_3d],
                initial_view_state=view_state,
                tooltip={"text": "{id_lote} - {municipio}\nCultivo: {cultivo}\nNDVI: {ndvi}\nRendimiento: {rendimiento_ton_ha} t/ha"},
            )
        )

with tab2:
    st.subheader("Distribución Espacial por Cultivo y Vigor Vegetal (NDVI)")
    if len(df_f) > 0:
        fig_map = px.scatter_mapbox(
            df_f,
            lat="latitud",
            lon="longitud",
            color="cultivo",
            size="ndvi",
            hover_name="municipio",
            hover_data=["departamento", "ndvi", "humedad_suelo_pct", "estado_fitosanitario"],
            zoom=5,
            height=520,
            mapbox_style="carto-darkmatter",
        )
        st.plotly_chart(fig_map, use_container_width=True)

with tab3:
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        fig_bar = px.bar(
            df_f,
            x="cultivo",
            y="ndvi",
            color="estado_fitosanitario",
            barmode="group",
            title="NDVI por Cultivo y Estado Fitosanitario",
        )
        st.plotly_chart(fig_bar, use_container_width=True)
    with col_g2:
        fig_scat = px.scatter(
            df_f,
            x="humedad_suelo_pct",
            y="ndvi",
            color="region",
            size="rendimiento_ton_ha",
            hover_name="municipio",
            title="Relación Humedad del Suelo vs Índice NDVI",
        )
        st.plotly_chart(fig_scat, use_container_width=True)

    st.dataframe(df_f, use_container_width=True)
    st.download_button(
        "⬇️ Descargar Datos Filtrados (CSV)",
        data=df_f.to_csv(index=False).encode("utf-8"),
        file_name="muestreo_agro_filtrado_selper.csv",
        mime="text/csv",
    )
