# Quindío Travel - Plataforma de Turismo Digital Eje Cafetero

Agencia de viajes turísticos especializada en el Eje Cafetero colombiano con RNT 18152. Plataforma híbrida frontend estático + backend dinámico.

## 🚀 Características Principales

- **Frontend Estático:** HTML5, CSS3, JavaScript Vanilla (sin framework)
- **Despliegue:** GitHub Pages vía GitHub Actions (`.github/workflows/deploy.yml`)
- **SEO Avanzado:** Schema.org, sitemap, hreflang, optimización Core Web Vitals
- **Sistema de Cotización:** Motor dinámico de precios con `docs/data/tarifas.json`
- **Chatbot IA:** "Don Chucho" - Asistente de viajes con fallback local (solo desarrollo, no se publica)
- **Multi-idioma:** Español (`/`), Inglés (`/en/`), Chino (`/zh/`) con hreflang `es`, `es-CO`, `en`, `zh-CN`, `x-default`

## 📁 Estructura del Proyecto

```
quindiotravel.com.co/
├── index.html                    # Página principal (4,973 líneas)
├── planes.html                   # Sistema de planes turísticos
├── blog/                         # Hub + 30 artículos SEO
├── en/ (5) y zh/ (1)             # Versiones en inglés y chino
├── programmatic-pages/ (112)     # Páginas pSEO (redirigen a /)
├── generated-pages/ (13)         # Páginas generadas (redirigen a /)
├── components/                   # Sistema modular (header, footer, 23 secciones)
├── assets/
│   ├── images/ [480 imágenes]
│   ├── js/ [31 scripts]
│   └── css/ [9 archivos]
├── docs/data/tarifas.json        # Precios que consume el cotizador
├── tests/                        # Suites Jest
└── scripts/                      # Automatización (validación, imágenes, SEO)
```

Carpetas internas que **se conservan en el repositorio pero no se publican**:
`lead_automation_system/`, `competitive-engine/`, `documentation_archive/`,
`don-chucho-backend/`, `scripts/`, `components/`, `docs/` (salvo `docs/data/`).

## 🛠️ Instalación y Desarrollo

### Requisitos Previos
- Node.js >= 18.0.0
- npm >= 9.0.0
- Python 3.x (solo para `competitive-engine` y `scripts/seo_audit.py`)

### Instalación
```bash
npm install

# Opcional: dependencias de Python
cd competitive-engine && pip install -r requirements.txt
```

### Scripts Disponibles
```bash
# Desarrollo y build
npm run dev
npm run build

# Verificación (ejecutar antes de cada commit)
npm test                      # 6 tests (cotizador y formularios)
node scripts/validate-links.js   # enlaces rotos, imágenes sin alt, totales

# Imágenes
node scripts/compress-images.mjs            # recomprimir >1 MB (sharp)
node scripts/compress-images.mjs --min=400000 --dry
node scripts/optimize-img-tags.mjs --dry    # lazy/fetchpriority/width+height

# Otros
npm run optimize:assets        # minifica CSS/JS
npm run seo:audit              # auditoría SEO (Python)
node scripts/generate-favicons.js
node scripts/analyze-all-sitemaps.js
node scripts/analyze-canonical.js
```

## 🚀 Despliegue (GitHub Pages)

1. Cada `push` a `main` ejecuta `.github/workflows/deploy.yml`:
   `checkout` → **exclusiones** → `configure-pages` → `upload-pages-artifact` → `deploy-pages`.
2. **Pages usa `build_type: workflow`** (Settings → Pages → Source: GitHub Actions).
   Si se cambia a "deploy from branch", se publica la rama completa y reaparecen las carpetas internas.
3. El paso de exclusiones elimina del artifact: carpetas internas de la lista superior,
   `.htaccess`, `.gitignore`, `package.json`, `.env*`, `*.pyc` y `__pycache__/`
   (`docs/` conserva únicamente `docs/data/`).

Comprobación tras un deploy: `/.htaccess` y `/scripts/validate-links.js` deben dar **404**;
`/docs/data/tarifas.json` y `/sitemap-main.xml` deben dar **200**.

## 📊 SEO y Sitemaps

- `robots.txt` → `sitemap.xml` (índice) → `sitemap-main.xml` (**93 URLs**, sin duplicadas)
- `/blog/` tiene `noindex,follow` y canonical a `/blog.html`
- Los archivos thin duplicados redirigen con `noindex` + canonical + meta refresh
- 404 personalizado (`404.html`) con mapa de redirects JS (reglas del antiguo `.htaccess`,
  que GitHub Pages ignora)

## 🎨 Sistema de Diseño

```css
--verde-cafe: #2E5A36
--verde-claro: #4E8755
--blanco: #FFFFFF
--amarillo-suave: #F4D35E
--marron-madera: #8D5B4C
```

## 📝 Información del Negocio

- **RNT:** 18152
- **Teléfono:** +57-317-4426044
- **Dominio:** quindiotravel.com.co
- **Región:** Quindío, Eje Cafetero, Colombia

## 🔧 Mantenimiento

| Tarea | Cómo |
|---|---|
| Actualizar precios | Editar `docs/data/tarifas.json` (se publica y lo consume el cotizador) |
| Recomprimir imágenes | `node scripts/compress-images.mjs` |
| Optimizar etiquetas `<img>` | `node scripts/optimize-img-tags.mjs --dry` y sin `--dry` |
| Generar páginas pSEO | Scripts en `competitive-engine/` |
| Validar antes de subir | `npm test` + `node scripts/validate-links.js` + `npm run build` |

## 📄 Licencia

Propiedad de Quindío Travel - Álvaro Alzate Ortiz

## 🆘 Soporte

Para soporte técnico contactar al administrador del sistema.
