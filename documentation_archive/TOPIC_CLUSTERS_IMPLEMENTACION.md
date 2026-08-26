# TOPIC CLUSTERS IMPLEMENTACIÓN - FASE 4

**Fecha:** 2026-08-20  
**Objetivo:** Reorganizar contenido en pillar pages con enlaces internos bidireccionales

---

## 🎯 **PILLAR PRINCIPAL: Turismo Eje Cafetero**

### **Página Central:** index.html
- Tema principal: Turismo Eje Cafetero y Quindío
- Keywords: "operador turístico quindio", "planes turisticos eje cafetero", "viajes quindio"

### **Supporting Pages Clusters:**

#### **Cluster 1: Destinos Principales**
- **salento.html** - Pueblo más colorido
- **valle-de-cocora.html** - Palmas de cera
- **filandia.html** - Pueblo más limpio
- **parque-del-cafe.html** - Parque temático

#### **Cluster 2: Servicios Específicos**
- **planes.html** - Planes turísticos
- **hoteles-en-salento-economicos.html** - Alojamiento
- **coffee-tour-quindio-precio.html** - Experiencias cafeteras

#### **Cluster 3: Información Práctica**
- **como-llegar-salento-desde-bogota.html** - Transporte
- **viajes-economicos-quindio.html** - Presupuesto

---

## 🔗 **ESTRATEGIA DE ENLACES INTERNOS BIDIRECCIONALES**

### **Enlaces desde index.html:**
- → salento.html: "Descubre Salento, el pueblo más colorido del Quindío"
- → valle-de-cocora.html: "Visita el Valle de Cocora con sus palmas de cera"
- → parque-del-cafe.html: "Disfruta del Parque del Café"
- → filandia.html: "Explora Filandia y su mirador"
- → planes.html: "Ver todos nuestros planes turísticos"
- → hoteles-en-salento-economicos.html: "Encuentra hoteles económicos en Salento"
- → coffee-tour-quindio-precio.html: "Vive la experiencia cafetera"
- → como-llegar-salento-desde-bogota.html: "Cómo llegar desde Bogotá"
- → viajes-economicos-quindio.html: "Viajes económicos al Quindío"

### **Enlaces hacia index.html:**
- Desde todas las páginas: "Volver a la página principal de Quindío Travel"
- Call-to-action: "Contactar operador turístico certificado RNT 18152"

### **Enlaces entre clusters:**
- salento.html ↔ valle-de-cocora.html (mismo destino)
- salento.html ↔ hoteles-en-salento-economicos.html (alojamiento)
- parque-del-cafe.html ↔ coffee-tour-quindio-precio.html (temática café)
- filandia.html ↔ salento.html (pueblos cercanos)
- como-llegar-salento-desde-bogota.html ↔ viajes-economicos-quindio.html (transporte + presupuesto)

---

## 📋 **IMPLEMENTACIÓN DE ENLACES INTERNOS**

### **Agregar en index.html (en sección de destinos):**
```html
<div class="pillar-links">
  <h3>🌿 Destinos Principales del Eje Cafetero</h3>
  <ul>
    <li><a href="salento.html">Salento - Pueblo más colorido</a></li>
    <li><a href="valle-de-cocora.html">Valle de Cocora - Palmas de cera</a></li>
    <li><a href="parque-del-cafe.html">Parque del Café - Atracciones</a></li>
    <li><a href="filandia.html">Filandia - Mirador panorámico</a></li>
  </ul>
</div>
```

### **Agregar enlaces de regreso en todas las páginas:**
```html
<div class="back-to-home">
  <a href="index.html">← Volver a Quindío Travel - Operador Turístico RNT 18152</a>
</div>
```

### **Enlaces contextuales específicos:**
- **salento.html**: Enlace a valle-de-cocora.html ("Caminata al Valle de Cocora")
- **valle-de-cocora.html**: Enlace a salento.html ("Base en Salento para tu visita")
- **parque-del-cafe.html**: Enlace a coffee-tour-quindio-precio.html ("Coffee tour complementario")
- **hoteles-en-salento-economicos.html**: Enlace a salento.html ("Dónde quedarse en Salento")

---

## 📊 **MAPA DE ENLACES INTERNOS**

```
index.html (PILLAR PRINCIPAL)
├── salento.html ↔ valle-de-cocora.html
├── parque-del-cafe.html ↔ coffee-tour-quindio-precio.html
├── filandia.html ↔ salento.html
├── planes.html (central de servicios)
├── hoteles-en-salento-economicos.html ↔ salento.html
├── como-llegar-salento-desde-bogota.html ↔ viajes-economicos-quindio.html
└── Todas las páginas → index.html (enlace de regreso)
```

---

## 🎯 **OBJETIVOS SEO DE LOS CLUSTERS**

### **Authority Building:**
- Fortalecer pillar page principal (index.html)
- Distribuir authority a supporting pages
- Crear silos temáticos coherentes

### **User Experience:**
- Navegación lógica entre temas relacionados
- Facilitar exploración del contenido
- Reducir bounce rate con enlaces relevantes

### **Crawling & Indexing:**
- Estructura clara para crawlers
- Profundidad de crawling optimizada
- Distribución de link equity efectiva

---

**Estado:** Estrategia de topic clusters definida, lista para implementación de enlaces internos