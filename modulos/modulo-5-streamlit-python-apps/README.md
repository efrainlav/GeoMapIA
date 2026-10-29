# 🚀 Módulo 5: Aplicaciones Web Analíticas con Python y Streamlit

- **Duración estimada:** 2.0 Horas
- **Modalidad:** Autodidacta (*Self-Paced*)
- **Entregables del módulo:**
  1. [`app_geoanalizador.py`](./app_geoanalizador.py) — Aplicación web completa en **Streamlit + PyDeck 3D + Plotly** donde cualquier usuario puede subir un archivo CSV o GeoJSON de muestreo agrícola/ambiental y analizarlo al instante.
  2. [`requirements.txt`](./requirements.txt) — Lista de dependencias lista para publicar gratis en **Streamlit Community Cloud**.

---

## 🎯 1. Objetivo de Aprendizaje
Aprender cuándo y cómo crear una **Web App en Python (Streamlit)** en lugar de un visor HTML/JS puro, permitiendo que usuarios finales carguen sus propias tablas de campo (CSV/Excel) y obtengan mapas 2D, extrusiones 3D con **PyDeck** y gráficos interactivos con **Plotly**.

---

## ⚖️ 2. ¿Cuándo usar HTML + Leaflet vs Python + Streamlit? (20 minutos)

| Criterio | Visor HTML + JS + Leaflet (Módulos 1, 2 y 4) | Web App Python + Streamlit (Módulo 5) |
| :--- | :--- | :--- |
| **Velocidad de carga** | ⚡ Instantánea (corre 100% en el navegador) | 🐢 Requiere servidor Python activo |
| **Alojamiento gratis** | **GitHub Pages** (ilimitado y ultrarrápido) | **Streamlit Community Cloud** |
| **Ideal para...** | Visores institucionales, portafolios, dashboards rápidos | Herramientas donde el usuario sube archivos para geoprocesar con `pandas`/`geopandas` |

---

## 💻 3. Cómo ejecutar tu App de Streamlit localmente (40 minutos)

1. Abre una terminal en la carpeta de este módulo (`modulos/modulo-5-streamlit-python-apps/`).
2. Instala las librerías (una sola vez):
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta la aplicación:
   ```bash
   streamlit run app_geoanalizador.py
   ```
4. Se abrirá automáticamente en `http://localhost:8501` cargando por defecto nuestro dataset de **20 lotes agrícolas de Colombia (`data/muestreo_agro_campo.csv`)**, o permitiéndote arrastrar tu propio archivo CSV con coordenadas.

---

## ✅ 4. Reto de Autoevaluación del Módulo 5

- [ ] Copia el contenido de [`app_geoanalizador.py`](./app_geoanalizador.py) en Claude o Gemini y pídele: *"Agrega en la barra lateral un filtro de rango (`st.slider`) por Altitud (`altitud_msnm`) para filtrar los cultivos de alta montaña vs llanura"*.

👉 **[Ir al Módulo 6: Git, GitHub y Despliegue Gratuito en la Nube](../modulo-6-github-despliegue/README.md)**

