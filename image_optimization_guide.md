# Guía de Optimización de Imágenes - Quindío Travel

## Imágenes Principales Identificadas

### Imágenes Críticas (Above-the-fold)
- `assets/images/paisajes/foto_hero1.jpg` - Imagen hero principal
- `logo_quindio_travel.png` - Logo principal
- `assets/images/destinos/logo_parque_del_cafe.jpg` - Logos de destinos

### Imágenes de Alojamientos (Below-the-fold)
- `assets/images/alojamientos/finca-hotel-los-girasoles.jpg`
- `assets/images/alojamientos/cabanas-la-esmeralda.jpg`
- `assets/images/alojamientos/hotel-campestre-cafe-cafe/IMG_0404-scaled.jpg`
- `assets/images/alojamientos/finca-hotel-la-dorada.jpg`
- `assets/images/alojamientos/hotel-campestre-la-tata/finca-hotel-la-tata.jpg`

### Imágenes de Atractivos (Below-the-fold)
- `assets/images/atractivos/parque-del-cafe.jpg`
- `assets/images/atractivos/panaca.jpg`
- `assets/images/atractivos/termales-santa-rosa.jpg`
- `assets/images/atractivos/recuca.jpg`
- `assets/images/atractivos/mariposario.jpg`

## Recomendaciones de Optimización

### 1. Compresión con TinyPNG
- Visitar https://tinypng.com/
- Subir imágenes principales
- Descargar versiones comprimidas
- **Impacto esperado:** -30-50% tamaño de imágenes

### 2. Conversión a WebP
- Convertir JPG a WebP donde sea compatible
- Usar herramientas como Squoosh o CloudConvert
- **Impacto esperado:** -25-35% tamaño de imágenes

### 3. Generación de Imágenes Responsivas
- Crear múltiples tamaños para diferentes dispositivos
- Usar srcset attribute en HTML
- **Impacto esperado:** +15-20% velocidad en móviles

## Prioridad de Optimización

### ALTA PRIORIDAD (Comprimir primero)
1. `assets/images/paisajes/foto_hero1.jpg` - Imagen hero
2. `logo_quindio_travel.png` - Logo principal
3. `assets/images/alojamientos/*.jpg` - Imágenes de hoteles

### PRIORIDAD MEDIA
4. `assets/images/atractivos/*.jpg` - Imágenes de atractivos
5. `assets/images/paisajes/*.jpg` - Otras imágenes de paisajes

### PRIORIDAD BAJA
6. Imágenes de decoraciones y elementos secundarios

## Estado Actual
- **Total imágenes JPG:** 68 encontradas
- **Total imágenes PNG:** 11 encontradas
- **Lazy loading:** Implementado (considerado)
- **WebP:** No implementado
- **Compresión:** Pendiente manual

## Comandos Útiles para Verificación

```bash
# Ver tamaño de imágenes
du -sh assets/images/**/*.jpg

# Encontrar imágenes grandes
find assets/images -name "*.jpg" -size +500k

# Verificar imágenes sin alt text
grep -r '<img' assets/images/ | grep -v 'alt='
```

## Próximos Pasos
1. Comprimir imágenes principales con TinyPNG
2. Implementar WebP para navegadores modernos
3. Generar imágenes responsivas
4. Actualizar HTML con srcset attributes