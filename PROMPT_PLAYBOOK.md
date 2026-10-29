# 🤖 Manual Maestro de Prompts Geoespaciales (`PROMPT_PLAYBOOK.md`)

Este recetario contiene las **plantillas oficiales de Prompts del curso GeoMapIA (SELPER Colombia)**. Todas están diseñadas bajo el **Framework C-T-D-E** (**C**ontexto, **T**ecnología, **D**atos, **E**stilo/Comportamiento) para que obtengas código funcional al primer intento en **Claude**, **Gemini** o **ChatGPT**.

> 💡 **Cómo usar este manual:** Copia el bloque de texto del prompt que necesites, reemplaza los textos entre corchetes `[COMO ESTE]` con tus propios datos o déjalos tal cual para practicar, y pégalo en tu IA favorita.

---

## 🧩 La Fórmula C-T-D-E para Geomática

Antes de pedirle cualquier visor o script a la IA, asegúrate de incluir estos 4 bloques:
1. **[C] Contexto y Rol:** *"Actúa como un desarrollador WebGIS Senior especialista en Percepción Remota y Sistemas de Información Geográfica..."*
2. **[T] Tecnología:** *"Crea un único archivo `index.html` autocontenido usando HTML5, Tailwind CSS (vía CDN) y Leaflet.js v1.9.4..."*
3. **[D] Datos y Sistema de Referencia:** *"Usa coordenadas en EPSG:4326 (WGS84). Mis datos tienen las siguientes columnas/propiedades: `id`, `municipio`, `ndvi_medio`, `alerta`..."*
4. **[E] Estilo y Comportamiento:** *"El mapa debe ocupar el 100% de la pantalla, tener popups con tabla limpia, leyenda en la esquina inferior derecha y control de capas..."*

---

## 🟢 MÓDULO 1: Prompts Iniciales para tu Primer Visor

### Prompt 1.1 — Mi primer visor interactivo en un solo archivo HTML
```text
[C] Actúa como un desarrollador WebGIS Senior de SELPER Colombia.
[T] Crea un archivo HTML único y autocontenido (incluyendo CSS y JavaScript en el mismo archivo) utilizando Leaflet 1.9.4 y Tailwind CSS vía CDN.
[D] Centra el mapa en Colombia (latitud 4.6097, longitud -74.0817, zoom 6). Incluye un arreglo en JavaScript con 8 estaciones de monitoreo ambiental distribuidas en distintas regiones de Colombia (Andina, Caribe, Pacífico, Amazonía, Orinoquía), cada una con: nombre, departamento, tipo ("Climática", "Hidrológica", "Satelital NDVI"), valor_ndvi (entre 0.2 y 0.85), alerta ("Baja", "Media", "Alta") y coordenadas [lat, lon] en EPSG:4326.
[E] Requisitos visuales:
1. Cabecera superior moderna con título "Visor de Monitoreo Ambiental SELPER" y contador total de estaciones.
2. Control de capas base con 3 opciones: OpenStreetMap, CartoDB Dark Matter (modo oscuro) y Esri World Imagery (Satélite).
3. Marcadores circulares (L.circleMarker) coloreados según el nivel de alerta (Verde = Baja, Naranja = Media, Rojo = Alta).
4. Al hacer clic en cada estación, muestra un popup estilizado con todos sus datos.
5. Agrega control de escala métrica y una leyenda flotante en la esquina inferior derecha.
Entrégame el código completo listo para guardar como visor.html y abrir en el navegador.
```

### Prompt 1.2 — Agregar geolocalización GPS y botón de vista inicial
```text
Sobre el código anterior de Leaflet, agrega dos botones flotantes personalizados en la esquina superior izquierda (debajo de los botones de zoom):
1. Un botón "🏠 Vista Colombia" que regrese el mapa suavemente (flyTo) al centro de Colombia (lat 4.6097, lon -74.0817, zoom 6).
2. Un botón "📍 Mi Ubicación" que use la API de geolocalización del navegador (map.locate), coloque un marcador azul con un círculo de precisión donde se encuentre el usuario y haga zoom a esa posición. Si el usuario rechaza el permiso, muestra una alerta amigable.
```

---

## 🔵 MÓDULO 2: Prompts para Leaflet Avanzado, Catastro, Coropletas y WMS

### Prompt 2.1 — Conectar servicios WMS oficiales y control de opacidad
```text
Actúa como especialista en estándares OGC y Leaflet. Necesito agregar a mi visor Leaflet una capa WMS externa y un control deslizante (slider) de opacidad.
1. Usa `L.tileLayer.wms` para conectar un servicio WMS (deja configurado como ejemplo el mosaico satelital/ambiental de NASA GIBS o una URL WMS parametrizable para IGAC/IDEAM, con `format: 'image/png'`, `transparent: true`).
2. Crea un panel flotante en la esquina superior derecha que permita encender/apagar la capa WMS y tenga un `<input type="range" min="0" max="1" step="0.05" value="0.7">` que actualice en tiempo real la opacidad (`wmsLayer.setOpacity(valor)`).
```

