# Indicaciones IA para Textos de Recomendación WhatsApp — Quindío Travel

**Uso:** Generar respuestas segmentadas por ChatGPT/DeepSeek a partir de esta plantilla.  
**Fuentes de verdad:** `docs/FUENTES_VERDAD_AUTORIZADAS.md` · `assets/js/planes-data.js`  
**Regla de oro:** La IA solo reorganiza y adapta tono. Los precios, incluye y hoteles salen de los bloques bloqueados abajo.

---

## 1. Reglas no negociables

| Regla | Detalle |
|-------|---------|
| ✅ Precios | **Solo** tablas Radio Taxi Temporada Baja (0, 4, 8, 12, 16, 20) o tarifas oficiales diciembre (Radio Taxi). |
| ❌ Prohibido inventar | Precios, descuentos, cupos, "mejor hotel", calificaciones, testimonios, disponibilidad. |
| ❌ Temporada alta / Placa Blanca | Nunca en mensajes base. Solo "cotización especial" si el cliente pregunta. |
| ✅ Testimonios | No inventar. Si no hay reseña real, no incluir. |
| ✅ Incluye | Copiar textual del bloque INCLUYE del plan. No agregar comidas/atractivos. |
| ✅ RNT | Firma: `RNT 18152` |
| ✅ Límite | Máx. 120–150 palabras por mensaje de bienvenida. |
| ✅ CTA | Un solo cierre: invitar a escribir WhatsApp (ya están en WhatsApp; el cierre es "¿te armo fechas/grupo?" o similar). |
| ✅ Tono | Cercano, colombiano, sin jerga de agencias genéricas. |

---

## 2. Bloque de entrada (copiar/pegar a la IA)

Pega SIEMPRE este bloque + el bloque del plan elegido + la instrucción de segmento.

```
EMPRESA: Quindío Travel (RNT 18152), Eje Cafetero, Colombia.
CANAL: WhatsApp. Mensaje de respuesta a un lead que pidió información.
PRECIOS: usa SOLO los valores del bloque del plan. No inventes ni redondees a tu gusto.
INCLUYE: usa SOLO el texto INCLUYE del plan.
TESTIMONIOS: no inventes.
EXTENSIÓN: 80–150 palabras.
ESTRUCTURA: 1 saludo personalizable → 2 por qué encaja este plan para {SEGMENTO} → 3 incluye clave (máx 4 bullets) → 4 desde precio (solo si aplica, con la aclaración de temporada) → 5 cierre con 1 pregunta fácil (fechas / número de personas).
IDIOMA: español neutro Colombia.
NO: emojis en exceso (máx 2-3), hashtags, links largos, "¡El mejor del mundo!".
```

---

## 3. Segmentos (instrucción final)

| Segmento | Instrucción a pegar tras el bloque del plan |
|----------|-----------------------------------------------|
| **Parejas** | Enfócate en: romance, fin de semana, poca logística, cena/desayuno, paseos a dos. Evita "diversión para niños". |
| **Familias** | Enfócate en: niños 2–10 años (precio niño del plan), PANACA/Parque del Café, comidas incluidas, seguridad. |
| **Viajero individual / amigos** | Enfócate en: flexibilidad, duración, atractivos, valor por persona. No asumas pareja ni hijos. |
| **Grupos** | Enfócate en: acomodación triple/cuádruple, logística de grupo, disponibilidad de cupos solo si está en el plan. |

---

## 4. Bloques por plan (datos bloqueados — no editar al pegar en la IA)

### PLAN 1 — Escapada Cafetera de Fin de Semana (2D/1N)
```
TITULO: Escapada Cafetera de Fin de Semana
DURACION: 2 días / 1 noche
GRUPO IDEAL (website): Parejas, Familias pequeñas
INCLUYE: alojamiento finca hotel, desayuno y cena, Pasaporte Múltiple Parque del Café, Pasaporte Terra PANACA, transporte interno (aeropuerto/terminal Armenia ↔ alojamiento ↔ atractivos). *Precio cuádruple.
ATRACTIVOS: Parque del Café, PANACA
ITINERARIO: D1 llegada + PANACA · D2 Parque del Café + regreso
HOTELES ASOCIADOS: hotel-campestre-la-tata, de-la-vega-hotel-campestre, finca-hotel-dorada
PRECIOS ECONÓMICO (Radio Taxi, temporada baja):
- Sin transporte: $425.000
- Doble: $796.000
- Triple: $668.000
- Cuádruple: $602.000
- Niño 2-10: $596.000
```

