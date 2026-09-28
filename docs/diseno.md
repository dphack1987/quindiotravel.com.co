# Quindío Travel — Sistema de Diseño (Fase 1)

> Única fuente de verdad de la línea visual. Cualquier cambio de diseño se documenta aquí **antes** de aplicarse en CSS.
> Investigación de competencia que respalda estas decisiones: auditoría de diseño 26-sep-2026 (agenciabotero, cocoratours, viajesarmenia, kuaraexpeditions + Booking/Airbnb/Skyscanner/Tripadvisor).

---

## 1. Tokens canónicos

**Ubicación única:** bloque `:root` de `styles.css` (línea ~265, bajo el comentario "TOKENS CANÓNICOS").

⚠️ **Prohibido** declarar `:root` con estos tokens en otros ficheros. El critical CSS inline de `index.html` solo replica el mínimo para el primer pintado y **debe coincidir exactamente** con los valores de `styles.css`.

### Colores
| Token | Valor | Uso |
|---|---|---|
| `--verde-cafe` | `#2E5A36` | Color de marca, headers, enlaces |
| `--verde-claro` | `#4E8755` | Gradientes, acentos secundarios |
| `--blanco` | `#FFFFFF` | Superficies |
| `--amarillo-suave` | `#E6B800` | Destacados, precios (contraste AA) |
| `--marron-madera` | `#8D5B4C` | Acento cálido, hovers |
| `--gris-claro` | `#F4F6F4` | Fondo de página |
| `--texto-oscuro` | `#2C3E35` | Texto principal |
| `--naranja-brillante` | `#E67300` | CTA/urgencia (contraste AA+) |
| `--azul-profundo` | `#4A90E2` | Enlaces informativos |
| `--vip-gold` | `#B8960C` | Badges VIP |
| `--whatsapp-verde` / `-oscuro` | `#25D366` / `#128C7E` | Botones WhatsApp |

> **Pendiente (Fase 2):** unificar el acento de CTA en un único ámbar (`--acento`) y dejar el naranja solo para urgencia. No hacer hasta revisión visual aprobada.

### Tipografía
| Token | Valor |
|---|---|
| `--font-titulos` | `'Fraunces', Georgia, 'Times New Roman', serif` |
| `--font-texto` | `'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif` |

- Carga: **auto-hospedada** en `assets/fonts/` (subconjunto latin, licencia OFL), declarada con `@font-face` al inicio de `styles.css`. Sin dependencia de terceros (Google Fonts está bloqueado en China y afectaría a `/zh/`).
- Pesos: Fraunces 600-900 (rango variable) · Inter 400-900 (rango variable) · `font-display: swap`.
- Regla: `* { font-family: var(--font-texto) }` y `h1,h2,h3,h4,.section-title { font-family: var(--font-titulos) }`.
- **Nunca** escribir `font-family:` literal fuera de este bloque.
- Al añadir pesos o subconjuntos: descargar de Google Fonts, guardar en `assets/fonts/` y añadir el `@font-face` correspondiente.

### Escalas (usar en lugar de valores sueltos)
- **Texto:** `--text-xs · --text-sm · --text-base · --text-md · --text-lg · --text-xl · --text-2xl · --text-hero` (ratio 1.25; `--text-hero` es fluido con `clamp`).
- **Radio:** `--radius-sm(8) · md(12) · lg(20) · xl(28) · pill(50)`.
- **Espacio:** `--space-1..16` (múltiplos de 4px).
- **Sombra:** `--shadow-sm · md · lg · xl` (4 niveles; sustituye a las 130 sombras sueltas).
- **z-index:** `--z-nav(1001) · --z-float(1002) · --z-sticky(1010) · --z-popup(2000) · --z-max(9999)`.
- **Movimiento:** `--transition-fast(.18s) · --transition-base(.3s)`.

---

## 2. Reglas de estilo (código)

1. **Un solo `:root`** (el de `styles.css`). Sin tokens duplicados.
2. **Sin `transition: all`** — declarar la propiedad concreta.
3. **Sin valores mágicos nuevos**: todo `font-size`, `border-radius`, `box-shadow`, `z-index` nuevos pasa por un token.
4. Los selectores duplicados existentes se irán eliminando progresivamente **reemplazando** su valor por `var(--token)`, nunca añadiendo otra capa.
5. Los bloques históricos (`ENRIQUECIMIENTO VISUAL HOME`, `REFINAMIENTO VISUAL PREMIUM`, `HERO VISUAL FIX`, `8 PATRONES GLOBALES`) son **legado congelado**: no ampliar, solo migrar a tokens.

## 3. Ficheros deprecated (no usar, no borrar aún)

| Fichero | Motivo |
|---|---|
| `styles.min.css` | Obsoleto/divergente; solo lo precachea `sw.js` |
| `assets/css/critical.css` + `.min.css` | 0 páginas lo referencian; `critical.min.css` lo precachea `sw.js` |
| `assets/css/wa-qualifier.css` | Huérfano |
| `components/` (todo) | Plantillas no ensambladas; sirven como documentación |

⚠️ **No borrar** `styles.min.css` ni `critical.min.css` hasta actualizar la lista de precache de `sw.js` (rompería la instalación del Service Worker).

---

## 4. Patrones de conversión (Fase 2, pendiente de aprobación)

Prioridad según investigación (Baymard + competencia local):
1. Buscador como contenido principal del home (arriba del fold, 2-3 campos).
2. Barra de cotización sticky → WhatsApp con mensaje precargado.
3. Precio visible en card: "Desde $425.000 COP" + chips "incluye".
4. Franja "RNT 18152 · Verifícanos" con botón copiar.
5. Reseñas de Google enlazadas junto al CTA.
6. Hero en 1ª posición (hoy está tras 3 bloques de promo).
7. FAQ visible (hoy solo existe como JSON-LD).

## 5. Innovación seleccionada (Fase 3)

**Buscador instantáneo de planes** sobre `planes.json` (filtros: destino, días, presupuesto, tipo) — 100% client-side, reutiliza `cotizador.js`/`tarifas.json`. Opción secundaria: mapa Leaflet del Eje Cafetero con GeoJSON estático (0 API key).

---

## Historial

| Fecha | Cambio |
|---|---|
| 2026-09-26 | Fase 1: tokens canónicos, tipografía Fraunces+Inter auto-hospedada (`assets/fonts/`), unificación de drift de color (`#F4D35E/#FF8C42/#D4AF37` → `#E6B800/#E67300/#B8960C` en todas las fuentes) |
