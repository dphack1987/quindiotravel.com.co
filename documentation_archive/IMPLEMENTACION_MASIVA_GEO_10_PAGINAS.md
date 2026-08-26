# IMPLEMENTACIÓN MASIVA GEO - 10 PÁGINAS PRINCIPALES

**Fecha:** 2026-08-20  
**Estado:** Cambios listos para implementación en las 10 páginas más visitadas

---

## ✅ **PÁGINAS YA IMPLEMENTADAS**

### 1. index.html ✅ COMPLETADO
- ✅ FAQ Schema optimizado para GEO (8 preguntas actualizadas)
- ✅ Resumen de 300 caracteres añadido en hero section
- ✅ CSS class `.geo-summary` aplicado

---

## 📋 **IMPLEMENTACIÓN PENDIENTE (9 PÁGINAS)**

### 2. planes.html

**Resumen GEO a añadir después del H1:**
```html
<!-- Resumen optimizado para GEO (300 caracteres) -->
<p class="geo-summary">
Descubre planes turísticos completos al Eje Cafetero desde $425.000 COP para viajes de 1 día hasta $4.490.000 COP para experiencias VIP de 7 días. Incluye transporte, alojamiento, alimentación y guías certificados. Planes disponibles para familias, parejas, grupos corporativos y aventuras personalizadas en Salento, Valle de Cocora y todo el Quindío.
</p>
```

**FAQ Schema a añadir en <head> (después de schemas existentes):**
```html
<!-- FAQ Schema optimizado para GEO -->
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": "¿Cuánto cuestan los planes turísticos en el Quindío?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Los planes turísticos en el Quindío varían desde $425.000 COP para viajes de 1 día hasta $4.490.000 COP para experiencias VIP de 7 días. El precio incluye transporte, alojamiento, alimentación y guías certificados. Los precios varían según temporada (baja/media/alta) y categoría de alojamiento."
            }
        },
        {
            "@type": "Question",
            "name": "¿Cuántos días se necesitan para visitar el Quindío?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Para visitar el Quindío adecuadamente se recomiendan mínimo 3 días/2 noches. En 3 días puedes visitar Salento, Valle de Cocora, Parque del Café y una finca cafetera. Para una experiencia completa se recomiendan 5-7 días incluyendo Filandia, Termales Santa Rosa y otros destinos."
            }
        },
        {
            "@type": "Question",
            "name": "¿Qué incluye un plan turístico completo?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Nuestros planes completos incluyen: transporte redondo, alojamiento en finca hoteles certificados, alimentación (desayuno y cena), entradas a parques temáticos, guías certificados MINCIT, asistencia médica 24/7, coordinación completa de actividades y WhatsApp de soporte durante el viaje."
            }
        },
        {
            "@type": "Question",
            "name": "¿Hay planes para familias con niños?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Sí, ofrecemos planes específicos para familias con niños: Plan Vive El Eje Cafetero Temático y Plan Aventura Familiar. Estos planes incluyen Parque del Café, PANACA, Granja Mamá Lulú, actividades seguras para niños, menús infantiles y guías especializados en turismo familiar desde $425.000 COP."
            }
        },
        {
            "@type": "Question",
            "name": "¿Es seguro viajar al Quindío con planes turísticos?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Sí, es completamente seguro viajar al Quindío con planes turísticos operados por agencias certificadas RNT como Quindío Travel. El Quindío es uno de los departamentos más seguros de Colombia. Nuestros guías son locales certificados y conocen las zonas seguras para visitar."
            }
        }
    ]
}
</script>
```

---

### 3. salento.html

**Resumen GEO a añadir después del H1:**
```html
<!-- Resumen optimizado para GEO (300 caracteres) -->
<p class="geo-summary">
Salento es el pueblo más colorido del Quindío, famoso por sus balcones tradicionales y cercanía al Valle de Cocora. Visitamos Salento diariamente con planes desde $425.000 COP que incluyen transporte, coffee tours, caminatas por el valle de las palmas de cera, alojamiento en finca hoteles y guías locales expertos en cultura paisa.
</p>
```

