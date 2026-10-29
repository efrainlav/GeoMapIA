# 🛰️🗺️ Curso Autodidacta SELPER: Creación de Visores Geográficos, Mapas Web y Dashboards con IA

> **Ficha Técnica — Programa de Formación Continua SELPER Colombia**
> - **Organiza / Dirigido a:** Comunidad de la **Sociedad Latinoamericana en Percepción Remota y Sistemas de Información Espacial (SELPER Colombia — [selper.org.co](https://selper.org.co/))**
> - **Duración total:** 14 horas (rango de dedicación: 10–16 horas)
> - **Modalidad:** *Self-paced* (100% Autodidacta, guiado paso a paso con plantillas de *prompts* y proyectos reproducibles)
> - **Enfoque:** *AI-First Geospatial Development* (Aprender a programar, integrar capas SIG/Teledetección, depurar y desplegar conversando con Claude, Gemini, ChatGPT o editores con IA)
> - **Perfil del participante:** Profesionales, investigadores, técnicos y estudiantes de SIG, Percepción Remota, Ciencias Ambientales, Ingeniería Catastral/Geodesia, Geografía y afines (sin requisito previo de programación web).

---

## 🎯 Objetivo General
Capacitar a los miembros y participantes de **SELPER** para **diseñar, desarrollar y desplegar en internet visores geográficos interactivos, comparadores satelitales y dashboards de análisis territorial** sin necesidad de escribir código desde cero de forma tradicional, dominando la ingeniería de *prompts* con **JavaScript (Leaflet / Chart.js / Turf.js)**, **Python (GeoPandas / Folium / Leafmap / Streamlit)** y **GitHub**.

---

## 🌎 Casos de Estudio Multisectoriales (Aplicados al Contexto Colombiano y Latinoamericano)
A lo largo del curso, el estudiante construirá herramientas combinando **4 ejes temáticos clave para SELPER**:
1. **🌳 Caso 1 — Monitoreo Ambiental y Percepción Remota:** Visor de focos de calor/deforestación y comparador multitemporal de imágenes satelitales / índices espectrales (NDVI/NDWI mediante servicios WMS/XYZ/COG).
2. **🏘️ Caso 2 — Catastro Multipropósito y Ordenamiento Territorial:** Visor interactivo de predios, estratificación, avalúos y uso del suelo urbano/rural.
3. **⚠️ Caso 3 — Gestión del Riesgo de Desastres:** Dashboard de monitoreo hidrometeorológico, susceptibilidad a deslizamientos/inundaciones e infraestructura crítica expuesta.
4. **🌾 Caso 4 — Agricultura y Recursos Hídricos:** Aplicativo en Python para carga de muestras de campo (CSV/GeoJSON), zonificación productiva y estadísticas por cuenca o municipio (datos DANE / IGAC / IDEAM).

---

## 📚 Contenido Detallado por Módulos (14 Horas)

### Módulo 1: Mentalidad *AI-First*, Entorno de Trabajo e Ingeniería de Prompts para SIG y Teledetección (2 Horas)
**Objetivo:** Configurar el entorno de trabajo gratuito y dominar la estructura exacta de un *prompt* para que Claude o Gemini generen código cartográfico limpio y sin errores.

1. **1.1. La revolución de la IA Generativa en la Geomática (30 min)**
   - Comparativa práctica para geomáticos: **Claude** (Artifacts para previsualizar mapas al instante), **Gemini** (gran ventana de contexto para leer GeoJSON/metadatos largos) y **ChatGPT**.
   - Configuración rápida del entorno: VS Code, extensión *Live Server*, Python y uso de la consola del navegador (`F12`) para detectar errores.
2. **1.2. Anatomía de un Visor Geográfico Web (30 min)**
   - Cómo se conectan **HTML** (estructura), **CSS** (diseño full-screen), **JavaScript** (interactividad en el navegador) y **Python** (geoprocesamiento).
   - Estándares espaciales web que debes indicarle a la IA: **GeoJSON**, **WMS / WMTS** (servicios del IGAC, IDEAM, SIAC), **Tiles XYZ** y **COG (Cloud Optimized GeoTIFF)**.
3. **1.3. Metodología de Prompting Geoespacial: El Framework *C-T-D-E* (40 min)**
   - **C**ontexto (rol: *Desarrollador WebGIS y Especialista en Percepción Remota*).
   - **T**ecnología (Leaflet 1.9+, Tailwind/Bootstrap, archivo único vs modular).
   - **D**atos (estructura de atributos, sistema de referencia `EPSG:4326` vs `MAGNA-SIRGAS / EPSG:9377`).
   - **E**stilo y Comportamiento (simbología, popups, leyendas, controles).
   - Técnica de *Debugging Asistido*: cómo copiar un error de consola y hacer que la IA lo repare en un paso.
4. **🛠️ Práctica Guiada 1 — Primer Visor SELPER (20 min):**
   - Crear mediante un único *prompt* un visor de estaciones de monitoreo en Colombia con cambio de mapa base (Satélite Esri / Topográfico / Modo Oscuro).

---

### Módulo 2: Creación de Visores Interactivos con HTML, JavaScript y Leaflet (2.5 Horas)
**Objetivo:** Construir visores cartográficos ligeros y personalizables usando **Leaflet.js**, incorporando capas vectoriales, satelitales y herramientas de consulta.

1. **2.1. Mapas Base, Servicios WMS Oficiales y Capas Satelitales (35 min)**
   - Prompts para configurar selectores de capas (`L.control.layers`).
   - Cómo pedirle a la IA que conecte servicios **WMS/WMTS** (ej. Ortofotos IGAC, capas ambientales o NASA GIBS / Sentinel Hub) y controle su opacidad con un deslizador (*slider*).
2. **2.2. Puntos Masivos, Clustering y Popups Enriquecidos (40 min)**
   - Simbología dinámica por categoría (ej. nivel de alerta roja/naranja/amarilla en estaciones IDEAM o focos de incendio FIRMS).
   - Implementación con IA de `Leaflet.markercluster` para visualizar miles de registros sin congelar el navegador.
   - Popups y paneles laterales con fichas técnicas, fotografías e hipervínculos.
3. **2.3. Polígonos, Mapas Coropléticos y Leyendas Dinámicas (45 min)**
   - Carga de GeoJSON de municipios, departamentos, cuencas hidrográficas o predios catastrales.
   - Prompts para clasificar rangos numéricos (coloración automática por hectáreas deforestadas, avalúo catastral o índice de vulnerabilidad).
   - Interactividad avanzada: resaltado al pasar el cursor (*hover*), zoom al polígono seleccionado y leyenda flotante profesional.
4. **🛠️ Proyecto del Módulo 2 — Caso Catastro y Ordenamiento Territorial (30 min):**
   - **Visor Catastral y de Uso del Suelo:** Mapa interactivo con consulta predial/municipal, filtro por uso del suelo, capa WMS de referencia con control de transparencia y buscador geográfico.

---

### Módulo 3: Automatización y Preparación de Datos Geoespaciales con Python + IA (2.5 Horas)
**Objetivo:** Utilizar Python (generado con IA) para transformar insumos crudos de SIG/Teledetección (Shapefiles, Excel, GeoTIFF) en datos optimizados para la web y reportes HTML.

1. **3.1. Geoprocesamiento en Python sin saber programar (35 min)**
   - Trabajo en la nube con **Google Colab** y en local.
   - Cómo darle a la IA la estructura de un Excel o Shapefile para que genere scripts con `pandas` y `geopandas` (cruces espaciales `sjoin`, cálculo de áreas y limpieza de atributos).
2. **3.2. Reproyección (MAGNA-SIRGAS a WGS84) y Optimización Web (45 min)**
   - Solución con IA al problema clásico: convertir de `EPSG:9377` (Origen Nacional Colombia) o UTM a `EPSG:4326` para que funcione en Leaflet.
   - Simplificación topológica con Python para reducir un Shapefile de 80 MB a un GeoJSON de 2 MB listo para la web.
3. **3.3. Visores Rápidos y Comparadores Satelitales desde Python (`Folium` y `Leafmap`) (30 min)**
   - Prompts para generar mapas en **Folium** y **Leafmap** exportables a `.html`.
   - Creación de un **Split-Map (Mapa de Cortina / Antes y Después)** para comparar imágenes satelitales o índices espectrales (ej. NDVI pre y post evento climático o avance urbano).
4. **🛠️ Proyecto del Módulo 3 — Caso Percepción Remota y Monitoreo Ambiental (40 min):**
   - **Comparador Multitemporal y Mapa de Calor:** Script asistido por IA que procesa puntos de focos de calor/deforestación, los cruza por municipio y exporta un visor *Split-Screen* satelital junto con un mapa de calor (*Heatmap*) en HTML.

---

### Módulo 4: Dashboards Geográficos Interactivos (Mapa + Gráficos + Análisis en Navegador) (3 Horas)
**Objetivo:** Integrar el visor cartográfico con gráficos estadísticos dinámicos, indicadores clave (KPIs) y herramientas de análisis espacial en tiempo real.

1. **4.1. Diseño de Interfaz (UI/UX) Profesional usando IA Multimodal (40 min)**
   - Cómo usar **Tailwind CSS** o **Bootstrap** mediante prompts para crear diseños modernos tipo *Centro de Monitoreo* (cabecera con logo institucional, tarjetas KPI, barra lateral de filtros).
   - **Prompting Visual:** Cómo subir el boceto o captura de un visor referente a Claude/Gemini para que replique la maquetación en HTML/CSS.
2. **4.2. Sincronización Bidireccional: Leaflet + Chart.js / Plotly (55 min)**
   - Prompts paso a paso para lograr reactividad total:
     - Filtrar por departamento, cuenca o fecha -> actualiza simultáneamente los polígonos del mapa, las tarjetas de indicadores y los gráficos de barras/series de tiempo.
     - Hacer clic en una unidad espacial del mapa -> despliega la curva histórica (ej. serie temporal de precipitación o NDVI) en el panel lateral.
3. **4.3. Geoprocesamiento en el Navegador con `Turf.js` y Herramientas de Dibujo (35 min)**
   - Cómo pedirle a la IA que integre `Leaflet-Geoman` y `Turf.js`: permitir que el usuario dibuje un polígono o un radio de influencia (*buffer*) en pantalla y el dashboard calcule al instante cuántos elementos o hectáreas quedan dentro.
4. **🛠️ Proyecto del Módulo 4 — Caso Gestión del Riesgo / Monitoreo Territorial (50 min):**
   - **Dashboard de Monitoreo de Riesgo y Territorio:** Panel integral con 4 KPIs dinámicos, mapa interactivo con filtros multicriterio, herramienta de área de afectación (*buffer*), gráfico temporal y botón de descarga de datos filtrados en CSV.

---

### Módulo 5: Aplicaciones Web Analíticas con Python y Streamlit (2 Horas)
**Objetivo:** Construir aplicaciones web interactivas en Python donde los usuarios puedan cargar sus propios datos espaciales y obtener análisis y mapas al instante.

1. **5.1. Arquitectura de una Web App Geoespacial en Python (20 min)**
   - Cuándo elegir un visor estático (HTML/JS/Leaflet) vs una aplicación dinámica en Python (**Streamlit**).
2. **5.2. Desarrollo con Prompts en Streamlit + Folium / Leafmap / PyDeck (60 min)**
   - Creación de una interfaz con barra lateral, pestañas y métricas usando solo scripts de Python generados por IA.
   - Implementación de un cargador de archivos (`st.file_uploader`) para que el usuario suba un CSV con coordenadas o un GeoJSON y se renderice automáticamente en el mapa.
   - Visualización 3D de densidad o variables territoriales (columnas hexagonales `H3` / extrusión 3D) con **PyDeck**.
3. **🛠️ Proyecto del Módulo 5 — Caso Agro / Recursos Naturales (40 min):**
   - **Geo-Analizador Interactivo en Streamlit:** Aplicación donde el profesional sube datos de muestreo de campo o zonificación agrícola, selecciona la variable de interés y obtiene mapa 2D/3D, estadísticas descriptivas y gráficos interactivos.

---

### Módulo 6: Git, GitHub y Despliegue Gratuito en la Nube (2 Horas)
**Objetivo:** Publicar los visores, comparadores satelitales y dashboards en internet con enlaces públicos gratuitos, creando un portafolio profesional para la comunidad SELPER.

1. **6.1. Git y GitHub para Profesionales Geoespaciales (con ayuda de IA) (35 min)**
   - Estructura óptima de un proyecto WebGIS (`index.html`, `/css`, `/js`, `/data`, `README.md`).
   - Cómo subir y actualizar proyectos usando **GitHub Desktop** o VS Code sin memorizar comandos de consola.
2. **6.2. Despliegue de Visores y Dashboards JS en GitHub Pages y Vercel (35 min)**
   - Publicación en 2 minutos con **GitHub Pages** (`https://usuario.github.io/visor-selper/`).
   - Diagnóstico y solución con IA de errores frecuentes en producción: rutas relativas/absolutas, errores CORS al cargar GeoJSON o servicios WMS, y manejo de archivos pesados.
3. **6.3. Despliegue de Aplicaciones Python en Streamlit Community Cloud (20 min)**
   - Generación con IA del archivo `requirements.txt` (incluyendo librerías geoespaciales sin conflictos).
   - Conexión directa desde GitHub a Streamlit Cloud para tener la aplicación Python corriendo 24/7 gratis.
4. **🛠️ Proyecto Final Integrador — Portafolio Geoespacial SELPER (30 min):**
   - Publicación de un **Hub / Portafolio Cartográfico Personal o Institucional** en GitHub Pages que integra los 4 proyectos desarrollados (Monitoreo Ambiental/Satelital, Catastro, Gestión del Riesgo y App en Streamlit), documentado con un `README.md` técnico generado con IA.

---

## 🛠️ Resumen del Stack Tecnológico del Curso

| Componente | Tecnologías que el alumno dominará con IA | Aplicación en los Casos SELPER |
| :--- | :--- | :--- |
| **Copilotos de IA** | Claude (Artifacts), Gemini, ChatGPT | Generación de código, maquetación visual, depuración y documentación. |
| **Frontend y Mapas Web** | HTML5, CSS3 (Tailwind/Bootstrap), JS, **Leaflet.js** | Visores rápidos, capas WMS/Satelitales, coropletas y clustering. |
| **Análisis en Navegador** | **Turf.js**, Leaflet-Geoman, **Chart.js** | Buffers en vivo, conteo espacial en cliente y gráficos sincronizados. |
| **Python Geoespacial** | Python, **GeoPandas**, Pandas, **Folium**, **Leafmap** | Limpieza de datos, reproyección (`EPSG:9377` -> `4326`), Split-Maps satelitales. |
| **Apps Analíticas y 3D** | **Streamlit**, **PyDeck**, Plotly | Aplicaciones interactivas con carga de archivos de usuario y mapas 3D. |
| **Despliegue y Versionado** | **Git, GitHub, GitHub Pages**, Streamlit Cloud | Publicación gratuita con URL pública para compartir con clientes o entidades. |

---

## 📦 Kit de Aprendizaje Autodidacta (*Self-Paced Kit*)
Para que cualquier integrante de **SELPER** pueda realizar el curso a su propio ritmo con éxito total, el curso incluye:
1. **📘 Manual de Prompts Geoespaciales (*Geo-Prompt Playbook*):** Más de 30 plantillas de *prompts* probadas para copiar, rellenar con tus propios datos y pegar en Claude o Gemini.
2. **🗂️ Paquete de Datos Abiertos de Colombia y LatAm:** Capas listas para usar (municipios DANE/IGAC simplificados, estaciones IDEAM simuladas/reales, puntos de focos de calor FIRMS, enlaces WMS y GeoJSON catastral de prueba).
3. **🚑 Guía Rápida de Resolución de Problemas con IA:** Qué hacer paso a paso cuando el mapa no carga, las coordenadas salen en otro continente o falla el despliegue en GitHub.
4. **✅ Retos Cortos de Validación por Módulo:** Ejercicios puntuales de 10 minutos donde el estudiante modifica su visor usando un nuevo *prompt* para afianzar su autonomía.