### Prompt 2.2 — Mapa Coroplético (Polígonos coloreados por variable) + Efecto Hover
```text
Tengo una capa GeoJSON de municipios/zonas con las siguientes propiedades en `feature.properties`:
- `nombre`: texto
- `departamento`: texto
- `deforestacion_ha`: número (entre 10 y 2500)
- `avaluo_promedio_m2`: número
- `riesgo`: texto ("Bajo", "Medio", "Alto")

Escribe el código en Leaflet para:
1. Crear una función `getColor(d)` que asigne una rampa de 5 colores (de amarillo claro a rojo oscuro) según el valor de `deforestacion_ha`.
2. Aplicar ese estilo con `L.geoJSON(datos, { style: ... })`.
3. Agregar eventos `mouseover` y `mouseout` para que al pasar el mouse sobre un polígono su borde se vuelva blanco y grueso, y muestre en un cuadro informativo flotante los datos de ese municipio.
4. Al hacer clic en un polígono, hacer zoom a sus límites (`map.fitBounds(e.target.getBounds())`).
5. Generar la leyenda dinámica correspondiente a los rangos de colores.
```

### Prompt 2.3 — Agrupación de miles de puntos con `Leaflet.markercluster` y filtro por atributo
```text
Modifica mi visor Leaflet para manejar cientos o miles de puntos usando el plugin `Leaflet.markercluster` (incluye sus CDNs oficiales de CSS y JS).
Además, agrega en una barra lateral izquierda un menú desplegable (`<select>`) para filtrar los puntos por la propiedad `alerta` ("Todas", "Alta", "Media", "Baja") y un buscador de texto por `nombre`. Cuando el usuario cambie el filtro, actualiza el grupo de clusters sin recargar la página.
```

---

## 🟡 MÓDULO 3: Prompts para Python Geoespacial (GeoPandas, Folium y Leafmap)

### Prompt 3.1 — Reproyección de MAGNA-SIRGAS (`EPSG:9377`) a Web (`EPSG:4326`) y simplificación
```text
Actúa como un analista SIG experto en Python y GeoPandas.
Tengo un archivo Shapefile o GeoPackage en el sistema de referencia oficial de Colombia MAGNA-SIRGAS Origen Nacional (EPSG:9377) que pesa demasiado para un visor web.
Escríbeme un script en Python comentando cada paso que:
1. Lea el archivo espacial con `geopandas.read_file()`.
2. Verifique su CRS actual y lo reproyecte a WGS84 geográfico (`EPSG:4326`).
3. Simplifique la geometría con `.simplify(tolerance=0.001, preserve_topology=True)` para reducir el tamaño del archivo sin perder forma visual.
4. Seleccione solo las columnas útiles, redondee las coordenadas a 5 decimales y lo exporte a un archivo `.geojson` ligero listo para Leaflet.
```

### Prompt 3.2 — Comparador Satelital Multitemporal (Split-Map / Cortina) en Python o HTML
```text
Quiero crear un comparador satelital de cortina deslizante (Split-Screen Antes/Después o RGB vs Terreno/Índice) para analizar cambios en la cobertura terrestre en Colombia.
Opción A: Dame un script en Python usando `folium` (con `DualMap` o plugin `SideBySideLayers`) que exporte un archivo HTML autónomo.
Opción B: Dame un archivo HTML directo con Leaflet y `leaflet-side-by-side` que compare dos capas satelitales/temáticas (por ejemplo, Esri World Imagery a la izquierda y OpenTopoMap + capa de focos de calor a la derecha) con una barra divisoria arrastrable en el centro.
```

---

## 🟣 MÓDULO 4: Prompts para Dashboards Geográficos (Leaflet + Chart.js + Turf.js)

