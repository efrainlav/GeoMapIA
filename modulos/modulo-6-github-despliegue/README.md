# ☁️ Módulo 6: Git, GitHub y Despliegue Gratuito en la Nube

- **Duración estimada:** 2.0 Horas
- **Modalidad:** Autodidacta (*Self-Paced*)
- **Entregable Final del Curso:** Tu **Portafolio Web Geoespacial SELPER** publicado en **GitHub Pages** (`https://tu-usuario.github.io/GeoMapIA/`) y tu aplicación de Python publicada en **Streamlit Community Cloud**.

---

## 🎯 1. Objetivo de Aprendizaje
Dominar la publicación de tus visores y dashboards en internet con una URL pública, segura (`https`) y 100% gratuita, para que puedas compartirlos con clientes, entidades públicas o en tu hoja de vida / LinkedIn.

---

## 📁 2. Estructura Limpia de un Proyecto Geoespacial en GitHub (30 minutos)

Antes de subir un proyecto a GitHub, verifica que tenga esta estructura ordenada (igual que este repositorio):

```text
GeoMapIA/
├── index.html                        # Portada / Hub principal (GitHub Pages busca este archivo)
├── README.md                         # Documentación profesional del repositorio
├── PROMPT_PLAYBOOK.md                # Tus prompts utilizados
├── data/                             # Capas GeoJSON y CSV optimizados (< 10 MB por archivo)
└── modulos/                          # Visores y dashboards individuales
```

---

## 🌐 3. Paso a Paso: Publicar en GitHub Pages en 2 Minutos (40 minutos)

1. Entra a tu repositorio en **GitHub.com**.
2. Haz clic en la pestaña superior **Settings** (Configuración).
3. En el menú lateral izquierdo, haz clic en **Pages**.
4. En la sección **Build and deployment** $\rightarrow$ **Branch**:
   - Selecciona la rama **`main`** y la carpeta **`/ (root)`**.
   - Haz clic en **Save**.
5. Espera 60 segundos y recarga la página: aparecerá tu enlace público oficial:
   `https://tu-usuario.github.io/GeoMapIA/`

---

## 🐍 4. Paso a Paso: Publicar tu App de Python en Streamlit Cloud (30 minutos)

Para publicar la aplicación del **Módulo 5 (`app_geoanalizador.py`)**:
1. Entra a [share.streamlit.io](https://share.streamlit.io/) e inicia sesión con tu cuenta de GitHub.
2. Haz clic en **Create app** $\rightarrow$ **Deploy a public app from GitHub**.
3. Selecciona este repositorio (`GeoMapIA`), rama `main`, y en **Main file path** escribe:
   `modulos/modulo-5-streamlit-python-apps/app_geoanalizador.py`
4. Haz clic en **Deploy!**. En 2 minutos tendrás tu aplicación analítica 2D/3D en Python corriendo en la nube gratis.

---

## 🏆 5. Proyecto Final Integrador SELPER (20 minutos)

¡Felicidades por llegar al final del curso! Para completar tu certificación autodidacta:
1. Abre el archivo [`index.html`](../../index.html) en la raíz de este proyecto (nuestro Portal Interactivo).
2. Usa el **Prompt 6.2** de [`PROMPT_PLAYBOOK.md`](../../PROMPT_PLAYBOOK.md) para personalizar el portal con tu nombre, tu perfil profesional de SELPER y un visor propio de tu región o proyecto.
3. Súbelo a tu repositorio de GitHub y comparte el enlace de tu **GitHub Pages**.
