# 🧠 Módulo 1: Mentalidad *AI-First*, Entorno de Trabajo e Ingeniería de Prompts para SIG y Teledetección

- **Duración estimada:** 2.0 Horas
- **Modalidad:** Autodidacta (*Self-Paced*)
- **Entregable del módulo:** [`visor-basico-selper.html`](./visor-basico-selper.html) (Tu primer visor interactivo de estaciones ambientales en Colombia generado con un solo prompt).

---

## 🎯 1. Objetivo de Aprendizaje
Al finalizar este módulo serás capaz de:
1. Configurar tu entorno de desarrollo gratuito para previsualizar visores web en segundos.
2. Comprender cómo se conectan **HTML**, **CSS**, **JavaScript (Leaflet)** y los formatos geoespaciales (**GeoJSON**, **WMS**, **EPSG:4326**).
3. Redactar *prompts* estructurados bajo la fórmula **C-T-D-E** para que Claude, Gemini o ChatGPT escriban código cartográfico sin errores.

---

## 🛠️ 2. Preparación de tu Entorno (15 minutos)

No necesitas instalar servidores complejos. Solo asegúrate de tener:
1. **Un navegador moderno:** Google Chrome, Brave, Edge o Firefox (usaremos la tecla `F12` para ver la consola si algo falla).
2. **Un editor de texto (Recomendado):** [Visual Studio Code](https://code.visualstudio.com/) con la extensión gratuita **Live Server** (de Ritwick Dey).
3. **Tu cuenta en al menos un asistente de IA:**
   - **Claude (Anthropic):** Ideal por su función *Artifacts*, que te permite ver el mapa funcionando dentro del mismo chat.
   - **Gemini (Google):** Ideal cuando necesitas adjuntar archivos GeoJSON/CSV grandes o capturas de pantalla de referencia.
   - **ChatGPT (OpenAI):** Excelente para iterar código rápidamente y explicar conceptos paso a paso.

---

## 🧩 3. La Anatomía de un Visor Web (20 minutos)

Cuando le pides un visor a la IA, ella genera 3 piezas que pueden vivir dentro de **un único archivo `.html`** para empezar:

| Componente | ¿Qué papel cumple en tu visor? | Ejemplo en el mundo SIG |
| :--- | :--- | :--- |
| **HTML** | Es el esqueleto donde se dibuja el mapa y los botones. | El marco de composición (`<div id="map"></div>`). |
| **CSS (Tailwind)** | Define tamaños, colores, leyendas flotantes y modo oscuro. | Que el mapa ocupe el `100%` de la pantalla (`100vh`). |
| **JavaScript (Leaflet.js)** | Carga los mapas base, dibuja puntos/polígonos y abre *popups*. | El motor de renderizado de tu proyecto en el navegador. |

> ⚠️ **Regla de Oro Geoespacial para la Web:**
> Todos los visores web en **Leaflet** trabajan por defecto en coordenadas geográficas **WGS84 (`EPSG:4326`)**. Si tus datos están en **MAGNA-SIRGAS Origen Nacional (`EPSG:9377`)**, primero le pediremos a la IA que los convierta (lo haremos a fondo en el Módulo 3).

---

## 🤖 4. El Método C-T-D-E de Ingeniería de Prompts Geoespaciales (35 minutos)

El error más común al usar IA es escribir: *"Hazme un mapa de Colombia con estaciones"*. Eso produce código incompleto. En cambio, usa siempre los **4 bloques C-T-D-E**:

1. **[C] Contexto:** Define el rol experto (*"Actúa como un desarrollador WebGIS Senior de SELPER Colombia..."*).
2. **[T] Tecnología:** Especifica librerías y formato de entrega (*"En un solo archivo HTML autocontenido usando Leaflet 1.9.4 y Tailwind CSS por CDN..."*).
3. **[D] Datos:** Describe exactamente los campos y coordenadas (*"Incluye 12 estaciones en Colombia con campos: nombre, region, ndvi, precipitacion_mm, alerta y coordenadas [lat, lon] en EPSG:4326..."*).
4. **[E] Estilo y Comportamiento:** Detalla qué quieres ver e interactuar (*"Agrega selector de capas Satélite/Oscuro/OSM, marcadores coloreados por nivel de alerta, leyenda flotante y botón de regresar a la vista general de Colombia"*).

---

## 💻 5. Práctica Guiada Paso a Paso (35 minutos)

### Paso 1: Copia y ejecuta tu primer Mega-Prompt
Abre Claude o Gemini, copia el **Prompt 1.1** de nuestro [`PROMPT_PLAYBOOK.md`](../../PROMPT_PLAYBOOK.md) y envíalo.

### Paso 2: Guarda y abre el resultado
1. Copia el código HTML que te entregó la IA.
2. Guárdalo en tu computadora como `mi-primer-visor.html` (o abre directamente nuestra solución de referencia [`visor-basico-selper.html`](./visor-basico-selper.html)).
3. Ábrelo en tu navegador haciendo doble clic o con *Open with Live Server*.

### Paso 3: Itera con un segundo Prompt
Pídele a la IA en el mismo chat:
> *"Agrega en la cabecera unos botones para filtrar las estaciones por nivel de alerta (Todas, Alta, Media, Baja) y un botón de 'Mi Ubicación GPS'."*

*(Observa cómo en [`visor-basico-selper.html`](./visor-basico-selper.html) ya hemos incluido estas mejoras para que compares tu resultado).*

---

## ✅ 6. Reto de Autoevaluación del Módulo 1 (15 minutos)

Antes de pasar al Módulo 2, verifica que lograste lo siguiente pidiéndoselo a la IA:
- [ ] Tu mapa abre a pantalla completa sin barras de desplazamiento innecesarias.
- [ ] Puedes alternar entre el mapa base **Satelital (Esri World Imagery)** y **Modo Oscuro (CartoDB Dark)**.
- [ ] Al hacer clic en una estación de monitoreo, se despliega un *Popup* con su valor de **NDVI**, **Precipitación** y **Región**.
- [ ] **Mini-Reto:** Pídele a la IA que agregue una estación adicional en tu municipio o ciudad natal con tus propios datos y verifica que aparezca en el mapa.

👉 **[Ir al Módulo 2: Creación de Visores Interactivos con HTML, JS y Leaflet](../modulo-2-visores-leaflet/README.md)**

