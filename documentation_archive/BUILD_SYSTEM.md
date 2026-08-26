# Sistema de Build - Quindío Travel

Este documento describe el sistema de build implementado con Vite para optimizar el proceso de desarrollo y despliegue del sitio Quindío Travel.

## 📋 Resumen

El sistema de build utiliza **Vite** como herramienta principal para:
- Compilar y optimizar assets (JS, CSS)
- Minificar automáticamente en producción
- Servir archivos estáticos con hot-reload en desarrollo
- Generar source maps para debugging
- Analizar el tamaño del bundle

## 🚀 Comandos Disponibles

### Desarrollo
```bash
npm run dev
```
Inicia el servidor de desarrollo en `http://localhost:3000` con:
- Hot Module Replacement (HMR)
- Source maps habilitados
- Recarga automática de cambios

### Build de Producción
```bash
npm run build
```
Compila el proyecto para producción:
- Minifica JS con Terser
- Optimiza CSS con cssnano
- Genera hashes para cache busting
- Output en directorio `dist/`

### Preview del Build
```bash
npm run preview
```
Previsualiza el build de producción localmente:
- Simula el entorno de producción
- Sirve desde `dist/`

### Análisis de Bundle
```bash
npm run build:analyze
```
Genera un reporte visual del bundle:
- Abre automáticamente un reporte interactivo
- Muestra tamaño gzip/brotli
- Identifica oportunidades de optimización

### Optimización de Assets
```bash
npm run optimize:assets
```
Minifica manualmente archivos CSS y JS:
- Genera versiones `.min.css` y `.min.js`
- Utiliza cssnano y Terser

## 📁 Estructura de Directorios

```
quindiotravel.com/
├── dist/                    # Output del build (generado)
│   ├── index.html
│   ├── assets/
│   │   ├── css/
│   │   ├── js/
│   │   ├── images/
│   │   └── videos/
│   └── ...                  # Otras páginas HTML
├── assets/                  # Assets originales
│   ├── css/
│   ├── js/
│   ├── images/
│   └── videos/
├── scripts/                 # Scripts de utilidad
│   └── optimize-assets.js
├── vite.config.js          # Configuración de Vite
├── postcss.config.js       # Configuración de PostCSS
└── package.json            # Dependencias y scripts
```

## ⚙️ Configuración

### Vite Config (`vite.config.js`)

- **Modo:** Multi-page static site
- **Input:** Detecta automáticamente todos los archivos `.html`
- **Output:** Preserva estructura de directorios
- **Optimización:** Terser para JS, cssnano para CSS
- **Source Maps:** Habilitados en desarrollo

### Archivos Copiados al Build

El sistema copia automáticamente al directorio `dist/`:
- Todos los archivos HTML (preservando estructura)
- Directorio `assets/images/`
- Directorio `assets/videos/`
- Directorio `assets/data/`
- Scripts Python (`*.py`)
- Backend de Don Chucho (`don-chucho-backend/`)
- Motor pSEO (`pseo-engine/`)
- Competitive Engine (`competitive-engine/`)

## 🔧 Integración con Workflows Existentes

### Scripts Python

Los scripts Python existentes **NO son afectados** por el build:
- Se copian tal cual al directorio `dist/`
- Pueden ejecutarse normalmente desde el build
- La generación de páginas funciona igual

### Archivos HTML

- **En desarrollo:** Sirven desde directorio original
- **En build:** Se copian a `dist/` sin modificaciones
- Referencias a assets se mantienen iguales

### Versiones Minificadas

El sistema genera automáticamente versiones minificadas:
- JS: `assets/js/*.min.js`
- CSS: `styles.min.css`, `assets/css/*.min.css`

Los archivos originales **NO se eliminan**, permitiendo:
- Desarrollo con archivos legibles
- Producción con archivos optimizados
- Rollback fácil si es necesario

## 📊 Optimizaciones Aplicadas

### JavaScript
- **Minificación:** Elimina espacios, comentarios, renombra variables
- **Dead code elimination:** Remueve código no utilizado
- **Tree shaking:** Solo incluye código necesario
- **Console removal:** Elimina `console.log` en producción

### CSS
- **Minificación:** Elimina espacios, comentarios
- **Autoprefixer:** Agrega prefijos de navegadores automáticamente
- **Optimización:** Fusiona reglas duplicadas, optimiza selectores

### Assets
- **Hashing:** Nombres con hash para cache busting
- **Compression:** Reporte de tamaño gzip/brotli
- **Structure:** Preserva organización original

## 🛠️ Solución de Problemas

### Build falla
```bash
# Limpiar cache e instalar dependencias
rm -rf node_modules .vite dist
npm install
npm run build
```

### Puerto 3000 en uso
```bash
# Cambiar puerto en vite.config.js
server: {
  port: 3001, // u otro puerto disponible
}
```

### Assets no se copian
Verificar que los directorios existan en `assets/` y que estén listados en `vite.config.js` en la sección `viteStaticCopy`.

## 📝 Flujo de Trabajo Recomendado

### Desarrollo Diario
1. `npm run dev` - Iniciar servidor de desarrollo
2. Editar archivos en directorio original
3. Ver cambios en tiempo real con HMR

### Pre-Producción
1. `npm run optimize:assets` - Minificar assets manualmente (opcional)
2. `npm run build:analyze` - Revisar tamaño del bundle
3. `npm run build` - Generar build final
4. `npm run preview` - Verificar build localmente

### Despliegue
1. `npm run build` - Generar `dist/`
2. Subir contenido de `dist/` al servidor
3. Verificar funcionalidad en producción

## 🔐 Seguridad

- **No se eliminan archivos originales**
- **Build es reproducible**
- **Source maps solo en desarrollo**
- **Console logs eliminados en producción**

## 📈 Performance

Antes del build:
- JS: Archivos individuales sin optimización
- CSS: Archivos sin minificar
- Sin cache busting

Después del build:
- JS: Minificado, tree-shaken, con hashes
- CSS: Minificado, autoprefijado, optimizado
- Cache busting automático con hashes

## 🤝 Mantenimiento

### Actualizar Vite
```bash
npm update vite
```

### Agregar nuevo plugin
1. Instalar: `npm install nombre-plugin -D`
2. Agregar a `vite.config.js` en array `plugins`
3. Rebuild para verificar

### Modificar configuración de optimización
Editar `vite.config.js`:
- `build.minify`: Cambiar minificador
- `build.terserOptions`: Configurar Terser
- `build.sourcemap`: Habilitar/deshabilitar source maps

## 📚 Recursos

- [Documentación de Vite](https://vitejs.dev/)
- [Documentación de Terser](https://terser.org/)
- [Documentación de cssnano](https://cssnano.co/)
- [PostCSS](https://postcss.org/)

---

**Nota:** Este sistema de build es **no destructivo**. Todos los archivos originales se preservan y el proceso es reversible. La funcionalidad existente del sitio no se modifica.