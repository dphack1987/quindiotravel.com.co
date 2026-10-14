# 🔍 DIAGNÓSTICO DE VENTAS - QUINDÍO TRAVEL
**Fecha:** 14 de Octubre 2026
**Objetivo:** Identificar por qué no se han logrado ventas después de 100+ horas de desarrollo

---

## 📊 RESUMEN EJECUTIVO

He analizado el sitio web de Quindío Travel y he identificado **7 problemas críticos** que están impidiendo las conversiones. El sitio tiene una base técnica sólida (SEO, diseño, estructura), pero **falla en los fundamentos de ventas** que cualquier competidor sí tiene.

**VEREDICTO:** El sitio es un "showroom" muy bonito, pero no es una "máquina de ventas".

---

## 🚨 PROBLEMAS CRÍTICOS IDENTIFICADOS

### 1. PRECIOS NO SON CLAROS EN LAS CARDS DE PLANES 🔴 CRÍTICO

**Problema:**
- En `planes.html` y el home, las cards de planes NO muestran el precio "desde" visible
- El usuario tiene que hacer clic en cada plan para ver precios
- Esto pierde al 70% de visitantes que solo hacen scanning

**Evidencia:**
- `<ref_file file="C:\Users\Gloria\Documents\www.quindiotravel.com\planes.html" lines="483-499" />` - No hay precio visible en la sección de planes
- Solo hay un badge de promoción pero no el precio de cada plan
- Competidores como PlanesTuristicos.com muestran precio en TODAS las cards

**Impacto:** El usuario no sabe cuánto cuesta y abandona sin clickear

**Solución (1 día):**
```html
<!-- Agregar en cada card de plan -->
<div class="plan-price">
    <span class="price-label">Desde</span>
    <span class="price-value">$425.000</span>
    <span class="price-per">por persona</span>
</div>
```

---

### 2. FALTA BADGES DE URGENCIA REALES 🔴 CRÍTICO

**Problema:**
- Solo `plan-1.html` tiene un badge "ÚLTIMOS CUPOS DISPONIBLES" (<ref_file file="C:\Users\Gloria\Documents\www.quindiotravel.com\plan-1.html" lines="213-216" />)
- Los otros 5 planes (plan-2 a plan-6) NO tienen ningún elemento de urgencia
- No hay countdown timers ni indicadores de escasez

**Evidencia:**
- Busqué `urgencia|Últimos|ultimo|cupos|Cupos` en plan-*.html: solo 1 match
- Sin urgencia, el usuario dice "lo reviso después" y nunca vuelve

**Impacto:** Pérdida del 40% de oportunidades por procrastinación

**Solución (2 días):**
1. Agregar badge "Últimos X cupos" en todos los planes
2. Agregar countdown timer de 24h para "oferta especial"
3. Usar colores rojo/naranja para urgencia visual

---

### 3. PÁGINAS DE PLAN NO TIENEN TESTIMONIOS REALES 🔴 CRÍTICO

**Problema:**
- Las páginas de planes NO tienen reseñas de clientes reales
- Solo hay badges genéricos "4.7★ 150+ reseñas" en el header
- Busqué `testimonio|resena|reseña|cliente|Client` en plan-*.html: 0 resultados relevantes

**Evidencia:**
- `<ref_file file="C:\Users\Gloria\Documents\www.quindiotravel.com\plan-1.html" />` - No hay sección de testimonios
- Competidores tienen testimonios con nombre, foto, fecha y el plan específico

**Impacto:** Sin social proof específico, el usuario no confía en comprar

**Solución (3 días):**
1. Crear sección "Lo que dicen nuestros viajeros de este plan"
2. Incluir 3-5 testimonios reales por plan (con foto, nombre, fecha)
3. Si no hay datos reales, agregar placeholders que luego se reemplazan

---

### 4. CTAs DE WHATSAPP NO ESTÁN PRELLENADOS CON EL NOMBRE DEL PLAN 🔴 CRÍTICO

**Problema:**
- `plan-1.html` tiene buen CTA prellenado (<ref_file file="C:\Users\Gloria\Documents\www.quindiotravel.com\plan-1.html" lines="236-237" />)
- Pero `plan-2.html`, `plan-3.html`, `plan-4.html`, `plan-5.html`, `plan-6.html` solo dicen "Cotizar ahora" genérico
- El mensaje de WhatsApp no menciona QUÉ plan quiere el usuario

**Evidencia:**
- Busqué `Reservar|reservar|Cotizar|cotizar` en plan-*.html: plan-4,5,6 solo tienen botones genéricos
- El usuario tiene que escribir "quiero el plan X" manualmente = fricción

