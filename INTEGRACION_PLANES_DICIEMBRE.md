# 📋 Guía de Integración: Planes Especiales para Diciembre

## Archivos Creados

Se han creado los siguientes archivos con toda la información del documento DOCX:

### 1. **Datos en JSON** 
📁 `datos/planes-especiales-diciembre.json`
- Estructura de datos completa y bien organizadas
- Fácil de leer y mantener
- Ideal para sincronización con backend

### 2. **Documentación Markdown**
📁 `docs/PLANES_ESPECIALES_DICIEMBRE.md`
- Información formateada en Markdown
- Tablas de tarifas comparativas
- Descripción completa de todos los hoteles
- Ideal para documentación y referencia

### 3. **Script JavaScript**
📁 `assets/js/planes-especiales-diciembre.js`
- Módulo JavaScript con todos los datos
- Funciones para generar HTML dinámicamente
- Método `initPlanesEspeciales()` para renderizar
- Exportable para uso modular

### 4. **Estilos CSS**
📁 `assets/css/planes-especiales-diciembre.css`
- Estilos responsive y modernos
- Tablas de tarifas estilizadas
- Tarjetas de hoteles con hover effects
- Animaciones suaves
- Adaptado para móvil

---

## 🔧 Cómo Integrar en tu Página

### Opción 1: Integración Rápida (Recomendada)

#### Paso 1: Agregar referencias en `planes.html`

En la sección `<head>`:
```html
<!-- CSS de Planes Especiales -->
<link rel="stylesheet" href="assets/css/planes-especiales-diciembre.css">
```

Antes del cierre de `</body>`:
```html
<!-- Script de Planes Especiales -->
<script src="assets/js/planes-especiales-diciembre.js"></script>
```

#### Paso 2: Agregar contenedor en el HTML

En el lugar donde quieras mostrar los planes especiales (por ejemplo, después de la sección de planes regulares):

```html
<!-- Contenedor para Planes Especiales de Diciembre -->
<div id="planes-especiales-container"></div>
```

### Opción 2: Integración Manual

Si prefieres un control más granular, puedes usar las funciones del script directamente:

```javascript
// Generar solo tabla de tarifas
const tablaRadioTaxi = generarTablaTarifas('radio_taxi');
const tablaPlacaBlanca = generarTablaTarifas('placa_blanca');

// Generar lista de servicios incluidos
const listaSericios = generarListaIncluye();

// Obtener tarifa específica
const tarifa = obtenerTarifa('Cabañas La Esmeralda', 'radio_taxi', 3);
```

### Opción 3: Integración con tu Sistema de Datos

Si usas un sistema de planes dinámico, puedes importar los datos JSON:

```javascript
// Cargar datos desde JSON
fetch('datos/planes-especiales-diciembre.json')
  .then(response => response.json())
  .then(data => {
    // Usar data.tarifas, data.hoteles, etc.
    console.log(data);
  });
```

---

## 📊 Estructura de Datos

### Plan Principal
```javascript
{
  "nombre": "Planes Especiales Temporada Alta - Diciembre a Enero",
  "temporada": "15 DICIEMBRE AL 20 ENERO",
  "duracion": { "dias": 4, "noches": 3 },
  "max_cupos": 30,
  "incluye": [...]
}
```

### Tarifas
```javascript
{
  "radio_taxi": [
    {
      "hotel": "Cabañas La Esmeralda",
      "categoria": "Intermedia",
      "pax_2": 1840000,
      "pax_3": 1589000,
      "pax_4": 1464000
    },
    // ... más hoteles
  ],
  "placa_blanca": [...]
}
```

### Hoteles
```javascript
{
  "cabanas_la_esmeralda": {
    "nombre": "CABAÑAS LA ESMERALDA",
    "categoria": "Intermedia",
    "servicios": [...]
  },
  // ... más hoteles
}
```

---

## 🎯 Funciones Disponibles

### `obtenerTarifa(nombreHotel, tipoTransporte, numPax)`
Obtiene el precio para una combinación específica
```javascript
obtenerTarifa('Cabañas La Esmeralda', 'radio_taxi', 3)
// Retorna: 1589000
```

### `generarTablaTarifas(tipoTransporte)`
Genera tabla HTML con todas las tarifas
```javascript
generarTablaTarifas('placa_blanca')
// Retorna: HTML string con tabla
```

### `generarListaIncluye()`
Genera lista HTML de servicios incluidos
```javascript
generarListaIncluye()
// Retorna: HTML string con lista
```

### `generarTarjetaHotel(hotelKey)`
Genera tarjeta HTML de un hotel específico
```javascript
generarTarjetaHotel('finca_hotel_los_girasoles')
// Retorna: HTML string con tarjeta del hotel
```

### `initPlanesEspeciales()`
Inicializa toda la sección (se ejecuta automáticamente)
```javascript
initPlanesEspeciales()
// Renderiza toda la sección en #planes-especiales-container
```

---

## 🎨 Personalización de Estilos

Los colores principales usados son:
- Verde primario: `#2E5E36` (color de marca)
- Verde oscuro: `#1b5e20` (títulos)
- Verde claro: `#e8f5e9` (fondos)
- Naranja: `#ff6f00` (acentos)

Para cambiar los colores, edita `assets/css/planes-especiales-diciembre.css`:

```css
.planes-header h2 {
  color: #2E5E36; /* Cambia este valor */
}
```

---

## 📱 Responsive Design

El diseño se adapta automáticamente a:
- **Desktop**: Grid de 3-4 columnas
- **Tablet**: Grid de 2 columnas
- **Mobile**: Grid de 1 columna

---

## ✅ Checklist de Integración

- [ ] Copiar `planes-especiales-diciembre.json` a `datos/`
- [ ] Copiar `planes-especiales-diciembre.js` a `assets/js/`
- [ ] Copiar `planes-especiales-diciembre.css` a `assets/css/`
- [ ] Agregar link a CSS en `<head>` de `planes.html`
- [ ] Agregar script antes de `</body>` en `planes.html`
- [ ] Agregar `<div id="planes-especiales-container"></div>` en el HTML
- [ ] Probar en navegador (F12 -> Console para ver errores)
- [ ] Verificar en móvil que se vea correctamente
- [ ] Probar botón de WhatsApp

---

## 🐛 Solución de Problemas

### La sección no aparece
- Verifica que el contenedor `<div id="planes-especiales-container"></div>` esté en el HTML
- Abre la consola (F12) y busca errores
- Asegúrate que el script se cargó correctamente

### Estilos no se aplican
- Verifica que el CSS se incluyó en la sección `<head>`
- Limpia la caché del navegador (Ctrl+F5)
- Verifica las rutas relativas de los archivos

### Datos no cargan desde JSON
- Verifica que el archivo está en `datos/planes-especiales-diciembre.json`
- Comprueba que tienes acceso al archivo (permisos)
- Usa el path absoluto si es necesario

---

## 📞 Datos de Contacto

**Álvaro Alzate Ortiz - Quindío Travel**
- Teléfono/WhatsApp: (317) 4426044
- Correo: gerencia@quindiotravel.net
- RNT: 18152

---

*Generado: 2026-08-13*
*Información extraída del documento: "planes especiales para diciembre con oferta max 30 cupos.docx"*
