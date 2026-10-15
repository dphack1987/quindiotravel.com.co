# Guía de Verificación de GTM - Quindío Travel

**Fecha:** 15 Octubre 2026  
**Objetivo:** Verificar que los eventos de tracking se envíen correctamente a Google Tag Manager

---

## 📊 EVENTOS CONFIGURADOS

### Eventos Personalizados en gtm-events.js

| Evento | Descripción | Parámetros |
|--------|-------------|------------|
| `view_plan` | Vista de página de plan específico | plan_name, page_path, page_title |
| `click_plan_card` | Clic en card de plan | plan_id, plan_name, page_path |
| `use_filter` | Uso de filtros en planes.html | filter_type, filter_value, page_path |
| `toggle_price_details` | Toggle de desglose de precios | action (open/close), page_path, plan_name |
| `scroll_depth` | Profundidad de scroll (25%, 50%, 75%, 100%) | scroll_percent, page_path, page_title, plan_name |
| `time_on_page` | Tiempo en página (30s, 60s, 120s) | time_seconds, page_path, page_title, plan_name |
| `click_comparison` | Clic en enlace de comparación | page_path, page_title |

### Eventos Existente en wa-track.js

| Evento | Descripción | Parámetros |
|--------|-------------|------------|
| `click_whatsapp` | Clic en enlace de WhatsApp | page_path, page_title, cta_text, cta_section, wa_number |

---

## 🔍 PASOS PARA VERIFICAR TRACKING

### Paso 1: Verificar que los scripts estén cargados

1. Abre el sitio en tu navegador: https://quindiotravel.com.co
2. Presiona `F12` para abrir las herramientas de desarrollador
3. Ve a la pestaña "Sources" o "Fuentes"
4. Busca los archivos:
   - `assets/js/wa-track.js`
   - `assets/js/gtm-events.js`
5. Verifica que ambos archivos estén cargados sin errores

### Paso 2: Verificar dataLayer

1. En las herramientas de desarrollador, ve a la "Console"
2. Escribe: `window.dataLayer`
3. Presiona Enter
4. Deberías ver un array con los eventos de GTM (incluyendo `gtm.js`)

### Paso 3: Usar Google Tag Assistant

1. Instala la extensión "Tag Assistant" de Chrome
2. Navega a https://quindiotravel.com.co
3. Activa Tag Assistant
4. Verifica que GTM-NVCL3PV4 esté activo
5. Verifica que no haya errores

### Paso 4: Verificar eventos en Preview Mode de GTM

1. Ve a: https://tagmanager.google.com/
2. Inicia sesión con tu cuenta de Google
3. Selecciona el contenedor GTM-NVCL3PV4
4. Haz clic en "Preview" o "Vista previa"
5. Ingresa la URL: https://quindiotravel.com.co
6. En la ventana de preview, interactúa con el sitio:
   - Haz clic en una card de plan
   - Usa los filtros en planes.html
   - Haz scroll en una página de plan
   - Haz clic en un enlace de WhatsApp
7. Verifica que los eventos aparezcan en el panel de GTM

### Paso 5: Verificar eventos en Google Analytics 4

1. Ve a: https://analytics.google.com/
2. Selecciona la propiedad GA4 de Quindío Travel
3. Ve a "Configuración" → "Eventos"
4. Verifica que los eventos personalizados estén registrados:
   - view_plan
   - click_plan_card
   - use_filter
   - toggle_price_details
   - scroll_depth
   - time_on_page
   - click_comparison
   - click_whatsapp

---

## 📋 CHECKLIST DE VERIFICACIÓN

### Carga de Scripts
- [ ] `wa-track.js` cargado sin errores
- [ ] `gtm-events.js` cargado sin errores
- [ ] `dataLayer` está definido en window
- [ ] GTM-NVCL3PV4 está activo (Tag Assistant)

### Eventos de Planes
- [ ] `view_plan` se dispara al cargar plan-1.html
- [ ] `view_plan` se dispara al cargar plan-2.html
- [ ] `view_plan` se dispara al cargar plan-3.html
- [ ] `view_plan` se dispara al cargar plan-4.html
- [ ] `view_plan` se dispara al cargar plan-5.html
- [ ] `view_plan` se dispara al cargar plan-6.html

### Eventos de Interacción
- [ ] `click_plan_card` se dispara al hacer clic en una card
- [ ] `use_filter` se dispara al cambiar un filtro
- [ ] `toggle_price_details` se dispara al abrir/cerrar precios
- [ ] `click_comparison` se dispara al hacer clic en "Comparar planes"

### Eventos de Comportamiento
- [ ] `scroll_depth` se dispara al 25% de scroll
- [ ] `scroll_depth` se dispara al 50% de scroll
- [ ] `scroll_depth` se dispara al 75% de scroll
- [ ] `scroll_depth` se dispara al 100% de scroll
- [ ] `time_on_page` se dispara a los 30 segundos
- [ ] `time_on_page` se dispara a los 60 segundos
- [ ] `time_on_page` se dispara a los 120 segundos

### Eventos de WhatsApp
- [ ] `click_whatsapp` se dispara al hacer clic en cualquier enlace de WhatsApp
- [ ] `wa_number` se captura correctamente (573174426044)
- [ ] `cta_section` se identifica correctamente

---

## 🛠️ SOLUCIÓN DE PROBLEMAS

### Problema: Los eventos no aparecen en GTM Preview

**Causas posibles:**
1. El script `gtm-events.js` no está cargado
2. Hay un error de JavaScript que previene la ejecución
3. El evento no tiene el nombre correcto

**Soluciones:**
1. Verifica en Console si hay errores de JavaScript
2. Verifica que el script esté en el HTML de la página
3. Agrega `console.log()` en el script para depurar

### Problema: Los eventos no aparecen en GA4

**Causas posibles:**
1. Los eventos no están configurados como eventos personalizados en GA4
2. GTM no está conectado a GA4
3. Hay un delay en el procesamiento de datos

**Soluciones:**
1. Configura los eventos personalizados en GA4
2. Verifica que el tag de GA4 esté activo en GTM
3. Espera 24-48 horas para que los datos aparezcan en GA4

### Problema: scroll_depth no se dispara

**Causa posible:**
El usuario no hace scroll suficiente para alcanzar los umbrales

**Solución:**
Haz scroll hasta el 25% de la página para verificar que el evento se dispare

---

## 📊 MÉTRICAS A MONITOREAR

Una vez verificado el tracking, monitorea estas métricas en GA4:

### Engagement
- Vistas de plan por usuario
- Tiempo promedio en página de plan
- Scroll depth promedio
- Tasa de rebote por plan

### Conversión
- Clics en WhatsApp por plan
- Tasa de conversión de view_plan → click_whatsapp
- Clics en filtros
- Uso de comparador de planes

### Comportamiento
- Planes más vistos
- Planes con mayor scroll depth
- Planes con mayor tiempo en página
- Filtros más usados

---

## 🎯 PRÓXIMOS PASOS

1. **Verificar tracking** usando esta guía
2. **Configurar triggers en GTM** para eventos personalizados
3. **Configurar conversiones en GA4** basadas en eventos
4. **Crear reportes personalizados** en GA4
5. **Monitorear métricas** semanalmente

---

*Última actualización: 15 Octubre 2026*