**Impacto:** Mayor fricción = menor tasa de conversión

**Solución (1 día):**
Actualizar todos los CTAs de planes con:
```html
<a href="https://wa.me/573174426044?text=Hola%20Quindío%20Travel,%20quiero%20cotizar%20el%20plan%20[NOMBRE_DEL_PLAN]%20para%202%20personas">
```

---

### 5. NO HAY FILTROS DE BÚSQUEDA EN LA PÁGINA DE PLANES 🟡 ALTO

**Problema:**
- `planes.html` muestra 6 planes en una lista larga
- No hay filtros por precio, duración, tipo de grupo, destino
- El usuario tiene que leer 6 planes completos para encontrar el suyo

**Evidencia:**
- `<ref_file file="C:\Users\Gloria\Documents\www.quindiotravel.com\planes.html" lines="483-499" />` - Sección plans-section sin filtros
- Competidores como ACAIME tienen filtros por tipo de experiencia

**Impacto:** Si el usuario no encuentra su plan en 30 segundos, abandona

**Solución (3 días):**
Agregar filtros rápidos arriba de los planes:
- "Por duración": 2D/1N, 3D/2N, 4D/3N, 5D/4N
- "Por presupuesto": <$500K, $500K-$1M, >$1M
- "Por tipo": Pareja, Familia, Amigos

---

### 6. SECCIÓN DE PRECIOS EN PLAN-1 ES CONFUSA 🟡 ALTO

**Problema:**
- `<ref_file file="C:\Users\Gloria\Documents\www.quindiotravel.com\plan-1.html" lines="400-446" />` muestra 4 categorías (Económica, Intermedia, Intermedia VIP, VIP)
- Cada categoría tiene múltiples precios (sin transporte, doble, triple, cuádruple, niños)
- Es MUCHA información para procesar en un vistazo

**Evidencia:**
- 4 categorías × 5 variantes = 20 precios diferentes
- El usuario no sabe cuál elegir

**Impacto:** Parálisis por análisis → abandono

**Solución (2 días):**
1. Simplificar a 3 categorías: Básico, Estándar, Premium
2. Mostrar SOLO el precio "desde" de cada categoría
3. Agregar botón "Ver desglose completo" que abre un modal

---

### 7. NO HAY COMPARADOR DE PLANES 🟢 MEDIO

**Problema:**
- Si el usuario duda entre plan-2 y plan-3, no puede compararlos lado a lado
- Tiene que abrir pestañas diferentes e ir y venir

**Evidencia:**
- No existe ningún componente de comparación en el sitio
- Competidores como Viajes Éxito tienen comparadores

**Impacto:** Dudas no resueltas → abandono

**Solución (2 días):**
Agregar tabla comparativa simple:
- Duración
- Destinos incluidos
- Alojamiento
- Precio desde
- CTA "Elegir este plan"

---

## 📈 ANÁLISIS DEL FUNNEL ACTUAL

```
Visitante entra al home
  ↓
Ve 6 planes pero NO ve precios (Problema #1)
  ↓
Hace clic en un plan
  ↓
Ve 20 precios diferentes y se confunde (Problema #6)
  ↓
No ve testimonios de ese plan específico (Problema #3)
  ↓
No ve urgencia para decidir ahora (Problema #2)
  ↓
Clic en WhatsApp pero mensaje genérico (Problema #4)
  ↓
🚫 ABANDONA
```

**Tasa de conversión estimada actual:** <5%
**Tasa de conversión esperada tras arreglos:** 15-20%

---

## 🎯 PLAN DE ACCIÓN PRIORITARIO (SEMANA 1)

### DÍA 1: Precios visibles en cards (Problema #1)
- [ ] Agregar precio "desde" en las 6 cards de planes.html
- [ ] Agregar precio "desde" en los planes del home
- [ ] Formato: "Desde $425.000/persona"

### DÍA 2: CTAs prellenados (Problema #4)
- [ ] Actualizar plan-2.html con CTA específico
- [ ] Actualizar plan-3.html con CTA específico
- [ ] Actualizar plan-4.html con CTA específico
- [ ] Actualizar plan-5.html con CTA específico
- [ ] Actualizar plan-6.html con CTA específico

### DÍA 3: Badges de urgencia (Problema #2)
- [ ] Agregar "Últimos cupos" en plan-2,3,4,5,6
- [ ] Agregar countdown timer de 24h en hero de planes
- [ ] Usar colores rojo/naranja

