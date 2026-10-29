"""
Generador de Presentaciones (.pptx nativo de PowerPoint + .html interactivo con Reveal.js)
para los 6 Módulos del Curso Autodidacta GeoMapIA — SELPER Colombia.
"""

import html
import subprocess
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET

BASE_DIR = Path(__file__).resolve().parents[1]
PANDOC_BIN = "/opt/homebrew/bin/pandoc"

# Definición completa de las 6 presentaciones (10 diapositivas teóricas y prácticas por módulo)
MODULOS_SLIDES = [
    {
        "num": 1,
        "folder": "modulo-1-prompts-fundamentos",
        "color_hex": "0EA5E9",
        "badge": "MÓDULO 1 • 2.0 HORAS",
        "titulo": "Mentalidad AI-First, Entorno WebGIS e Ingeniería de Prompts (C-T-D-E)",
        "subtitulo": "Fundamentos teóricos y prácticos para crear mapas web conversando con IA • SELPER Colombia",
        "demo_link": "./visor-basico-selper.html",
        "slides": [
            {
                "title": "1. El Cambio de Paradigma en la Geomática",
                "left_title": "Enfoque Tradicional WebGIS",
                "left_items": [
                    "Meses aprendiendo sintaxis de HTML, CSS, JS y librerías antes de ver un mapa.",
                    "Alta fricción por errores de punto y coma, rutas o versiones de paquetes.",
                    "Dependencia total de un programador externo para publicar un visor sencillo.",
                    "Mucho tiempo invertido en código repetitivo (boilerplate)."
                ],
                "right_title": "Enfoque AI-First para Especialistas SIG",
                "right_items": [
                    "Tú aportas el criterio espacial, cartográfico y temático (el QUÉ y el PORQUÉ).",
                    "La IA (Claude, Gemini, ChatGPT) escribe la sintaxis técnica (el CÓMO).",
                    "Creación de prototipos funcionales en minutos mediante Prompts estructurados.",
                    "Aprendizaje inverso: entiendes el código viendo funcionar tu propio mapa."
                ],
                "note": "El profesional de SELPER no es reemplazado por la IA; se convierte en Arquitecto Geoespacial capaz de desplegar sus propios visores."
            },
            {
                "title": "2. ¿Qué Asistente de IA elegir para cada tarea SIG?",
                "left_title": "Claude (Anthropic) y ChatGPT (OpenAI)",
                "left_items": [
                    "Claude (Sonnet + Artifacts): Renderiza visores HTML/Leaflet en vivo dentro del chat.",
                    "Excelente precisión generando dashboards extensos en un solo archivo.",
                    "ChatGPT: Muy versátil para explicar errores paso a paso y generar scripts Python.",
                    "Ideal para iterar funciones específicas de filtrado o simbología."
                ],
                "right_title": "Gemini (Google) y Editores con IA",
                "right_items": [
                    "Gemini: Ventana de contexto masiva ideal para pegar archivos GeoJSON/CSV largos.",
                    "Multimodalidad nativa: sube una captura de un dashboard y pídele la maqueta HTML.",
                    "VS Code + extensiones de IA: Edita archivos directamente en tu carpeta local.",
                    "Regla práctica: ¡El mismo Prompt C-T-D-E funciona en cualquiera de ellos!"
                ],
                "note": "No dependas de una sola herramienta: aprende la estructura universal del prompt geoespacial."
            },
            {
                "title": "3. Anatomía Técnica de un Visor Geográfico Web",
                "left_title": "Las 3 Capas del Navegador (Frontend)",
                "left_items": [
                    "1. HTML5 (Estructura): Crea el contenedor <div id='map'></div> y los paneles.",
                    "2. CSS3 / Tailwind (Diseño): Define que el mapa mida 100vh y estiliza leyendas.",
                    "3. JavaScript + Leaflet.js (Lógica): Carga teselas satelitales, dibuja capas y popups.",
                    "Todo puede convivir en un único archivo .html para facilitar el aprendizaje."
                ],
                "right_title": "El Flujo de Carga en el Navegador",
                "right_items": [
                    "Paso 1: El navegador lee las librerías por CDN (sin instalar nada en disco).",
                    "Paso 2: Leaflet inicializa el lienzo centrado en coordenadas [Lat, Lon] y Zoom.",
                    "Paso 3: Se conectan los Mapas Base (OSM, CartoDB Dark, Esri World Imagery).",
                    "Paso 4: Se superponen tus datos vectoriales (GeoJSON) o servicios OGC (WMS)."
                ],
                "note": "Si el contenedor <div id='map'> no tiene altura en CSS (height), el mapa saldrá en blanco."
            },
            {
                "title": "4. Estándares de Datos Espaciales en la Web",
                "left_title": "Formatos Vectoriales y Tabulares",
                "left_items": [
                    "GeoJSON (.geojson): El estándar rey de los visores web (basado en JSON).",
                    "CSV con Lat/Lon: Ideal para tablas de Excel de muestreo o estaciones.",
                    "Shapefile (.shp): Formato de escritorio (QGIS/ArcGIS); debe convertirse a GeoJSON.",
                    "KML / GPX: Formatos comunes en GPS y Google Earth fácilmente convertibles."
                ],
                "right_title": "Servicios Ráster y Satelitales OGC",
                "right_items": [
                    "Tiles XYZ: Cuadrículas pre-renderizadas por nivel de zoom ({z}/{x}/{y}.png).",
                    "WMS / WMTS: Estándar OGC usado por IGAC, IDEAM, SIAC y NASA GIBS.",
                    "COG (Cloud Optimized GeoTIFF): Imágenes satelitales optimizadas para lectura parcial.",
                    "Siempre indica a la IA cuál de estos formatos vas a consumir."
                ],
                "note": "Un Shapefile consta de varios archivos (.shp, .dbf, .shx, .prj); la web prefiere un único archivo .geojson."
            },
            {
                "title": "5. Sistemas de Referencia: MAGNA-SIRGAS vs WGS84 Web",
                "left_title": "Cartografía Oficial en Colombia",
                "left_items": [
                    "MAGNA-SIRGAS Origen Nacional (EPSG:9377) o antiguos orígenes (EPSG:3116).",
                    "Coordenadas planas en metros (ej. Este: 4.885.000 m, Norte: 2.065.000 m).",
                    "Excelentes para medir áreas en hectáreas y distancias métricas en SIG.",
                    "⚠️ Si las cargas directo en Leaflet, ¡tus puntos saldrán fuera del planeta!"
                ],
                "right_title": "Estándar de Mapas Web (Leaflet / Web Mercator)",
                "right_items": [
                    "Las librerías web esperan coordenadas geográficas WGS84 (EPSG:4326).",
                    "Valores en grados decimales (Colombia aprox: Latitud -4° a 13°, Longitud -79° a -66°).",
                    "Atención al orden: Leaflet usa [Latitud, Longitud], mientras GeoJSON usa [Lon, Lat].",
                    "La IA puede detectar y transformar tus coordenadas automáticamente."
                ],
                "note": "En tu prompt especifica siempre: 'Mis coordenadas están en EPSG:4326 (Latitud, Longitud para Colombia)'."
            },
            {
                "title": "6. Metodología C-T-D-E de Ingeniería de Prompts SIG",
                "left_title": "C (Contexto) + T (Tecnología)",
                "left_items": [
                    "[C] Contexto y Rol: 'Actúa como un desarrollador WebGIS Senior de SELPER Colombia...'",
                    "Define el propósito temático: monitoreo ambiental, catastro o gestión del riesgo.",
                    "[T] Tecnología: 'Crea un único archivo HTML autocontenido con Leaflet 1.9.4 y Tailwind CSS por CDN.'",
                    "Evita que la IA divida el proyecto en 10 archivos complejos cuando estás empezando."
                ],
                "right_title": "D (Datos) + E (Estilo y Comportamiento)",
                "right_items": [
                    "[D] Datos: Lista los nombres exactos de las columnas/propiedades y el EPSG:4326.",
                    "Ejemplo: 'propiedades: id, nombre, region, ndvi, precipitacion_mm, alerta'.",
                    "[E] Estilo: Especifica mapas base, colores por categoría, popups, leyenda y filtros.",
                    "Pide siempre: 'Entrégame el código completo y funcional listo para abrir'."
                ],
                "note": "El Framework C-T-D-E reduce en un 90% las alucinaciones y errores de código en Claude y Gemini."
            },
            {
                "title": "7. Comparativa: Prompt Ambiguo vs Prompt C-T-D-E",
                "left_title": "❌ Prompt Ambiguo (Resultado Pobre)",
                "left_items": [
                    "'Hazme una página web con un mapa de Colombia que tenga estaciones ambientales.'",
                    "Problema 1: La IA no sabe qué librería usar (puede usar Google Maps con API Key de pago).",
                    "Problema 2: No incluye estilos de altura y el mapa sale en blanco.",
                    "Problema 3: No agrega leyenda, ni control de capas, ni datos realistas."
                ],
                "right_title": "✅ Prompt C-T-D-E (Resultado Profesional)",
                "right_items": [
                    "'[C] Rol WebGIS SELPER. [T] 1 archivo HTML con Leaflet 1.9.4 y Tailwind CDN.'",
                    "'[D] Centro en [4.6097, -74.0817], zoom 6. 12 estaciones con ndvi, precipitacion y alerta.'",
                    "'[E] Capas CartoDB Dark + Esri Satélite, círculos por color de alerta, filtro y leyenda.'",
                    "Resultado: Un visor completo de nivel institucional en menos de 30 segundos."
                ],
                "note": "La calidad de tu visor web es directamente proporcional a la precisión de tu bloque [D] Datos y [E] Estilo."
            },
            {
                "title": "8. Depuración Asistida (AI Debugging) con F12",
                "left_title": "¿Cómo leer errores en el navegador?",
                "left_items": [
                    "1. Abre tu archivo HTML en Chrome, Edge o Firefox.",
                    "2. Presiona la tecla F12 (o Clic Derecho -> Inspeccionar).",
                    "3. Abre la pestaña 'Console' (Consola).",
                    "4. Cualquier error de sintaxis o carga aparecerá en texto rojo con el número de línea."
                ],
                "right_title": "El Prompt Reparador en 1 Paso",
                "right_items": [
                    "No intentes adivinar el error en soledad: cópialo y pégalo en el chat de la IA.",
                    "Prompt: 'Mi visor presenta este error en la consola F12: [PEGAR ERROR]. Corrige mi código.'",
                    "Errores típicos que la IA resuelve al instante: comillas sin cerrar, CDN caído o CORS.",
                    "Para abrir archivos externos (.geojson), usa la extensión 'Live Server' en VS Code."
                ],
                "note": "Aprender a usar F12 + IA te garantiza que nunca te quedarás bloqueado estudiando de forma autodidacta."
            },
            {
                "title": "9. Resumen y Práctica del Módulo 1",
                "left_title": "Lo que hemos dominado hoy",
                "left_items": [
                    "Configuración del entorno ligero (Navegador + VS Code + Live Server + IA).",
                    "Comprensión de HTML + CSS + JS (Leaflet) + EPSG:4326.",
                    "Aplicación práctica del Framework C-T-D-E para crear tu primer visor.",
                    "Flujo de inspección y corrección de errores con la consola F12."
                ],
                "right_title": "Tu Reto Práctico Autodidacta",
                "right_items": [
                    "1. Abre el laboratorio: visor-basico-selper.html.",
                    "2. Haz clic en '🤖 Ver Prompt Usado' y cópialo en Claude o Gemini.",
                    "3. Pídele a la IA que agregue una estación en tu municipio y un filtro por región.",
                    "4. Guarda tu versión y marca el Módulo 1 como completado en el portal."
                ],
                "note": "¡Estás listo para el Módulo 2: Mapas Coropléticos, Servicios WMS y Clustering con Leaflet!"
            }
        ]
    },
    {
        "num": 2,
        "folder": "modulo-2-visores-leaflet",
        "color_hex": "10B981",
        "badge": "MÓDULO 2 • 2.5 HORAS",
        "titulo": "Visores Interactivos con HTML, JavaScript y Leaflet.js",
        "subtitulo": "Servicios WMS oficiales, mapas coropléticos dinámicos, clustering e inspectores prediales",
        "demo_link": "./visor-catastral-ambiental.html",
        "slides": [
            {
                "title": "1. Arquitectura Interna de Leaflet.js",
                "left_title": "¿Por qué Leaflet es el estándar WebGIS?",
                "left_items": [
                    "Librería Open Source ultraligera (~42 KB) y 100% compatible con móviles.",
                    "No requiere claves de pago (API Keys) ni cuentas de tarjeta de crédito.",
                    "Ecosistema enorme de plugins: MarkerCluster, Heatmaps, Side-by-Side, Geoman.",
                    "Los modelos de IA (Claude/Gemini) conocen su documentación a la perfección."
                ],
                "right_title": "Objetos Fundamentales que genera la IA",
                "right_items": [
                    "L.map('map'): Instancia principal del mapa vinculada al div HTML.",
                    "L.tileLayer(url): Conecta mapas base (OSM, Carto, Esri Satélite).",
                    "L.tileLayer.wms(url, opciones): Conecta geoservicios institucionales OGC.",
                    "L.geoJSON(datos, {style, onEachFeature}): Renderiza capas vectoriales con estilos."
                ],
                "note": "Conocer el nombre de estos 4 objetos te permite darle instrucciones quirúrgicas a la IA."
            },
            {
                "title": "2. Mapas Base (Basemaps) y Teselas XYZ",
                "left_title": "Cómo funcionan los Tiles {z}/{x}/{y}",
                "left_items": [
                    "El mundo se divide en una pirámide de imágenes de 256x256 píxeles según el zoom (z).",
                    "Al mover el mapa, Leaflet solo descarga los cuadros visibles en pantalla.",
                    "Proveedores gratuitos recomendados: CartoDB Dark/Positron, OpenStreetMap, Esri Imagery.",
                    "OpenTopoMap: Excelente para contexto fisiográfico y cuencas hidrográficas."
                ],
                "right_title": "Selector de Capas (L.control.layers)",
                "right_items": [
                    "Recibe dos diccionarios: Capas Base (excluyentes) y Capas Superpuestas (checkboxes).",
                    "Puedes pedirle a la IA que deje el Modo Oscuro o Satélite activo por defecto.",
                    "Importante: incluir siempre la atribución (attribution) del proveedor.",
                    "También puedes crear botones propios en Tailwind CSS fuera del control clásico."
                ],
                "note": "Un mapa base oscuro (CartoDB Dark Matter) hace que tus capas temáticas brillen con alto contraste."
            },
            {
                "title": "3. Integración de Servicios OGC WMS / WMTS",
                "left_title": "Geoservicios Oficiales en Colombia y el Mundo",
                "left_items": [
                    "IGAC (Colombia en Mapas): Ortofotos, cartografía básica y catastro.",
                    "IDEAM / SIAC: Zonificación climática, coberturas de la tierra Corine Land Cover.",
                    "Servicio Geológico Colombiano (SGC): Amenaza sísmica y movimientos en masa.",
                    "NASA GIBS / Copernicus: Índices satelitales diarios y anomalías térmicas."
                ],
                "right_title": "Parámetros Clave para pedirle a la IA",
                "right_items": [
                    "Usar L.tileLayer.wms('URL_BASE_WMS', { layers: 'nombre_capa', format: 'image/png', transparent: true }).",
                    "Sin transparent: true, el servicio WMS tapará con un fondo blanco tu mapa base.",
                    "Agrega siempre un deslizador (<input type='range'>) que llame a capa.setOpacity(val).",
                    "Así el usuario puede comparar la ortofoto o capa temática con el catastro."
                ],
                "note": "Verifica que el servidor WMS soporte EPSG:3857 o EPSG:4326 y esté publicado sobre HTTPS."
            },
            {
                "title": "4. Estructura de un GeoJSON y Carga en el Visor",
                "left_title": "Anatomía de un FeatureCollection",
                "left_items": [
                    "Un GeoJSON es una lista de objetos llamados 'features' (entidades espaciales).",
                    "Cada feature tiene dos partes: 'geometry' (Point, LineString, Polygon) y 'properties'.",
                    "En 'properties' viaja la tabla de atributos (código DANE, área, NDVI, avalúo).",
                    "Es legible como texto plano: puedes copiar un fragmento y pegarlo en el prompt."
                ],
                "right_title": "Dos formas de cargarlo en tu visor",
                "right_items": [
                    "1. Embebido en una variable JS (const datos = {...}): Funciona sin servidor al hacer doble clic.",
                    "2. Externo con fetch('./data/municipios.geojson'): Ideal para producción y GitHub Pages.",
                    "Tip: Muéstrale a la IA solo el primer 'feature' de tu GeoJSON para que conozca los campos.",
                    "Nunca pegues un GeoJSON de 50.000 líneas entero en el chat; pega solo el esquema."
                ],
                "note": "Darle a la IA un ejemplo real de 'feature.properties' garantiza que los popups y filtros funcionen a la primera."
            },
            {
                "title": "5. Teoría y Diseño de Mapas Coropléticos Web",
                "left_title": "Clasificación y Rampas de Color",
                "left_items": [
                    "Un mapa coroplético colorea polígonos (municipios, cuencas, predios) según un valor numérico.",
                    "Rampas secuenciales (amarillo a rojo): para deforestación, riesgo o densidad.",
                    "Rampas divergentes (rojo a amarillo a verde): para índices como NDVI o balance hídrico.",
                    "La función obtenerColor(valor, variable) en JS evalúa umbrales y devuelve el código HEX."
                ],
                "right_title": "Cambio Dinámico de Variable Temática",
                "right_items": [
                    "Con un menú <select>, un solo visor sirve para múltiples estudios.",
                    "El usuario elige entre: 'Deforestación (ha)', 'Avalúo Catastral ($/ha)' o 'NDVI'.",
                    "Al cambiar el selector, se vuelve a aplicar el estilo y se regenera la leyenda.",
                    "Ahorra crear 3 mapas separados y permite comparar patrones territoriales."
                ],
                "note": "Usa opacidad de relleno entre 0.65 y 0.80 (fillOpacity) para dejar ver el relieve o satélite debajo."
            },
            {
                "title": "6. Interactividad Avanzada: Hover, Zoom y Paneles",
                "left_title": "Eventos del Mouse (onEachFeature)",
                "left_items": [
                    "mouseover: Resalta el polígono bajo el cursor (borde grueso y mayor opacidad).",
                    "mouseout: Restaura el estilo original con capaGeoJSON.resetStyle(e.target).",
                    "click: Ejecuta map.fitBounds(e.target.getBounds()) para encuadrar el municipio.",
                    "Mejora drásticamente la experiencia de usuario frente a un mapa estático."
                ],
                "right_title": "Inspector Lateral vs Popup Tradicional",
                "right_items": [
                    "El popup clásico requiere hacer clic en cada polígono uno por uno.",
                    "Un Panel Inspector Fijo se actualiza instantáneamente al mover el mouse.",
                    "Permite mostrar fichas catastrales o ambientales con múltiples indicadores.",
                    "En el Prompt 2.2 pedimos ambos: resaltado hover + ficha en tiempo real."
                ],
                "note": "En dispositivos táctiles (móviles), el evento click cumple simultáneamente el rol de inspección."
            },
            {
                "title": "7. Agrupación de Puntos Masivos (MarkerCluster)",
                "left_title": "El Problema de Saturación Visual",
                "left_items": [
                    "Dibujar 5.000 marcadores DOM individuales vuelve lento el navegador y tapa el mapa.",
                    "Solución 1: L.markerClusterGroup() agrupa puntos cercanos en círculos con contador.",
                    "Los círculos cambian de color (verde, amarillo, naranja) según la densidad.",
                    "Al hacer clic en un cluster o acercar el zoom, los puntos se despliegan suavemente."
                ],
                "right_title": "Renderizado en Canvas para Puntos Simples",
                "right_items": [
                    "Solución 2: Activar preferCanvas: true al crear el objeto L.map.",
                    "Dibuja decenas de miles de L.circleMarker sobre un único lienzo HTML5 Canvas.",
                    "Ideal para focos de calor satelitales (FIRMS) o levantamientos LiDAR/GPS.",
                    "Puedes combinar clustering con filtros de búsqueda en tiempo real."
                ],
                "note": "En tu prompt solo necesitas pedir: 'Agrupa los puntos usando Leaflet.markercluster vía CDN'."
            },
            {
                "title": "8. Buscadores, Filtros de Atributos y Leyendas",
                "left_title": "Filtrado Reactivo en el Cliente",
                "left_items": [
                    "La opción filter: (feature) => {...} de L.geoJSON decide qué polígonos mostrar.",
                    "Conectamos una caja de texto (<input>) para buscar por nombre de municipio o uso.",
                    "Conectamos un <select> para filtrar por Región Natural (Andina, Caribe, Amazonía...).",
                    "La respuesta es instantánea (0 milisegundos de espera de servidor)."
                ],
                "right_title": "Leyendas Cartográficas Automáticas",
                "right_items": [
                    "Todo mapa técnico de SELPER exige una leyenda clara con unidades de medida.",
                    "La leyenda se construye en HTML/Tailwind posicionada con z-[500] sobre el mapa.",
                    "Al cambiar la variable del mapa, una función JS actualiza los rangos y colores.",
                    "Evita leyendas estáticas en imagen que quedan desactualizadas."
                ],
                "note": "Asegúrate de usar z-index >= 500 en tus paneles flotantes para que queden por encima de los controles de Leaflet."
            },
            {
                "title": "9. Resumen y Práctica del Módulo 2",
                "left_title": "Competencias Adquiridas",
                "left_items": [
                    "Manejo de capas base, superposiciones satelitales/WMS y control de opacidad.",
                    "Creación de mapas coropléticos multi-variable con leyendas dinámicas.",
                    "Implementación de eventos hover, zoom automático e inspectores prediales.",
                    "Agrupación de puntos con MarkerCluster y filtrado por texto y región."
                ],
                "right_title": "Tu Reto Práctico Autodidacta",
                "right_items": [
                    "1. Explora el laboratorio: visor-catastral-ambiental.html.",
                    "2. Cambia entre Deforestación, Avalúo Catastral y NDVI en el panel izquierdo.",
                    "3. Usa el Prompt 2.2 para agregar una variable nueva (ej. Riesgo de Inundación).",
                    "4. Marca el Módulo 2 como completado en el portal del curso."
                ],
                "note": "En el Módulo 3 aprenderemos a preparar y automatizar datos espaciales con Python + IA."
            }
        ]
    },
    {
        "num": 3,
        "folder": "modulo-3-python-geodatos",
        "color_hex": "F59E0B",
        "badge": "MÓDULO 3 • 2.5 HORAS",
        "titulo": "Automatización de Datos Geoespaciales y Mapas con Python + IA",
        "subtitulo": "GeoPandas, reproyección MAGNA-SIRGAS a WGS84, Folium y Comparadores Satelitales Split-Map",
        "demo_link": "./comparador-satelital-split.html",
        "slides": [
            {
                "title": "1. ¿Por qué usar Python en el Desarrollo de Visores Web?",
                "left_title": "Los Cuellos de Botella antes del Visor",
                "left_items": [
                    "Archivos Shapefile (.shp) de 150 MB que congelan cualquier navegador web.",
                    "Tablas de Excel con coordenadas sucias, comas en vez de puntos o celdas vacías.",
                    "Capas en proyección plana MAGNA-SIRGAS (EPSG:9377) incompatibles con Leaflet.",
                    "Necesidad de cruzar miles de puntos contra polígonos municipales cada semana."
                ],
                "right_title": "Python + IA como Tubería (Pipeline) Automática",
                "right_items": [
                    "No necesitas memorizar funciones de Python: le describes la entrada y salida a la IA.",
                    "Un script de 20 líneas limpia, reproyecta, simplifica y exporta a .geojson en 2 segundos.",
                    "Puedes ejecutarlo gratis en la nube con Google Colab (sin instalar nada) o en local.",
                    "Además, librerías como Folium y Leafmap exportan visores HTML directos desde Python."
                ],
                "note": "Python prepara y optimiza el dato pesado; JavaScript/Leaflet lo visualiza a máxima velocidad."
            },
            {
                "title": "2. El Ecosistema Python Geoespacial Esencial",
                "left_title": "Manipulación de Datos (Pandas y GeoPandas)",
                "left_items": [
                    "pandas: Lee archivos Excel (.xlsx) y CSV, filtra filas, calcula promedios y limpia nulos.",
                    "geopandas: Extiende pandas agregando una columna 'geometry' (puntos, líneas, polígonos).",
                    "Lee y escribe cualquier formato con una línea: gpd.read_file() y gdf.to_file().",
                    "shapely y pyproj: Motores internos para geometría y transformación de coordenadas."
                ],
                "right_title": "Visualización Web desde Python",
                "right_items": [
                    "folium: Envuelve Leaflet.js en Python; permite exportar mapas interactivos a .html.",
                    "leafmap: Creado por Qiusheng Wu; ideal para Percepción Remota, COG y Split-Maps.",
                    "geopy: Geocodificación gratuita (convierte direcciones de texto en Lat/Lon).",
                    "En tu prompt indica qué librerías prefieres para que el script sea limpio."
                ],
                "note": "En Google Colab puedes instalar GeoPandas y Folium con una sola celda: !pip install geopandas folium leafmap"
            },
            {
                "title": "3. Reproyección en Colombia: EPSG:9377 a EPSG:4326",
                "left_title": "Diagnóstico del Sistema de Referencia (CRS)",
                "left_items": [
                    "En GeoPandas, gdf.crs muestra el sistema actual de tu capa.",
                    "Capas nacionales del IGAC/DANE suelen venir en EPSG:9377 (Origen Nacional) o EPSG:3116.",
                    "Sus coordenadas se ven así: X = 4885210.45, Y = 2065120.12 (metros).",
                    "Para la web necesitamos grados decimales WGS84 (EPSG:4326): Lon = -74.08, Lat = 4.60."
                ],
                "right_title": "La Transformación Exacta en 1 Línea",
                "right_items": [
                    "Comando clave: gdf_web = gdf.to_crs(epsg=4326).",
                    "Si un archivo no tiene .prj definido, primero se asigna con gdf.set_crs(epsg=9377).",
                    "En el Prompt 3.1 le pedimos a la IA que verifique automáticamente el CRS antes de exportar.",
                    "Evita reproyectar manualmente capa por capa en software de escritorio."
                ],
                "note": "Regla de oro antes de publicar en GitHub: verifica siempre que tu GeoJSON final esté en EPSG:4326."
            },
            {
                "title": "4. Optimización y Adelgazamiento de Capas para la Web",
                "left_title": "¿Por qué pesa tanto un GeoJSON crudo?",
                "left_items": [
                    "1. Exceso de vértices: Un río o municipio digitalizado a escala 1:1.000 tiene millones de nodos.",
                    "2. Exceso de decimales: Coordenadas como -74.08174928374928 (14 decimales son sub-milimétricos).",
                    "3.Exceso de columnas: Tablas con 80 campos innecesarios que viajan por internet.",
                    "Un visor web óptimo debe cargar capas de menos de 3 a 5 MB."
                ],
                "right_title": "Las 3 Técnicas de Reducción en Python",
                "right_items": [
                    "1. Simplificación topológica: gdf['geometry'] = gdf.simplify(0.0005, preserve_topology=True).",
                    "2. Filtrado de columnas: conservar solo las 5 o 6 variables que se muestran en el visor.",
                    "3. Redondeo de coordenadas a 5 decimales (~1 metro de precisión real en terreno).",
                    "Resultado: Un archivo de 60 MB baja a 1.5 MB y carga instantáneamente en móviles."
                ],
                "note": "preserve_topology=True asegura que los municipios vecinos no se separen ni creen huecos al simplificar."
            },
            {
                "title": "5. Cruces Espaciales (Spatial Join) y Limpieza con IA",
                "left_title": "Cómo darle contexto de tus datos a la IA",
                "left_items": [
                    "Ejecuta print(df.head(3)) y print(df.columns) en Python.",
                    "Copia esas 5 líneas de salida y pégalas en el bloque [D] Datos de tu prompt.",
                    "La IA verá los nombres exactos de tus columnas, tildes, mayúsculas y tipos de datos.",
                    "Así el script generado nunca fallará por KeyError o columnas inexistentes."
                ],
                "right_title": "Operaciones Espaciales Automatizadas",
                "right_items": [
                    "Cruce punto-polígono: gpd.sjoin(puntos_focos, poligonos_municipios, predicate='within').",
                    "Agregación estadística: contar cuántos focos de calor o predios hay por municipio.",
                    "Unión tabular (merge): unir estadísticas del DANE por código DIVIPOLA (codigo_dane).",
                    "Exportación directa del resultado enriquecido a GeoJSON."
                ],
                "note": "En lugar de hacer 10 pasos manuales en un SIG de escritorio, guardas un script reproducible."
            },
            {
                "title": "6. Percepción Remota Web: Comparadores Split-Map",
                "left_title": "¿Qué es un Split-Map (Mapa de Cortina)?",
                "left_items": [
                    "Divide el visor con una barra vertical deslizante para comparar dos capas sincronizadas.",
                    "Aplicación 1: Antes y Después de un incendio forestal, inundación o deforestación.",
                    "Aplicación 2: Imagen Satelital Óptica RGB (izquierda) vs Índice NDVI o Relieve (derecha).",
                    "Aplicación 3: Ortofoto histórica vs Catastro multipropósito actual."
                ],
                "right_title": "Cómo se construye con Python o JS",
                "right_items": [
                    "En Python: Leafmap (m.split_map(left_layer, right_layer)) o Folium DualMap.",
                    "En HTML/JS puro: Sincronización de recorte CSS (clip: rect(...)) sobre dos TileLayers.",
                    "Permite añadir botones de salto rápido (flyTo) a zonas críticas de estudio.",
                    "Nuestro entregable comparador-satelital-split.html implementa este patrón completo."
                ],
                "note": "El Split-Map es una de las herramientas de comunicación visual más impactantes para proyectos de SELPER."
            },
            {
                "title": "7. Mapas de Calor (Heatmaps) de Fenómenos Espaciales",
                "left_title": "Teoría de Densidad Kernel en el Navegador",
                "left_items": [
                    "Transforma nubes de puntos (ej. alertas térmicas MODIS/VIIRS de FIRMS) en una superficie continua.",
                    "Cada punto aporta intensidad según un peso opcional [latitud, longitud, intensidad].",
                    "Parámetros clave: radius (radio de influencia en píxeles), blur (suavizado) y gradient.",
                    "Se recalcula dinámicamente a medida que el usuario acerca o aleja el zoom."
                ],
                "right_title": "Cuándo usar Heatmap vs MarkerCluster",
                "right_items": [
                    "Usa Heatmap cuando importa el patrón de concentración espacial (focos de calor, delitos, casos).",
                    "Usa MarkerCluster cuando el usuario necesita hacer clic en cada individuo para leer su ficha.",
                    "¡Ambos pueden combinarse como capas opcionales en el mismo visor!",
                    "En Python se genera con folium.plugins.HeatMap(datos).add_to(mapa)."
                ],
                "note": "Un buen gradiente térmico va de azul/cian (baja densidad) pasando por amarillo hasta rojo intenso (núcleo)."
            },
            {
                "title": "8. Ejecución del Pipeline Python del Módulo 3",
                "left_title": "Nuestro Script procesamiento_y_mapas.py",
                "left_items": [
                    "Lee data/muestreo_agro_campo.csv con 20 lotes agrícolas en distintas regiones de Colombia.",
                    "Valida coordenadas, redondea a 5 decimales y estructura propiedades temáticas.",
                    "Exporta automáticamente data/muestreo_agro_optimizado.geojson.",
                    "Incluye la plantilla completa de reproyección EPSG:9377 -> EPSG:4326 con GeoPandas."
                ],
                "right_title": "Cómo probarlo y adaptarlo a tus datos",
                "right_items": [
                    "Ejecuta en terminal: python3 modulos/modulo-3-python-geodatos/procesamiento_y_mapas.py",
                    "Reemplaza el CSV de ejemplo por una tabla propia de tu entidad o investigación.",
                    "Usa el Prompt 3.1 del Playbook para pedirle a Claude/Gemini cruces adicionales.",
                    "Conecta el GeoJSON resultante directamente a tus visores de los Módulos 2 y 4."
                ],
                "note": "Este flujo separa limpiamente los datos (/data) de la visualización (/modulos)."
            },
            {
                "title": "9. Resumen y Práctica del Módulo 3",
                "left_title": "Competencias Adquiridas",
                "left_items": [
                    "Conversión automatizada de tablas CSV/Excel y Shapefiles a GeoJSON web.",
                    "Solución definitiva al cambio de proyección MAGNA-SIRGAS (9377) a WGS84 (4326).",
                    "Simplificación geométrica para que capas pesadas carguen en milisegundos.",
                    "Construcción de comparadores satelitales Split-Map y Mapas de Calor."
                ],
                "right_title": "Tu Reto Práctico Autodidacta",
                "right_items": [
                    "1. Abre comparador-satelital-split.html y desliza la cortina sobre el Arco Amazónico.",
                    "2. Prueba los botones de salto a Ciénaga Grande y Páramo de Chingaza.",
                    "3. Pídele a la IA agregar un cuarto botón de salto hacia tu área de estudio en Colombia.",
                    "4. Marca el Módulo 3 como completado en el portal."
                ],
                "note": "¡Siguiente paso: Módulo 4, donde uniremos Mapas + Gráficos Estadísticos + Geoprocesamiento en Vivo!"
            }
        ]
    },
    {
        "num": 4,
        "folder": "modulo-4-dashboards-geograficos",
        "color_hex": "A855F7",
        "badge": "MÓDULO 4 • 3.0 HORAS",
        "titulo": "Dashboards Geográficos Interactivos (Leaflet + Chart.js + Turf.js)",
        "subtitulo": "Diseño UI/UX con IA, sincronización bidireccional mapa-gráficos y geoprocesamiento en el navegador",
        "demo_link": "./dashboard-riesgo-territorio.html",
        "slides": [
            {
                "title": "1. De Visor Cartográfico a Dashboard de Decisión (SDSS)",
                "left_title": "¿Qué diferencia a un Dashboard Geográfico?",
                "left_items": [
                    "Un visor tradicional solo muestra dónde están las cosas en el espacio.",
                    "Un Dashboard responde simultáneamente: ¿Cuántos son?, ¿Cuál es la tendencia? y ¿Dónde es crítico?",
                    "Integra 4 componentes en una sola pantalla: Filtros + Tarjetas KPI + Mapa + Gráficos.",
                    "Permite a tomadores de decisiones explorar escenarios sin depender de reportes estáticos PDF."
                ],
                "right_title": "Aplicaciones Clave en la Comunidad SELPER",
                "right_items": [
                    "Salas de crisis de Gestión del Riesgo (monitoreo de lluvias, caudales y alertas).",
                    "Tableros de control de deforestación y focos de calor por departamento o CAR.",
                    "Seguimiento de avance de actualización catastral multipropósito.",
                    "Monitoreo agroclimático de cultivos, humedad del suelo y vigor vegetal (NDVI)."
                ],
                "note": "El objetivo de diseño es 'Zero-Scroll': toda la información crítica visible en el 100% de la ventana (100vh)."
            },
            {
                "title": "2. Diseño UI/UX Profesional con IA Multimodal",
                "left_title": "Distribución en Cuadrícula (12 Columnas)",
                "left_items": [
                    "En Tailwind CSS dividimos la pantalla con grid-cols-12:",
                    "• 3 columnas izquierdas: Panel de filtros multicriterio y herramientas espaciales.",
                    "• 6 columnas centrales: Fila superior con 4 tarjetas KPI + Mapa Leaflet amplio.",
                    "• 3 columnas derechas: 2 gráficos estadísticos apilados (Barras + Dona/Línea)."
                ],
                "right_title": "Técnica de Prompting Visual (Imagen a Código)",
                "right_items": [
                    "Puedes dibujar un boceto en papel o tomar captura de pantalla de un tablero referente.",
                    "Sube la imagen a Claude o Gemini junto con tu prompt.",
                    "Instrucción: 'Replica exactamente esta distribución de paneles usando Tailwind CSS en modo oscuro.'",
                    "La IA traducirá proporciones, colores y jerarquía visual a código HTML/CSS limpio."
                ],
                "note": "El modo oscuro (bg-slate-950) reduce la fatiga visual en centros de monitoreo y resalta la simbología."
            },
            {
                "title": "3. Arquitectura de Sincronización Bidireccional",
                "left_title": "El Patrón de 'Fuente Única de Verdad'",
                "left_items": [
                    "Mantenemos en memoria el arreglo original (estacionesData) y el filtrado (datosFiltrados).",
                    "Todos los controles (select de Región, select de Alerta, slider de Precipitación) llaman a una sola función:",
                    "actualizarDashboard()",
                    "Esto evita que el mapa muestre una cosa y los gráficos muestren otra distinta."
                ],
                "right_title": "Los 4 Pasos Internos de actualizarDashboard()",
                "right_items": [
                    "Paso 1: Filtra el arreglo según los controles activos.",
                    "Paso 2: Recalcula sumas, promedios y máximos, y actualiza el texto de los 4 KPIs.",
                    "Paso 3: Limpia la capa de Leaflet (clearLayers) y dibuja solo los puntos filtrados.",
                    "Paso 4: Recalcula las series por región/alerta y ejecuta chart.update() en Chart.js."
                ],
                "note": "Pídele siempre a la IA: 'Centraliza toda la reactividad en una única función actualizarDashboard()'."
            },
            {
                "title": "4. Gráficos Estadísticos Dinámicos con Chart.js",
                "left_title": "¿Por qué Chart.js es ideal junto a Leaflet?",
                "left_items": [
                    "Renderiza sobre HTML5 <canvas> con animaciones fluidas al cambiar datos.",
                    "Se adapta automáticamente al tamaño del contenedor (responsive: true, maintainAspectRatio: false).",
                    "Soporta gráficos de barras, líneas temporales, donas, radar y dispersión.",
                    "Se actualiza en vivo modificando chart.data.datasets[0].data y llamando a chart.update()."
                ],
                "right_title": "Agregación de Datos en JavaScript (reduce / map)",
                "right_items": [
                    "La IA genera automáticamente las funciones de agrupación por categoría o región.",
                    "Ejemplo 1: Promedio de precipitación (mm) agrupado por Región Natural.",
                    "Ejemplo 2: Conteo de estaciones por Nivel de Alerta (Alta, Media, Baja).",
                    "Los colores del gráfico de dona deben coincidir exactamente con los colores del mapa."
                ],
                "note": "Consistencia cartográfica: si 'Alerta Alta' es rojo (#ef4444) en el mapa, debe ser rojo (#ef4444) en el gráfico."
            },
            {
                "title": "5. Geoprocesamiento en el Navegador con Turf.js",
                "left_title": "¿Qué es Turf.js (Client-Side GIS)?",
                "left_items": [
                    "Es un motor de análisis espacial escrito 100% en JavaScript que corre dentro del navegador.",
                    "Trabaja nativamente sobre objetos GeoJSON sin necesitar servidor PostGIS ni Python detrás.",
                    "Ejecuta buffers, intersecciones, áreas, distancias, centroides, Voronoi y conteos en milisegundos.",
                    "Se carga con una sola línea CDN: @turf/turf."
                ],
                "right_title": "Operaciones Clave implementadas en el Módulo 4",
                "right_items": [
                    "1. turf.point([lon, lat]): Crea el punto donde el usuario hizo clic en el mapa.",
                    "2. turf.buffer(punto, radioKm, {units: 'kilometers'}): Genera el polígono circular exacto.",
                    "3. turf.pointsWithinPolygon(puntos, buffer): Filtra qué estaciones caen dentro del radio.",
                    "4. Muestra al instante en el panel cuántas estaciones quedan afectadas y cuáles son."
                ],
                "note": "Recuerda: Turf.js sigue el estándar GeoJSON, por lo que sus coordenadas se pasan en orden [Longitud, Latitud]."
            },
            {
                "title": "6. Caso Práctico: Análisis de Radio de Impacto en Vivo",
                "left_title": "Flujo de Usuario en Situación de Emergencia",
                "left_items": [
                    "Escenario: Se reporta un evento hidroclimático o incendio en una coordenada específica.",
                    "El analista activa '📐 Buffer Espacial (Turf.js)' e ingresa un radio (ej. 180 km).",
                    "Al hacer clic en el mapa, se dibuja el área de influencia en color cian traslúcido.",
                    "El sistema identifica automáticamente las estaciones e infraestructura dentro del anillo."
                ],
                "right_title": "Otras Funciones de Turf.js que puedes pedir a la IA",
                "right_items": [
                    "turf.area(poligono): Calcula el área en m² (dividir entre 10.000 para hectáreas).",
                    "turf.nearestPoint(puntoObjetivo, coleccionPuntos): Encuentra la estación más cercana.",
                    "turf.bboxClip / turf.intersect: Recorta capas vectoriales en vivo.",
                    "turf.tin / turf.isolines: Interpolación espacial directamente en el cliente."
                ],
                "note": "Con Turf.js conviertes un visor pasivo en una verdadera herramienta de análisis SIG en la nube."
            },
            {
                "title": "7. Exportación de Reportes y Datos Filtrados (CSV)",
                "left_title": "Por qué incluir un botón de descarga",
                "left_items": [
                    "Después de filtrar por región, umbral de lluvia y nivel de alerta, el usuario quiere llevarse el dato.",
                    "Sin servidor backend, JavaScript puede construir un archivo CSV en memoria usando Blob.",
                    "El archivo descargado contiene únicamente los registros que cumplen el filtro actual.",
                    "Se abre directamente en Excel o QGIS conservando sus columnas de latitud y longitud."
                ],
                "right_title": "Código que genera la IA con un Prompt simple",
                "right_items": [
                    "Prompt: 'Agrega un botón que exporte el arreglo datosFiltradosActuales a un archivo .csv'.",
                    "Usa new Blob([contenidoCSV], { type: 'text/csv;charset=utf-8;' }).",
                    "Crea un enlace temporal <a> con download='reporte_filtrado_selper.csv'.",
                    "Cierra el ciclo completo: Visualizar -> Filtrar -> Analizar -> Exportar."
                ],
                "note": "También puedes pedirle a la IA que exporte los resultados del análisis de Turf.js en formato GeoJSON."
            },
            {
                "title": "8. Resumen y Práctica del Módulo 4",
                "left_title": "Competencias Adquiridas",
                "left_items": [
                    "Diseño de interfaces de Centro de Monitoreo con Tailwind CSS y Prompting Visual.",
                    "Sincronización en tiempo real entre controles, 4 KPIs, Leaflet y Chart.js.",
                    "Geoprocesamiento en el navegador (Buffers y conteo en polígono) con Turf.js.",
                    "Generación y descarga de reportes CSV dinámicos desde el navegador."
                ],
                "right_title": "Tu Reto Práctico Autodidacta",
                "right_items": [
                    "1. Abre dashboard-riesgo-territorio.html y filtra por región y precipitación.",
                    "2. Activa la casilla 'Buffer Espacial (Turf.js)' y haz clic en varios puntos del mapa.",
                    "3. Pídele a Claude/Gemini que agregue al resultado del Buffer el promedio de NDVI dentro del círculo.",
                    "4. Marca el Módulo 4 como completado en el portal."
                ],
                "note": "¡En el Módulo 5 daremos el salto a Aplicaciones Web en Python y 3D con Streamlit y PyDeck!"
            }
        ]
    },
    {
        "num": 5,
        "folder": "modulo-5-streamlit-python-apps",
        "color_hex": "EC4899",
        "badge": "MÓDULO 5 • 2.0 HORAS",
        "titulo": "Aplicaciones Web Analíticas con Python, Streamlit y PyDeck 3D",
        "subtitulo": "Construcción de herramientas donde el usuario sube sus propios datos espaciales y los analiza en 2D y 3D",
        "demo_link": "./app_geoanalizador.py",
        "slides": [
            {
                "title": "1. ¿Cuándo elegir HTML/JS vs Python con Streamlit?",
                "left_title": "Visor HTML + JS + Leaflet (Módulos 1, 2 y 4)",
                "left_items": [
                    "Corre 100% en el navegador del visitante (velocidad instantánea).",
                    "Se aloja gratis de forma ilimitada en GitHub Pages.",
                    "Ideal para visores públicos, portafolios y tableros con datos pre-cargados.",
                    "No requiere servidor de Python encendido."
                ],
                "right_title": "Web App Python + Streamlit (Módulo 5)",
                "right_items": [
                    "Permite ejecutar todo el poder científico de Python (Pandas, GeoPandas, Scikit-Learn) en vivo.",
                    "Convertir un script de Python en una página web toma solo 15 líneas de código.",
                    "Ideal para herramientas donde el usuario sube un Excel/CSV/GeoJSON para procesarlo.",
                    "Se despliega gratis en Streamlit Community Cloud conectado a tu GitHub."
                ],
                "note": "Un especialista completo de SELPER domina ambos mundos y elige la herramienta según la necesidad del proyecto."
            },
            {
                "title": "2. ¿Cómo funciona el Modelo Reactivo de Streamlit?",
                "left_title": "De Script a Interfaz Web sin HTML ni CSS",
                "left_items": [
                    "En Streamlit no escribes etiquetas <div> ni funciones complicadas de eventos.",
                    "Cada vez que el usuario mueve un control, Streamlit re-ejecuta el script de arriba a abajo.",
                    "Una variable recibe directamente el valor del control: region = st.sidebar.selectbox(...).",
                    "La IA genera scripts de Streamlit extremadamente compactos y fáciles de leer."
                ],
                "right_title": "Componentes Esenciales para Geomática",
                "right_items": [
                    "st.set_page_config(layout='wide'): Activa el modo de pantalla ancha.",
                    "st.sidebar: Crea el panel lateral retráctil para filtros y carga de archivos.",
                    "st.columns(4) + st.metric(): Crea la fila superior de tarjetas KPI.",
                    "st.tabs(['Mapa 3D', 'Mapa 2D', 'Gráficos']): Organiza la app en pestañas limpias."
                ],
                "note": "Para probar tu app localmente solo ejecutas en terminal: streamlit run app_geoanalizador.py"
            },
            {
                "title": "3. Carga Dinámica de Archivos del Usuario (st.file_uploader)",
                "left_title": "Democratizando el Análisis Espacial",
                "left_items": [
                    "Un técnico de campo toma datos con GPS y los guarda en un archivo CSV o Excel.",
                    "Con st.sidebar.file_uploader('Sube tu CSV', type=['csv']), puede arrastrarlo a tu app.",
                    "Si el usuario aún no ha subido nada, la app carga por defecto nuestro dataset de muestra.",
                    "Así la aplicación nunca se ve vacía al abrirla por primera vez."
                ],
                "right_title": "Validación Automática que pedimos en el Prompt",
                "right_items": [
                    "Verificar que existan las columnas de coordenadas (latitud / longitud).",
                    "Eliminar filas vacías con df.dropna(subset=['latitud', 'longitud']).",
                    "Detectar automáticamente las columnas numéricas para ofrecerlas en un selector.",
                    "Permitir descargar la tabla procesada y filtrada con st.download_button()."
                ],
                "note": "En el Prompt 5.1 pedimos siempre este patrón: 'Dataset de respaldo por defecto + file_uploader opcional'."
            },
            {
                "title": "4. Visualización Geoespacial 3D con PyDeck (Deck.gl)",
                "left_title": "¿Qué es PyDeck?",
                "left_items": [
                    "Es la interfaz en Python de Deck.gl (creada por Uber para visualización espacial WebGL).",
                    "Viene integrada nativamente en Streamlit mediante st.pydeck_chart().",
                    "Permite inclinar la cámara (pitch=45) y rotar el mapa en 3 dimensiones.",
                    "Renderiza cientos de miles de elementos en 3D usando la tarjeta gráfica (GPU)."
                ],
                "right_title": "Capas 3D de Alto Impacto en Agricultura y Ambiente",
                "right_items": [
                    "ColumnLayer: Levanta cilindros 3D sobre cada lote o estación según una variable.",
                    "Ejemplo: La altura representa el Rendimiento (ton/ha), la Altitud (msnm) o el NDVI.",
                    "HexagonLayer: Agrupa puntos en celdas hexagonales 3D para medir densidad espacial.",
                    "Incluye tooltips interactivos al pasar el cursor sobre cada columna 3D."
                ],
                "note": "Mantén presionada la tecla Ctrl (o Cmd en Mac) + clic izquierdo y arrastra para girar el mapa 3D en PyDeck."
            },
            {
                "title": "5. Mapas 2D y Gráficos Analíticos con Plotly Express",
                "left_title": "Mapas Interactivos con px.scatter_mapbox",
                "left_items": [
                    "Plotly Express permite crear mapas 2D sin necesidad de token usando mapbox_style='carto-darkmatter'.",
                    "Codifica simultáneamente 2 variables: Color por tipo de cultivo y Tamaño por índice NDVI.",
                    "Incluye herramientas de selección por lazo (Lasso Select) y caja directamente en el mapa.",
                    "Se inserta en Streamlit con st.plotly_chart(fig, use_container_width=True)."
                ],
                "right_title": "Gráficos Estadísticos Conectados al Filtro",
                "right_items": [
                    "Gráfico de barras agrupadas: Comparativa de NDVI por Cultivo y Estado Fitosanitario.",
                    "Gráfico de dispersión (Scatter): Relación entre Humedad del Suelo (%) y Vigor NDVI.",
                    "Tabla interactiva ordenable con st.dataframe(df_filtrado).",
                    "Todo responde en milisegundos al cambiar la Región o los Cultivos en la barra lateral."
                ],
                "note": "Plotly incluye un botón de cámara en cada gráfico para descargar la figura en PNG de alta resolución para informes."
            },
            {
                "title": "6. Optimización y Archivo requirements.txt",
                "left_title": "Acelerando tu App con @st.cache_data",
                "left_items": [
                    "Si tu app carga un GeoJSON o CSV grande, no querrás leerlo del disco en cada clic.",
                    "Al decorar la función de lectura con @st.cache_data, Streamlit guarda el dato en memoria RAM.",
                    "Los filtros posteriores se ejecutan de forma instantánea.",
                    "Pídele siempre a la IA: 'Usa @st.cache_data para las funciones de carga de datos'."
                ],
                "right_title": "El Archivo requirements.txt para la Nube",
                "right_items": [
                    "Para que Streamlit Cloud sepa qué instalar en su servidor Linux, necesita requirements.txt.",
                    "Incluye únicamente las librerías externas importadas (streamlit, pandas, pydeck, plotly).",
                    "Evita poner librerías del sistema estándar de Python (como os, json, pathlib o math).",
                    "En este módulo ya dejamos creado requirements.txt listo para desplegar."
                ],
                "note": "Un requirements.txt limpio y minimalista garantiza que el despliegue en la nube tarde menos de 90 segundos."
            },
            {
                "title": "7. Resumen y Práctica del Módulo 5",
                "left_title": "Competencias Adquiridas",
                "left_items": [
                    "Criterio arquitectónico para elegir entre Leaflet (JS) y Streamlit (Python).",
                    "Construcción de aplicaciones con carga de archivos de usuario (file_uploader).",
                    "Visualización 3D de variables territoriales y agrícolas con PyDeck.",
                    "Integración de mapas y gráficos estadísticos interactivos con Plotly."
                ],
                "right_title": "Tu Reto Práctico Autodidacta",
                "right_items": [
                    "1. Revisa el código de app_geoanalizador.py en la carpeta del Módulo 5.",
                    "2. Ejecútalo con streamlit run app_geoanalizador.py o pruébalo en Streamlit Cloud.",
                    "3. Pídele a la IA agregar un filtro deslizante (st.slider) por Altitud (msnm).",
                    "4. Marca el Módulo 5 como completado en el portal."
                ],
                "note": "¡Vamos al último módulo: Módulo 6, donde publicaremos todo nuestro portafolio en internet gratis!"
            }
        ]
    },
    {
        "num": 6,
        "folder": "modulo-6-github-despliegue",
        "color_hex": "38BDF8",
        "badge": "MÓDULO 6 • 2.0 HORAS",
        "titulo": "Git, GitHub y Despliegue Gratuito en la Nube (GitHub Pages y Streamlit Cloud)",
        "subtitulo": "Publicación profesional de visores, resolución de errores CORS/rutas y creación de tu portafolio SELPER",
        "demo_link": "../../index.html",
        "slides": [
            {
                "title": "1. ¿Por qué Git y GitHub son Indispensables en Geomática?",
                "left_title": "Más allá de guardar carpetas con nombres 'Final_v2_ahora_si'",
                "left_items": [
                    "Git es un sistema de control de versiones: registra cada cambio en tu código y datos.",
                    "Si un nuevo prompt rompe tu visor, puedes regresar al estado exacto de hace 10 minutos.",
                    "GitHub es la plataforma en la nube donde alojas tus repositorios y colaboras.",
                    "Además, GitHub te regala alojamiento web gratuito (GitHub Pages) para tus visores."
                ],
                "right_title": "Los 4 Conceptos que debes conocer",
                "right_items": [
                    "1. Repositorio (Repo): La carpeta principal de tu proyecto (ej. GeoMapIA).",
                    "2. Commit: Una 'fotografía' guardada de tus avances con un mensaje descriptivo.",
                    "3. Rama principal (main): La línea oficial de tu proyecto lista para el público.",
                    "4. Push: Subir tus commits locales desde tu computador hacia GitHub.com."
                ],
                "note": "Puedes usar GitHub Desktop o el panel lateral de VS Code para hacer Commit y Push con un solo clic."
            },
            {
                "title": "2. Estructura Óptima de un Repositorio WebGIS",
                "left_title": "Organización Profesional de Carpetas",
                "left_items": [
                    "index.html en la raíz: Es la puerta de entrada que busca automáticamente GitHub Pages.",
                    "README.md: La portada técnica y comercial que explica qué hace tu proyecto.",
                    "/data: Carpeta dedicada a tus capas .geojson y .csv optimizados.",
                    "/modulos o /visores: Subcarpetas ordenadas para cada visor o dashboard."
                ],
                "right_title": "Buenas Prácticas de Nombres de Archivo",
                "right_items": [
                    "Usa siempre minúsculas y guiones medios: visor-catastral.html (nunca espacios ni tildes).",
                    "⚠️ En Windows/Mac 'Datos.geojson' y 'datos.geojson' parecen iguales, pero en Linux (GitHub) son distintos.",
                    "Incluye un archivo .gitignore para no subir archivos temporales (.DS_Store, __pycache__).",
                    "Mantén cada archivo GeoJSON por debajo de 10-15 MB para carga rápida."
                ],
                "note": "Una estructura limpia facilita que tanto tus colegas de SELPER como la IA entiendan tu proyecto."
            },
            {
                "title": "3. Despliegue de Visores HTML/JS en GitHub Pages",
                "left_title": "Paso a Paso (Toma menos de 2 minutos)",
                "left_items": [
                    "1. Entra a tu repositorio en GitHub.com (ej. github.com/tu-usuario/GeoMapIA).",
                    "2. Haz clic en la pestaña superior 'Settings' (Configuración).",
                    "3. En el menú izquierdo, selecciona la sección 'Pages'.",
                    "4. En 'Branch', elige 'main' y carpeta '/ (root)', y presiona 'Save'."
                ],
                "right_title": "¿Qué ocurre automáticamente?",
                "right_items": [
                    "GitHub compila y publica tu sitio bajo certificado de seguridad HTTPS gratuito.",
                    "Obtienes tu URL pública: https://tu-usuario.github.io/GeoMapIA/",
                    "Cada vez que hagas un nuevo 'git push' desde tu PC, la web se actualizará sola en 1 minuto.",
                    "Puedes compartir ese enlace por WhatsApp, correo, informes o LinkedIn."
                ],
                "note": "Alternativas gratuitas adicionales con conexión directa a GitHub: Vercel y Netlify."
            },
            {
                "title": "4. Solución a los 3 Errores Clásicos en Producción",
                "left_title": "Error 1 y 2: Rutas Rotas y Bloqueo CORS",
                "left_items": [
                    "Error de ruta absoluta: usar fetch('/data/capa.geojson') falla en subcarpetas de GitHub Pages.",
                    "Solución: Usar siempre ruta relativa con punto inicial: fetch('./data/capa.geojson').",
                    "Error CORS local: abrir con doble clic (file://) bloquea fetch().",
                    "Al subirlo a GitHub Pages (https://), ¡el error CORS desaparece porque ya es un servidor real!"
                ],
                "right_title": "Error 3: Contenido Mixto (Mixed Content HTTP vs HTTPS)",
                "right_items": [
                    "GitHub Pages corre sobre HTTPS seguro.",
                    "Si conectas un servicio WMS o librería con 'http://' (sin la s), el navegador lo bloqueará.",
                    "Asegúrate de que todos los enlaces CDN y servicios WMS usen 'https://'.",
                    "Consulta nuestra GUIA_SOLUCION_ERRORES.md para los prompts reparadores."
                ],
                "note": "Si algo no carga en GitHub Pages, abre F12 -> pestaña Network (Red) y busca líneas en color rojo (Error 404)."
            },
            {
                "title": "5. Despliegue de Apps Python en Streamlit Community Cloud",
                "left_title": "Por qué GitHub Pages no ejecuta Python",
                "left_items": [
                    "GitHub Pages es un servidor de archivos estáticos (ejecuta HTML, CSS y JS en el navegador).",
                    "Una aplicación de Streamlit (.py) requiere un servidor con un intérprete de Python vivo.",
                    "Para eso existe Streamlit Community Cloud (share.streamlit.io), 100% gratuito.",
                    "Se conecta directamente a tu mismo repositorio de GitHub."
                ],
                "right_title": "Los 3 Pasos en share.streamlit.io",
                "right_items": [
                    "1. Inicia sesión con tu cuenta de GitHub y haz clic en 'Create app'.",
                    "2. Elige tu repositorio (GeoMapIA) y la rama 'main'.",
                    "3. Indica la ruta del archivo: modulos/modulo-5-streamlit-python-apps/app_geoanalizador.py.",
                    "Streamlit leerá automáticamente el requirements.txt y publicará tu URL pública."
                ],
                "note": "Cualquier cambio que subas a GitHub actualizará en vivo tu aplicación de Streamlit sin reiniciar nada."
            },
            {
                "title": "6. Tu Portafolio Geoespacial y Cierre del Curso SELPER",
                "left_title": "Documentación de Alto Impacto con IA",
                "left_items": [
                    "Un buen proyecto sin un buen README.md pasa desapercibido.",
                    "Usa el Prompt 6.2 de nuestro Playbook para generar insignias, descripción técnica y créditos.",
                    "Personaliza el archivo index.html de este curso para convertirlo en tu Hub Cartográfico personal.",
                    "Enlaza tus 4 casos aplicados: Ambiental/Satelital, Catastro, Gestión del Riesgo y Agro 3D."
                ],
                "right_title": "Tu Nueva Capacidad como Profesional AI-First",
                "right_items": [
                    "Pasaste de consumidor de software SIG cerrado a creador de plataformas web abiertas.",
                    "Dominas la fórmula C-T-D-E para comunicarte con cualquier modelo presente o futuro.",
                    "Sabes integrar Leaflet, Turf.js, Chart.js, GeoPandas, Streamlit y GitHub.",
                    "¡Comparte tus visores con la comunidad de SELPER Colombia (selper.org.co)!"
                ],
                "note": "¡Felicitaciones por completar las 14 horas del Curso Autodidacta GeoMapIA — SELPER Colombia!"
            }
        ]
    }
]


