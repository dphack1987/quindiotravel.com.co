# Guía de Modularización de index.html

## Estado Actual
- **index.html:** 6,663 líneas (excesivo para mantenimiento)
- **CSS inline:** ~3,468 líneas
- **JavaScript inline:** ~282 líneas

## Componentes del Head Creados
He creado los 4 componentes del head que faltaban en `components/head/`:

1. **meta-tags.html** - Meta tags básicos y SEO
2. **open-graph.html** - Open Graph y Twitter Cards  
3. **critical-css.html** - CSS crítico inline para above-the-fold
4. **resources.html** - Favicon, preload de recursos críticos

## Implementación Sugerida

### Paso 1: Reemplazar head en index.html
El head actual de index.html (líneas 3-100 aprox.) debería reemplazarse con:

```html
<head>
    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-NVCL3PV4');</script>
    <!-- End Google Tag Manager -->
    
    <!-- Componentes del Head -->
    <!--#include file="components/head/meta-tags.html" -->
    <!--#include file="components/head/resources.html" -->
    <!--#include file="components/head/open-graph.html" -->
    <!--#include file="components/head/critical-css.html" -->
    
    <!-- Hreflang (ya implementado) -->
    <link rel="alternate" hreflang="es" href="https://quindiotravel.com.co/">
    <link rel="alternate" hreflang="es-CO" href="https://quindiotravel.com.co/">
    <link rel="alternate" hreflang="en" href="https://quindiotravel.com.co/?lang=en">
    <link rel="alternate" hreflang="pt" href="https://quindiotravel.com.co/?lang=pt">
    <link rel="alternate" hreflang="fr" href="https://quindiotravel.com.co/?lang=fr">
    <link rel="alternate" hreflang="x-default" href="https://quindiotravel.com.co/">
    
    <!-- Language Detector -->
    <script src="assets/js/language-detector.js" defer></script>
</head>
```

### Paso 2: Extraer CSS inline
El CSS inline (~3,468 líneas) debería moverse a:
- `assets/css/critical.css` - CSS above-the-fold
- `assets/css/main.css` - CSS principal ya existe

### Paso 3: Extraer JavaScript inline  
El JavaScript inline (~282 líneas) debería moverse a:
- `assets/js/main.js` - Funcionalidad principal
- `assets/js/hero.js` - Funcionalidad del hero

### Paso 4: Componentes de secciones
Secciones grandes deberían extraerse a componentes:
- `components/sections/hero.html` - Hero section
- `components/sections/trust-badges.html` - Trust badges
- `components/sections/destinations.html` - Destinos principales
- `components/sections/planes.html` - Planes destacados
- `components/sections/footer.html` - Footer

## Sistema de Build

### Opción A: Vite con includes (Recomendado)
Configurar Vite para procesar includes SSI:

```javascript
// vite.config.js
import { defineConfig } from 'vite';
import { viteStaticCopy } from 'vite-plugin-static-copy';

export default defineConfig({
  plugins: [
    viteStaticCopy({
      targets: [
        { src: 'components', dest: '.' }
      ]
    })
  ]
});
```

### Opción B: 11ty (Static Site Generator)
Instalar 11ty para procesamiento de componentes:

```bash
npm install @11ty/eleventy --save-dev
```

Configurar `.eleventy.js` para procesar includes.

## Beneficios Esperados
- **Mantenibilidad:** Reducción de 6,663 a ~500 líneas en index.html
- **Reutilización:** Componentes compartidos entre páginas
- **Performance:** Critical CSS optimizado
- **Colaboración:** Equipos pueden trabajar en componentes separados

## Próximos Pasos
1. Configurar sistema de build (Vite u 11ty)
2. Reemplazar head en index.html con componentes
3. Extraer CSS inline a archivos separados
4. Extraer JavaScript inline a módulos
5. Crear componentes de secciones principales
6. Validar que todo funciona correctamente

## Nota Importante
Esta es una guía de implementación. Los cambios no se han aplicado aún para evitar romper el sitio funcionando. Se recomienda hacer esto en un entorno de desarrollo primero.