### PLAN 2 — Aventura Natural en el Eje Cafetero (3D/2N)
```
TITULO: Aventura Natural en el Eje Cafetero
DURACION: 3 días / 2 noches
GRUPO IDEAL (website): Familias, Amigos
INCLUYE: alojamiento finca hotel tradicional, desayunos y cenas, PANACA Pasaporte Terra, Parque del Café Pasaporte Múltiple, transporte interno. *Precio cuádruple.
ATRACTIVOS: Parque del Café, PANACA
ITINERARIO: D1 llegada · D2 PANACA · D3 Parque del Café + regreso
HOTELES ASOCIADOS: finca-hotel-la-esmeralda, hotel-campestre-la-tata
PRECIOS ECONÓMICO (Radio Taxi, temporada baja):
- Sin transporte: $562.000
- Doble: $935.000
- Triple: $805.000
- Cuádruple: $735.000
- Niño 2-10: $729.000
```

### PLAN 3 — Experiencia Completa del Eje Cafetero (4D/3N)
```
TITULO: Experiencia Completa del Eje Cafetero
DURACION: 4 días / 3 noches
GRUPO IDEAL (website): Familias, Grupos
INCLUYE: alojamiento, desayunos y cenas, Valle de Cocora, Salento, Filandia, PANACA, Parque del Café, transporte interno. *Precio cuádruple.
ATRACTIVOS: Parque del Café, PANACA, Salento, Valle de Cocora, Filandia
ITINERARIO: D1 llegada · D2 Valle de Cocora + Salento + Filandia · D3 PANACA · D4 Parque del Café + regreso
HOTELES ASOCIADOS: finca-hotel-los-girasoles, finca-hotel-la-esmeralda, finca-hotel-la-dorada
PRECIOS ECONÓMICO (Radio Taxi, temporada baja):
- Sin transporte: $777.000
- Doble: $1.385.000
- Triple: $1.170.000
- Cuádruple: $1.050.000
- Niño 2-10: $1.038.000
```

### PLAN 4 — Relax y Aventura en Termales del Eje (4D/3N)
```
TITULO: Relax y Aventura en Termales del Eje
DURACION: 4 días / 3 noches
GRUPO IDEAL (website): Parejas, Familias
INCLUYE: alojamiento, desayunos y cenas, Balneario Santa Rosa de Cabal, Parque del Café, PANACA, transporte interno. *Precio cuádruple.
ATRACTIVOS: Parque del Café, PANACA, Termales Santa Rosa
ITINERARIO: D1 llegada · D2 Balneario Santa Rosa de Cabal · D3 PANACA · D4 Parque del Café + regreso
HOTELES ASOCIADOS: finca-hotel-los-girasoles, hotel-campestre-cafe-cafe
PRECIOS ECONÓMICO (Radio Taxi, temporada baja):
- Sin transporte: $798.000
- Doble: $1.495.000
- Triple: $1.250.000
- Cuádruple: $1.125.000
- Niño 2-10: $1.110.000
```

### PLAN 5 — Experiencia Premium del Eje Cafetero / Cultural (4D/3N)
```
TITULO: Experiencia Premium del Eje Cafetero (badge: Vivencial Cultural)
DURACION: 4 días / 3 noches
GRUPO IDEAL (website): Amigos, Familias
INCLUYE: alojamiento, desayunos y cenas, Parque Los Arrieros, PANACA, Parque del Café, transporte interno. *Precio cuádruple.
ATRACTIVOS: Parque Los Arrieros, PANACA, Parque del Café
ITINERARIO: D1 llegada · D2 Parque Los Arrieros · D3 PANACA · D4 Parque del Café + regreso
HOTELES ASOCIADOS: finca-hotel-la-esmeralda, finca-hotel-los-girasoles
PRECIOS ECONÓMICO (Radio Taxi, temporada baja):
- Sin transporte: $788.000
- Doble: $1.297.000
- Triple: $1.120.000
- Cuádruple: $1.020.000
- Niño 2-10: $998.000
```

