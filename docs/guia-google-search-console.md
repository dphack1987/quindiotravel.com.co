# Guía de Configuración: Google Search Console

## Paso 1: Crear cuenta en Google Search Console

1. Accede a [https://search.google.com/search-console](https://search.google.com/search-console)
2. Inicia sesión con tu cuenta de Google (gerencia@quindiotravel.net)
3. Haz clic en "Agregar propiedad" y selecciona "Prefijo de URL"
4. Ingresa: `https://quindiotravel.com.co/`

## Paso 2: Verificar propiedad

### Opción A: Archivo HTML (Recomendado)
1. Descarga el archivo HTML de verificación
2. Súbelo al directorio raíz del sitio: `C:\Users\user\Documents\www.quindiotravel.com\`
3. Haz clic en "Verificar"

### Opción B: Meta Tag
1. Copia el meta tag proporcionado
2. Pégalo en el `<head>` de `index.html`
3. Sube los cambios y haz clic en "Verificar"

## Paso 3: Configurar Sitemap

1. En el menú izquierdo, selecciona "Sitemaps"
2. En el campo "Agregar un nuevo sitemap", ingresa: `sitemap.xml`
3. Haz clic en "Enviar"
4. Verifica que el estado sea "Correcto"

## Paso 4: Configurar Configuración Internacional

1. Ve a "Configuración" > "Configuración internacional"
2. Agrega las variantes de idioma:
   - Español: `https://quindiotravel.com.co/` (predeterminado)
   - Inglés: `https://quindiotravel.com.co/?lang=en`
   - Portugués: `https://quindiotravel.com.co/?lang=pt`

## Paso 5: Monitorear Indexación

### Revisar Indexación
1. Ve a "Índice" > "Cobertura"
2. Revisa el estado de indexación de todas las páginas
3. Corrige errores si existen

### Inspeccionar URL
1. Usa la herramienta "Inspección de URL"
2. Ingresa URLs importantes (index.html, planes.html, salento.html, etc.)
3. Solicita indexación si es necesario

## Paso 6: Monitorear Rendimiento

1. Ve a "Rendimiento" en el menú izquierdo
2. Configura filtros:
   - Consultas: Verificar keywords SEO implementadas
   - Páginas: Monitorear tráfico por página
   - Países: Verificar tráfico por ubicación
   - Dispositivos: Analizar rendimiento móvil vs desktop

## Paso 7: Configurar Alertas

1. Ve a "Configuración" > "Alertas"
2. Activa alertas para:
   - Errores de indexación
   - Problemas de usabilidad móvil
   - Problemas de AMP (si aplica)
   - Errores de rastreo

## Paso 8: Revisar Mejoras

1. Ve a "Mejoras" en el menú izquierdo
2. Revisa:
   - Usabilidad móvil
   - Experiencia de usuario en el núcleo web
   - Datos estructurados (Schema.org)

## Palabras clave a monitorear

Basado en las optimizaciones SEO implementadas:

### Keywords principales
- "guía de turismo en el Eje Cafetero Quindío"
- "planes turísticos en Quindío Eje Cafetero"
- "viajes Eje Cafetero Quindío con itinerario"
- "paquetes turísticos completos en el Eje Cafetero"

### Keywords secundarias
- "Salento Quindío Pueblo Patrimonio"
- "Filandia Quindío Mirador Artesanías"
- "Parque del Café Quindío Atracciones"
- "Valle de Cocora Quindío Palma de Cera"

## Frequencia recomendada de revisión

- **Diaria**: Revisar alertas y errores críticos
- **Semanal**: Analizar rendimiento y keywords
- **Mensual**: Revisar mejoras técnicas y usabilidad móvil
- **Trimestral**: Auditoría completa de SEO

## Métricas clave a monitorear

1. **Impresiones**: Cuántas veces aparece tu sitio en resultados
2. **Clics**: Cuántas veces hacen clic en tu sitio
3. **CTR**: Tasa de clics (clics/impresiones)
4. **Posición promedio**: Ranking promedio en resultados
5. **Cobertura del índice**: Porcentaje de páginas indexadas

## Troubleshooting común

### Páginas no indexadas
- Verificar robots.txt no bloquea páginas importantes
- Revisar meta robots no tengan "noindex"
- Verificar canonical URLs están correctas
- Solicitar indexación manualmente

### Bajo CTR
- Optimizar meta titles y descriptions
- Verificar que aparezcan en resultados relevantes
- Revisar posicionamiento (posición >10 tiene bajo CTR)

### Errores de usabilidad móvil
- Revisar media queries en CSS
- Verificar viewport configuration
- Probar en diferentes dispositivos móviles

## Recursos adicionales

- [Documentación oficial GSC](https://support.google.com/webmasters/answer/4515942)
- [Guía de inicio de SEO](https://developers.google.com/search/docs)