def build_title_slide_xml(mod: dict, total_slides: int) -> str:
    """Construye el XML OpenXML nativo para la diapositiva de portada del módulo."""
    color = mod["color_hex"]
    badge = html.escape(mod["badge"])
    titulo = html.escape(mod["titulo"])
    subtitulo = html.escape(mod["subtitulo"])

    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
       xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
       xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld>
    <p:bg>
      <p:bgPr>
        <a:solidFill><a:srgbClr val="0F172A"/></a:solidFill>
        <a:effectLst/>
      </p:bgPr>
    </p:bg>
    <p:spTree>
      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
      <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>

      <!-- Barra superior de color del módulo -->
      <p:sp>
        <p:nvSpPr><p:cNvPr id="2" name="TopBar"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="0" y="0"/><a:ext cx="9144000" cy="140000"/></a:xfrm>
          <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
          <a:solidFill><a:srgbClr val="{color}"/></a:solidFill>
        </p:spPr>
      </p:sp>

      <!-- Tarjeta Central de Portada -->
      <p:sp>
        <p:nvSpPr><p:cNvPr id="3" name="HeroCard"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="550000" y="750000"/><a:ext cx="8044000" cy="3600000"/></a:xfrm>
          <a:prstGeom prst="roundRect"><a:avLst/></a:prstGeom>
          <a:solidFill><a:srgbClr val="1E293B"/></a:solidFill>
          <a:ln w="19050"><a:solidFill><a:srgbClr val="{color}"/></a:solidFill></a:ln>
        </p:spPr>
        <p:txBody>
          <a:bodyPr lIns="360000" rIns="360000" tIns="320000" bIns="320000" anchor="ctr"/>
          <a:lstStyle/>
          <a:p>
            <a:r>
              <a:rPr lang="es-CO" sz="1300" b="1"><a:solidFill><a:srgbClr val="{color}"/></a:solidFill></a:rPr>
              <a:t>🛰️ CURSO AUTODIDACTA GEOMAPIA • SELPER COLOMBIA ({badge})</a:t>
            </a:r>
          </a:p>
          <a:p>
            <a:pPr spcBef="180000"/>
            <a:r>
              <a:rPr lang="es-CO" sz="2800" b="1"><a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill></a:rPr>
              <a:t>{titulo}</a:t>
            </a:r>
          </a:p>
          <a:p>
            <a:pPr spcBef="200000"/>
            <a:r>
              <a:rPr lang="es-CO" sz="1500"><a:solidFill><a:srgbClr val="94A3B8"/></a:solidFill></a:rPr>
              <a:t>{subtitulo}</a:t>
            </a:r>
          </a:p>
          <a:p>
            <a:pPr spcBef="260000"/>
            <a:r>
              <a:rPr lang="es-CO" sz="1200" b="1"><a:solidFill><a:srgbClr val="38BDF8"/></a:solidFill></a:rPr>
              <a:t>Sociedad Latinoamericana en Percepción Remota y Sistemas de Información Espacial — https://selper.org.co/</a:t>
            </a:r>
          </a:p>
        </p:txBody>
      </p:sp>

      <!-- Footer -->
      <p:sp>
        <p:nvSpPr><p:cNvPr id="4" name="Footer"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="550000" y="4620000"/><a:ext cx="8044000" cy="360000"/></a:xfrm>
          <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
          <a:noFill/>
        </p:spPr>
        <p:txBody>
          <a:bodyPr/>
          <a:lstStyle/>
          <a:p>
            <a:r>
              <a:rPr lang="es-CO" sz="1050"><a:solidFill><a:srgbClr val="64748B"/></a:solidFill></a:rPr>
              <a:t>Presentación Teórica y Práctica • Diapositiva 1 de {total_slides}</a:t>
            </a:r>
          </a:p>
        </p:txBody>
      </p:sp>
    </p:spTree>
  </p:cSld>