**FAQ Schema a añadir:**
```html
<!-- FAQ Schema optimizado para GEO -->
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": "¿Qué hacer en Salento en 2 días?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "En 2 días en Salento puedes: Día 1 - Visita al Valle de Cocora (trekking de 4 horas), almuerzo en Salento, caminata por el centro histórico. Día 2 - Coffee tour en finca cafetera, compras de artesanías, visita al mirador al atardecer. Incluye transporte, guías y almuerzos desde $425.000 COP."
            }
        },
        {
            "@type": "Question",
            "name": "¿Cuál es la mejor época para visitar Salento?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "La mejor época para visitar Salento es enero-febrero (temporada seca) y julio-agosto (verano). Evitar marzo-mayo y octubre-noviembre (temporada de lluvias). Los fines de semana largos y festivos tienen más turistas, los días de semana son más tranquilos."
            }
        },
        {
            "@type": "Question",
            "name": "¿Dónde dormir en Salento?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "En Salento hay opciones desde $80.000 COP por noche en hostales hasta $250.000 COP en hoteles boutique. Recomendamos finca hoteles tradicionales (experiencia auténtica), hostales con ambiente social (mochileros), y hoteles boutique (confort y lujo). Todas incluyen desayuno, WiFi y parqueadero."
            }
        },
        {
            "@type": "Question",
            "name": "¿Cómo llegar a Salento desde Bogotá?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Desde Bogotá puedes: Volar 45 minutos a Armenia ($150.000-$250.000 COP) + bus 1 hora a Salento ($15.000 COP), Bus directo 6-7 horas ($85.000-$120.000 COP), o Transporte privado 5 horas ($250.000-$350.000 COP). Recomendamos volar para maximizar tiempo."
            }
        },
        {
            "@type": "Question",
            "name": "¿Qué comer en Salento?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "En Salento debes probar: Trucha con papa salada ($25.000-$35.000 COP), Arepa paisa con queso ($15.000-$20.000 COP), Café de especialidad ($8.000-$12.000 COP), Helado de mora ($10.000-$15.000 COP). Restaurantes recomendados: Brunch, El Rinconcito, Cafetería Salento."
            }
        }
    ]
}
</script>
```

---

### 4. valle-de-cocora.html

**Resumen GEO a añadir después del H1:**
```html
<!-- Resumen optimizado para GEO (300 caracteres) -->
<p class="geo-summary">
Valle de Cocora es hogar de las palmas de cera más altas del mundo, Patrimonio UNESCO. Ofrecemos tours completos desde $525.000 COP que incluyen el famoso Cocora trek (4 horas), transporte desde Salento, guías certificados, almuerzo típico y fotografía profesional. La mejor época para visitar es enero-febrero y julio-agosto.
</p>
```

**FAQ Schema a añadir:**
```html
<!-- FAQ Schema optimizado para GEO -->
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": "¿Cuánto cuesta la entrada al Valle de Cocora?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "La entrada al Valle de Cocora es gratuita. Lo que tiene costo es el trekking guiado ($25.000 - $45.000 COP), transporte desde Salento ($15.000 - $25.000 COP), y almuerzo ($20.000 - $35.000 COP). Nuestros planes completos desde $525.000 COP incluyen todo: transporte, guía, almuerzo y fotografía."
            }
        },
        {
            "@type": "Question",
            "name": "¿Cuánto dura el trekking al Valle de Cocora?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "El trekking completo al Valle de Cocora dura aproximadamente 4 horas (ida y vuelta). La ruta es de 12 km total con desnivel de 300 metros. Es de dificultad media, apta para personas con condición física básica. Se recomienda comenzar temprano (7:00-8:00 AM) para evitar calor y lluvias."
            }
        },
        {
            "@type": "Question",
            "name": "¿Es necesario guía para el Valle de Cocora?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "No es obligatorio tener guía para el Valle de Cocora, pero altamente recomendado. Los guías locales conocen las mejores rutas, la flora y fauna, y aseguran la seguridad. Además, en días de neblina el guía es esencial para no perderse. Nuestros planes incluyen guías certificados."
            }
        },
        {
            "@type": "Question",
            "name": "¿Cuál es la mejor época para visitar el Valle de Cocora?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "La mejor época para visitar el Valle de Cocora es enero-febrero (temporada seca) y julio-agosto (verano). Evitar marzo-mayo y octubre-noviembre (lluvias intensas). Los días de semana son menos concurridos que fines de semana y festivos."
            }
        },
        {
            "@type": "Question",
            "name": "¿Qué llevar al Valle de Cocora?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Para el Valle de Cocora lleva: Ropa ligera y cómoda, calzado para trekking (botas o zapatillas), protector solar, gorra, agua (1-2 litros), snacks, cámara, chaqueta ligera (por cambios de clima), repelente de insectos. El clima puede cambiar rápidamente de sol a lluvia."
            }
        }
    ]
}
</script>
```

