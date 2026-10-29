# 🐍 Módulo 3: Automatización y Preparación de Datos Geoespaciales con Python + IA

- **Duración estimada:** 2.5 Horas
- **Modalidad:** Autodidacta (*Self-Paced*)
- **Entregables del módulo:**
  1. [`procesamiento_y_mapas.py`](./procesamiento_y_mapas.py) — Script en Python generado con IA para limpiar CSVs, reproyectar de **MAGNA-SIRGAS (`EPSG:9377`)** a **WGS84 (`EPSG:4326`)**, simplificar geometrías y exportar mapas en **Folium**.
  2. [`comparador-satelital-split.html`](./comparador-satelital-split.html) — Comparador Satelital Multitemporal (*Split-Map* de cortina deslizante + Mapa de Calor de focos térmicos FIRMS).

---

## 🎯 1. Objetivo de Aprendizaje
Utilizar Python asistido por IA (en **Google Colab** o en tu computador) para resolver los cuellos de botella de datos antes de llevarlos a la web:
1. Limpiar bases de datos en Excel/CSV y convertirlas en capas `GeoJSON` listas para Leaflet.
2. Transformar coordenadas del sistema oficial de Colombia **MAGNA-SIRGAS Origen Nacional (`EPSG:9377`)** al estándar web **WGS84 (`EPSG:4326`)** y reducir el peso de Shapefiles pesados.
3. Generar **Mapas de Cortina (*Split-Map*)** y **Mapas de Calor (*Heatmaps*)** para estudios de Percepción Remota y Monitoreo Ambiental.

---

## 🔄 2. El Problema #1 en Colombia: `EPSG:9377` vs `EPSG:4326` (45 minutos)

Cuando descargas un Shapefile oficial del **IGAC, IDEAM, ANLA o DANE**, suele venir en coordenadas planas proyectadas en metros (**MAGNA-SIRGAS Origen Nacional `EPSG:9377`** o `EPSG:3116`). Si intentas cargarlo directamente en un visor web, no se verá en Colombia.

### Cómo pedirle a la IA el script de conversión y optimización:
Usa el **Prompt 3.1** de nuestro [`PROMPT_PLAYBOOK.md`](../../PROMPT_PLAYBOOK.md). La IA generará un flujo con `geopandas` que ejecuta 3 líneas mágicas:
```python
gdf = gpd.read_file("capa_igac_9377.shp")
gdf_web = gdf.to_crs(epsg=4326)  # Reproyecta a Lat/Lon WGS84
gdf_web["geometry"] = gdf_web["geometry"].simplify(0.001, preserve_topology=True)
gdf_web.to_file("capa_optimizada_web.geojson", driver="GeoJSON")
```

---

## 🛰️ 3. Comparadores Satelitales (*Split-Screen*) y Mapas de Calor (45 minutos)

En **SELPER**, una de las visualizaciones más potentes para teledetección es el **Comparador de Cortina (*Split-Map*)**, que permite deslizar una barra vertical para comparar dos capas sobre la misma zona (por ejemplo, **Imagen Satelital Óptica RGB** a la izquierda vs **Topografía / Índices / Focos de Deforestación** a la derecha).

1. Revisa el script [`procesamiento_y_mapas.py`](./procesamiento_y_mapas.py) para ver cómo se automatiza desde Python.
2. Abre en tu navegador [`comparador-satelital-split.html`](./comparador-satelital-split.html) y arrastra la barra divisoria central de izquierda a derecha sobre la Amazonía colombiana (Chiribiquete / Guaviare / Caquetá) o cambia de zona con los botones de navegación rápida.

---

## ✅ 4. Reto de Autoevaluación del Módulo 3

- [ ] Abre [`comparador-satelital-split.html`](./comparador-satelital-split.html) y prueba los botones de salto rápido entre **Guaviare/Chiribiquete**, **Ciénaga Grande de Santa Marta** y **Páramo de Chingaza**.
- [ ] Pídele a Claude o Gemini usando el **Prompt 3.2** que cambie una de las capas del comparador por una capa WMS de tu entidad o por un mapa de relieve sombreado (*Hillshade*).

👉 **[Ir al Módulo 4: Construcción de Dashboards Geográficos (Mapa + Gráficos + Filtros)](../modulo-4-dashboards-geograficos/README.md)**