</p:sld>'''


def build_content_slide_xml(mod: dict, s: dict, idx: int, total_slides: int) -> str:
    """Construye el XML OpenXML de una diapositiva de contenido a 2 columnas con nota clave inferior."""
    color = mod["color_hex"]
    badge = html.escape(mod["badge"])
    slide_title = html.escape(s["title"])
    left_title = html.escape(s["left_title"])
    right_title = html.escape(s["right_title"])
    note = html.escape(s["note"])

    def build_bullets(items):
        out = []
        for item in items:
            txt = html.escape(item)
            out.append(f'''
          <a:p>
            <a:pPr spcBef="90000"/>
            <a:r>
              <a:rPr lang="es-CO" sz="1250"><a:solidFill><a:srgbClr val="E2E8F0"/></a:solidFill></a:rPr>
              <a:t>▸ {txt}</a:t>
            </a:r>
          </a:p>''')
        return "".join(out)

    left_paragraphs = build_bullets(s["left_items"])
    right_paragraphs = build_bullets(s["right_items"])

    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
       xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
       xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld>
    <p:bg>
      <p:bgPr>
        <a:solidFill><a:srgbClr val="0F172A"/></a:solidFill>
        <a:effectLst/>
      </p:bgPr>
    </p:bg>
    <p:spTree>
      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
      <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>

      <!-- Barra superior de acento -->
      <p:sp>
        <p:nvSpPr><p:cNvPr id="2" name="TopBar"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="0" y="0"/><a:ext cx="9144000" cy="95000"/></a:xfrm>
          <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
          <a:solidFill><a:srgbClr val="{color}"/></a:solidFill>
        </p:spPr>
      </p:sp>

      <!-- Encabezado de la Diapositiva -->
      <p:sp>
        <p:nvSpPr><p:cNvPr id="3" name="Header"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="420000" y="180000"/><a:ext cx="8300000" cy="720000"/></a:xfrm>
          <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
          <a:noFill/>
        </p:spPr>
        <p:txBody>
          <a:bodyPr/>
          <a:lstStyle/>
          <a:p>
            <a:r>
              <a:rPr lang="es-CO" sz="1050" b="1"><a:solidFill><a:srgbClr val="{color}"/></a:solidFill></a:rPr>
              <a:t>{badge} • TEORÍA Y ARQUITECTURA GEOMAPIA</a:t>
            </a:r>
          </a:p>
          <a:p>
            <a:pPr spcBef="40000"/>
            <a:r>
              <a:rPr lang="es-CO" sz="2100" b="1"><a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill></a:rPr>
              <a:t>{slide_title}</a:t>
            </a:r>
          </a:p>
        </p:txBody>
      </p:sp>

      <!-- Columna Izquierda -->
      <p:sp>
        <p:nvSpPr><p:cNvPr id="4" name="LeftCol"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="420000" y="980000"/><a:ext cx="4020000" cy="3050000"/></a:xfrm>
          <a:prstGeom prst="roundRect"><a:avLst/></a:prstGeom>
          <a:solidFill><a:srgbClr val="1E293B"/></a:solidFill>
          <a:ln w="12700"><a:solidFill><a:srgbClr val="334155"/></a:solidFill></a:ln>
        </p:spPr>
        <p:txBody>
          <a:bodyPr lIns="200000" rIns="200000" tIns="180000" bIns="180000"/>
          <a:lstStyle/>
          <a:p>
            <a:r>
              <a:rPr lang="es-CO" sz="1450" b="1"><a:solidFill><a:srgbClr val="38BDF8"/></a:solidFill></a:rPr>
              <a:t>{left_title}</a:t>
            </a:r>
          </a:p>{left_paragraphs}
        </p:txBody>
      </p:sp>

      <!-- Columna Derecha -->
      <p:sp>
        <p:nvSpPr><p:cNvPr id="5" name="RightCol"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="4700000" y="980000"/><a:ext cx="4020000" cy="3050000"/></a:xfrm>
          <a:prstGeom prst="roundRect"><a:avLst/></a:prstGeom>
          <a:solidFill><a:srgbClr val="1E293B"/></a:solidFill>
          <a:ln w="12700"><a:solidFill><a:srgbClr val="{color}"/></a:solidFill></a:ln>
        </p:spPr>
        <p:txBody>
          <a:bodyPr lIns="200000" rIns="200000" tIns="180000" bIns="180000"/>
          <a:lstStyle/>
          <a:p>
            <a:r>
              <a:rPr lang="es-CO" sz="1450" b="1"><a:solidFill><a:srgbClr val="34D399"/></a:solidFill></a:rPr>
              <a:t>{right_title}</a:t>
            </a:r>
          </a:p>{right_paragraphs}
        </p:txBody>
      </p:sp>

      <!-- Caja Inferior de Concepto Clave -->
      <p:sp>
        <p:nvSpPr><p:cNvPr id="6" name="BottomNote"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="420000" y="4160000"/><a:ext cx="8300000" cy="540000"/></a:xfrm>
          <a:prstGeom prst="roundRect"><a:avLst/></a:prstGeom>
          <a:solidFill><a:srgbClr val="090D16"/></a:solidFill>
          <a:ln w="12700"><a:solidFill><a:srgbClr val="{color}"/></a:solidFill></a:ln>
        </p:spPr>
        <p:txBody>
          <a:bodyPr lIns="180000" rIns="180000" anchor="ctr"/>
          <a:lstStyle/>
          <a:p>
            <a:r>
              <a:rPr lang="es-CO" sz="1200" b="1"><a:solidFill><a:srgbClr val="FBBF24"/></a:solidFill></a:rPr>
              <a:t>💡 CONCEPTO CLAVE: </a:t>
            </a:r>
            <a:r>
              <a:rPr lang="es-CO" sz="1200"><a:solidFill><a:srgbClr val="F8FAFC"/></a:solidFill></a:rPr>
              <a:t>{note}</a:t>
            </a:r>
          </a:p>
        </p:txBody>
      </p:sp>

      <!-- Pie de Diapositiva -->
      <p:sp>
        <p:nvSpPr><p:cNvPr id="7" name="Footer"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="420000" y="4760000"/><a:ext cx="8300000" cy="300000"/></a:xfrm>
          <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
          <a:noFill/>
        </p:spPr>
        <p:txBody>
          <a:bodyPr/>
          <a:lstStyle/>
          <a:p>
            <a:r>
              <a:rPr lang="es-CO" sz="950"><a:solidFill><a:srgbClr val="64748B"/></a:solidFill></a:rPr>
              <a:t>SELPER Colombia (selper.org.co) • Curso Autodidacta GeoMapIA • Diapositiva {idx} de {total_slides}</a:t>
            </a:r>
          </a:p>
        </p:txBody>
      </p:sp>
    </p:spTree>
  </p:cSld>
</p:sld>'''