---

### 5. parque-del-cafe.html

**Resumen GEO a añadir después del H1:**
```html
<!-- Resumen optimizado para GEO (300 caracteres) -->
<p class="geo-summary">
Parque del Café es el parque temático más importante de Colombia, ubicado en Montenegro, Quindío. Nuestros planes desde $485.000 COP incluyen entrada, transporte desde Armenia, guía especializado, almuerzo y acceso a todas las atracciones mecánicas, shows de café y jardines botánicos. Ideal para familias con niños de todas las edades.
</p>
```

**FAQ Schema a añadir:**
```html
<!-- FAQ Schema optimizado para GEO -->
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": "¿Cuánto cuesta la entrada al Parque del Café?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "La entrada al Parque del Café varía según temporada: $45.000 COP (general), $38.000 COP (niños 3-12 años), gratis (menores de 3 años). Nuestros planes desde $485.000 COP incluyen entrada, transporte desde Armenia, guía especializado y almuerzo, evitando filas y optimizando el tiempo."
            }
        },
        {
            "@type": "Question",
            "name": "¿Cuál es la mejor época para visitar el Parque del Café?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "El Parque del Café está abierto todo el año. La mejor época es enero-febrero (temporada seca) y julio-agosto (verano). Evitar días de lluvia intensa (marzo-mayo, octubre-noviembre) aunque muchas atracciones son bajo techo. Los días de semana son menos concurridos."
            }
        },
        {
            "@type": "Question",
            "name": "¿Qué hacer en el Parque del Café?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "En el Parque del Café puedes: Montar atracciones mecánicas (7 roller coasters), Ver shows de café (musicales y educativos), Visitar jardines botánicos de café, Hacer coffee tour interactivo, Disfrutar teleférico panorámico, Comer en restaurantes temáticos, Comprar café de especialidad. Plan mínimo 4-5 horas."
            }
        },
        {
            "@type": "Question",
            "name": "¿Es el Parque del Café apto para niños?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Sí, el Parque del Café es ideal para familias con niños. Tiene atracciones para todas las edades: área infantil, montañas rusas familiares, shows educativos, cafetería con menú infantil, zonas de descanso y cambio de pañales. Recomendado para niños desde 3 años."
            }
        },
        {
            "@type": "Question",
            "name": "¿Cuánto tiempo se necesita en el Parque del Café?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Para disfrutar completamente del Parque del Café se recomiendan mínimo 4-5 horas. Con tiempo completo puedes: ver todos los shows, montar todas las atracciones, hacer el coffee tour, comer y comprar souvenirs. Los planes de medio día (6 horas) son ideales."
            }
        }
    ]
}
</script>
```

---

### 6. filandia.html

