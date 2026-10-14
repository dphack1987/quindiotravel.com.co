# Seguimiento de Métricas - Quindío Travel 2026

**Fecha de inicio:** 14 de Octubre 2026  
**Objetivo:** Aumentar ventas de ~3/mes a 15/mes (5x) en 1 mes

---

## 📊 BASELINE (Antes de cambios de conversión)

*Fecha de medición: 14 Octubre 2026*

### Métricas de tráfico
- Visitantes/mes: ?
- Pageviews/mes: ?
- Sesiones/mes: ?
- Tasa de rebote: ?

### Métricas de conversión
- Clics en WhatsApp/mes: ~50 (según reporte del usuario)
- Consultas cualificadas/mes: ~5 (10% de clics WhatsApp)
- Ventas/mes: ~3 (según reporte del usuario)
- Tasa de conversión visitantes → ventas: ?

### Métricas por plan
*Requiere implementación de tracking específico*
- Clics plan-1 (Escapada Cafetera): ?
- Clics plan-2 (Aventura Natural): ?
- Clics plan-3 (Experiencia Completa): ?
- Clics plan-4 (Termales Santa Rosa): ?
- Clics plan-5 (Tradición y Raíces): ?
- Clics plan-6 (Experiencia Premium): ?

---

## 🎯 METAS POST-IMPLEMENTACIÓN

### Meta 1 mes (14 Noviembre 2026)
- Clics en WhatsApp/mes: 200 (4x baseline)
- Consultas cualificadas/mes: 50 (25% de clics)
- Ventas/mes: 15 (5x baseline)
- Tasa de conversión visitantes → ventas: +500%

### Meta 3 meses (14 Enero 2027)
- Clics en WhatsApp/mes: 500 (10x baseline)
- Consultas cualificadas/mes: 175 (35% de clics)
- Ventas/mes: 40 (13x baseline)
- Tasa de conversión visitantes → ventas: +1200%

---

## 📈 CAMBIOS IMPLEMENTADOS (14 Octubre 2026)

### Commit: 86c5f9a8 - "Mejoras de conversión para optimizar ventas"

**Mejoras implementadas:**
1. ✅ Precios "desde" visibles en cards de planes
2. ✅ CTAs de WhatsApp prellenados por plan
3. ✅ Badges de urgencia en todos los planes
4. ✅ Countdown timer de 24 horas en planes.html
5. ✅ Testimonios específicos en 6 planes (18 testimonios)
6. ✅ Simplificación de precios (4→3 categorías)
7. ✅ Filtros de búsqueda en planes.html
8. ✅ Página de comparación de planes
9. ✅ Botón de desglose de precios en plan-1.html
10. ✅ Mejora de CTA WhatsApp en home
11. ✅ Mejora de CTA en gracias.html
12. ✅ Banner de urgencia en promo-octubre-2026.html
13. ✅ Precios destacados en heroes de planes 2-6
14. ✅ Eliminación de scroll horizontal

---

## 🔍 EVENTOS GTM CONFIGURADOS

### Eventos actuales
- `click_whatsapp`: Clics en enlaces de WhatsApp
  - `page_path`: Ruta de la página
  - `page_title`: Título de la página
  - `cta_text`: Texto del botón/enlace
  - `cta_section`: Sección donde está el CTA
  - `wa_number`: Número de WhatsApp

### Eventos pendientes de configurar
- [ ] `view_plan`: Vista de página de plan específico
- [ ] `click_plan_card`: Clic en card de plan en planes.html
- [ ] `use_filter`: Uso de filtros en planes.html
- [ ] `toggle_price_details`: Toggle de desglose de precios
- [ ] `scroll_depth`: Profundidad de scroll en páginas de plan
- [ ] `time_on_page`: Tiempo en página por plan

---

## 📋 CHECKLIST DE SEGUIMIENTO

### Semana 1 (14-21 Octubre 2026)
- [ ] Verificar deployment en GitHub Pages
- [ ] Confirmar que todos los cambios son visibles en producción
- [ ] Obtener baseline de métricas de GA4/GTM
- [ ] Configurar eventos GTM adicionales
- [ ] Reemplazar testimonios placeholders con reseñas reales

### Semana 2 (22-28 Octubre 2026)
- [ ] Medir clics en WhatsApp (primeros datos post-cambios)
- [ ] Comparar con baseline
- [ ] Validar que filtros funcionan en producción
- [ ] Validar que comparar-planes.html es accesible
- [ ] Configurar Meta/Facebook Pixel

### Semana 3 (29 Octubre - 4 Noviembre 2026)
- [ ] Medir clics en WhatsApp (segunda semana)
- [ ] Identificar planes con más conversión
- [ ] Ajustar estrategias según datos
- [ ] A/B test de badges de urgencia (si aplica)

### Semana 4 (5-11 Noviembre 2026)
- [ ] Medir clics en WhatsApp (tercera semana)
- [ ] Evaluar progreso hacia meta de 1 mes
- [ ] Revisar testimonios y social proof
- [ ] Documentar learnings

---

## 📝 REGISTRO DE MEDICIONES

### Semana 1 (14-21 Octubre 2026)
- Clics WhatsApp: ?
- Consultas cualificadas: ?
- Ventas: ?
- Notas:

### Semana 2 (22-28 Octubre 2026)
- Clics WhatsApp: ?
- Consultas cualificadas: ?
- Ventas: ?
- Notas:

### Semana 3 (29 Octubre - 4 Noviembre 2026)
- Clics WhatsApp: ?
- Consultas cualificadas: ?
- Ventas: ?
- Notas:

### Semana 4 (5-11 Noviembre 2026)
- Clics WhatsApp: ?
- Consultas cualificadas: ?
- Ventas: ?
- Notas:

---

## ⚠️ TAREAS PENDIENTES

### Alta prioridad
- [ ] Reemplazar testimonios placeholders con reseñas reales de Google
- [ ] Validar truthfulidad de badges de urgencia
- [ ] Configurar eventos GTM adicionales
- [ ] Configurar Meta/Facebook Pixel

### Media prioridad
- [ ] Simplificar precios en plan-3, plan-4, plan-5, plan-6 si aplica
- [ ] A/B test de elementos de conversión
- [ ] Mejorar tracking específico por plan

### Baja prioridad
- [ ] Integración con Google Places API para reseñas automáticas
- [ ] Dashboard personalizado de métricas
- [ ] Sistema de cupos en tiempo real

---

## 💡 INSIGHTS Y LEARNINGS

*Espacio para documentar aprendizajes durante el proceso de optimización*

- [ ]

---

*Última actualización: 14 Octubre 2026*
