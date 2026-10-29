# 🚑 Guía de Supervivencia Autodidacta: Solución a los 6 Errores más Comunes en Mapas Web

Cuando programas visores con ayuda de IA (Claude, Gemini, ChatGPT), el **95% de los problemas** se debe a uno de los siguientes 6 casos. Aquí tienes cómo identificarlos y qué decirle a la IA para repararlos en 30 segundos.

---

## 1. ⬜ "El mapa no se ve o aparece como un recuadro gris/en blanco"
- **Causa:** El contenedor `<div id="map"></div>` no tiene una altura (`height`) definida en CSS, o el archivo de estilos `leaflet.css` no se cargó antes del script.
- **Cómo pedirle a la IA que lo arregle:**
  > *"Mi div `#map` sale en blanco o con altura 0. Asegúrate de incluir el `<link>` oficial de `leaflet.css` en el `<head>` y de asignarle una altura explícita en CSS (por ejemplo `height: 100vh;` o `height: 600px;`) y agrega `setTimeout(() => map.invalidateSize(), 200)`."*

---

## 2. 🌊 "Mis puntos o polígonos de Colombia aparecen en la Antártida o en el Océano Índico"
- **Causa 1 (Coordenadas invertidas):** **Leaflet** usa `[Latitud, Longitud]` (ej. `[4.609, -74.081]`), mientras que el estándar **GeoJSON** usa `[Longitud, Latitud]` (ej. `[-74.081, 4.609]`).
- **Causa 2 (Sistema de coordenadas proyectado):** Tus datos están en metros (`MAGNA-SIRGAS Origen Nacional EPSG:9377` o `EPSG:3116` con valores como `4885000, 2065000`) en lugar de grados geográficos (`EPSG:4326`).
- **Cómo pedirle a la IA que lo arregle:**
  > *"Mis datos de Colombia aparecen desplazados en otro continente. Verifica si las coordenadas están invertidas `[lon, lat]` vs `[lat, lon]` o si están en MAGNA-SIRGAS (`EPSG:9377`), y dame el código para transformarlas a `EPSG:4326`."*

---

## 3. 🚫 Error en consola: `Access to fetch at 'file:///...' from origin 'null' has been blocked by CORS policy`
- **Causa:** Abriste el archivo `index.html` haciendo **doble clic** desde tu carpeta, y el navegador bloquea por seguridad la lectura de archivos externos (`.geojson` o `.csv`) cuando usas el protocolo `file://`.
- **Solución en 10 segundos (Elige una):**
  1. **En VS Code:** Haz clic derecho sobre tu archivo `.html` y selecciona **"Open with Live Server"**.
  2. **Con Python en terminal:** Ejecuta `python3 -m http.server 8000` en la carpeta del proyecto y abre `http://localhost:8000` en el navegador.
  3. **Con la IA (Sin servidor):** Pídele a la IA: *"Incrusta el contenido del GeoJSON directamente como una variable `const datosGeoJSON = {...}` dentro del mismo archivo HTML/JS para que funcione al abrirlo con doble clic."*

---

## 4. 🐢 "El navegador se congela o tarda mucho al cargar mi GeoJSON / Shapefile"
- **Causa:** Estás intentando cargar en el navegador un archivo `.geojson` de más de 15–50 MB exportado directamente desde QGIS o ArcGIS con exceso de vértices y 15 decimales por coordenada.
- **Solución:**
  1. Usa el **script de Python del Módulo 3** (`geopandas` + `.simplify(0.001)`) para reducir el peso en un 90%.
  2. Si son muchos puntos (más de 1,000), pídele a la IA: *"Activa `preferCanvas: true` en las opciones de `L.map` y agrupa los puntos con `Leaflet.markercluster`."*

---

## 5. 🔗 "En mi computadora funciona perfecto, pero al subirlo a GitHub Pages no cargan las capas"
- **Causa:** Rutas con mayúsculas/minúsculas distintas (GitHub Pages distingue entre `Datos.geojson` y `datos.geojson`) o rutas absolutas que empiezan con `/` en lugar de `./`.
- **Cómo pedirle a la IA que lo arregle:**
  > *"Voy a publicar este visor en GitHub Pages dentro de una subcarpeta. Cambia todas las rutas de carga de datos (`fetch`) para que sean rutas relativas que empiecen por `./` y verifica que los CDN usen `https://`."*

---

## 6. 🔍 Cómo usar la Consola del Navegador (`F12`) como un Experto
1. Con tu visor abierto en Google Chrome, Edge o Firefox, presiona la tecla **`F12`** (o clic derecho $\rightarrow$ **Inspeccionar**).
2. Haz clic en la pestaña **Console (Consola)**.
3. Si hay una línea en **color rojo**, cópiala completa y pégala en Claude o Gemini usando el **Prompt 6.1** de nuestro [`PROMPT_PLAYBOOK.md`](./PROMPT_PLAYBOOK.md).
