# Quindío Travel - Plataforma de Turismo Digital Eje Cafetero

Agencia de viajes turísticos especializada en el Eje Cafetero colombiano con RNT 18152. Plataforma híbrida frontend estático + backend dinámico.

## 🚀 Características Principales

- **Frontend Estático:** HTML5, CSS3, JavaScript Vanilla
- **Backend Dinámico:** Node.js/Express para chatbot con IA
- **SEO Avanzado:** Schema.org, sitemaps múltimples, optimización Core Web Vitals
- **Sistema de Cotización:** Motor dinámico de precios con JSON
- **Chatbot IA:** "Don Chucho" - Asistente de viajes con fallback local
- **Multi-idioma:** Español, Inglés, Portugués, Francés

## 📁 Estructura del Proyecto

```
quindiotravel.com.co/
├── index.html                    # Página principal (6,706 líneas)
├── planes.html                   # Sistema de planes turísticos
├── components/                   # Sistema modular
│   ├── header/header.html
│   ├── footer/footer.html
│   └── sections/ [16 secciones]
├── assets/                      # Recursos digitales
│   ├── images/ [479+ imágenes]
│   ├── js/ [24 scripts]
│   └── css/ [3 archivos]
├── blog/                        # Contenido SEO (30 artículos)
├── en/                          # Versión en inglés
├── don-chucho-backend/          # Sistema de chatbot con IA
├── competitive-engine/          # Sistema de SEO técnico (Python)
├── docs/                        # Documentación técnica
└── scripts/                     # Scripts de automatización
```

## 🛠️ Instalación y Desarrollo

### Requisitos Previos
- Node.js >= 18.0.0
- npm >= 9.0.0
- Python 3.x (para competitive-engine)

### Instalación
```bash
# Instalar dependencias
npm install

# Instalar dependencias de Python (opcional)
cd competitive-engine
pip install -r requirements.txt
```

### Scripts Disponibles
```bash
# Desarrollo
npm run dev

# Build
npm run build

# Optimizar assets
npm run optimize:assets

# Generar favicons
node scripts/generate-favicons.js

# Análisis SEO
node scripts/analyze-all-sitemaps.js
node scripts/analyze-canonical.js
```

## 🤖 Sistema Don Chucho (Chatbot IA)

### Backend Setup
```bash
cd don-chucho-backend
npm install
cp .env.example .env
# Configurar variables de entorno en .env
npm start
```

### Variables de Entorno Requeridas
- `MONGODB_URI`
- `DB_NAME`
- `API_KEY`
- `QUINDIO_WHATSAPP`
- `OPENAI_API_KEY` (opcional)

## 📊 SEO y Sitemaps

### Sitemaps Activos
- `sitemap.xml` - Principal (104 URLs válidas)
- `sitemap-main.xml` - Páginas principales
- `sitemap-content.xml` - Contenido estructurado

### Scripts de Análisis
- `scripts/analyze-sitemap-404.js` - Detectar URLs 404
- `scripts/analyze-canonical.js` - Verificar canonical tags
- `scripts/analyze-all-sitemaps.js` - Análisis completo

## 🎨 Sistema de Diseño

### Colores Principales
```css
--verde-cafe: #2E5A36
--verde-claro: #4E8755
--blanco: #FFFFFF
--amarillo-suave: #E6B800
--marron-madera: #8D5B4C
```

## 📝 Información del Negocio

- **RNT:** 18152
- **Teléfono:** +57-317-4426044
- **Dominio:** quindiotravel.com.co
- **Región:** Quindío, Eje Cafetero, Colombia

## 🔧 Mantenimiento

### Actualizar Precios
Editar `docs/data/tarifas.json`

### Generar Nuevas Páginas
Usar scripts en `competitive-engine/`

### Optimizar Imágenes
```bash
npm run optimize:assets
```

## 📄 Licencia

Propiedad de Quindío Travel - Álvaro Alzate Ortiz

## 🆘 Soporte

Para soporte técnico contactar al administrador del sistema.