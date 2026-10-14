# Guía para Reemplazar Testimonios Placeholders con Reseñas Reales

**Fecha:** 14 Octubre 2026  
**Objetivo:** Reemplazar los 18 testimonios placeholders con reseñas verificadas de clientes reales

---

## 📍 UBICACIÓN DE TESTIMONIOS PLACEHOLDERS

Los testimonios actuales están en las siguientes páginas:

| Página | Plan | Cantidad de testimonios | Líneas aprox. |
|--------|------|------------------------|---------------|
| plan-1.html | Escapada Cafetera (2D/1N) | 3 | ~790-820 |
| plan-2.html | Aventura Natural (3D/2N) | 3 | ~600-630 |
| plan-3.html | Experiencia Completa (4D/3N) | 3 | ~630-660 |
| plan-4.html | Termales Santa Rosa (4D/3N) | 3 | ~640-670 |
| plan-5.html | Tradición y Raíces (4D/3N) | 3 | ~620-650 |
| plan-6.html | Experiencia Premium (5D/4N) | 3 | ~660-690 |

---

## 📋 FORMATO DE TESTIMONIO ACTUAL

Cada testimonio placeholder tiene este formato:

```html
<div class="testimonial-card">
    <div class="testimonial-header">
        <div class="testimonial-avatar">
            <i class="fas fa-user"></i>
        </div>
        <div class="testimonial-info">
            <h4 class="testimonial-name">[Nombre Placeholder]</h4>
            <div class="testimonial-meta">
                <span class="testimonial-date">[Fecha Placeholder]</span>
                <span class="testimonial-group">[Tipo de grupo]</span>
            </div>
        </div>
        <div class="testimonial-rating">
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
        </div>
    </div>
    <p class="testimonial-text">[Texto placeholder]</p>
</div>
```

---

## ✅ REQUISITOS PARA RESEÑAS REALES

