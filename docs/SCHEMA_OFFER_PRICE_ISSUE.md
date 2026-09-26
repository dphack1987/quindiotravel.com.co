# Issue: Schema.org Offer sin price - Planes Turísticos

## 📋 Problema Identificado

Los archivos de planes (plan-1.html, plan-2.html, etc.) tienen Schema.org `Offer` sin el campo `price`, lo que limita los rich results en Google.

## 🔍 Análisis de Complejidad

### Estructura de Precios Actual
- **6 planes** con diferentes duraciones (2d1n, 3d2n, 4d3n, 5d4n)
- **4 categorías** por plan: económica, intermedia, intermedia_vip, vip
- **2 temporadas**: baja y alta
- **4 ocupaciones** por categoría: doble, triple, cuadruple
- **Precios niños** (2-10 años)
- **Precios con/sin transporte**

### Ejemplo de Complejidad (plan1_2d1n)
```
economica: $425.000 (baja) / $430.000 (alta)
intermedia: $442.000 (baja) / $450.000 (alta)
intermedia_vip: $590.000 (baja) / $962.000 (alta)
vip: $645.000 (baja) / $1.295.000 (alta)
```

## 🎯 Soluciones Posibles

### Opción 1: Rango de Precios (Recomendada)
```json
"offers": {
    "@type": "Offer",
    "priceCurrency": "COP",
    "price": "425000",
    "priceSpecification": {
        "@type": "PriceSpecification",
        "priceCurrency": "COP",
        "minPrice": "425000",
        "maxPrice": "1295000",
        "priceComponentType": "https://schema.org/BasePrice"
    }
}
```

### Opción 2: Ofertas Múltiples
Crear múltiples `Offer` para cada categoría/ocupación.

### Opción 3: Precio Base con Notas
Usar el precio más bajo con notas sobre variaciones.

## ⚠️ Riesgos

- **Engañoso:** Un solo price no representa la complejidad real
- **Confusión:** Usuarios pueden esperar un precio que no aplica a su caso
- **Manual:** Requiere actualización manual cuando cambian precios

## 📊 Prioridad

**BAJA** - Los rich results funcionan sin price, solo menos completos. Es mejor resolver esto con un análisis cuidadoso que introducir datos incorrectos.

## 🔄 Próximos Pasos

1. Decidir la estrategia de precios para Schema.org
2. Implementar la solución elegida consistentemente en todos los planes
3. Validar con Google Rich Results Test
4. Documentar la estructura final elegida

---
*Generado: 2026-09-26*
*Basado en auditoría de SEO consolidada*