def crear_pptx_modulo(mod: dict, out_pptx_path: Path) -> None:
    """Usa pandoc para generar el contenedor .pptx con el número exacto de diapositivas y luego inyecta el diseño OpenXML."""
    total_slides = 1 + len(mod["slides"])
    # Generar markdown con exactamente `total_slides` diapositivas de nivel 2
    md_blocks = [f"## Portada Modulo {mod['num']}\n\n- SELPER\n"]
    for i, s in enumerate(mod["slides"], start=2):
        md_blocks.append(f"## Slide {i}\n\n- Contenido\n")
    raw_md = "\n".join(md_blocks)

    tmp_pptx = Path(f"/tmp/base_mod_{mod['num']}.pptx")
    subprocess.run(
        [PANDOC_BIN, "-f", "markdown", "-t", "pptx", "--slide-level=2", "-o", str(tmp_pptx)],
        input=raw_md.encode("utf-8"),
        check=True,
    )

    # Reemplazar cada slideN.xml con nuestro XML rico y estilizado
    with zipfile.ZipFile(tmp_pptx, "r") as zin, zipfile.ZipFile(out_pptx_path, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            if item.filename == "ppt/slides/slide1.xml":
                zout.writestr(item, build_title_slide_xml(mod, total_slides).encode("utf-8"))
            elif item.filename.startswith("ppt/slides/slide") and item.filename.endswith(".xml"):
                num_str = item.filename.replace("ppt/slides/slide", "").replace(".xml", "")
                s_idx = int(num_str)
                if 2 <= s_idx <= total_slides:
                    slide_data = mod["slides"][s_idx - 2]
                    zout.writestr(
                        item,
                        build_content_slide_xml(mod, slide_data, s_idx, total_slides).encode("utf-8"),
                    )
                else:
                    zout.writestr(item, zin.read(item.filename))
            else:
                zout.writestr(item, zin.read(item.filename))


def crear_html_reveal_modulo(mod: dict, out_html_path: Path, pptx_filename: str) -> None:
    """Crea una presentación web interactiva con Reveal.js + Tailwind y botón de descarga del archivo .pptx."""
    total_slides = 1 + len(mod["slides"])
    sections_html = []

    # Diapositiva 1: Portada
    sections_html.append(f"""
      <section>
        <div class="max-w-5xl mx-auto bg-slate-900/95 border-2 rounded-3xl p-10 text-left shadow-2xl" style="border-color: #{mod['color_hex']}">
          <div class="inline-block text-xs font-extrabold uppercase tracking-widest px-3 py-1 rounded-full mb-4" style="background: #{mod['color_hex']}22; color: #{mod['color_hex']}; border: 1px solid #{mod['color_hex']}66;">
            🛰️ CURSO AUTODIDACTA GEOMAPIA • {html.escape(mod['badge'])}
          </div>
          <h1 class="!text-3xl md:!text-5xl font-extrabold text-white leading-tight mb-4">
            {html.escape(mod['titulo'])}
          </h1>
          <p class="!text-base md:!text-xl text-slate-300 mb-6">
            {html.escape(mod['subtitulo'])}
          </p>
          <div class="flex flex-wrap items-center justify-between gap-4 pt-6 border-t border-slate-800 text-xs text-slate-400">
            <span>Sociedad Latinoamericana en Percepción Remota y Sistemas de Información Espacial (<a href="https://selper.org.co/" target="_blank" class="text-sky-400 underline">SELPER Colombia</a>)</span>
            <span class="text-slate-300 font-semibold">Usa las flechas ⬅️ ➡️ del teclado para avanzar ({total_slides} diapositivas)</span>
          </div>
        </div>
      </section>
    """)

    # Diapositivas de contenido
    for idx, s in enumerate(mod["slides"], start=2):
        left_li = "".join(
            f'<li class="flex items-start gap-2 text-slate-200"><span class="text-sky-400 font-bold">▸</span><span>{html.escape(it)}</span></li>'
            for it in s["left_items"]
        )
        right_li = "".join(
            f'<li class="flex items-start gap-2 text-slate-200"><span class="text-emerald-400 font-bold">▸</span><span>{html.escape(it)}</span></li>'
            for it in s["right_items"]
        )

        sections_html.append(f"""
      <section>
        <div class="max-w-6xl mx-auto text-left">
          <div class="flex items-center justify-between mb-2">
            <span class="text-xs font-extrabold uppercase tracking-wider" style="color: #{mod['color_hex']}">
              {html.escape(mod['badge'])} • TEORÍA Y FUNDAMENTOS
            </span>
            <span class="text-xs text-slate-400 font-mono">Diapositiva {idx} / {total_slides}</span>
          </div>
          <h2 class="!text-2xl md:!text-3xl font-extrabold text-white mb-5">
            {html.escape(s['title'])}
          </h2>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-5 mb-5">
            <div class="bg-slate-900/90 border border-slate-700 rounded-2xl p-6">
              <h3 class="!text-base md:!text-lg font-bold text-sky-400 mb-3 border-b border-slate-800 pb-2">
                {html.escape(s['left_title'])}
              </h3>
              <ul class="space-y-2.5 !text-xs md:!text-sm leading-relaxed list-none !ml-0">
                {left_li}
              </ul>
            </div>

            <div class="bg-slate-900/90 border rounded-2xl p-6" style="border-color: #{mod['color_hex']}88">
              <h3 class="!text-base md:!text-lg font-bold text-emerald-400 mb-3 border-b border-slate-800 pb-2">
                {html.escape(s['right_title'])}
              </h3>
              <ul class="space-y-2.5 !text-xs md:!text-sm leading-relaxed list-none !ml-0">
                {right_li}
              </ul>
            </div>
          </div>

          <div class="bg-slate-950 border rounded-xl p-4 !text-xs md:!text-sm text-slate-200 flex items-center gap-3" style="border-color: #{mod['color_hex']}66">
            <span class="text-amber-400 font-bold shrink-0">💡 CONCEPTO CLAVE:</span>
            <span>{html.escape(s['note'])}</span>
          </div>
        </div>
      </section>
        """)

    html_doc = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Presentación Módulo {mod['num']} — {html.escape(mod['titulo'])} | SELPER Colombia</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.css" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/theme/black.css" />
  <style>
    body {{ background-color: #020617; }}
    .reveal .slides {{ text-align: left; }}
    .reveal h1, .reveal h2, .reveal h3 {{ text-transform: none; font-family: ui-sans-serif, system-ui, sans-serif; }}
  </style>
</head>
<body class="bg-slate-950 text-slate-100">

  <!-- Barra Superior Fija con Descarga de PowerPoint (.pptx) -->
  <header class="fixed top-0 left-0 right-0 h-12 bg-slate-900/90 backdrop-blur border-b border-slate-800 px-4 flex items-center justify-between z-50 text-xs">
    <div class="flex items-center gap-3">
      <a href="../../index.html" class="bg-slate-800 hover:bg-slate-700 text-sky-400 px-3 py-1 rounded-lg font-semibold border border-slate-700">
        ← Portal Curso
      </a>
      <span class="font-bold text-white truncate max-w-md">
        📽️ Presentación Teórica — Módulo {mod['num']}: {html.escape(mod['titulo'])}
      </span>
    </div>
    <div class="flex items-center gap-2">
      <a href="./{pptx_filename}" download class="bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold px-3 py-1 rounded-lg shadow transition flex items-center gap-1">
        ⬇️ Descargar PowerPoint (.pptx)
      </a>
      <a href="{mod['demo_link']}" class="bg-sky-600 hover:bg-sky-500 text-white font-semibold px-3 py-1 rounded-lg transition hidden sm:inline-block">
        🚀 Ir al Laboratorio Práctico →
      </a>
    </div>
  </header>

  <div class="reveal pt-6">
    <div class="slides">
      {"".join(sections_html)}
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.js"></script>
  <script>
    Reveal.initialize({{
      hash: true,
      slideNumber: 'c/t',
      controls: true,
      progress: true,
      center: true,
      width: 1280,
      height: 720,
      margin: 0.06
    }});
  </script>
</body>
</html>"""

    out_html_path.write_text(html_doc, encoding="utf-8")


def main():
    for mod in MODULOS_SLIDES:
        mod_dir = BASE_DIR / "modulos" / mod["folder"]
        pptx_name = f"presentacion-modulo-{mod['num']}.pptx"
        html_name = f"presentacion-modulo-{mod['num']}.html"

        out_pptx = mod_dir / pptx_name
        out_html = mod_dir / html_name

        crear_pptx_modulo(mod, out_pptx)
        crear_html_reveal_modulo(mod, out_html, pptx_name)
        print(f"[OK] Módulo {mod['num']}: {out_pptx.name} ({out_pptx.stat().st_size // 1024} KB) + {out_html.name}")


if __name__ == "__main__":
    main()
