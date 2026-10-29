# 🗺️ Módulo 2: Creación de Visores Interactivos con HTML, JavaScript y Leaflet

- **Duración estimada:** 2.5 Horas
- **Modalidad:** Autodidacta (*Self-Paced*)
- **Entregable del módulo:** [`visor-catastral-ambiental.html`](./visor-catastral-ambiental.html) (Visor multipropósito con polígonos coropléticos de deforestación/avalúo catastral, servicios WMS/Satelitales con control de transparencia, agrupación de puntos con *MarkerCluster* y buscador).

---

## 🎯 1. Objetivo de Aprendizaje
Dominar la construcción de visores geográficos completos usando **Leaflet.js** guiando a la IA para:
1. Integrar servicios **WMS/WMTS** y capas satelitales con control deslizante (*slider*) de opacidad.
2. Crear **mapas coropléticos** (polígonos coloreados automáticamente según hectáreas deforestadas, avalúo catastral por hectárea o NDVI) con efectos interactivos al pasar el cursor (*hover*).
3. Implementar agrupación automática de puntos masivos con **`Leaflet.markercluster`** y paneles laterales de filtrado.

---

## 🛰️ 2. Integración de Servicios WMS y Capas Satelitales con IA (35 minutos)

En Colombia y Latinoamérica, las instituciones oficiales (IGAC, IDEAM, SIAC, Servicio Geológico Colombiano, NASA GIBS) publican su cartografía mediante el estándar **WMS (Web Map Service)**.

### ¿Qué debes especificarle siempre a la IA cuando pides una capa WMS?
1. La **URL base** del servicio WMS.
2. El nombre exacto de la capa (`layers: '...'`).
3. El formato con transparencia (`format: 'image/png'`, `transparent: true`).
4. Un control deslizante (`<input type="range">`) conectado a `capaWMS.setOpacity(valor)`.

> 💡 **Prueba el Prompt 2.1** de nuestro [`PROMPT_PLAYBOOK.md`](../../PROMPT_PLAYBOOK.md) para ver cómo Claude o Gemini generan el control de opacidad perfecto.

---

## 🎨 3. Polígonos GeoJSON, Mapas Coropléticos e Interactividad (50 minutos)

Un visor profesional no solo muestra polígonos de un mismo color, sino que **permite cambiar en vivo la variable temática** (por ejemplo, alternar entre *Deforestación (ha)*, *Avalúo Catastral (Millones COP/ha)* e *Índice Vegetacional NDVI*).

### Cómo pedirle una Coropleta Dinámica a la IA:
Pídele a la IA que programe 3 funciones conectadas en `L.geoJSON`:
1. `style(feature)`: Asigna el `fillColor` dependiendo del atributo que el usuario haya elegido en un selector `<select>`.
2. `onEachFeature(feature, layer)`: Configura los eventos `mouseover` (resaltar borde blanco y actualizar el panel de inspección flotante) y `click` (`map.fitBounds(layer.getBounds())` para hacer zoom automático al municipio o predio).
3. `actualizarLeyenda(variable)`: Actualiza automáticamente los colores y rangos de la leyenda en la esquina inferior derecha.

---

## 📍 4. Agrupación de Puntos (*Marker Clustering*) (30 minutos)

Si cargas más de 200 puntos individuales (como focos de calor FIRMS o predios urbanos), el mapa se satura visualmente. La solución estándar es el plugin **`Leaflet.markercluster`**.

- **Prompt clave:** *"Incluye por CDN `Leaflet.markercluster` y envuelve mis puntos dentro de `L.markerClusterGroup()` para que se agrupen en círculos numerados al alejar el zoom."*

---

## 🛠️ 5. Proyecto Práctico del Módulo 2 (35 minutos)

1. Abre el archivo [`visor-catastral-ambiental.html`](./visor-catastral-ambiental.html) en tu navegador.
2. En la barra lateral izquierda:
   - Cambia la **Variable Coroplética de Polígonos** entre *Deforestación (ha)*, *Avalúo Catastral (M$/ha)* e *Índice NDVI Promedio* y observa cómo cambian los colores del mapa y la leyenda.
   - Mueve el deslizador de **Opacidad de Capa Satelital / Relieve WMS** para superponer la información.
   - Usa el **Buscador por Municipio o Uso del Suelo** y haz clic en cualquier zona para hacer zoom automático.

---

## ✅ 6. Reto de Autoevaluación del Módulo 2

- [ ] Copia el código de [`visor-catastral-ambiental.html`](./visor-catastral-ambiental.html), pégalo en Claude o Gemini y pídele: *"Agrega una cuarta opción en el selector de variable coroplética que coloree los municipios según `riesgo_inundacion` (Crítico = Rojo, Alto = Naranja, Medio = Amarillo, Bajo = Verde)"*.
- [ ] Verifica que la leyenda cambie automáticamente cuando seleccionas esa cuarta opción.

👉 **[Ir al Módulo 3: Automatización y Preparación de Datos Geoespaciales con Python + IA](../modulo-3-python-geodatos/README.md)**