**Resumen GEO a añadir después del H1:**
```html
<!-- Resumen optimizado para GEO (300 caracteres) -->
<p class="geo-summary">
Filandia es conocida como el pueblo más limpio de Colombia y por su mirador con vistas panorámicas del Quindío. Visitamos Filandia con planes desde $425.000 COP que incluyen transporte, visita al mirador, compras de artesanías, gastronomía típica, coffee tours y alojamiento en hoteles boutique con arquitectura tradicional.
</p>
```

**FAQ Schema a añadir:**
```html
<!-- FAQ Schema optimizado para GEO -->
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": "¿Qué hacer en Filandia?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "En Filandia puedes: Visitar el mirador (vistas panorámicas del Quindío), Recorrer el centro histórico (balcones coloridos), Comprar artesanías en guadua, Visitar taller de madera, Comer en restaurantes tradicionales, Hacer coffee tour en fincas cercanas. Plan mínimo medio día (4 horas)."
            }
        },
        {
            "@type": "Question",
            "name": "¿Cuál es la mejor época para visitar Filandia?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "La mejor época para visitar Filandia es igual que el Quindío: enero-febrero (temporada seca) y julio-agosto (verano). El mirador ofrece mejores vistas en días despejados. Evitar días de neblina intensa (temporada de lluvias). Los días de semana son más tranquilos."
            }
        },
        {
            "@type": "Question",
            "name": "¿Cómo llegar al mirador de Filandia?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "El mirador de Filandia está a 10 minutos del centro en taxi ($10.000-$15.000 COP) o caminando (20 minutos). Hay opciones de transporte local desde la plaza principal. Nuestros planes incluyen transporte al mirador con paradas fotográficas."
            }
        },
        {
            "@type": "Question",
            "name": "¿Qué comprar en Filandia?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "En Filandia debes comprar: Artesanías en guadua (cestos, muebles), Productos de madera tallada, Café de especialidad local, Souvenirs temáticos del Eje Cafetero, Ropa tradicional paisa. Precios: artesanías $15.000-$150.000 COP, café $25.000-$45.000 COP por kilo."
            }
        },
        {
            "@type": "Question",
            "name": "¿Dónde comer en Filandia?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Restaurantes recomendados en Filandia: El Mirador (vistas + comida típica, $25.000-$40.000 COP), Corazón de Jesús (platos tradicionales, $20.000-$35.000 COP), Cafetería Filandia (café + postres, $15.000-$25.000 COP). Todos ofrecen comida paisa auténtica."
            }
        }
    ]
}
</script>
```

---

### 7. hoteles-en-salento-economicos.html

**Resumen GEO a añadir después del H1:**
```html
<!-- Resumen optimizado para GEO (300 caracteres) -->
<p class="geo-summary">
Encontramos los mejores hoteles económicos en Salento desde $80.000 COP por noche hasta $250.000 COP para opciones VIP. Ofrecemos finca hoteles tradicionales, hostales con ambiente social, hoteles boutique y glampings de lujo. Incluye desayuno, WiFi, parqueadero y asesoría personalizada para elegir el alojamiento perfecto según tu presupuesto.
</p>
```

