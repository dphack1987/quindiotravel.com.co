# Implementación de A/B Testing para Plan Exclusivo

## 🎯 Objetivo del A/B Testing

Optimizar la conversión del Plan Exclusivo Salento, Filandia y Coffee Tour El Ocaso para el mercado español (Madrid y Barcelona).

## 📊 Métricas a Medir

### KPIs Principales:
- **CTR (Click-Through Rate):** Porcentaje de usuarios que hacen clic en CTA
- **Conversion Rate:** Porcentaje de usuarios que contactan por WhatsApp
- **Time on Page:** Tiempo promedio en la página
- **Bounce Rate:** Porcentaje de rebote
- **Cost per Lead:** Costo por lead generado

### Objetivos:
- CTR > 3%
- Conversion Rate > 8%
- Time on Page > 2 minutos
- Bounce Rate < 60%

## 🧪 Pruebas A/B Recomendadas

### PRUEBA 1: Headline del Hero Section

**Variante A (Actual):**
```
Plan Exclusivo Salento, Filandia y Coffee Tour El Ocaso
4 Días / 3 Noches de experiencia premium en el corazón del Eje Cafetero
```

**Variante B (Enfoque Precio):**
```
Colombia desde 280€: Plan Exclusivo 4D/3N
Salento, Valle de Cocora, Filandia y Coffee Tour El Ocaso
```

**Variante C (Enfoque Urgencia):**
```
¡Últimos Cupos! Plan Exclusivo al Eje Cafetero
4 Días / 3 Noches desde 280€ por persona
```

**Implementación:**
```javascript
// A/B Testing para Headline
const headlineVariants = [
    {
        name: 'A-Original',
        title: 'Plan Exclusivo Salento, Filandia y Coffee Tour El Ocaso',
        subtitle: '4 Días / 3 Noches de experiencia premium en el corazón del Eje Cafetero'
    },
    {
        name: 'B-PriceFocus',
        title: 'Colombia desde 280€: Plan Exclusivo 4D/3N',
        subtitle: 'Salento, Valle de Cocora, Filandia y Coffee Tour El Ocaso'
    },
    {
        name: 'C-Urgency',
        title: '¡Últimos Cupos! Plan Exclusivo al Eje Cafetero',
        subtitle: '4 Días / 3 Noches desde 280€ por persona'
    }
];

// Asignar variante aleatoria
const selectedVariant = headlineVariants[Math.floor(Math.random() * headlineVariants.length)];

// Aplicar variante
document.querySelector('.hero h1').textContent = selectedVariant.title;
document.querySelector('.hero p').textContent = selectedVariant.subtitle;

// Tracking
trackABTest('headline_test', selectedVariant.name);
```

---

### PRUEBA 2: CTA Button Color y Texto