### 1. Fuente de datos
Las reseñas deben venir de:
- **Google Business Profile** (https://g.page/quindiotravel/review)
- **TripAdvisor** (si hay perfil)
- **Facebook** (si hay reseñas verificadas)
- **WhatsApp** (conversaciones reales de clientes felices)

### 2. Información requerida por reseña
Para cada reseña real, necesitas:
- ✅ **Nombre completo** (o iniciales si el cliente prefiere privacidad)
- ✅ **Fecha del viaje** (mes/año real)
- ✅ **Tipo de grupo** (pareja, familia, amigos, solo)
- ✅ **Plan específico** (Escapada Cafetera, Aventura Natural, etc.)
- ✅ **Texto de la reseña** (mínimo 50 caracteres, máximo 300)
- ✅ **Rating** (debe ser 4 o 5 estrellas para usarlo en el sitio)
- ✅ **Fuente** (Google, TripAdvisor, Facebook, WhatsApp)
- ✅ **Permiso del cliente** (autorización explícita para publicar)

### 3. Verificación
- ❌ NO inventar nombres
- ❌ NO inventar reseñas
- ❌ NO usar reseñas de otros operadores turísticos
- ✅ Usar solo reseñas de clientes reales de Quindío Travel
- ✅ Mantener la esencia del texto original (puedes editar por longitud)
- ✅ Si la reseña original tiene errores gramaticales, corregirlos

---

## 📝 EJEMPLO DE REEMPLAZO

### Placeholder actual (plan-1.html):
```html
<div class="testimonial-card">
    <div class="testimonial-header">
        <div class="testimonial-avatar">
            <i class="fas fa-user"></i>
        </div>
        <div class="testimonial-info">
            <h4 class="testimonial-name">María González</h4>
            <div class="testimonial-meta">
                <span class="testimonial-date">Septiembre 2026</span>
                <span class="testimonial-group">Pareja</span>
            </div>
        </div>
        <div class="testimonial-rating">
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
        </div>
    </div>
    <p class="testimonial-text">Excelente experiencia en Salento y Valle de Cocora. La guía fue muy amable y nos explicó todo sobre el cultivo de café. Recomendado 100%.</p>
</div>
```

### Reemplazo con reseña real:
```html
<div class="testimonial-card">
    <div class="testimonial-header">
        <div class="testimonial-avatar">
            <i class="fas fa-user"></i>
        </div>
        <div class="testimonial-info">
            <h4 class="testimonial-name">Carlos Ruiz</h4>
            <div class="testimonial-meta">
                <span class="testimonial-date">Agosto 2026</span>
                <span class="testimonial-group">Pareja</span>
            </div>
        </div>
        <div class="testimonial-rating">
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
        </div>
    </div>
    <p class="testimonial-text">Viajamos en agosto y fue espectacular. El Valle de Cocora se veía hermoso y la visita a la finca cafetera fue muy educativa. El transporte fue puntual y cómodo.</p>
</div>
```

---

## 🔍 CÓMO OBTENER RESEÑAS REALES

### Opción 1: Google Business Profile
1. Ir a https://business.google.com/
2. Iniciar sesión con la cuenta de Quindío Travel
3. Navegar a "Reseñas"
4. Filtrar por reseñas de 4-5 estrellas
5. Copiar nombre, fecha y texto de cada reseña
6. Identificar el plan del cliente (revisando historial de WhatsApp si es necesario)

### Opción 2: WhatsApp
1. Revisar historial de conversaciones con clientes
2. Buscar mensajes positivos después del viaje
3. Pedir permiso al cliente para usar su testimonio
4. Solicitar nombre, fecha de viaje y tipo de grupo

### Opción 3: Solicitar reseñas nuevas
1. Enviar mensaje a clientes recientes:
   ```
   Hola [Nombre], esperamos que hayas disfrutado tu viaje al Eje Cafetero.
   ¿Podrías dejarnos una reseña en Google? Nos ayuda mucho a mejorar.
   Link: https://g.page/quindiotravel/review
   ```
2. Una vez que dejen la reseña, copiarla al sitio

---

## 📊 PLANILLA DE RECOLECCIÓN DE RESEÑAS

Usa esta planilla para organizar las reseñas reales antes de reemplazarlas:

| Plan | Nombre | Fecha viaje | Tipo grupo | Rating | Texto reseña | Fuente | ¿Autorizado? |
|------|--------|-------------|-------------|--------|---------------|--------|--------------|
| plan-1 | | | | ⭐⭐⭐⭐⭐ | | | |
| plan-1 | | | | ⭐⭐⭐⭐⭐ | | | |
| plan-1 | | | | ⭐⭐⭐⭐⭐ | | | |
| plan-2 | | | | ⭐⭐⭐⭐⭐ | | | |
| plan-2 | | | | ⭐⭐⭐⭐⭐ | | | |
| plan-2 | | | | ⭐⭐⭐⭐⭐ | | | |
| plan-3 | | | | ⭐⭐⭐⭐⭐ | | | |
| plan-3 | | | | ⭐⭐⭐⭐⭐ | | | |
| plan-3 | | | | ⭐⭐⭐⭐⭐ | | | |
| plan-4 | | | | ⭐⭐⭐⭐⭐ | | | |
| plan-4 | | | | ⭐⭐⭐⭐⭐ | | | |
| plan-4 | | | | ⭐⭐⭐⭐⭐ | | | |
| plan-5 | | | | ⭐⭐⭐⭐⭐ | | | |
| plan-5 | | | | ⭐⭐⭐⭐⭐ | | | |
| plan-5 | | | | ⭐⭐⭐⭐⭐ | | | |
| plan-6 | | | | ⭐⭐⭐⭐⭐ | | | |
| plan-6 | | | | ⭐⭐⭐⭐⭐ | | | |
| plan-6 | | | | ⭐⭐⭐⭐⭐ | | | |

---

## ⚠️ ADVERTENCIAS LEGALES

### Ley de Protección de Datos (Colombia)
- Los clientes tienen derecho a la privacidad
- Debes obtener autorización explícita antes de publicar
- Si un cliente solicita remover su testimonio, hacerlo inmediatamente
- Puedes usar iniciales si el cliente prefiere anonimato

### FTC Guidelines (si publicas en EE.UU.)
- Los testimonios deben ser verídicos
- No puedes pagar por reseñas positivas
- Debe ser claro que son opiniones de clientes reales

---

## 🚀 PASOS PARA REEMPLAZO

1. **Recolectar reseñas reales** (tiempo estimado: 2-3 horas)
   - Revisar Google Business Profile
   - Revisar WhatsApp
   - Solicitar reseñas a clientes recientes

2. **Llenar planilla** (tiempo estimado: 30 minutos)
   - Organizar por plan
   - Verificar autorización

3. **Reemplazar en archivos HTML** (tiempo estimado: 1 hora)
   - Abrir cada archivo plan-X.html
   - Buscar sección de testimonios
   - Reemplazar placeholders con datos reales

4. **Verificar** (tiempo estimado: 30 minutos)
   - Abrir cada página en navegador
   - Verificar que testimonios se vean correctamente
   - Verificar enlaces a Google Reviews

5. **Commit y push** (tiempo estimado: 10 minutos)
   - Hacer commit con mensaje: "Reemplazar testimonios placeholders con reseñas reales"
   - Push a GitHub

---

## 📞 SOPORTE

Si necesitas ayuda para:
- Exportar reseñas de Google Business Profile
- Formatear correctamente los testimonios
- Verificar que los cambios se vean bien

Contacta a Devin o revisa la documentación de Google Business Profile.

---

*Última actualización: 14 Octubre 2026*