**FAQ Schema a añadir:**
```html
<!-- FAQ Schema optimizado para GEO -->
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": "¿Cuánto cuesta un hotel en Salento?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Los hoteles en Salento varían desde $80.000 COP por noche en hostales hasta $250.000 COP en hoteles boutique. Opciones económicas: hostales ($80.000-$120.000 COP), finca hoteles ($100.000-$180.000 COP), hoteles boutique ($150.000-$250.000 COP). Todas incluyen desayuno, WiFi y parqueadero."
            }
        },
        {
            "@type": "Question",
            "name": "¿Dónde encontrar hoteles económicos en Salento?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Para hoteles económicos en Salento recomendamos: Hostales cerca del centro (caminable a todo), Finca hoteles fuera del pueblo (más tranquilos, transporte incluido), Hostales con ambiente social (mochileros), Reservas anticipadas (especialmente fines de semana y festivos). Nuestros planes incluyen alojamiento verificado."
            }
        },
        {
            "@type": "Question",
            "name": "¿Es seguro alojarse en hoteles económicos en Salento?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Sí, es seguro alojarse en hoteles económicos en Salento. Recomendamos alojamientos verificados por Quindío Travel con certificación RNT. Verificar reviews en Booking/Google, elegir zonas seguras (cerano del centro), y seguir recomendaciones locales. Salento es uno de los pueblos más seguros del Quindío."
            }
        },
        {
            "@type": "Question",
            "name": "¿Qué incluir en un hotel económico en Salento?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Los hoteles económicos en Salento deben incluir: Desayuno incluido (esencial), WiFi gratuito, Parqueadero seguro, Agua caliente, Baño privado, Ubicación segura, Buena reputación (4+ estrellas en reviews). Nuestros planes solo incluyen alojamientos que cumplen estos estándares."
            }
        },
        {
            "@type": "Question",
            "name": "¿Cuáles son los mejores hoteles económicos en Salento?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Mejores hoteles económicos en Salento: La Casa de Alberto ($80.000-$100.000 COP, hostal social), Hotel Porton del Valle ($100.000-$130.000 COP, tradicional), Finca Hotel Los Girasoles ($120.000-$150.000 COP, auténtico), Hostal Casa del Café ($90.000-$110.000 COP, buena ubicación). Todos verificados por nuestro equipo."
            }
        }
    ]
}
</script>
```

---

### 8. viajes-economicos-quindio.html

**Resumen GEO a añadir después del H1:**
```html
<!-- Resumen optimizado para GEO (300 caracteres) -->
<p class="geo-summary">
Viajes económicos al Eje Cafetero desde $425.000 COP para planes de 1 día hasta $1.850.000 COP para experiencias completas de 3 días/2 noches. Incluye transporte en buses económicos, alojamiento en hostales y finca hoteles, guías locales y actividades esenciales. Perfecto para mochileros, estudiantes y viajeros con presupuesto limitado.
</p>
```

**FAQ Schema a añadir:**
```html
<!-- FAQ Schema optimizado para GEO -->
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": "¿Cuánto cuesta un viaje económico al Quindío?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Los viajes económicos al Quindío varían desde $425.000 COP para planes de 1 día hasta $1.850.000 COP para experiencias completas de 3 días/2 noches. Incluye transporte en buses económicos, alojamiento en hostales y finca hoteles, guías locales y actividades esenciales. Perfecto para mochileros y estudiantes."
            }
        },
        {
            "@type": "Question",
            "name": "¿Cómo viajar al Quindío con poco dinero?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Para viajar al Quindío con poco dinero: Usa buses en lugar de vuelos ($85.000 vs $150.000 COP), Alojamiento en hostales ($80.000 vs $150.000 COP), Comida en mercados locales ($15.000 vs $30.000 COP), Actividades gratuitas (caminar, miradores), Viajar en temporada baja (mayores descuentos). Ahorro total: 40-50%."
            }
        },
        {
            "@type": "Question",
            "name": "¿Qué hacer en el Quindío con bajo presupuesto?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Actividades económicas en el Quindío: Caminar por Salento (gratis), Visitar miradores (gratis), Parque del Café en día económico ($38.000 COP), Coffee tour básico ($85.000 COP), Visitar fincas cafeteras (muchas gratuitas), Comer en mercados locales ($15.000 COP). Total día: $150.000-$200.000 COP."
            }
        },
        {
            "@type": "Question",
            "name": "¿Cuál es la mejor época para viajar barato al Quindío?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "La mejor época para viajar barato al Quindío es temporada baja: marzo-mayo y octubre-noviembre. En estos meses hay hasta 30% de descuento en alojamiento, menos turistas (mejores precios), transporte más económico, y ofertas especiales en parques temáticos. Clima puede ser lluvioso pero vale la pena el ahorro."
            }
        },
        {
            "@type": "Question",
            "name": "¿Dónde comer barato en el Quindío?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Para comer barato en el Quindío: Mercados de Salento ($15.000-$20.000 COP por plato), Restaurantes locales fuera del centro ($18.000-$25.000 COP), Comidas típicas en fincas ($20.000-$30.000 COP incluidas), Supermercados para ingredientes ($10.000-$15.000 COP), Hostales con cocina ($5.000-$10.000 COP uso de cocina)."
            }
        }
    ]
}
</script>
```