**Variante A (Actual):**
- Color: Verde WhatsApp (#25D366)
- Texto: "Cotizar Ahora"

**Variante B:**
- Color: Naranja (#FF6B35)
- Texto: "Consultar Precio"

**Variante C:**
- Color: Azul (#1E88E5)
- Texto: "Reservar Ahora"

**Implementación:**
```javascript
// A/B Testing para CTA Buttons
const ctaVariants = [
    {
        name: 'A-WhatsAppGreen',
        color: '#25D366',
        text: 'Cotizar Ahora'
    },
    {
        name: 'B-Orange',
        color: '#FF6B35',
        text: 'Consultar Precio'
    },
    {
        name: 'C-Blue',
        color: '#1E88E5',
        text: 'Reservar Ahora'
    }
];

const selectedCTA = ctaVariants[Math.floor(Math.random() * ctaVariants.length)];

document.querySelectorAll('.btn-primary').forEach(btn => {
    btn.style.backgroundColor = selectedCTA.color;
    btn.textContent = selectedCTA.text;
});

trackABTest('cta_button_test', selectedCTA.name);
```

---

### PRUEBA 3: Precio Display Format

**Variante A (Actual):**
```
Desde 280€ / persona
* Precios desde 280€ por persona (Sujeto a tipo de cambio oficial)
```

**Variante B (Tabla):**
```
💶 PRECIOS PARA TURISTAS ESPAÑOLES
• Cuádruple: 280€ / persona
• Triple: 315€ / persona
• Doble: 390€ / persona
```

**Variante C (Badge):**
```
🔥 OFERTA LIMITADA
Desde 280€ por persona
```

---

### PRUEBA 4: Imagen del Hero Section

**Variante A (Actual):**
- `eje-cafetero-aerial-view.jpg`

**Variante B:**
- `valle-cocora-hero-banner.jpg`

**Variante C:**
- `filandia-mirador.jpg`

**Implementación:**
```javascript
// A/B Testing para Imagen Hero
const imageVariants = [
    'assets/images/paisajes/eje-cafetero-aerial-view.jpg',
    'assets/images/paisajes/valle-cocora-hero-banner.jpg',
    'assets/images/atractivos/filandia/mirador-filandia.jpg'
];

const selectedImage = imageVariants[Math.floor(Math.random() * imageVariants.length)];
document.querySelector('.hero').style.backgroundImage = `linear-gradient(rgba(89, 60, 31, 0.85), rgba(85, 139, 62, 0.75)), url('${selectedImage}')`;

trackABTest('hero_image_test', selectedImage);
```

---

### PRUEBA 5: Posición del CTA en Hero

**Variante A (Actual):**
- CTA en hero después del texto

**Variante B:**
- CTA superpuesto sobre la imagen

**Variante C:**
- CTA sticky al hacer scroll

---

## 🔧 Herramientas de A/B Testing

### Opción 1: Google Optimize (Recomendado)
```html
<!-- Google Optimize -->
<script src="https://www.googleoptimize.com/optimize.js?id=OPT_CONTAINER_ID"></script>
```

### Opción 2: VWO (Visual Website Optimizer)
```html
<!-- VWO SmartCode -->
<script type='text/javascript'>
var _vwo_code=(function(){
var account_id=YOUR_ACCOUNT_ID,
settings_tolerance=2000,
library_tolerance=2500,
use_existing_jquery=false,
is_spa=1,
hide_element='body',
/* DO NOT EDIT BELOW THIS LINE */
f=false,d=document,code={use_existing_jquery:function(){return use_existing_jquery;},library_tolerance:function(){return library_tolerance;},finish:function(){if(!f){f=true;var a=d.getElementById('_vis_opt_path_hides');if(a)a.parentNode.removeChild(a);}},finished:function(){return f;},load:function(a){var b=d.createElement('script');b.src=a;b.type='text/javascript';b.innerText;b.onerror=function(){_vwo_code.finish();};d.getElementsByTagName('head')[0].appendChild(b);},init:function(){settings_timer=setTimeout('_vwo_code.finish()',settings_tolerance);var a=d.createElement('style'),b='body{opacity:0 !important;filter:alpha(opacity=0) !important;background:none !important;}',h=d.getElementsByTagName('head')[0];a.setAttribute('id','_vis_opt_path_hides');a.setAttribute('type','text/css');if(a.styleSheet)a.styleSheet.cssText=b;else a.appendChild(d.createTextNode(b));h.appendChild(a);this.load('//dev.visualwebsiteoptimizer.com/j.php?a='+account_id+'&u='+encodeURIComponent(d.URL)+'&f='+(+is_spa)+'&r='+Math.random());return settings_timer;}};}());_vwo_settings_timer=_vwo_code.init();
</script>
```

### Opción 3: Implementación Propia (JavaScript)
```javascript
// Sistema de A/B Testing Propio
class ABTestManager {
    constructor() {
        this.tests = {};
        this.sessionId = this.generateSessionId();
    }
    
    generateSessionId() {
        return 'session_' + Math.random().toString(36).substr(2, 9);
    }
    
    registerTest(testName, variants) {
        this.tests[testName] = {
            variants: variants,
            assigned: this.assignVariant(variants)
        };
        
        // Guardar en localStorage para consistencia
        localStorage.setItem(`ab_test_${testName}`, this.tests[testName].assigned);
        
        return this.tests[testName].assigned;
    }
    
    assignVariant(variants) {
        // Verificar si ya existe asignación
        const stored = localStorage.getItem(`ab_test_${testName}`);
        if (stored) return stored;
        
        // Asignar aleatoriamente
        const randomIndex = Math.floor(Math.random() * variants.length);
        return variants[randomIndex];
    }
    
    trackConversion(testName, variant) {
        // Enviar datos al servidor de analytics
        console.log(`Conversion tracked: ${testName} - ${variant}`);
        
        // Aquí integrar con Google Analytics u otra plataforma
        if (typeof gtag !== 'undefined') {
            gtag('event', 'conversion', {
                'event_category': 'ab_test',
                'event_label': `${testName}_${variant}`,
                'value': 1
            });
        }
    }
}

// Uso
const abTest = new ABTestManager();
const headlineVariant = abTest.registerTest('headline_test', ['A-Original', 'B-PriceFocus', 'C-Urgency']);
```

---

## 📱 Pruebas Específicas para Móviles

### PRUEBA MÓVIL 1: Tamaño de CTA
- **Variante A:** 12px padding
- **Variante B:** 18px padding (más grande para touch)

### PRUEBA MÓVIL 2: Posición de Precio
- **Variante A:** Precio en hero
- **Variante B:** Precio visible siempre (sticky)

### PRUEBA MÓVIL 3: Navegación
- **Variante A:** Scroll tradicional
- **Variante B:** Botón de WhatsApp flotante

---

## 🎯 Segmentación de Pruebas

### Por Ubicación:
- Madrid vs Barcelona
- España vs Europa general

### Por Dispositivo:
- Desktop vs Mobile vs Tablet

### Por Fuente de Tráfico:
- Organic vs Paid vs Social

---

## 📅 Cronograma de Pruebas

### Semana 1-2: Headline y CTA Colors
- Prueba headlines (A/B/C)
- Prueba colores de CTA (A/B/C)

### Semana 3-4: Precio Display e Imágenes
- Prueba formatos de precio
- Prueba imágenes del hero

### Semana 5-6: Optimización Móvil
- Pruebas específicas para móvil
- Mejoras de UX mobile

### Semana 7-8: Segmentación
- Pruebas por ubicación
- Pruebas por dispositivo

---

## 📈 Análisis de Resultados

### Estadísticas Necesarias:
- Tasa de conversión por variante
- Diferencia estadísticamente significativa (p < 0.05)
- Tamaño de muestra adecuado (mínimo 1,000 visitantes por variante)

### Herramientas de Análisis:
- Google Analytics 4
- Hotjar (grabaciones de sesiones)
- Crazy Egg (mapas de calor)

---

## 🔄 Iteración y Optimización

### Proceso:
1. Ejecutar prueba
2. Recopilar datos (mínimo 1 semana)
3. Analizar resultados
4. Implementar ganador
5. Crear nueva hipótesis
6. Repetir

### Ejemplo de Iteración:
```
Prueba 1: Headline A vs B
Resultado: B tiene 15% más conversiones
Acción: Implementar B como control
Nueva Prueba: B vs C (nueva hipótesis)
```

---

## 🛠️ Implementación Rápida

### Código de Tracking de Conversión:
```javascript
// Agregar a todos los CTAs de WhatsApp
document.querySelectorAll('a[href*="wa.me"]').forEach(link => {
    link.addEventListener('click', function() {
        // Rastrear conversión
        const variant = localStorage.getItem('ab_test_headline_test');
        trackConversion('headline_test', variant);
        
        // Rastrear CTA
        const ctaVariant = localStorage.getItem('ab_test_cta_button_test');
        trackConversion('cta_button_test', ctaVariant);
    });
});
```

### Dashboard de Monitoreo:
```javascript
// Función para mostrar estadísticas en tiempo real
function showABTestStats() {
    const tests = ['headline_test', 'cta_button_test', 'price_display_test'];
    
    tests.forEach(test => {
        const variant = localStorage.getItem(`ab_test_${test}`);
        console.log(`${test}: ${variant}`);
    });
}

// Ejecutar en consola del navegador
showABTestStats();
```

---

## 📝 Checklist de Implementación

- [ ] Configurar herramienta de A/B testing
- [ ] Definir hipótesis de pruebas
- [ ] Implementar código de tracking
- [ ] Configurar eventos de conversión
- [ ] Establecer período de prueba
- [ ] Monitorear resultados diariamente
- [ ] Analizar significancia estadística
- [ ] Implementar variante ganadora
- [ ] Documentar aprendizajes
- [ ] Planificar siguientes pruebas

---

## 🎯 KPIs de Éxito

### Objetivos después de 8 semanas:
- Aumento del 20% en conversión de WhatsApp
- Reducción del 15% en bounce rate
- Aumento del 30% en time on page
- CTR promedio > 4%

---

*Este documento proporciona un framework completo para implementar A/B testing en el Plan Exclusivo. Adaptar según recursos disponibles y objetivos específicos de marketing.*