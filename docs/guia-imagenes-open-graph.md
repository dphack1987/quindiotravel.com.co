# Guía para Imágenes Optimizadas de Open Graph

## Especificaciones Técnicas para Open Graph Images

### Dimensiones Recomendadas
- **Facebook/LinkedIn**: 1200x630 píxeles (ratio 1.91:1)
- **Twitter**: 1200x675 píxeles (ratio 16:9) o 1200x600 (ratio 2:1)
- **Tamaño máximo**: 8MB (Facebook), 5MB (Twitter)
- **Formato**: JPG o PNG

### Imágenes Necesarias por Página

#### 1. Homepage (index.html)
- **Archivo actual**: `assets/images/paisajes/foto_hero1.jpg`
- **Nombre sugerido**: `og-home-1200x630.jpg`
- **Contenido sugerido**: 
  - Paisaje principal del Eje Cafetero
  - Logo de Quindío Travel integrado sutilmente
  - Texto opcional: "Planes Todo Incluido Eje Cafetero 2026"
  - Colores corporativos: verde (#2E5E36) y marrón madera

#### 2. Planes (planes.html)
- **Archivo actual**: `assets/images/planes/plan1.jpg`
- **Nombre sugerido**: `og-planes-1200x630.jpg`
- **Contenido sugerido**:
  - Collage de los 6 planes principales
  - Precios visibles: "Desde $450,000 COP"
  - Iconos de destinos: café, palma de cera, termas
  - Call-to-action: "Cotiza Gratis"

#### 3. Salento (salento.html)
- **Archivo actual**: `assets/images/destinos/salento.png`
- **Nombre sugerido**: `og-salento-1200x630.jpg`
- **Contenido sugerido**:
  - Balcones coloridos característicos
  - Mirador principal
  - Texto: "🌈 Salento - Pueblo Patrimonio"
  - Colores vibrantes de la arquitectura

#### 4. Valle de Cocora (valle-de-cocora.html)
- **Archivo actual**: `assets/images/paisajes/foto_hero1.jpg`
- **Nombre sugerido**: `og-cocora-1200x630.jpg`
- **Contenido sugerido**:
  - Palmas de cera majestuosas
  - Camino principal del valle
  - Texto: "🌴 Valle de Cocora - Palma de Cera más Alta"
  - Senderistas en perspectiva

#### 5. Hoteles (hotel-campestre-cafe-cafe.html)
- **Archivo actual**: `assets/images/alojamientos/hotel-cafe-cafe.jpg`
- **Nombre sugerido**: `og-hotel-cafe-cafe-1200x630.jpg`
- **Contenido sugerido**:
  - Fachada del hotel con piscina
  - Amenidades visibles
  - Texto: "⭐⭐⭐ Alojamiento VIP"
  - Precio: "Desde $120,000/noche"

## Herramientas Recomendadas para Creación

### Gratis
- **Canva**: Plantillas de Open Graph predefinidas
- **Adobe Express**: Templates de redes sociales
- **Figma**: Diseño profesional gratuito
- **Remove.bg**: Eliminar fondos de imágenes

### De Pago
- **Adobe Photoshop**: Edición profesional
- **Sketch**: Diseño UI/UX

## Checklist de Optimización

### Para Cada Imagen
- [ ] Dimensiones correctas (1200x630 px)
- [ ] Tamaño bajo 5MB
- [ ] Formato JPG (calidad 80-90%)
- [ ] Nombre descriptivo del archivo
- [ ] Texto legible (mínimo 24px)
- [ ] Colores corporativos integrados
- [ ] Logo de marca visible pero no dominante
- [ ] Sin bordes blancos innecesarios
- [ ] Optimizada para móvil y desktop

### Seguridad de Texto
- **Zona segura central**: 900x500 px (evitar texto en bordes)
- **Tamaño mínimo de texto**: 24px para títulos, 18px para subtítulos
- **Contraste**: Mínimo 4.5:1 para accesibilidad

### Rendimiento
- **Compresión JPG**: 80-90% de calidad
- **Tamaño objetivo**: 100-300KB por imagen
- **WebP opcional**: Formato moderno si el servidor lo soporta

## Integración en el Código

### Ejemplo de Implementación
```html
<meta property="og:image" content="https://quindiotravel.com.co/assets/images/og/og-home-1200x630.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Paisaje del Eje Cafetero - Quindío Travel 2026">
<meta property="og:image:type" content="image/jpeg">
```

## Validación

### Herramientas de Testing
- **Facebook Sharing Debugger**: https://developers.facebook.com/tools/debug/
- **Twitter Card Validator**: https://cards-dev.twitter.com/validator
- **LinkedIn Post Inspector**: https://www.linkedin.com/post-inspector/

### Pasos de Validación
1. Subir la imagen al servidor
2. Probar en Facebook Sharing Debugger
3. Probar en Twitter Card Validator
4. Verificar que aparezca correctamente en móviles
5. Comprobar carga rápida (menos de 3 segundos)

## Cronograma Sugerido

### Prioridad Alta
1. Homepage OG image
2. Planes OG image
3. Salento OG image

### Prioridad Media
4. Valle de Cocora OG image
5. Parque del Café OG image
6. Filandia OG image

### Prioridad Baja
7. Hoteles individuales OG images
8. Blog posts OG images

## Recursos Adicionales

### Plantillas
- Canva Open Graph Templates: https://www.canva.com/templates/search/open-graph/
- Figma Community: https://www.figma.com/community

### Guías Oficiales
- Facebook Open Graph: https://developers.facebook.com/docs/sharing/webmasters/images/
- Twitter Cards: https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/abouts-cards

### Herramientas de Compresión
- TinyJPG: https://tinyjpg.com/
- ImageOptim: https://imageoptim.com/
- Squoosh: https://squoosh.app/

## Mantenimiento

### Actualización Periódica
- Revisar imágenes cada 6 meses
- Actualizar con fotos nuevas de alta calidad
- A/B testing con diferentes diseños
- Monitorear engagement en redes sociales

### Métricas a Seguir
- CTR (Click-Through Rate) en resultados de búsqueda
- Engagement en redes sociales
- Tiempo de carga de imágenes
- Conversiones desde imágenes OG