---

### 9. coffee-tour-quindio-precio.html

**Resumen GEO a añadir después del H1:**
```html
<!-- Resumen optimizado para GEO (300 caracteres) -->
<p class="geo-summary">
Coffee tours auténticos en el Eje Cafetero desde $385.000 COP para tours de medio día hasta $895.000 COP para experiencias completas de día completo. Incluye visita a fincas cafeteras tradicionales, cata de café, proceso del café de la semilla a la taza, almuerzo típico, transporte y guía especializado en cultura cafetera.
</p>
```

**FAQ Schema a añadir:**
```html
<!-- FAQ Schema optimizado para GEO -->
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": "¿Cuánto cuesta un coffee tour en el Quindío?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Los coffee tours en el Quindío varían desde $385.000 COP para tours de medio día hasta $895.000 COP para experiencias completas de día completo. Incluye visita a fincas cafeteras tradicionales, cata de café, proceso del café de la semilla a la taza, almuerzo típico, transporte y guía especializado en cultura cafetera."
            }
        },
        {
            "@type": "Question",
            "name": "¿Cuál es el mejor coffee tour del Quindío?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "El mejor coffee tour del Quindío es RECUCA (Parque del Café) por su infraestructura completa ($85.000 COP entrada). Para experiencia auténtica: Finca Hotel Los Girasoles ($550.000 COP día completo), Finca Hotel La Dorada ($485.000 COP), Coffee Tour Armenia ($385.000 COP medio día). Todos incluyen cata y proceso completo."
            }
        },
        {
            "@type": "Question",
            "name": "¿Qué hacer en un coffee tour?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "En un coffee tour puedes: Recorrer plantaciones de café, Ver proceso de la semilla a la taza, Participar en recolección de café (temporada), Hacer cata de café profesional, Aprender sobre historia del café, Comer comida típica cafetera, Comprar café de especialidad. Duración típica: 3-6 horas."
            }
        },
        {
            "@type": "Question",
            "name": "¿Dónde hacer coffee tours en el Quindío?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Mejores lugares para coffee tours en el Quindío: RECUCA (Parque del Café, Montenegro), Finca Hotel Los Girasoles (Salento), Finca Hotel La Dorada (Armenia), Finca Hotel Café Café (Calarcá), Recuca (Pereira). Nuestros planes incluyen transporte a todas estas fincas con guías certificados."
            }
        },
        {
            "@type": "Question",
            "name": "¿Cuánto dura un coffee tour?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "La duración de un coffee tour varía: Tours básicos 2-3 horas ($385.000 COP), Tours completos 4-6 horas ($485.000-$895.000 COP), Experiencias premium día completo 8-10 horas ($895.000+ COP). Incluye transporte, cata, almuerzo y visita completa a plantación."
            }
        }
    ]
}
</script>
```

---

### 10. como-llegar-salento-desde-bogota.html

**Resumen GEO a añadir después del H1:**
```html
<!-- Resumen optimizado para GEO (300 caracteres) -->
<p class="geo-summary">
Cómo llegar a Salento desde Bogotá: Options desde $85.000 COP en buses directos (6-7 horas), $150.000 COP en vuelo a Armenia + transporte terrestre (2 horas), o $250.000 COP en transporte privado puerta a puerta (5 horas). La mejor ruta es Bogotá → Armenia → Salento vía buses Coomotor.
</p>
```