### Prompt 4.1 — Dashboard completo sincronizado (Mapa + 4 KPIs + Gráficos Chart.js)
```text
[C] Actúa como Arquitecto de Dashboards Geoespaciales Senior.
[T] Crea un Dashboard en un solo archivo HTML usando Tailwind CSS, Leaflet.js y Chart.js (todos por CDN).
[D] Usa un conjunto de datos GeoJSON embebido de 15 estaciones/zonas de Colombia con las propiedades: `nombre`, `region` ("Andina", "Caribe", "Amazonía", "Pacífico", "Orinoquía"), `precipitacion_mm`, `ndvi`, `area_afectada_ha` y `nivel_riesgo` ("Bajo", "Medio", "Alto", "Crítico").
[E] Estructura la pantalla tipo Centro de Control (100vh sin scroll general):
1. Barra lateral izquierda con filtros por `region`, `nivel_riesgo` y un slider de `precipitacion_mm` mínima.
2. Fila superior con 4 tarjetas KPI que se recalculen dinámicamente según los elementos filtrados: Total Zonas, Precipitación Media (mm), NDVI Promedio y Hectáreas Afectadas Totales.
3. Panel central con el mapa Leaflet interactivo.
4. Panel derecho con 2 gráficos de Chart.js (un gráfico de barras de Hectáreas por Región y un gráfico de dona de distribución por Nivel de Riesgo).
5. Sincronización total: Al cambiar cualquier filtro, deben actualizarse al mismo tiempo el mapa, los 4 KPIs y los 2 gráficos de Chart.js. Incluye un botón para descargar los datos filtrados en formato CSV.
```

### Prompt 4.2 — Análisis Espacial en el Navegador con `Turf.js` (Radio de Afectación / Buffer)
```text
Quiero agregar análisis espacial en tiempo real a mi visor Leaflet usando la librería `Turf.js` (vía CDN).
Haz que cuando el usuario active el modo "Analizar Radio de Impacto" y haga clic en cualquier punto del mapa:
1. Se tome un radio en kilómetros desde un input numérico (por ejemplo, 50 km).
2. Se genere un polígono circular exacto con `turf.buffer(punto, radio, {units: 'kilometers'})` y se dibuje en el mapa en color cian semitransparente.
3. Se evalúe con `turf.pointsWithinPolygon` cuántas estaciones/puntos de mi capa caen dentro de ese radio de impacto y se muestre el resumen estadístico en pantalla.
```

---

## 🟠 MÓDULO 5: Prompts para Aplicaciones Web en Python con Streamlit

### Prompt 5.1 — Aplicación Geo-Analítica en Streamlit con carga de archivos y Mapa 3D
```text
Actúa como desarrollador experto en Python Geoespacial y Streamlit.
Crea un archivo `app_geoanalizador.py` y su respectivo `requirements.txt` para una aplicación web llamada "GeoAnalizador SELPER".
Funcionalidades requeridas:
1. Si el usuario no sube ningún archivo, carga automáticamente un dataset de ejemplo de muestreo agrícola/ambiental de Colombia (`latitud`, `longitud`, `cultivo`, `ndvi`, `humedad_suelo`, `altitud_msnm`, `rendimiento_ton_ha`).
2. Permite en la barra lateral (`st.sidebar`) subir un archivo propio en formato CSV o GeoJSON (`st.file_uploader`), elegir la columna para colorear y filtrar por categorías.
3. Muestra en la parte superior 4 métricas (`st.metric`).
4. Crea 3 pestañas (`st.tabs`):
   - Pestaña 1 ("🗺️ Visor 2D Interactivo"): Mapa Folium o PyDeck 2D coloreado por la variable seleccionada.
   - Pestaña 2 ("🧊 Densidad y Extrusión 3D"): Mapa 3D con `pydeck` (`HexagonLayer` o `ColumnLayer`) mostrando la altura de las columnas según la variable numérica elegida.
   - Pestaña 3 ("📈 Estadísticas y Descarga"): Gráfico interactivo con `plotly.express` y tabla con botón de descarga CSV.
```

---

## 🔴 MÓDULO 6: Prompts para Depuración de Errores y Despliegue en GitHub

### Prompt 6.1 — Reparar un mapa que sale en blanco o con error en Consola (`F12`)
```text
Mi visor web con Leaflet no se visualiza correctamente (el mapa sale gris/en blanco o no cargan los datos).
Abajo te pego:
1. El error exacto que me aparece en la pestaña "Console" de las herramientas de desarrollador del navegador (F12).
2. Mi código actual.

Error en consola:
[PEGA AQUÍ EL ERROR ROJO DE LA CONSOLA]

Código actual:
[PEGA AQUÍ TU CÓDIGO]

Explícame brevemente en español por qué ocurrió el error y entrégame el bloque de código corregido.
```

### Prompt 6.2 — Generar un `README.md` profesional para mi repositorio de GitHub
```text
Actúa como especialista en documentación de proyectos Open Source geoespaciales.
Acabo de crear un visor geográfico llamado "[NOMBRE DE TU PROYECTO]" para "[PROPÓSITO: ej. Monitoreo de Deforestación / Catastro / Gestión del Riesgo]".
Usa las tecnologías: HTML5, Leaflet.js, Chart.js y datos en formato GeoJSON.
Redáctame un archivo `README.md` atractivo con emojis, insignias (badges), descripción del proyecto, capturas de pantalla (deja los enlaces de marcador de posición), lista de funcionalidades, tecnologías usadas, cómo ejecutarlo localmente y créditos para la comunidad SELPER Colombia.
```

