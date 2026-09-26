# Recomendaciones para Limpieza de Peso Muerto - Quindío Travel

## 📋 Problema Identificado

Según la auditoría consolidada, existen aproximadamente **168 MB de archivos publicables sin usar**:
- **20/20 vídeos** (90 MB)
- **326/483 imágenes** (78 MB) 
- **44 grupos de duplicados** (31 MB)

## ⚠️ Riesgos de Limpieza Automática

### Por qué NO proceder con limpieza automática:

1. **Análisis complejo requerido:**
   - Algunas imágenes pueden ser referenciadas dinámicamente por JavaScript
   - Videos pueden ser usados en landing pages específicas
   - Imágenes duplicadas pueden tener propósitos diferentes (resolución, formato)

2. **Riesgo de romper funcionalidad:**
   - Eliminar una imagen puede romper una página específica
   - Videos pueden ser cargados lazy o condicionalmente
   - Algunos assets pueden ser precacheados por service workers

3. **Validación manual necesaria:**
   - Cada archivo debe ser verificado individualmente
   - Referencias cruzadas entre HTML, CSS, JS y JSON
   - Análisis de logs de acceso para confirmar uso real

## 🎯 Recomendación Segura

### Opción 1: Auditoría Manual Priorizada
1. Identificar los 20 videos más grandes
2. Verificar cada uno manualmente en el código
3. Eliminar solo los confirmados como no usados

### Opción 2: Script de Análisis Profundo
1. Crear script que analice todas las referencias
2. Incluir análisis de carga dinámica, lazy loading, JavaScript
3. Generar reporte detallado antes de cualquier eliminación

### Opción 3: Auditoría de Logs (Si está disponible)
1. Analizar logs de acceso del servidor
2. Identificar archivos con 0 accesos en último mes
3. Priorizar limpieza basada en datos reales

## 📊 Archivos Potenciales para Revisión Prioritaria

### Videos (90 MB - mayor impacto)
- Revisar `assets/videos/` manualmente
- Verificar si están referenciados en algún HTML o JS
- Considerar conversión a formatos más eficientes (WebM)

### Imágenes Duplicadas (31 MB)
- Usar script existente `compress-images.mjs` con análisis
- Identificar duplicados exactos vs versiones optimizadas
- Mantener solo la versión más eficiente

## 🔧 Script Recomendado

Crear un script de análisis más profundo:

```javascript
// analyze-unused-assets.js
// Analiza referencias en HTML, CSS, JS, JSON
// Genera reporte de potencialmente no usados
// Requiere aprobación manual antes de eliminar
```

## 🎯 Prioridad

**BAJA** - La limpieza de peso muerto mejora performance pero NO es crítica. 
- Seguridad y SEO tienen prioridad más alta
- Riesgo de romper funcionalidad es significativo
- Mejor abordar con análisis profundo y manual

## 📅 Recomendación de Implementación

1. **Próximo mes:** Auditoría manual de videos (mayor impacto)
2. **Mes siguiente:** Script de análisis profundo de imágenes
3. **Continuo:** Monitoreo de nuevos assets agregados

---
*Generado: 2026-09-26*
*Basado en auditoría de SEO consolidada*
*Decisión: NO proceder con limpieza automática por seguridad*