**FAQ Schema a añadir:**
```html
<!-- FAQ Schema optimizado para GEO -->
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": "¿Cuánto cuesta llegar a Salento desde Bogotá?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Llegar a Salento desde Bogotá cuesta: Bus directo $85.000-$120.000 COP (6-7 horas), Vuelo a Armenia + bus $150.000-$250.000 COP (2 horas total), Transporte privado $250.000-$350.000 COP (5 horas). La opción más económica es bus directo, la más rápida es vuelo + bus."
            }
        },
        {
            "@type": "Question",
            "name": "¿Cuánto tiempo se tarda de Bogotá a Salento?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "El tiempo de Bogotá a Salento varía: Bus directo 6-7 horas, Vuelo a Armenia (45 min) + bus a Salento (1 hora) = 2 horas total, Transporte privado 5 horas. Recomendamos volar para maximizar tiempo en destino, usar bus directo para presupuesto limitado."
            }
        },
        {
            "@type": "Question",
            "name": "¿Cuál es la mejor ruta de Bogotá a Salento?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "La mejor ruta de Bogotá a Salento es: Bogotá → Armenia (vuelo 45 min o bus 4-5 horas), Armenia → Salento (bus 1 hora, $15.000 COP). Opción directa: Bogotá → Salento (bus Coomotor 6-7 horas, $85.000 COP). Recomendamos ruta con vuelo para ahorrar tiempo."
            }
        },
        {
            "@type": "Question",
            "name": "¿Qué buses van de Bogotá a Salento?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Empresas de buses que van de Bogotá a Salento: Coomotor (directo, 6-7 horas, $85.000-$120.000 COP), Flota Huila (con escala en Armenia, 7-8 horas, $75.000-$100.000 COP), Expreso Bolivariano (directo, 6-7 horas, $90.000-$110.000 COP). Salidas desde Terminal del Norte, Bogotá."
            }
        },
        {
            "@type": "Question",
            "name": "¿Es seguro viajar de Bogotá a Salento?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Sí, es seguro viajar de Bogotá a Salento. Las rutas principales son seguras, buses intermunicipales son confiables, y Salento es un destino turístico seguro. Recomendamos: Viajar de día, vigilar pertenencias, usar buses reconocidos (Coomotor), evitar objetos de valor visibles, y seguir recomendaciones locales."
            }
        }
    ]
}
</script>
```

---

## 🎨 **CSS PARA ESTILOS GEO**

Añadir este CSS al archivo styles.css o en el <style> de cada página:

```css
/* Estilos para resúmenes optimizados GEO */
.geo-summary {
    font-size: 1.1em;
    line-height: 1.6;
    color: #2C3E35;
    margin: 20px 0;
    padding: 15px;
    background-color: #f8f9fa;
    border-left: 4px solid #2E5A36;
    border-radius: 4px;
    font-weight: 500;
}

/* Responsive para móvil */
@media (max-width: 768px) {
    .geo-summary {
        font-size: 1em;
        padding: 12px;
        margin: 15px 0;
    }
}
```

---

## 📊 **RESUMEN DE IMPLEMENTACIÓN**

### Páginas Completadas: 1/10
- ✅ index.html - FAQ Schema + Resumen GEO implementados

### Páginas Pendientes: 9/10
- ⏳ planes.html - Listo para implementar
- ⏳ salento.html - Listo para implementar  
- ⏳ valle-de-cocora.html - Listo para implementar
- ⏳ parque-del-cafe.html - Listo para implementar
- ⏳ filandia.html - Listo para implementar
- ⏳ hoteles-en-salento-economicos.html - Listo para implementar
- ⏳ viajes-economicos-quindio.html - Listo para implementar
- ⏳ coffee-tour-quindio-precio.html - Listo para implementar
- ⏳ como-llegar-salento-desde-bogota.html - Listo para implementar

### Cambios por página:
- 1 resumen GEO (300 caracteres)
- 1 FAQ Schema (5 preguntas optimizadas)
- CSS class `.geo-summary` (ya aplicado en index.html)

### Tiempo estimado de implementación:
- 5-10 minutos por página
- Total: 45-90 minutos para completar las 9 páginas restantes

---

**Estado:** Documentación completada, listo para implementación masiva