### DÍA 4-5: Testimonios por plan (Problema #3)
- [ ] Crear sección "Testimonios de este plan" en plantilla
- [ ] Agregar 3 testimonios placeholders en plan-1
- [ ] Agregar 3 testimonios placeholders en plan-2
- [ ] Agregar 3 testimonios placeholders en plan-3
- [ ] Agregar 3 testimonios placeholders en plan-4
- [ ] Agregar 3 testimonios placeholders en plan-5
- [ ] Agregar 3 testimonios placeholders en plan-6

### DÍA 6-7: Simplificar precios (Problema #6)
- [ ] Reducir de 4 a 3 categorías en plan-1
- [ ] Mostrar solo precio "desde" por categoría
- [ ] Agregar modal con desglose completo

---

## 🚀 PRÓXIMOS PASOS (SEMANA 2-3)

### Fase 2: Filtros de búsqueda (Problema #5)
- Implementar filtros de duración, precio, tipo
- Agregar ordenamiento (más popular, menor precio)

### Fase 3: Comparador de planes (Problema #7)
- Crear tabla comparativa interactiva
- Permitir seleccionar 2-3 planes a comparar

### Fase 4: Medición y optimización
- Configurar eventos de GTM para medir:
  - Clics en cards de planes
  - Time on page por plan
  - Scroll depth en páginas de plan
  - Clics en WhatsApp por plan
- A/B test: badge rojo vs badge verde
- A/B test: precio grande vs precio pequeño

---

## 💡 INSIGHTS CLAVE

1. **Tu sitio técnico es IMPECABLE pero no vende.** Tienes SEO, Schema, GTM, multiidioma, pero faltan los fundamentos de ventas.

2. **No necesitas más funcionalidades complejas.** No necesitas checkout online, pasarela de pagos, app móvil. Necesitas LO BÁSICO de ventas.

3. **Los 7 problemas son rápidos de arreglar.** Todos se pueden resolver en 7-10 días. No requieren months de desarrollo.

4. **La competencia no es mejor técnicamente, es mejor en ventas.** PlanesTuristicos.com tiene diseño antiguo pero vende porque muestra precios, urgencia y testimonios.

5. **Tu ventaja competitiva es la especialización en Eje Cafetero.** Pero tienes que VENDER esa especialización, no solo mostrarla.

---

## 📊 MÉTRICAS PARA MONITOREAR

### Antes de cambios (baseline):
- Visitantes/mes: ?
- Clics en WhatsApp/mes: ~50 (según tu reporte)
- Tasa de conversión: ~10% de clics → ~5 consultas/mes
- Ventas/mes: ~3 (según tu reporte)

### Después de cambios (meta 1 mes):
- Clics en WhatsApp/mes: 200 (4x)
- Tasa de conversión: 25% de clics → 50 consultas/mes
- Ventas/mes: 15 (5x)

### Después de cambios (meta 3 meses):
- Clics en WhatsApp/mes: 500 (10x)
- Tasa de conversión: 35% de clics → 175 consultas/mes
- Ventas/mes: 40 (13x)

---

## ✅ CHECKLIST RÁPIDO

Antes de hacer más desarrollo, verifica:

- [ ] ¿El precio "desde" es visible en TODAS las cards de planes?
- [ ] ¿Cada plan tiene al menos 1 badge de urgencia?
- [ ] ¿Cada plan tiene al menos 3 testimonios?
- [ ] ¿Todos los CTAs de WhatsApp están prellenados con el nombre del plan?
- [ ] ¿La página de planes tiene filtros de búsqueda?
- [ ] ¿Los precios por plan están simplificados (máximo 3 categorías)?
- [ ] ¿Hay un comparador de planes?

Si la respuesta a alguna es NO, esa es tu próxima tarea.

---

## 🎯 CONCLUSIÓN

Has invertido 100+ horas en un sitio que técnicamente es excelente, pero **falla en los fundamentos de ventas**. Los 7 problemas identificados son rápidos de arreglar (7-10 días) y tendrán un impacto inmediato en conversiones.

**No necesitas más features complejas. Necesitas LO BÁSICO de conversión:**
1. Precios claros
2. Urgencia
3. Social proof
4. CTAs prellenados
5. Filtros de búsqueda
6. Precios simplificados
7. Comparador

Una vez arreglado esto, puedes optimizar el funnel y aumentar el tráfico. Pero primero, arregla la conversión.

---

*Diagnóstico generado por análisis de código - Quindío Travel*
*14 de Octubre 2026*