### PLAN 6 — La Experiencia Definitiva del Eje Cafetero (5D/4N)
```
TITULO: La Experiencia Definitiva del Eje Cafetero
DURACION: 5 días / 4 noches
GRUPO IDEAL (website): Parejas, Grupos VIP
INCLUYE: PANACA, Balneario Santa Rosa de Cabal, Parque del Café, RECUCA, Valle de Cocora, transporte interno. *Precio cuádruple. (Según descripción oficial del website.)
ATRACTIVOS: Parque del Café, PANACA, Termales Santa Rosa, RECUCA, Valle de Cocora
ITINERARIO: D1 llegada · D2 PANACA · D3 Balneario Santa Rosa · D4 Parque del Café · D5 Valle de Cocora + RECUCA + regreso
HOTELES ASOCIADOS: hotel-campestre-cafe-cafe, hotel-campestre-las-camelias, finca-hotel-los-girasoles
PRECIOS ECONÓMICO (Radio Taxi, temporada baja):
- Sin transporte: $1.008.000
- Doble: $1.800.000
- Triple: $1.520.000
- Cuádruple: $1.380.000
- Niño 2-10: $1.360.000
```

### PLAN EXCLUSIVO — Salento-Filandia-Ocaso (4D/3N)
```
TITULO: Plan Exclusivo Salento–Filandia–Ocaso
DURACION: 4 días / 3 noches
INCLUYE (oficial): 3 noches Hotel Vista Hermosa o similar (Salento), 3 desayunos SOLO, Valle de Cocora con Mirador el Bosque, Filandia (Mirador, Museo del Canasto, Calle del Tiempo Detenida), Coffee Tour El Ocaso, asistencia médica, transporte aeropuerto Pereira/Armenia ↔ hotel ↔ atractivos, regreso aeropuerto, comisión 10%.
PRECIOS (Hotel Vista Hermosa o similar):
- Doble: $1.830.000
- Triple: $1.480.000
- Cuádruple: $1.310.000
```

### PLANES ESPECIALES DICIEMBRE (15 dic – 20 ene) — SOLO Radio Taxi
```
TITULO: Plan Especial Diciembre (temporada alta)
DURACION: 4 días / 3 noches · máx 30 cupos
INCLUYE: 3 noches, 3 desayunos, 3 cenas, Pasaporte Parque del Café, Valle de Cocora, Salento y Filandia (mirador, museo del canasto, calle del tiempo detenida), PANACA, RECUCA, asistencia médica, transporte terminal ↔ alojamiento ↔ atractivos.
TARIFAS RADIO TAXI (por persona):
- Cabañas La Esmeralda (Intermedia): 2 pax $1.840.000 · 3 pax $1.589.000 · 4 pax $1.464.000
- Finca Hotel Los Girasoles (Intermedia VIP): 2 pax $2.828.000 · 3 pax $2.577.000 · 4 pax $2.452.000
- Hotel Campestre Café Café (Intermedia VIP): 2 pax $4.034.000 · 3 pax $3.784.000 · 4 pax $3.658.000
NO mencionar Placa Blanca en mensajes base (solo cotización especial si preguntan).
```

---

## 5. Prompt maestro (copiar completo en ChatGPT/DeepSeek)

```
Eres redactor de WhatsApp para Quindío Travel (RNT 18152), agencia del Eje Cafetero.

REGLAS:
- Usa SOLO precios e incluye del bloque del plan que te doy abajo.
- No inventes precios, testimonios, descuentos, cupos ni calificaciones.
- No menciones temporada alta ni Placa Blanca salvo que yo lo pida.
- Tono cercano colombiano, 80–150 palabras, máx 3 emojis.
- Estructura: saludo → encaje con el segmento → 4 bullets de incluye → precio base opcional → 1 pregunta de cierre (fechas o personas).
- Firma implícita: operador con RNT 18152.

SEGMENTO: {{parejas | familias | individual | grupos}}
BLOQUE DEL PLAN:
{{pegar bloque §4}}

Genera 3 variantes del mensaje (A más cálida, B más directa, C más orientada a precio). Numéralas A, B, C.
```

---

## 6. Checklist antes de guardar en la biblioteca

- [ ] ¿Todos los números coinciden con §4 / FUENTES_VERDAD?
- [ ] ¿Aparece algún hotel atractivo o comida que NO esté en INCLUYE?
- [ ] ¿Hay testimonio o "mejores reseñas" inventados?
- [ ] ¿Menciona Placa Blanca o temporada alta sin que aplique?
- [ ] ¿CTA es una sola acción (responder / dar fechas)?
- [ ] ¿Menos de 150 palabras?

Si un ítem falla → rechazar y regenerar con el mismo bloque.

---

## 7. Flujo recomendado (por semana)

1. Elegir 1 plan × 1 segmento.
2. Pegar prompt maestro + bloque plan + segmento.
3. Tomar solo 1 de las 3 variantes.
4. Revisar checklist §6 (5 min).
5. Guardar en biblioteca con etiqueta: `PLAN-3_FAMILIA_B_2026-09`.
6. Usar en WhatsApp Business / respuesta manual.
