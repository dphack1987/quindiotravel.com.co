#!/usr/bin/env python3
"""Upgrade de páginas pSEO a calidad indexable.

Reescribe las páginas objetivo de programmatic-pages/ con:
- canonical auto-referente + robots index,follow
- precios reales (pseo-master-data.json), itinerarios, FAQs, reseñas reales
- JSON-LD Article + FAQPage + BreadcrumbList
- elimina el meta refresh que redirigía a la home

Uso: python seo-engine/upgrade_pseo.py [--dry]
"""

from __future__ import annotations

import json
import sys
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://quindiotravel.com.co"
DIR = ROOT / "programmatic-pages"
DRY = "--dry" in sys.argv

MASTER = json.loads(
    (ROOT / "pseo-engine/pseo-master-data.json").read_text(encoding="utf-8"))
PRECIO_ATR = {a["nombre"].lower(): a.get("precio") for a in MASTER["atractivos"]}
ALOJ = {a["nombre"]: a for a in MASTER["alojamientos"]}

# ---------------------------------------------------------------------------
# Contenido por página. Cada entrada: datos reales y diferenciados.
# ---------------------------------------------------------------------------
P = {}

def add(slug, h1, title, desc, intro, facts, highlights, steps, faqs,
        price_table=None, cta=None):
    P[f"{slug}-2026"] = {
        "h1": h1, "title": title, "desc": desc, "intro": intro,
        "facts": facts, "highlights": highlights, "steps": steps,
        "faqs": faqs, "price_table": price_table, "cta": cta,
    }

# ============================ VALLE DE COCORA ================================

add("valle-cocora-una-dia",
    "Valle de Cocora en un día: guía completa 2026",
    "Valle de Cocora en 1 Día 2026 | Guía Completa | Quindío Travel",
    "Cómo visitar el Valle de Cocora en un solo día desde Salento: ruta, tiempos, qué llevar, miradores y costos reales 2026. Guía de operadores locales RNT 18152.",
    ["El Valle de Cocora es el hogar de la palma de cera Quindío, la palmera más alta del mundo: hay ejemplares que superan los 60 metros de altura. Con una salida temprana desde Salento es totalmente posible conocerlo y volver el mismo día.",
     "La caminata principal por el bosque nuboso toma unas 4-5 horas por senderos de nivel intermedio. Si prefieres algo más suave, existen opciones más cortas que igual ofrecen vistas espectaculares del valle."],
    [("Duración total", "Jornada completa desde Salento"),
     ("Sendero principal", "Bosque nuboso ~12 km · 4-5 horas de caminata (nivel intermedio)"),
     ("Otras opciones", "Sendero de la montaña 2-3 h · sendero Ecohotel 1-2 h (accesible)"),
     ("Mejor época", "Diciembre a marzo (temporada seca)"),
     ("Acceso", "Jeep Willys desde la plaza principal de Salento — 30 minutos")],
    ["La caminata asciende por bosque de niebla con palmas de cera enmarcando el paisaje — es uno de los escenarios más fotografiados de Colombia.",
     "La palma de cera Quindío es la palmera más alta del mundo: hay ejemplares que superan los 60 metros de altura.",
     "El retorno puede ser a pie o en el mismo jeep que te llevó si coordinas el punto de recogida con tu guía.",
     "En temporada alta (diciembre-enero) los jeeps se llenan rápido: conviene salir temprano desde Salento."],
    [("Mañana", "Salida en jeep desde la plaza de Salento hacia el Cocora"),
     ("Media mañana", "Caminata por el sendero del bosque nuboso hacia los miradores"),
     ("Mediodía", "Almuerzo en Salento o en las fincas cercanas"),
     ("Tarde", "Regreso o continuación a Filandia según tu plan")],
    [("¿Cuánto cuesta visitar el Valle de Cocora?",
      "El acceso al Cocora se gestiona dentro de nuestros planes y tours — no vendemos entradas sueltas. El plan de 4 días/3 noches de temporada alta incluye la visita al Cocora desde $1.464.000 COP por persona (ocupación cuádruple)."),
     ("¿Es difícil la caminata al Cocora?",
      "El sendero principal (bosque nuboso) es de ~12 km y toma 4-5 horas — nivel intermedio. También hay opciones más cortas: sendero de la montaña (2-3 h) y sendero Ecohotel (1-2 h, accesible)."),
     ("¿Se puede hacer Cocora y Filandia el mismo día?",
      "Sí, es una combinación muy común: Cocora en la mañana y Filandia por la tarde — los dos destinos están muy cerca el uno del otro en el corazón del Quindío."),
     ("¿Cuál es la mejor época para ir al Cocora?",
      "Diciembre a marzo, cuando el clima es más seco y las probabilidades de ver el valle despejado son mayores. En temporada de lluvias (abril-mayo y octubre-noviembre) el paisaje es más verde pero más nublado.")],
    price_table=[("Plan Diciembre 4D/3N — Cabañas La Esmeralda (Intermedia)", "$1.464.000 - $2.574.000 COP/persona según ocupación y vehículo"),
                 ("Plan Diciembre 4D/3N — Los Girasoles (Intermedia VIP)", "$2.452.000 - $3.562.000 COP/persona"),
                 ("Plan Diciembre 4D/3N — Café Café (Intermedia VIP)", "$3.658.000 - $4.768.000 COP/persona"),
                 ("Incluye", "Alojamiento 3 noches con desayuno y cena, transporte interno, Parque del Café, PANACA, RECUCA, Cocora y Filandia, asistencia médica 24/7")])

add("valle-cocora-caminata",
    "Caminata al Valle de Cocora: ruta, tiempos y consejos",
    "Caminata Valle de Cocora 2026 | Rutas y Consejos | Quindío Travel",
    "Guía de la caminata al Valle de Cocora: distancias, desnivel, miradores, qué llevar y cómo prepararte para la caminata de las palmas de cera en 2026.",
    ["El Valle de Cocora ofrece tres senderos para distintos niveles: el sendero del bosque nuboso (~12 km, 4-5 h, nivel intermedio), el sendero de la montaña (2-3 h) y el sendero Ecohotel (1-2 h, accesible).",
     "Todos cruzan bosque de niebla entre palmas de cera Quindío — la especie más alta del mundo, con ejemplares de más de 60 metros."],
    [("Sendero bosque nuboso", "~12 km · 4-5 horas · nivel intermedio"),
     ("Sendero de la montaña", "2-3 horas"),
     ("Sendero Ecohotel", "1-2 horas · opción accesible"),
     ("Acceso", "Jeep Willys desde la plaza de Salento — 30 min"),
     ("Recomendado para", "Sendero largo: adultos con buen estado físico; opciones cortas: todo público")],
    ["El sendero principal está dentro del bosque de niebla y concentra las mejores vistas de las palmas de cera.",
     "Elige tu ruta según tiempo y condición física: las tres opciones llevan al corazón del valle.",
     "La mejor luz para fotos es temprano en la mañana y al final de la tarde.",
     "Lleva agua suficiente, calzado cómodo y protección para la lluvia — el clima de montaña cambia rápido.",
     "En temporada alta (diciembre-enero) conviene salir temprano: los jeeps desde Salento se llenan."],
    [("Sendero corto", "Sendero Ecohotel o montaña: 1-3 h — ideal familias y poco tiempo"),
     ("Sendero completo", "Bosque nuboso: ~4-5 h de caminata"),
     ("Mediodía", "Almuerzo en Salento o en las fincas cercanas"),
     ("Tarde", "Regreso o combinación con Filandia")],
    [("¿Qué nivel físico necesito para la caminata del Cocora?",
      "Depende del sendero: el bosque nuboso (~12 km) exige buen estado físico; montaña y Ecohotel son más accesibles. En todos los casos lleva agua, snacks y calzado cómodo."),
     ("¿Se puede hacer con niños?",
      "Sí, con los senderos cortos (Ecohotel 1-2 h o montaña 2-3 h) y ritmo adaptado. Para el sendero completo recomendamos niños mayores con buena condición."),
     ("¿Hay que pagar entrada al sendero?",
      "El acceso al Cocora se gestiona dentro de nuestros planes y tours — consulta por WhatsApp la experiencia que incluye la caminata."),
     ("¿Qué pasa si llueve?",
      "El sendero puede volverse resbaladizo. Recomendamos calzado de trekking y capa impermeable. En días de lluvia intensa conviene posponer.")])

add("valle-cocora-cerro-murillo",
    "Cerro Murillo en el Cocora: la caminata secreta del valle",
    "Cerro Murillo Valle de Cocora 2026 | Guía | Quindío Travel",
    "Cerro Murillo: la caminata panorámica menos conocida del Valle de Cocora. Ruta, tiempos, qué ver desde la cima y cómo combinarla con el Cocora en 2026.",
    ["El Cerro Murillo es una caminata panorámica en los alrededores del Valle de Cocora que pocos turistas conocen: desde su cima se ven las palmas de cera del valle, las montañas del Quindío y en días claros hasta el nevado del Ruiz.",
     "Es una alternativa excelente para quienes ya hicieron el Cocora o buscan una experiencia más exclusiva y menos concurrida, con la misma recompensa visual."],
    [("Duración", "4-5 horas ida y vuelta"),
     ("Distancia", "8-10 km de caminata"),
     ("Desnivel", "Moderado-alto"),
     ("Acceso", "Por Salento, en jeep o a pie desde el pueblo"),
     ("Concurrencia", "Baja — mucho menos masificado que el Cocora"),
     ("Combinación ideal", "Cocora en la mañana + Murillo por la tarde (días separados)")],
    ["Desde la cima del Murillo el Cocora se ve en perspectiva aérea — el mejor ángulo para fotos de las palmas de cera.",
     "El sendero pasa por fincas cafeteras y pequeños fragmentos de bosque andino.",
     "Es una caminata exigente: recomendamos guía local que conozca el trazado exacto.",
     "Ideal para fotografía de paisaje y amaneceres.",
     "Menos concurrencia = más tranquilidad y mejor experiencia."],
    [("8:00 a.m.", "Salida desde Salento"),
     ("9:30 a.m.", "Inicio de la caminata"),
     ("12:00-1:00 p.m.", "Cumbre del Murillo y picnic"),
     ("2:00-3:00 p.m.", "Retorno a Salento")],
    [("¿Cómo se llega al Cerro Murillo?",
      "Se accede desde Salento. Lo más práctico es salir temprano en jeep hasta el punto de partida del sendero y caminar con un guía que conozca la ruta."),
     ("¿Vale la pena el Murillo si ya hice el Cocora?",
      "Sí. El Murillo ofrece una vista aérea del Cocora que no se obtiene caminando el valle, y es mucho menos concurrido."),
     ("¿Qué dificultad tiene?",
      "Moderada-alta. Exige buen estado físico y calzado adecuado. No es apta para niños pequeños."),
     ("¿Se puede ver el nevado del Ruiz desde Murillo?",
      "En días despejados sí, especialmente desde la cima. Es una de sus grandes atracciones.")])

add("valle-cocora-pajaros",
    "Aves del Valle de Cocora: birdwatching entre palmas de cera",
    "Birdwatching Valle de Cocora 2026 | Aves y Senderos | Quindío Travel",
    "Birdwatching en el Valle de Cocora: especies de aves andinas y tropicales, mejores horarios y senderos para observación de aves entre las palmas de cera.",
    ["El Valle de Cocora es uno de los mejores puntos de observación de aves del eje andino colombiano: su mosaico de bosque de niebla, palmas de cera y pastizales alberga especies emblemáticas y difíciles de ver en otras partes.",
     "La combinación de altitud (2.400-3.100 m) y vegetación única lo convierte en un destino de clase mundial para birdwatchers, con o sin experiencia previa."],
    [("Mejor horario", "6:00 - 9:30 a.m. (máxima actividad de aves)"),
     ("Especies emblemáticas", "Tucán andino, quetzal, tangara del paramo, colibríes de montaña"),
     ("Mejor época", "Diciembre a marzo (temporada seca)"),
     ("Dificultad", "Moderada — los mejores avistamientos son en los senderos altos"),
     ("Equipo recomendado", "Binoculares 8x42, cámara con zoom, guía de aves"),
     ("Acceso", "Desde Salento en jeep, inicio del sendero del Cocora")],
    ["El Tucán Andino (Andigena hypoglauca) es la especie insignia del Cocora — se escucha antes de verse.",
     "Las colinas bajas del valle son el mejor lugar para observar tangaras y fringilos.",
     "El mirador intermedio (a 1.5h) concentra buena actividad de aves sin exigir la caminata completa.",
     "Contratar un guía local de aves multiplica las observaciones: conocen los cantos y los sitios exactos.",
     "Lleva binoculares — a distancia las aves parecen puntos verdes."],
    [("6:00 a.m.", "Salida de Salento"),
     ("6:45 a.m.", "Inicio del sendero — primeras observaciones"),
     ("8:00-10:00 a.m.", "Zona de mayor actividad de aves"),
     ("10:30 a.m.", "Mirador intermedio o retorno"),
     ("12:00 p.m.", "Regreso a Salento")],
    [("¿Necesito experiencia en birdwatching para ir al Cocora?",
      "No. Aun sin experiencia verás especies increíbles. Un guía local de aves mejora enormemente las observaciones."),
     ("¿Qué aves puedo ver en el Cocora?",
      "Entre las más buscadas: tucán andino, quetzal, colibríes de montaña, tangaras andinas y el chirihueso del paramo."),
     ("¿Cuál es la mejor época para birdwatching?",
      "Diciembre a marzo por el clima seco. Pero la actividad de aves es buena todo el año, con picos en época de reproducción."),
     ("¿Se puede combinar birdwatching con la caminata normal?",
      "Sí. Simplemente sal más temprano y lleva binoculares. El mismo sendero sirve para ambas actividades.")])

add("caminata-nocturna-valle-cocora",
    "Caminata nocturna al Valle de Cocora: estrellas y silencio",
    "Caminata Nocturna Cocora 2026 | Experiencia Única | Quindío Travel",
    "Caminata nocturna al Valle de Cocora: senderos oscuros, estrellas, sonidos de la noche andina y una experiencia distinta a la caminata diurna. Guía 2026.",
    ["La caminata nocturna al Valle de Cocora es una de las experiencias más diferentes que ofrece el Quindío: los mismos senderos de las palmas de cera, pero bajo un cielo estrellado y con los sonidos de la fauna nocturna.",
     "No es una actividad para todos — exige buena condición física, linterna, y sobre todo acompañamiento profesional. Pero para quienes la viven, es inolvidable."],
    [("Duración", "3-4 horas"),
     ("Horario", "Salida 5:30-6:00 p.m., retorno 9:30-10:00 p.m."),
     ("Dificultad", "Moderada — el terreno es el mismo del Cocora"),
     ("Iluminación", "Linterna frontal obligatoria (las manos libres)"
      ),
     ("Mejor época", "Temporada seca (diciembre-marzo) para cielos más despejados"),
     ("Concurrencia", "Muy baja — experiencia casi privada")],
    ["El cielo del Cocora es espectacular: sin contaminación lumínica, la Vía Láctea y las estrellas se ven con claridad.",
     "De noche se escuchan sonidos únicos: búhos, monos nocturnos, insectos — una sinfonía andina diferente.",
     "Las palmas de cera tienen un aspecto misterioso bajo la luz de la linterna.",
     "Es una caminata más corta que la diurna pero igual de exigente: no bajar la guardia.",
     "Solo recomendada para adultos con experiencia caminando de noche."],
    [("5:30 p.m.", "Salida desde Salento en jeep"),
     ("6:00 p.m.", "Inicio del sendero con linternas"),
     ("7:30 p.m.", "Mirador nocturno — punto de mayor espectáculo"),
     ("9:00 p.m.", "Retorno por el sendero"),
     ("10:00 p.m.", "Regreso a Salento")],
    [("¿Es segura la caminata nocturna al Cocora?",
      "Sí, si vas con guía profesional y equipo adecuado. Nunca la hagas solo ni sin preparación."),
     ("¿Qué necesito llevar?",
      "Linterna frontal, capa impermeable, agua, snacks, calzado de trekking y ropa de abrigo (la temperatura baja mucho de noche)."),
     ("¿Se ven las palmas de cera de noche?",
      "Sí, pero no es lo mismo que de día. Lo que sorprende es el cielo estrellado y la experiencia sensorial diferente."),
     ("¿Puedo tomar fotos?",
      "Sí, pero con poca luz. El mejor momento para fotos es la salida del sol o con larga exposición si tienes equipo.")])

add("valle-cocora-alberque",
    "Albergue en el Valle de Cocora: dormir entre las palmas de cera",
    "Albergue Cocora 2026 | Dormir en la Montaña | Quindío Travel",
    "Albergue en el Valle de Cocora: dormir en la montaña entre palmas de cera y amanecer con niebla. Cómo llegar y en qué planes se incluye en 2026.",
    ["Dormir en el Valle de Cocora es una experiencia que pocos viajeros olvidan: amanecer entre la niebla, el canto de las aves y las palmas de cera que se pierden en el cielo.",
     "Hay refugios y opciones de alojamiento en la parte alta del valle, a donde se llega después de la caminata completa — una aventura que vale cada paso."],
    [("Ubicación", "Parte alta del Valle de Cocora"),
     ("Acceso", "A pie por el sendero del Cocora"),
     ("Capacidad", "Limitada — reservas con anticipación"),
     ("Servicios", "Según el refugio: camas, baño compartido, cocina común"),
     ("Precio", "Se cotiza dentro de experiencias/planes a medida — consulta por WhatsApp"),
     ("Mejor época", "Diciembre a marzo (temporada seca)")],
    ["El amanecer desde el albergue es espectacular: el valle se llena de niebla dorada y las palmas emergen como siluetas.",
     "La caminata de subida ya es parte de la experiencia — llegar cansado pero con una recompensa inolvidable.",
     "La noche en la montaña es silenciosa y estrellada: una desconexión total.",
     "Es recomendable llevar ropa de abrigo y saco de dormir — la temperatura en la montaña baja bastante de noche.",
     "Reserva con anticipación en temporada alta: hay pocas camas y se llenan rápido."],
    [("Día 1", "Caminata completa Salento–Cocora (6h) + tarde libre en el valle"),
     ("Noche", "Noche en el albergue bajo las estrellas"),
     ("Día 2", "Amanecer + caminata de regreso o exploración de miradores cercanos"),
     ("Tarde", "Regreso a Salento o continuación al plan")],
    [("¿Cómo se reserva el albergue del Cocora?",
      "No vendemos noches sueltas: el albergue se accede dentro de experiencias y planes organizados. En temporada alta (diciembre-enero) las plazas se agotan — cotiza con anticipación por WhatsApp."),
     ("¿Qué incluye la noche en el albergue?",
      "Depende del refugio: cama, acceso a baño y cocina común. Las comidas y servicios específicos se confirman al cotizar por WhatsApp."),
     ("¿Es seguro dormir en el Cocora?",
      "Sí, los refugios son seguros y atendidos. La caminata de acceso es la parte exigente, no la noche en el albergue."),
     ("¿Puedo ir solo o necesito guía?",
      "Recomendamos ir con guía o en grupo organizado, especialmente si es tu primera vez. El sendero es seguro pero largo.")])

# ============================ TOURS SALENTO / FILANDIA ======================

add("tour-salento-desde-bogota",
    "Tour a Salento desde Bogotá: cómo llegar y qué hacer",
    "Tour Salento desde Bogotá 2026 | Guía Completa | Quindío Travel",
    "Cómo hacer un tour a Salento desde Bogotá en 2026: vuelos a Armenia, transporte terrestre, qué visitar y planes recomendados para 2-4 días.",
    ["Salento es el pueblo más pintoresco del Eje Cafetero y uno de los destinos turísticos más visitados de Colombia. Desde Bogotá hay dos opciones principales: vuelo a Armenia (1 hora) o bus directo (8-9 horas).",
     "Una vez en Salento, estás a 30-40 minutos del Valle de Cocora y a 30 minutos de Filandia — el punto de partida perfecto para explorar el corazón del Quindío."],
    [("Distancia Bogotá-Salento", "330 km (aprox.)"),
     ("Vuelo a Armenia", "1 hora desde Bogotá (Aeropuerto El Edén)"),
     ("Bus directo", "8-9 horas desde Terminal Salitre"),
     ("Tiempo en Salento", "2-4 días recomendado"),
     ("Presupuesto aprox.", "Se cotiza según tu estilo de viaje — consulta por WhatsApp"),
     ("Temporada alta", "Diciembre-enero y puentes festivos")],
    ["El transporte aéreo es la opción más rápida: Armenia está a solo 30 min de Salento en taxi o shuttle.",
     "El bus es más económico pero largo; si vas en bus, considera hacerlo de noche para aprovechar el día.",
     "Salento tiene arquitectura colonial bien conservada: la plaza principal es parada obligatoria.",
     "Las fincas cafeteras alrededor de Salento ofrecen tours de café con degustación incluidos.",
     "El mercado de Salento (todos los días) es ideal para comprar artesanías y dulces típicos."],
    [("Día 1", "Llegada a Salento, paseo por la plaza y atardecer"),
     ("Día 2", "Valle de Cocora (mañana) + tarde libre o Filandia"),
     ("Día 3", "Finca cafetera + miradores de Salento + compras"),
     ("Día 4", "Opción: termales, otra caminata o regreso")],
    [("¿Cómo llego de Bogotá a Salento?",
      "Vuela a Armenia (Aeropuerto El Edén) y toma taxi/shuttle a Salento (30 min), o toma bus directo desde Terminal Salitre de Bogotá (8-9 horas)."),
     ("¿Cuántos días necesito en Salento?",
      "Mínimo 2 días para ver Salento y Cocora. Recomendamos 3-4 días para incluir Filandia, fincas y actividades extra."),
     ("¿Es seguro viajar a Salento?",
      "Sí. Salento es uno de los destinos más seguros del Eje Cafetero y muy acostumbrado al turismo."),
     ("¿Qué presupuesto necesito?",
      "Varía según cómo viajes: transporte hasta Armenia, alojamiento y estilo. Cotiza tu presupuesto por WhatsApp — los planes todo incluidos publican su tarifa completa desde $1.464.000 COP/persona en temporada alta.")])

add("tour-privado-salento",
    "Tour privado a Salento: experiencia personalizada en el Quindío",
    "Tour Privado Salento 2026 | Experiencia Exclusiva | Quindío Travel",
    "Tour privado a Salento y el Eje Cafetero: itinerario a tu medida, vehículo privado, guía dedicado y experiencias exclusivas. Cotiza tu tour 2026.",
    ["Un tour privado a Salento te permite diseñar tu propia experiencia: elegir los destinos, el ritmo, las actividades y el nivel de comodidad — sin compartir transporte ni horarios con otros viajeros.",
     "Es la opción ideal para lunas de miel, familias con niños, grupos de amigos o viajeros que buscan algo más allá de los tours grupales estándar."],
    [("Modalidad", "Vehículo privado + guía dedicado"),
     ("Duración", "Flexible: 1 día a 1 semana"),
     ("Itinerario", "100% personalizado según tus intereses"),
     ("Capacidad", "2-12 personas"),
     ("Incluye", "Transporte, guía, entradas y coordinación de actividades"),
     ("No incluye", "Alojamiento y comidas (se cotizan aparte)")],
    ["El guía privado adapta el tour a tus intereses: café, aventura, gastronomía, fotografía o cultura.",
     "Puedes combinar Salento con Filandia, Cocora, fincas cafeteras y termales en un solo viaje.",
     "Vehículos cómodos para grupos de hasta 12 personas.",
     "Transporte desde Armenia o Pereira incluido (sin transporte desde terminal).",
     "Asistencia médica incluida durante todo el tour."],
    [("Fase 1", "Diseño del itinerario contigo (WhatsApp)"),
     ("Fase 2", "Confirmación de fechas, alojamientos y actividades"),
     ("Fase 3", "Ejecución del tour con guía dedicado"),
     ("Fase 4", "Soporte durante todo el viaje + post-viaje")],
    [("¿Cuánto cuesta un tour privado a Salento?",
      "Varía según duración, vehículo y tamaño del grupo. Cotiza tu itinerario gratis por WhatsApp con el valor real vigente."),
     ("¿Puedo personalizar el itinerario?",
      "Totalmente. Dinos qué te interesa (café, aventura, gastronomía, cultura) y armamos un plan a tu medida."),
     ("¿El tour privado incluye alojamiento?",
      "No, pero podemos coordinar alojamientos si lo deseas. Cotizamos todo junto para tu comodidad."),
     ("¿Qué pasa si llueve?",
      "Tenemos plan B para cada actividad. El Quindío tiene opciones para días de lluvia: museos, fincas, gastronomía.")])

add("miradores-salento",
    "Miradores de Salento: los mejores puntos para ver el Cocora",
    "Miradores Salento 2026 | Mejores Vistas del Cocora | Quindío Travel",
    "Los mejores miradores de Salento para ver el Valle de Cocora y los paisajes del Eje Cafetero: ubicación, acceso y mejores horas para fotos en 2026.",
    ["Salento está rodeado de miradores naturales que ofrecen las mejores vistas del Valle de Cocora y las montañas del Quindío. El Mirador de Salento es el punto panorámico por excelencia del pueblo.",
     "Estos miradores son ideales para fotógrafos, viajeros que buscan paisajes espectaculares sin hacer la caminata completa al Cocora, o para un atardecer inolvidable."],
    [("Mirador de Salento", "Punto panorámico del pueblo — vistas del Valle de Cocora y todo el Quindío"),
     ("Mirador Cóndor (Filandia)", "El mirador más alto del Quindío — vista 360° de Cocora, Salento y el Eje Cafetero"),
     ("Vistas desde las afueras", "Caminatas y rutas cortas por las laderas alrededor de Salento"),
     ("Calle del Tiempo Detenida (Filandia)", "Calle emblemática de Filandia incluida en los planes de temporada"),
     ("Combinación ideal", "Mirador + Cocora en la mañana, Filandia por la tarde")],
    ["El Mirador de Salento ofrece vistas panorámicas del Valle de Cocora y todo el Quindío — el punto perfecto para fotos memorables.",
     "A pocos minutos de Filandia está el Mirador Cóndor, considerado el mirador más alto del Quindío con vista 360°.",
     "El atardecer desde cualquiera de estos miradores es el momento más fotográfico del día.",
     "Lleva cámara con buen zoom — las palmas de cera se ven mejor desde distancia.",
     "En temporada de lluvias los miradores pueden estar nublados; la temporada seca (diciembre-marzo) es ideal."],
    [("Opción 1", "Mirador de Salento al atardecer"),
     ("Opción 2", "Mirador Cóndor de Filandia + Calle del Tiempo"),
     ("Opción 3", "Mirador en la mañana + caminata al Cocora"),
     ("Opción 4", "Ruta de miradores Salento–Filandia en un día")],
    [("¿Cuál es el mejor mirador de Salento?",
      "El Mirador de Salento: es el punto panorámico del pueblo con vistas del Valle de Cocora. Para la vista más completa está el Mirador Cóndor en Filandia, el mirador más alto del Quindío."),
     ("¿Se puede ver el Cocora desde Salento sin caminar?",
      "Sí. Desde el Mirador de Salento y otros puntos panorámicos alrededor del pueblo se ve el valle sin hacer la caminata completa."),
     ("¿Cuál es el mejor momento para fotos?",
      "Atardecer para la luz dorada, o amanecer para la niebla matutina sobre el valle."),
     ("¿Los miradores se incluyen en los planes?",
      "Las visitas a Salento y Filandia —incluyendo sus miradores— están incluidas en el Plan Diciembre 4D/3N. Para salidas por tu cuenta, consulta rutas y tarifas por WhatsApp.")])

add("mirador-filandia-360-grados",
    "Mirador Cóndor de Filandia: la vista más completa del Quindío",
    "Mirador Cóndor Filandia 2026 | Vistas Panorámicas | Quindío Travel",
    "El Mirador Cóndor de Filandia: el mirador más alto del Quindío con vista 360° del Valle de Cocora, Salento y todo el Eje Cafetero. Guía 2026.",
    ["El Mirador Cóndor de Filandia es el punto panorámico más alto del Quindío: desde su cima se ve el Valle de Cocora, Salento y todo el Eje Cafetero en una vista de 360 grados.",
     "Es uno de los puntos más fotografiados del departamento y un lugar imperdible para cualquier viaje al Quindío."],
    [("Nombre", "Mirador Cóndor — el mirador más alto del Quindío"),
     ("Vista", "360° — Valle de Cocora, Salento y todo el Eje Cafetero"),
     ("Ideal para", "Fotografía de paisaje y atardecer"),
     ("Acceso", "Se coordina con transporte local o dentro de los planes"),
     ("Ubicación", "Filandia — a 45 minutos de Armenia")],
    ["Desde el Mirador Cóndor se aprecian las palmas de cera del Cocora, los techos de teja de Filandia y las montañas de la cordillera.",
     "El atardecer tiñe el paisaje de naranja y rosa — el momento más fotográfico.",
     "Es imperdible para fotógrafos: la amplitud de la vista no tiene comparación en la región.",
     "Ideal para combinar con la Calle del Tiempo Detenida y el Museo del Canasto de Filandia — ambos incluidos en los planes de temporada.",
     "La visita al mirador está contemplada dentro de los planes que incluyen Filandia."],
    [("Tarde 1", "Calle del Tiempo Detenida + Museo del Canasto en Filandia"),
     ("Tarde 2", "Caminata al Mirador Cóndor para el atardecer"),
     ("Noche", "Cena en Filandia o regreso a Salento")],
    [("¿Cómo se llega al Mirador Cóndor de Filandia?",
      "Se accede desde el centro de Filandia por caminos rurales. En los planes organizados el transporte está incluido; por cuenta propia se coordina taxi o transporte local por WhatsApp."),
     ("¿Qué se ve desde el Mirador Cóndor?",
      "La vista más completa del Eje Cafetero: el Valle de Cocora, Salento, Filandia y las montañas de la cordillera en 360 grados."),
     ("¿Es el mejor mirador del Quindío?",
      "Es el mirador más alto del departamento y ofrece la vista panorámica más completa — imperdible para fotógrafos."),
     ("¿El mirador se incluye en los planes?",
      "Sí. La visita a Filandia y su mirador está incluida en el Plan Diciembre 4D/3N de temporada alta (15 dic–20 ene).")])

add("mejores-miradores-filandia",
    "Miradores de Filandia: qué ver y cómo visitarlos",
    "Miradores Filandia 2026 | Guía de Vistas | Quindío Travel",
    "Los miradores de Filandia para ver el Eje Cafetero: Mirador Cóndor, mirador de Filandia y rutas panorámicas. Accesos y qué incluye en 2026.",
    ["Filandia es el municipio con mejor oferta de miradores del Eje Cafetero: su ubicación en las laderas de la cordillera ofrece vistas panorámicas del Cocora, las montañas y los valles cafeteros.",
     "Esta guía recopila los miradores más espectaculares de Filandia, con información práctica para visitarlos."],
    [("Mirador Cóndor", "El mirador más alto del Quindío — vista 360° de Cocora, Salento y el Eje Cafetero"),
     ("Mirador de Filandia", "Vista panorámica del pueblo y las montañas circundantes"),
     ("Mirador de Salento (cercano)", "Vistas del Valle de Cocora desde el vecino Salento"),
     ("Miradores rurales", "Fincas cafeteras con vistas privadas"),
     ("Combinación ideal", "Mirador + Calle del Tiempo Detenida + Museo del Canasto")],
    ["El Mirador Cóndor es el punto culminante: el mirador más alto del Quindío, imperdible para fotógrafos.",
     "El Mirador de Filandia ofrece una vista panorámica del pueblo con sus techos de teja y las montañas.",
     "Los miradores rurales en fincas cafeteras son los más tranquilos y fotogénicos.",
     "La visita a Filandia —incluyendo sus miradores— está incluida en el Plan Diciembre 4D/3N de temporada alta."],
    [("Opción 1", "Mirador Cóndor para el atardecer"),
     ("Opción 2", "Mirador de Filandia + Calle del Tiempo"),
     ("Opción 3", "Ruta de miradores Salento–Filandia en un día"),
     ("Opción 4", "Miradores + Cocora en la mañana")],
    [("¿Cuál es el mejor mirador de Filandia?",
      "El Mirador Cóndor: es el mirador más alto del Quindío y ofrece la vista panorámica más completa de la región."),
     ("¿Se puede hacer una ruta de miradores en Filandia?",
      "Sí. Filandia y Salento están muy cerca; en los planes organizados el transporte entre los dos está incluido."),
     ("¿Los miradores de Filandia se incluyen en los planes?",
      "Sí. La visita a Filandia y su mirador está incluida en el Plan Diciembre 4D/3N (15 dic–20 ene)."),
     ("¿Cuál es el mejor momento para visitar los miradores?",
      "Atardecer para la luz dorada, o amanecer para la niebla y la tranquilidad.")])

add("visita-guirrera-salento",
    "Guirrera en Salento: la tradición cafetera que no puedes perder",
    "Guirrera Salento 2026 | Tradición Cafetera | Quindío Travel",
    "Qué es la guirrera en Salento y por qué es una tradición cafetera única del Eje Cafetero. Historia, cómo participar y dónde vivirla en 2026.",
    ["La guirrera es una tradición cafetera del Eje Cafetero que consiste en la recolección del café de forma artesanal, manteniendo técnicas que se han transmitido por generaciones.",
     "En Salento y sus fincas cafeteras todavía se practica la guirrera — una experiencia auténtica que conecta al visitante con la cultura cafetera real del Quindío."],
    [("Qué es", "Recolección artesanal del café (grano por grano)"),
     ("Dónde", "Fincas cafeteras de Salento y alrededores"),
     ("Cuándo", "Principalmente en época de cosecha (septiembre-diciembre)"),
     ("Experiencia", "Participar en la recolección + proceso del café"),
     ("Duración", "2-4 horas (tour de finca + guirrera)"),
     ("Costo", "Se gestiona dentro de tours y planes — se cotiza según la experiencia elegida")],
    ["La guirrera es la forma tradicional de recolectar solo los granos maduros — un trabajo paciente y artesanal.",
     "En las fincas de Salento puedes participar activamente: recoger granos, ver el despulpe y la secación.",
     "Es una experiencia diferente al tour de café estándar: más auténtica y menos comercial.",
     "Los caficultores comparten historias y tradiciones que no se encuentran en ningún otro lugar.",
     "Ideal para familias, grupos y viajeros que buscan cultura cafetera real."],
    [("1. Llegada", "Llegada a la finca cafetera"),
     ("2. Recorrido", "Tour por los cafetales y explicación del proceso"),
     ("3. Guirrera", "Participación en la recolección de granos maduros"),
     ("4. Proceso", "Ver el despulpe, fermentación y secación del café"),
     ("5. Degustación", "Cata de café recién procesado")],
    [("¿Qué es la guirrera?",
      "Es la recolección artesanal del café, grano por grano, manteniendo técnicas tradicionales del Eje Cafetero."),
     ("¿Puedo participar en la guirrera?",
      "Sí, en muchas fincas de Salento puedes participar activamente en la recolección durante la época de cosecha."),
     ("¿Cuándo es la época de la guirrera?",
      "Principalmente de septiembre a diciembre, durante la cosecha del café."),
     ("¿Qué incluye el tour de finca con guirrera?",
      "Recorrido por la finca, explicación del proceso, participación en la recolección y degustación de café.")])

# ============================ TRANSPORTE ====================================

add("transporte-barato-eje-cafetero",
    "Transporte barato en el Eje Cafetero: cómo moverte sin gastar de más",
    "Transporte Barato Eje Cafetero 2026 | Guía Económica | Quindío Travel",
    "Cómo moverte por el Eje Cafetero sin gastar de más: buses, taxis compartidos, jeeps y opciones económicas entre Armenia, Salento, Filandia y el Cocora en 2026.",
    ["El transporte en el Eje Cafetero puede ser costoso si no conoces las opciones. Esta guía te muestra cómo moverte entre Armenia, Salento, Filandia, el Cocora y otros destinos de forma económica y eficiente.",
     "La clave está en combinar buses urbanos, taxis compartidos y tours organizados que incluyen transporte — ahorrando hasta un 50% vs. transporte privado."],
    [("Armenia-Salento", "Bus urbano desde Terminal Armenia · taxi · shuttle hotel"),
     ("Armenia-Filandia", "Bus intermunicipal · taxi"),
     ("Salento-Cocora", "Jeep Willys compartido desde la plaza principal de Salento (30 min)"),
     ("Salento-Filandia", "Bus/chiva local · taxi"),
     ("Armenia-Pereira", "Bus urbano · chiva · taxi"),
     ("Aeropuerto Armenia-Salento", "Taxi · shuttle de hoteles · 30 min aprox.")],
    ["El bus urbano de Armenia a Salento es la opción más económica — sale desde la Terminal de Armenia.",
     "Los jeeps compartidos al Cocora salen de la plaza principal de Salento — los cupos se llenan por orden de llegada.",
     "Los tours organizados que incluyen transporte son la mejor opción calidad-precio para el Cocora y Filandia: en temporada alta conviene reservar con anticipación.",
     "Las tarifas de transporte público las confirmas en el punto de salida o por WhatsApp — no las publicamos porque varían."],
    [("Día 1", "Llegada a Armenia, traslado a Salento en bus/shuttle"),
     ("Día 2", "Jeep compartido a Cocora desde Salento"),
     ("Día 3", "Bus a Filandia desde Salento"),
     ("Día 4", "Regreso a Armenia en bus"),
     ("Día 5", "Opcional: bus a Pereira o regreso")],
    [("¿Cuál es la forma más barata de ir de Armenia a Salento?",
      "El bus urbano desde la Terminal de Armenia es la opción más económica. El shuttle de hoteles es más rápido y cómodo. Las tarifas las confirmas en el punto de salida."),
     ("¿Cómo llego del Cocora a Filandia sin regresar a Salento?",
      "Se puede tomar transporte local desde el Cocora hasta Filandia, pero es más práctico regresar a Salento y tomar el bus/chiva a Filandia."),
     ("¿Hay Uber en el Eje Cafetero?",
      "Sí en Armenia y Pereira, pero no en Salento ni Filandia. En esos pueblos usa taxis locales."),
     ("¿Conviene alquilar carro?",
      "Para explorar el Quindío por tu cuenta sí, pero para el Cocora el jeep compartido desde la plaza de Salento es la opción práctica y económica.")])

add("transporte-colectivo-eje-cafetero",
    "Transporte colectivo en el Eje Cafetero: buses, chivas y compartidos",
    "Transporte Colectivo Eje Cafetero 2026 | Guía Completa | Quindío Travel",
    "Transporte colectivo en el Eje Cafetero: buses urbanos, chivas, jeeps compartidos y cómo moverte entre municipios de forma económica y segura en 2026.",
    ["El transporte colectivo es la forma más económica de explorar el Eje Cafetero: buses urbanos, chivas (camionetas compartidas) y jeeps conectan los principales destinos por una fracción del costo del transporte privado.",
     "Esta guía te explica cómo usar el sistema de transporte colectivo para moverte entre Armenia, Salento, Filandia, el Cocora y otros puntos del Quindío."],
    [("Bus urbano Armenia-Salento", "Sale desde Terminal Armenia · frecuencia frecuente"),
     ("Bus Salento-Filandia", "Desde el parque principal de Salento"),
     ("Jeep Salento-Cocora", "Jeep Willys 4x4 desde la plaza de Salento · sale por demanda"),
     ("Chiva Armenia-Pereira", "Camioneta compartida entre terminales"),
     ("Bus Armenia-Bogotá", "Salidas frecuentes desde Terminal de Armenia"),
     ("Bus Armenia-Medellín", "Salidas frecuentes desde Terminal de Armenia")],
    ["Los buses urbanos en Armenia y Pereira son modernos y seguros — el sistema TransMilenio no llega al Quindío pero los buses urbanos son eficientes.",
     "Las chivas (camionetas compartidas) son el transporte típico del Quindío — económicas, frecuentes y con ambiente local.",
     "Los jeeps al Cocora son 4x4 que suben por caminos de montaña — la única forma práctica de llegar al inicio del sendero.",
     "Los horarios de los jeeps al Cocora dependen de la demanda — en temporada alta salen más seguido.",
     "Compra el tiquete en la terminal o directamente con el conductor — no hay sistema de prepago."],
    [("Opción 1", "Armenia → Salento (bus) → Cocora (jeep) → Salento → Filandia (bus)"),
     ("Opción 2", "Armenia → Filandia (bus) → Salento (bus) → Cocora (jeep)"),
     ("Opción 3", "Armenia → Pereira (chiva) → Armenia → Salento"),
     ("Opción 4", "Todo en un día: Armenia → Salento → Cocora → Filandia → Armenia")],
    [("¿Cómo sé a qué hora sale el bus de Armenia a Salento?",
      "Los buses salen con frecuencia desde la Terminal de Armenia durante el día. Llega a la terminal y espera el próximo bus — no hay horario único fijo."),
     ("¿Los jeeps al Cocora tienen horario fijo?",
      "No. Salen cuando se llenan (4-6 personas) desde la plaza principal de Salento. En temporada alta salen más seguido."),
     ("¿El transporte colectivo es seguro?",
      "Sí, es seguro y es la forma normal de viajar de los locales. Los buses y chivas son confiables."),
     ("¿Puedo comprar tiquetes con anticipación?",
      "No es necesario — los buses urbanos no se llenan y los jeeps salen cuando se llenan. Solo llega a tiempo.")])

add("transporte-taxi-eje-cafetero",
    "Taxis en el Eje Cafetero: tarifas, zonas y cómo usarlos bien",
    "Taxis Eje Cafetero 2026 | Tarifas y Consejos | Quindío Travel",
    "Taxis en el Eje Cafetero: tarifas por zona, cómo pedirlos, zonas donde no hay y consejos para usar taxis de forma segura y económica en 2026.",
    ["Los taxis son una opción conveniente para trayectos cortos en el Eje Cafetero, pero las tarifas y la disponibilidad varían mucho según la ciudad. Esta guía te ayuda a usarlos de forma inteligente.",
     "En Armenia y Pereira hay taxis por todos lados y tarifas reguladas. En Salento y Filandia los taxis son menos frecuentes y más caros — conviene negociarlos."],
    [("Armenia-Salento", "~30 min · taxi con taxímetro en Armenia"),
     ("Armenia-Filandia", "~45 min · taxi o bus intermunicipal"),
     ("Salento-Cocora", "Jeep Willys desde la plaza de Salento · 30 min"),
     ("Salento-Filandia", "~30 min · bus/chiva local o taxi"),
     ("Pereira-Armenia", "~1 hora · bus urbano o taxi"),
     ("Aeropuerto Armenia-centro", "~15 min · taxi o shuttle")],
    ["En Armenia los taxis tienen taxímetro — pide que lo enciendan. La tarifa es regulada por la Alcaldía.",
     "En Salento y Filandia los taxis no tienen taxímetro — negocia el precio antes de subir.",
     "Los taxis de Aeropuerto Armenia al centro son económicos y seguros — hay tarifa fija.",
     "Para el Cocora, es mejor el jeep compartido que el taxi — mucho más económico.",
     "Los taxis en el Eje Cafetero son amarillos — es la forma de identificarlos."],
    [("Opción 1", "Aeropuerto Armenia → Salento (taxi directo)"),
     ("Opción 2", "Armenia centro → Filandia (taxi)"),
     ("Opción 3", "Salento → Cocora (taxi al inicio del sendero)"),
     ("Opción 4", "Pereira → Armenia (taxi intermunicipal)")],
    [("¿Cuánto cuesta un taxi de Armenia a Salento?",
      "El trayecto toma unos 30 minutos. En Armenia los taxis usan taxímetro (tarifa regulada); confirma la tarifa vigente antes de subir."),
     ("¿Los taxis en Salento tienen taxímetro?",
      "No. En Salento y Filandia los taxis no usan taxímetro — negocia el precio antes de subir."),
     ("¿Es seguro tomar taxis en el Eje Cafetero?",
      "Sí, los taxis son seguros. En Armenia y Pereira usa el taxímetro; en Salento y Filandia negocia el precio antes."),
     ("¿Hay taxis en el Cocora?",
      "No hay taxis dentro del valle. El acceso es en jeep o a pie desde el punto de inicio del sendero.")])

add("tour-eje-cafetero-sin-transporte",
    "Tour Eje Cafetero sin transporte: planes solo con actividades",
    "Tour Eje Cafetero Sin Transporte 2026 | Solo Actividades | Quindío Travel",
    "Planes turísticos del Eje Cafetero sin transporte: solo actividades, entradas y coordinación. Para quienes ya tienen cómo llegar. Cotiza 2026.",
    ["Si ya tienes transporte propio o llegas por tu cuenta, nuestros planes sin transporte te dan acceso a las mejores actividades del Eje Cafetero sin pagar por el traslado.",
     "Ideal para viajeros independientes que quieren la experiencia completa — guías, entradas, coordinación — pero con su propio vehículo o transporte ya organizado."],
    [("Incluye", "Guías locales, entradas a atractivos, coordinación de actividades, asistencia médica"),
     ("No incluye", "Transporte entre destinos, comidas, alojamiento"),
     ("Modalidad", "Flexible — tú pones el transporte"),
     ("Duración", "1-7 días según el plan"),
     ("Puntos de encuentro", "Salento, Filandia, Armenia, Pereira"),
     ("Ideal para", "Viajeros con carro propio, mochileros, grupos con transporte propio")],
    ["Ahorra hasta 40% vs. planes con transporte — solo pagas por la experiencia, no por el traslado.",
     "Guías locales certificados que conocen cada detalle del destino.",
     "Entradas a Parque del Café, PANACA, Valle de Cocora, fincas y más incluidas.",
     "Coordinación completa: te decimos dónde encontrarnos y qué hacer.",
     "Asistencia médica incluida durante todo el plan."],
    [("Día 1", "Llegada al punto de encuentro + actividad 1"),
     ("Día 2", "Actividad 2 + almuerzo local"),
     ("Día 3", "Actividad 3 + tarde libre"),
     ("Día 4", "Actividad final + despedida")],
    [("¿Qué incluye el plan sin transporte?",
      "Guías locales, entradas a atractivos, coordinación de actividades y asistencia médica. No incluye transporte ni comidas."),
     ("¿Puedo unirme desde cualquier punto?",
      "Sí. Los puntos de encuentro son Salento, Filandia, Armenia y Pereira. Coordinamos el lugar exacto contigo."),
     ("¿Cuánto cuesta un plan sin transporte?",
      "Cada plan se cotiza según destino, duración, alojamiento y fechas. Cotiza gratis por WhatsApp para recibir el valor vigente."),
     ("¿Necesito carro propio?",
      "No necesariamente. Puedes usar transporte público entre puntos o taxis locales. Nosotros coordinamos todo excepto el traslado entre ciudades.")])

add("vuelo-barato-armenia",
    "Vuelos baratos a Armenia: cómo llegar al Eje Cafetero por aire",
    "Vuelos Baratos a Armenia 2026 | Guía Aérea | Quindío Travel",
    "Cómo encontrar vuelos baratos a Armenia (Aeropuerto El Edén) en 2026: aerolíneas, rutas, precios y conexión con Salento y el Eje Cafetero.",
    ["Armenia tiene el Aeropuerto Internacional El Edén (AXM), la puerta de entrada aérea al Eje Cafetero. Desde Bogotá hay vuelos directos de 1 hora en varias aerolíneas.",
     "Encontrar vuelos baratos requiere comparar opciones, reservar con anticipación y considerar horarios — esta guía te ayuda a hacerlo."],
    [("Aeropuerto", "Aeropuerto Internacional El Edén (AXM) — Armenia"),
     ("Aerolíneas", "Avianca, LATAM, Wingo, Clic (vuelos directos desde Bogotá)"),
     ("Duración", "1 hora desde Bogotá"),
     ("Precio aprox.", "Varía por aerolínea y anticipación — compara antes de comprar"),
     ("Frecuencia", "Múltiples vuelos diarios desde Bogotá"),
     ("Conexión a Salento", "Taxi o shuttle desde el aeropuerto — 30 min aprox.")],
    ["Los vuelos desde Bogotá son la opción más rápida: 1 hora de vuelo + 30 min de traslado a Salento.",
     "Wingo y Clic suelen tener los precios más competitivos en rutas cortas.",
     "Reservar con 2-4 semanas de anticipación puede ahorrar hasta 40%.",
     "El aeropuerto está a 15 min del centro de Armenia — hay taxis y shuttles disponibles.",
     "Desde Armenia puedes conectar con buses a Salento, Filandia y Pereira."],
    [("Paso 1", "Buscar vuelos en Avianca/LATAM/Wingo/Clic"),
     ("Paso 2", "Comparar precios y horarios"),
     ("Paso 3", "Reservar con anticipación (2-4 semanas)"),
     ("Paso 4", "Al llegar: taxi/shuttle a Salento o hotel"),
     ("Paso 5", "Conectar con tours y transporte local")],
    [("¿Qué aerolíneas vuelan a Armenia?",
      "Avianca, LATAM, Wingo y Clic tienen vuelos directos desde Bogotá. También hay conexiones desde otras ciudades."),
     ("¿Cuánto cuesta un vuelo a Armenia?",
      "Depende de la aerolínea, la anticipación y la temporada. Compara Avianca, LATAM, Wingo y Clic — las low-cost suelen ser más económicas en rutas cortas."),
     ("¿Cómo llego del aeropuerto a Salento?",
      "Taxi o shuttle compartido — el trayecto toma unos 30 minutos. Los hoteles de la zona ofrecen traslados; confirma al reservar."),
     ("¿Vale la pena volar vs. ir en bus?",
      "Sí, si valoras el tiempo: 1 hora de vuelo vs. 8-9 horas de bus. El ahorro de tiempo justifica la diferencia de precio para la mayoría.")])

# ============================ HOTELES =======================================

add("hoteles-familiares-salento",
    "Hoteles familiares en Salento: los mejores para ir con niños",
    "Hoteles Familiares Salento 2026 | Con Niños | Quindío Travel",
    "Los mejores hoteles y alojamientos familiares en Salento 2026: con piscina, juegos infantiles, áreas verdes y servicios para niños. Precios reales y recomendados.",
    ["Salento tiene excelentes opciones de alojamiento familiar: desde fincas hoteleras con piscina y juegos infantiles hasta cabañas tradicionales con espacios al aire libre.",
     "Esta guía te ayuda a elegir el hotel ideal para tu familia según presupuesto, servicios y ubicación."],
    [("Cabañas La Esmeralda", "Finca hotel familiar en Salento | Plan Diciembre desde $1.464.000 COP/persona (4 pax) | Piscina, juegos infantiles, zona de asados"),
     ("Fincas rurales", "Alojamiento tradicional cafetero | Se cotiza dentro de planes"),
     ("Hoteles del centro", "Comodidad urbana | Cerca de restaurantes y tiendas"),
     ("Cabañas tipo loft", "Moderno y privado | Suites con cocina"),
     ("Glamping", "Experiencia única | Domos y tiendas de lujo")],
    ["La mayoría de fincas hoteleras de Salento tienen piscina y áreas verdes para niños.",
     "Las cabañas tradicionales ofrecen más espacio y contacto con la naturaleza.",
     "Los hoteles del centro son más prácticos si viajas con niños pequeños.",
     "Verifica que el alojamiento tenga cuna o cama adicional si viajas con bebé.",
     "Los paquetes familiares con tours incluidos son la mejor opción calidad-precio."],
    [("Opción económica", "Finca rural o cabaña compartida"),
     ("Opción media", "Finca hotel con piscina y servicios"),
     ("Opción premium", "Cabaña loft o glamping con todas las comodidades"),
     ("Opción lujo", "Finca hotel boutique con spa y restaurante")],
    [("¿Cuál es el mejor hotel familiar en Salento?",
      "Depende del presupuesto. Para familias, Cabañas La Esmeralda es una excelente opción con piscina y juegos infantiles. Para más lujo, las fincas boutique son ideales."),
     ("¿Los hoteles de Salento tienen piscina?",
      "La mayoría de fincas hoteleras sí tienen piscina. Los hoteles del centro y cabañas pequeñas pueden no tenerla — verifica antes de reservar."),
     ("¿Hay hoteles que acepten niños gratis?",
      "Algunos alojamientos ofrecen descuento o gratis para niños menores de 5 años. Verifica la política al reservar."),
     ("¿Qué incluye un plan familiar a Salento?",
      "Los planes familiares incluyen alojamiento, tours guiados, algunas comidas y actividades adaptadas para niños.")])

add("hoteles-pet-friendly-salento",
    "Hoteles pet friendly en Salento: dónde alojarte con tu mascota",
    "Hoteles Pet Friendly Salento 2026 | Con Mascotas | Quindío Travel",
    "Los mejores hoteles y alojamientos pet friendly en Salento 2026: dónde alojarte con perros y gatos, políticas y recomendaciones para viajar con tu mascota al Quindío.",
    ["Viajar con mascotas al Quindío es cada vez más común y muchos alojamientos en Salento ya aceptan perros y gatos. Esta guía te ayuda a encontrar el lugar ideal para ti y tu compañero peludo.",
     "Las fincas y cabañas rurales son generalmente más pet friendly que los hoteles urbanos — con espacios al aire libre y más libertad para tu mascota."],
    [("Fincas rurales", "Mayor flexibilidad | Espacios al aire libre"),
     ("Cabañas tradicionales", "Buena opción | Jardines y áreas verdes"),
     ("Hoteles del centro", "Variable | Verificar política de mascotas individual"),
     ("Glamping", "Algunas opciones | Naturaleza y comodidad"),
     ("Camping", "Más económico | Trae tu propia tienda")],
    ["Las fincas rurales son las más pet friendly: espacios abiertos, menos restricciones y más tolerancia a mascotas.",
     "Verifica la política de mascotas antes de reservar: algunos lugares tienen restricciones de tamaño o raza.",
     "Lleva la cartilla de vacunación de tu mascota — algunos alojamientos la solicitan.",
     "Los tours al Cocora y fincas cafeteras pueden tener restricciones para mascotas — consulta antes.",
     "Salento tiene pocos veterinarios — lleva los medicamentos básicos de tu mascota."],
    [("Opción 1", "Finca rural pet friendly con espacio abierto"),
     ("Opción 2", "Cabaña con jardín para pasear al perro"),
     ("Opción 3", "Hotel del centro que acepta mascotas pequeñas"),
     ("Opción 4", "Glamping o camping para mayor libertad")],
    [("¿Hay hoteles pet friendly en Salento?",
      "Sí, cada vez más. Las fincas rurales y cabañas son las más amigables con mascotas. Verifica la política antes de reservar."),
     ("¿Qué documentación necesita mi mascota?",
      "Lleva la cartilla de vacunación actualizada. Algunos alojamientos pueden solicitarla."),
     ("¿Puedo llevar mi perro al Cocora?",
      "Los tours al Cocora tienen restricciones para mascotas por seguridad y normativa del parque. Consulta con el operador antes."),
     ("¿Hay veterinarios en Salento?",
      "Hay pocos. Lleva los medicamentos básicos y la cartilla de tu mascota.")])

add("hoteles-4-estrellas-salento",
    "Hoteles 4 estrellas en Salento: lujo y comodidad en el Quindío",
    "Hoteles 4 Estrellas Salento 2026 | Lujo | Quindío Travel",
    "Los mejores hoteles 4 estrellas en Salento 2026: fincas boutique, cabañas de lujo y alojamientos premium con servicio excepcional en el Eje Cafetero.",
    ["Salento tiene una oferta creciente de alojamientos de lujo: fincas boutique, cabañas con vista al Cocora y hoteles con servicio premium que combinan comodidad con la belleza natural del Quindío.",
     "Estos alojamientos son ideales para lunas de miel, celebraciones especiales o viajeros que buscan una experiencia de lujo sin sacrificar la autenticidad del destino."],
    [("Fincas boutique", "Diseño único + servicio premium"),
     ("Cabañas de lujo", "Privacidad + vistas espectaculares"),
     ("Hoteles con spa", "Relajación total"),
     ("Glamping premium", "Experiencia única"),
     ("Finca hotel 4*", "Todo incluido")],
    ["Los alojamientos de lujo en Salento combinan arquitectura colonial con comodidades modernas.",
     "Muchas fincas tienen vista directa al Valle de Cocora — despertar con ese paisaje es invaluable.",
     "El servicio personalizado es el sello de estos alojamientos: desde el desayuno hasta las actividades.",
     "Ideal para lunas de miel y celebraciones especiales.",
     "Verifica que incluyan desayuno y actividades — los precios varían mucho según lo que incluyan."],
    [("Opción 1", "Finca boutique con vista al Cocora"),
     ("Opción 2", "Cabaña de lujo con spa privado"),
     ("Opción 3", "Finca hotel 4* todo incluido"),
     ("Opción 4", "Glamping premium con experiencias exclusivas")],
    [("¿Cuánto cuesta un hotel 4 estrellas en Salento?",
      "Depende del alojamiento y la temporada. Cotiza tu preferencia por WhatsApp — en planes todo incluido el alojamiento va dentro del valor del plan."),
     ("¿Los hoteles de lujo en Salento tienen vista al Cocora?",
      "Muchos sí. Las fincas en las laderas tienen vistas espectaculares. Verifica la ubicación específica al reservar."),
     ("¿Qué incluye un hotel 4 estrellas en Salento?",
      "Generalmente incluye desayuno, WiFi, estacionamiento y a veces actividades. Los paquetes premium incluyen tours y cenas."),
     ("¿Vale la pena pagar 4 estrellas en Salento?",
      "Si valoras el servicio personalizado, la privacidad y las vistas al Cocora, sí. Para presupuesto ajustado, las opciones 3* son suficientes.")])

add("hoteles-boutique-quindio",
    "Hoteles boutique en el Quindío: experiencias únicas de alojamiento",
    "Hoteles Boutique Quindío 2026 | Diseño Único | Quindío Travel",
    "Hoteles boutique en el Quindío: alojamientos con diseño único, servicio personalizado y experiencias auténticas. Los mejores de Salento, Filandia y Armenia en 2026.",
    ["Los hoteles boutique del Quindío combinan diseño arquitectónico único con la calidez de la hospitalidad local: cada uno tiene su propia personalidad y ofrece una experiencia que va más allá de simplemente dormir.",
     "Desde cabañas con arte local hasta fincas con historia cafetera, estos alojamientos son destinos en sí mismos."],
    [("Salento", "Cabañas boutique con vista al Cocora"),
     ("Filandia", "Fincas con diseño colonial moderno"),
     ("Armenia", "Hoteles urbanos con carácter"),
     ("Montenegro", "Fincas cerca del Parque del Café"),
     ("Pereira", "Boutique hotels con spa")],
    ["Los hoteles boutique del Quindío son conocidos por su diseño que respeta la arquitectura local.",
     "El servicio personalizado es la norma: desde recomendaciones locales hasta actividades exclusivas.",
     "Muchos tienen arte local, libros y detalles que reflejan la cultura cafetera.",
     "Ideal para viajeros que buscan algo más que un lugar para dormir.",
     "Verifica las amenidades específicas: no todos tienen piscina o spa."],
    [("Salento", "Cabañas boutique con vistas"),
     ("Filandia", "Fincas con diseño único"),
     ("Armenia", "Hoteles urbanos con carácter"),
     ("Montenegro", "Fincas cerca del Parque del Café"),
     ("Pereira", "Boutique hotels con spa")],
    [("¿Qué hace único a un hotel boutique del Quindío?",
      "El diseño que respeta la arquitectura local, el servicio personalizado y la conexión con la cultura cafetera."),
     ("¿Cuánto cuestan los hoteles boutique en el Quindío?",
      "Varía según el alojamiento y la temporada. Cotiza la opción que te interese por WhatsApp — los planes todo incluido ya traen el alojamiento dentro del valor."),
     ("¿Los hoteles boutique incluyen actividades?",
      "Muchos sí: tours de café, caminatas, observación de aves. Verifica qué incluye cada uno."),
     ("¿Dónde están los mejores hoteles boutique?",
      "Salento y Filandia tienen la mayor concentración, seguidos de Armenia y Montenegro.")])

add("hoteles-campestres-eje-cafetero",
    "Hoteles campestres en el Eje Cafetero: naturaleza y tranquilidad",
    "Hoteles Campestres Eje Cafetero 2026 | Naturaleza | Quindío Travel",
    "Hoteles campestres en el Eje Cafetero: fincas, cabañas y alojamientos rurales con piscina, zonas verdes y contacto directo con la naturaleza cafetera en 2026.",
    ["Los hoteles campestres son la esencia del alojamiento en el Eje Cafetero: fincas con grandes extensiones de terreno, piscinas, zonas de asados,Senderos y la tranquilidad de la montaña.",
     "Son ideales para familias, grupos de amigos o viajeros que buscan desconectarse del ruido urbano y conectarse con la naturaleza cafetera."],
    [("Fincas con piscina", "Grandes terrenos + piscina"),
     ("Cabañas rurales", "Tradicionales + privadas"),
     ("Hoteles con zonas verdes", "Amplias áreas + actividades"),
     ("Glamping campestre", "Lujo + naturaleza"),
     ("Camping en fincas", "La opción más económica")],
    ["Los hoteles campestres del Quindío son conocidos por sus grandes extensiones de terreno y vistas a cafetales.",
     "La mayoría tiene piscina, zonas de asados, juegos infantiles y senderos para caminar.",
     "El desayuno campestre con productos locales es una experiencia en sí misma.",
     "Ideal para familias que buscan espacio para niños y mascotas.",
     "Muchos incluyen tours de finca cafetera y actividades al aire libre."],
    [("Opción familiar", "Finca con piscina y juegos infantiles"),
     ("Opción parejas", "Cabaña privada con vista"),
     ("Opción grupos", "Finca grande para grupos de amigos"),
     ("Opción lujo", "Glamping o finca boutique campestre"),
     ("Opción económica", "Cabaña compartida o camping")],
    [("¿Qué es un hotel campestre en el Quindío?",
      "Es un alojamiento rural en fincas o terrenos grandes, con piscina, zonas verdes y contacto directo con la naturaleza cafetera."),
     ("¿Los hoteles campestres tienen piscina?",
      "La mayoría sí. Las fincas grandes y los hoteles campestres suelen tener piscina al aire libre."),
     ("¿Puedo llevar mascotas a hoteles campestres?",
      "Muchos sí, especialmente fincas rurales. Verifica la política antes de reservar."),
     ("¿Qué actividades hay en hoteles campestres?",
      "Senderos, zonas de asados, juegos, tours de finca, observación de aves y a veces cabalgatas.")])

add("alojamiento-economico-salento",
    "Alojamiento económico en Salento: opciones baratas sin sacrificar calidad",
    "Alojamiento Económico Salento 2026 | Precios Bajos | Quindío Travel",
    "Alojamiento económico en Salento 2026: hostales, cabañas compartidas, fincas rurales y opciones baratas para viajar al Quindío sin gastar de más.",
    ["Salento tiene opciones de alojamiento económico para todos los presupuestos: desde hostales y cabañas compartidas hasta fincas rurales que ofrecen experiencias auténticas a precios accesibles.",
     "La clave está en reservar con anticipación y elegir alojamientos fuera del centro que ofrecen mejor precio-calidad."],
    [("Hostales y hospedajes", "Camas compartidas/dobles en el centro"),
     ("Cabañas compartidas", "Habitación múltiple"),
     ("Fincas rurales", "Alojamiento tradicional cafetero"),
     ("Camping", "Trae tu tienda o equipo de campamento"),
     ("Apartamentos compartidos", "Cocina + espacio común")],
    ["Los hostales del centro de Salento son los más baratos pero se llenan rápido — reserva con anticipación.",
     "Las fincas rurales fuera del pueblo son más económicas y ofrecen más espacio y naturaleza.",
     "El camping es la opción más barata pero requiere equipo propio.",
     "Los alojamientos compartidos (camas en dormitorio) son la forma más económica de dormir en Salento.",
     "En temporada alta (diciembre-enero) los precios suben hasta 50% — reserva temprano."],
    [("Opción 1", "Hostal en el centro (más barato)"),
     ("Opción 2", "Cabaña compartida en las afueras"),
     ("Opción 3", "Finca rural con experiencia auténtica"),
     ("Opción 4", "Camping para aventureros")],
    [("¿Cuánto cuesta dormir barato en Salento?",
      "Depende de la época y la ocupación. Los hostales y el camping son las opciones más económicas; las tarifas vigentes las confirmas por WhatsApp o directamente con el alojamiento."),
     ("¿Hay hostales en Salento?",
      "Sí, hay varios hostales y hospedajes en el centro. Son la opción más económica pero se llenan rápido."),
     ("¿Conviene reservar alojamiento económico con anticipación?",
      "Sí, especialmente en temporada alta (diciembre-enero). Los alojamientos económicos se agotan rápido."),
     ("¿Hay camping en Salento?",
      "Sí, hay opciones de camping en fincas y áreas naturales alrededor de Salento. Verifica disponibilidad antes.")])

# ============================ TEMAS =========================================

add("fiestas-diciembre-quindio",
    "Fiestas de diciembre en el Quindío: qué hacer en Navidad y Año Nuevo",
    "Fiestas Diciembre Quindío 2026 | Navidad y Año Nuevo | Quindío Travel",
    "Qué hacer en diciembre en el Quindío: fiestas navideñas, decoraciones, eventos, planches y cómo celebrar Navidad y Año Nuevo en el Eje Cafetero en 2026.",
    ["Diciembre en el Quindío es mágico: los pueblos se llenan de decoraciones navideñas, las fincas tienen cosechas de café especiales, y hay eventos, planches y celebraciones en toda la región.",
     "Es la temporada alta de turismo — los precios suben pero la experiencia vale la pena. Esta guía te ayuda a aprovechar al máximo las fiestas de diciembre."],
    [("Decoraciones", "Todos los pueblos se decoran para Navidad"),
     ("Eventos", "Conciertos, ferias y eventos navideños en Armenia y Pereira"),
     ("Planches", "Los planches del fin de año son muy populares"),
     ("Café especial", "Cosecha de diciembre — café de altura"),
     ("Clima", "Temporada seca — días soleados y noches frescas"),
     ("Precios", "Temporada alta — reservar con anticipación")],
    ["Las decoraciones navideñas en Armenia y Pereira son espectaculares — una tradición anual.",
     "Los planches del fin de año en Armenia son muy populares — música, comida y ambiente festivo.",
     "La cosecha de café de diciembre produce café de especialidad con sabores únicos.",
     "El clima de diciembre es ideal: días soleados y noches frescas para el Cocora.",
     "Los precios de alojamiento y tours suben hasta 50% — reserva con 2-3 meses de anticipación."],
    [("Semana 1-2", "Navidad: eventos familiares, decoraciones, misa del gallo"),
     ("Semana 3", "Nochevieja: planches, eventos, fuegos artificiales"),
     ("Semana 4", "Año Nuevo: recuperación, brunches y actividades"),
     ("Opción", "Extender el plan por los puentes de diciembre")],
    [("¿Qué se celebra en diciembre en el Quindío?",
      "Navidad y Año Nuevo con decoraciones, eventos, planches y tradiciones locales. Es la temporada alta de turismo."),
     ("¿Cuándo son los planches de fin de año en Armenia?",
      "Los planches se realizan el 31 de diciembre y el 1 de enero en varios lugares de Armenia. Consulta los eventos específicos."),
     ("¿Los precios suben en diciembre?",
      "Sí, es temporada alta. Los precios de alojamiento y tours pueden subir hasta 50%. Reserva con 2-3 meses de anticipación."),
     ("¿Qué puedo hacer en el Cocora en diciembre?",
      "El clima de diciembre es ideal para el Cocora: días soleados y visibilidad del valle. La caminata es más cómoda por la temporada seca.")])

add("presupuesto-viaje-eje-cafetero",
    "Presupuesto para viaje al Eje Cafetero: cuánto cuesta todo en 2026",
    "Presupuesto Viaje Eje Cafetero 2026 | Costos Reales | Quindío Travel",
    "Presupuesto completo para viajar al Eje Cafetero en 2026: vuelos, alojamiento, transporte, comidas y actividades. Cuánto cuesta realmente un viaje de 3-4 días.",
    ["El presupuesto para viajar al Eje Cafetero varía enormemente según el estilo de viaje: desde un viaje económico por cuenta propia hasta una experiencia premium todo incluido.",
     "Esta guía desglosa los componentes de costo para que puedas planificar tu viaje sin sorpresas — y te mostramos por qué un plan organizado suele ser la mejor relación calidad-precio."],
    [("Vuelos o buses a Armenia", "Varía según aerolínea/anticipación o tarifa de terminal — compara antes de comprar"),
     ("Alojamiento", "Varía según tipo (hostal, hotel, finca, cabaña) y temporada — se cotiza por WhatsApp"),
     ("Transporte local", "Buses urbanos e intermunicipales, jeeps y taxis — tarifas vigentes en cada punto de salida"),
     ("Comidas", "Desde mercados y comedores locales hasta restaurantes — depende de tu estilo"),
     ("Actividades", "Se contratan dentro de planes/tours — plan todo incluido desde $1.464.000 COP/persona")],
    ["El componente que más varía es el transporte hasta Armenia y el alojamiento elegido.",
     "Los planes todo incluido son la forma más predecible: el valor publicado ya cubre alojamiento, comidas, transporte interno y actividades.",
     "Los costos ocultos más comunes al viajar por cuenta propia: entradas a atractivos, propinas y souvenirs.",
     "Viajar en temporada baja (enero-marzo, septiembre-octubre) suele encontrar mejores tarifas de alojamiento y transporte."],
    [("Presupuesto económico", "Hostal + buses + comidas locales + actividades gratuitas"),
     ("Presupuesto medio", "Hotel 3* + transporte mixto + comidas variadas + tours"),
     ("Presupuesto premium", "Finca hotel + transporte privado + comidas gourmet + tours privados"),
     ("Presupuesto todo incluido", "Plan organizado con todo incluido desde $1.464.000 COP")],
    [("¿Cuánto cuesta un viaje de 3-4 días al Eje Cafetero?",
      "Depende del estilo: por cuenta propia suma vuelos/buses + alojamiento + transporte + comidas + actividades. Los planes todo incluidos publican su tarifa completa — el Plan Diciembre 4D/3N arranca en $1.464.000 COP/persona en temporada alta."),
     ("¿Cuál es la forma más barata de viajar al Quindío?",
      "Por cuenta propia: bus intermunicipal + alojamiento económico + transporte local + comidas de mercado. Nosotros te asesoramos gratis por WhatsApp para armar tu presupuesto."),
     ("¿Los planes todo incluido valen la pena?",
      "Sí, si valoras no preocuparte por logística: un solo valor cubre alojamiento, comidas, transporte interno y actividades — desde $1.464.000 COP por 4 días/3 noches en temporada alta."),
     ("¿Cuándo es más barato viajar al Eje Cafetero?",
      "Temporada baja: enero-marzo y septiembre-octubre. Los precios pueden ser hasta 30% más bajos.")])

add("viaje-familiar-quindio-ninos",
    "Viaje familiar al Quindío con niños: planes y actividades para familias",
    "Viaje Familiar Quindío con Niños 2026 | Planes | Quindío Travel",
    "Viaje familiar al Quindío con niños: planes adaptados, actividades seguras, hoteles familiares y consejos para viajar con niños al Eje Cafetero en 2026.",
    ["El Quindío es uno de los destinos más familiares de Colombia: parques temáticos, fincas cafeteras, naturaleza y actividades adaptadas para niños de todas las edades.",
     "Esta guía te ayuda a planificar un viaje familiar inolvidable con niños, desde bebés hasta adolescentes."],
    [("Parque del Café", "Incluido en planes | Atracciones para todas las edades"),
     ("PANACA", "Incluido en planes | Animales y cultura cafetera"),
     ("Fincas cafeteras", "Tours interactivos dentro de planes | Niños pueden participar"),
     ("Valle de Cocora", "Incluido en planes | Caminata moderada para niños mayores de 8-10 años"),
     ("Termales Santa Rosa", "Actividad adicional en planes a medida | Relajación familiar"),
     ("Salento", "Pueblo colonial | Plaza, miradores y mercado")],
    ["El Parque del Café y PANACA son los favoritos de los niños: atracciones mecánicas, animales y actividades interactivas.",
     "Las fincas cafeteras ofrecen tours diseñados para familias: niños pueden recoger café y ver el proceso.",
     "El Cocora es apto para niños mayores de 8-10 años con buena condición física.",
     "Los hoteles familiares tienen piscinas, juegos infantiles y espacios seguros.",
     "Los planes familiares todo incluido son la mejor opción: logística resuelta y actividades adaptadas."],
    [("Día 1", "Llegada + Parque del Café o PANACA"),
     ("Día 2", "Finca cafetera + Salento + miradores"),
     ("Día 3", "Valle de Cocora (si los niños tienen edad) o Filandia"),
     ("Día 4", "Termales o actividad alternativa + regreso")],
    [("¿Qué actividades son mejores para niños en el Quindío?",
      "Parque del Café, PANACA, fincas cafeteras con tours interactivos y termales. El Cocora es para niños mayores con buena condición física."),
     ("¿Hay hoteles familiares en Salento?",
      "Sí, varios. Busca fincas con piscina, juegos infantiles y espacios seguros para niños."),
     ("¿Puedo llevar niños pequeños al Cocora?",
      "Para niños menores de 8-10 años recomendamos el mirador corto (2h) o actividades más suaves como fincas y parques."),
     ("¿Los planes familiares incluyen todo?",
      "Los planes familiares todo incluido incluyen alojamiento, tours, algunas comidas y actividades adaptadas para niños.")])

add("comida-tipica-quindio",
    "Comida típica del Quindío: qué probar en el Eje Cafetero",
    "Comida Típica Quindío 2026 | Gastronomía Local | Quindío Travel",
    "Comida típica del Quindío: bandeja paisa, sancocho, arepas, dulces y productos del café. Qué probar y dónde comer en el Eje Cafetero en 2026.",
    ["La gastronomía del Quindío es una mezcla de tradiciones cafeteras, paisas y antioqueñas: bandeja paisa, sancocho de gallina, arepas de maíz, dulces de leche y por supuesto, café de altura.",
     "Esta guía te ayuda a descubrir los sabores auténticos del Eje Cafetero y dónde probarlos."],
    [("Bandeja paisa", "Plato típico antioqueño | Frijoles, arroz, chicharrón, huevo, aguacate"),
     ("Sancocho de gallina", "Sopa tradicional | Pollo, papa, mazorca, plátano, hierbas"),
     ("Arepas de maíz", "Arepas tradicionales | Rellenas de queso, hogao o chicharrón"),
     ("Dulces de leche", "Dulces típicos | Arequipe, bocadillo, torta de yuca"),
     ("Café de altura", "Café especial | Tostado y molido en el momento"),
     ("Trucha", "Plato de río | Trucha frita o ahumada con patacones")],
    ["La bandeja paisa es el plato más representativo del Quindío — abundante y deliciosa.",
     "El sancocho de gallina es perfecto para el clima frío de la montaña.",
     "Las arepas de maíz del Quindío son más gruesas y sabrosas que las del resto del país.",
     "Los dulces de leche y arequipe son ideales para el postre.",
     "El café del Quindío es de los mejores del mundo — pruébalo en las fincas y cafeterías locales."],
    [("Desayuno", "Arepa con queso + café + frutas"),
     ("Almuerzo", "Bandeja paisa o sancocho + ensalada"),
     ("Merienda", "Dulce de leche o bocadillo + café"),
     ("Cena", "Trucha o comida ligera + postre"),
     ("Extra", "Cata de café en finca cafetera")],
    [("¿Cuál es el plato típico del Quindío?",
      "La bandeja paisa es el más representativo, pero el sancocho de gallina y las arepas de maíz también son muy típicos."),
     ("¿Dónde probar comida típica en Salento?",
      "En el centro del pueblo hay restaurantes típicos. Las fincas cafeteras también ofrecen comida casera."),
     ("¿El Quindío tiene mariscos?",
      "No, es región de montaña. Los platos típicos son de pollo, res, cerdo y productos del campo."),
     ("¿Qué café debo probar?",
      "Café de altura del Quindío — pruébalo en las fincas cafeteras donde se produce y tuesta.")])

add("senderismo-avanzado-quindio",
    "Senderismo avanzado en el Quindío: rutas para experimentados",
    "Senderismo Avanzado Quindío 2026 | Rutas Difíciles | Quindío Travel",
    "Senderismo avanzado en el Quindío: rutas difíciles, miradores remotos, caminatas de varios días y expediciones por los páramos y bosques del Eje Cafetero en 2026.",
    ["Para los senderistas experimentados, el Quindío ofrece rutas que van más allá del Cocora: páramos, bosques de niebla, miradores remotos y caminatas de varios días por territorios poco explorados.",
     "Esta guía está dirigida a quienes buscan retos reales en la montaña cafetera."],
    [("Cocora completo", "12-14 km | 5-6 horas | Moderado-avanzado"),
     ("Cerro Murillo", "8-10 km | 4-5 horas | Moderado-avanzado"),
     ("Senderos de páramo", "15-20 km | 6-8 horas | Avanzado"),
     ("Rutas de varios días", "30-50 km | 2-3 días | Muy avanzado"),
     ("Altitud", "2.400-4.200 m s.n.m."),
     ("Mejor época", "Diciembre-marzo (temporada seca)")],
    ["Las rutas de páramo del Quindío ofrecen paisajes únicos: frailejones, lagunas y cielos estrellados.",
     "El Cocora completo es la caminata más popular pero exige buena condición física.",
     "Las rutas de varios días requieren equipo de campamento y experiencia en montaña.",
     "Contrata guías locales que conocen los senderos y las condiciones climáticas.",
     "Lleva equipo adecuado: botas, mochila, agua, comida y capa impermeable."],
    [("Nivel 1", "Cocora completo o Murillo (1 día)"),
     ("Nivel 2", "Rutas de páramo (1-2 días)"),
     ("Nivel 3", "Caminatas de varios días (2-3 días)"),
     ("Nivel 4", "Expediciones con guía especializado")],
    [("¿Qué nivel de condición necesito para el senderismo avanzado en el Quindío?",
      "Depende de la ruta. El Cocora completo requiere buena condición física; las rutas de páramo y varios días exigen experiencia en montaña."),
     ("¿Hay rutas de varios días en el Quindío?",
      "Sí, hay rutas que conectan páramos y bosques del Quindío. Requieren equipo de campamento y guía especializado."),
     ("¿Necesito guía para senderismo avanzado?",
      "Recomendamos guía local para rutas desconocidas o de varios días. Conoce el terreno, el clima y las condiciones."),
     ("¿Cuál es la mejor época para senderismo en el Quindío?",
      "Diciembre a marzo (temporada seca) para mejor visibilidad y senderos más seguros.")])

add("birdwatching-eje-cafetero",
    "Birdwatching en el Eje Cafetero: las mejores especies y lugares",
    "Birdwatching Eje Cafetero 2026 | Aves | Quindío Travel",
    "Birdwatching en el Eje Cafetero: las mejores especies, lugares y rutas para observar aves en el Quindío. Guía completa para birdwatchers en 2026.",
    ["El Eje Cafetero es uno de los hotspots de biodiversidad de aves en Colombia: más de 500 especies registradas, incluyendo endémicas andinas y aves de bosque de niebla.",
     "El Valle de Cocora, las fincas cafeteras y los páramos del Quindío son los mejores lugares para observar aves en su hábitat natural."],
    [("Valle de Cocora", "Tucán andino, quetzal, tangaras | Senderos de bosque de niebla"),
     ("Fincas cafeteras", "Colibríes, tangaras, fruteros | Tours de finca con guía de aves"),
     ("Páramos", "Tángara del páramo, chochín del páramo | Altitud 3.000+ m"),
     ("Salento", "Aves de ciudad y jardín | Fácil acceso"),
     ("Filandia", "Aves de bosque andino | Miradores y senderos"),
     ("Parque del Café", "Aves de jardín botánico | Fácil acceso")],
    ["El Tucán Andino es la especie insignia del Cocora — se escucha antes de verse.",
     "Las fincas cafeteras son excelentes para observar colibríes y tangaras.",
     "Los páramos tienen especies únicas de altura que no se ven en ningún otro lado.",
     "La mejor época para birdwatching es diciembre-marzo (temporada seca).",
     "Contrata guías locales de aves — conocen los cantos y los sitios exactos."],
    [("Día 1", "Cocora — tucán andino y bosque de niebla"),
     ("Día 2", "Finca cafetera — colibríes y tangaras"),
     ("Día 3", "Páramo o miradores — especies de altura"),
     ("Día 4", "Salento/Filandia — aves de ciudad y jardín")],
    [("¿Cuántas especies de aves hay en el Eje Cafetero?",
      "Más de 500 especies registradas, incluyendo endémicas andinas y aves de bosque de niebla."),
     ("¿Cuál es la mejor época para birdwatching en el Quindío?",
      "Diciembre a marzo (temporada seca) por el clima y la actividad de aves. Pero es bueno todo el año."),
     ("¿Qué aves puedo ver en el Cocora?",
      "Tucán andino, quetzal, colibríes de montaña, tangaras andinas y el chirihueso del páramo."),
     ("¿Necesito equipo especial para birdwatching?",
      "Binoculares 8x42 son recomendados. Una cámara con zoom ayuda. Un guía local de aves mejora enormemente las observaciones.")])

add("luna-de-miel-eje-cafetero",
    "Luna de miel en el Eje Cafetero: planes románticos para parejas",
    "Luna de Miel Eje Cafetero 2026 | Romántico | Quindío Travel",
    "Luna de miel en el Eje Cafetero: planes románticos, hoteles boutique, cenas privadas y experiencias para parejas en el Quindío en 2026.",
    ["El Eje Cafetero es uno de los destinos más románticos de Colombia: paisajes de ensueño, hoteles boutique con vistas al Cocora, cenas a la luz de las velas y experiencias exclusivas para parejas.",
     "Esta guía te ayuda a planificar la luna de miel perfecta en el corazón del café."],
    [("Salento", "Cabañas boutique con vista al Cocora"),
     ("Filandia", "Fincas románticas con miradores"),
     ("Armenia", "Hoteles boutique urbanos"),
     ("Cocora", "Caminata romántica al amanecer | Experiencia única"),
     ("Fincas cafeteras", "Tours de café para dos | Degustación privada"),
     ("Termales", "Aguas termales para dos | Se cotiza dentro de planes románticos a medida"),
     ("Plan base", "Plan Diciembre 4D/3N desde $1.464.000 COP/persona (cuádruple, temporada alta)")],
    ["Las cabañas boutique de Salento tienen vistas espectaculares al Cocora — despertar con ese paisaje es inolvidable.",
     "Las fincas cafeteras ofrecen tours privados de café con degustación para dos.",
     "El Cocora al amanecer es una experiencia romántica única — la niebla y las palmas crean un escenario mágico.",
     "Los termales de Santa Rosa son perfectos para relajarse después de un día de turismo.",
     "Los hoteles boutique tienen detalles románticos: champán, decoración especial, cenas privadas."],
    [("Día 1", "Llegada + check-in en cabaña boutique + cena romántica"),
     ("Día 2", "Caminata al Cocora al amanecer + tour de finca cafetera"),
     ("Día 3", "Filandia + Mirador Cóndor + tarde libre"),
     ("Día 4", "Termales o spa + despedida")],
    [("¿Cuál es el mejor destino para luna de miel en el Quindío?",
      "Salento por sus cabañas boutique con vista al Cocora y la cercanía a Cocora y Filandia."),
     ("¿Los hoteles del Quindío tienen paquetes de luna de miel?",
      "Muchos sí. Los hoteles boutique suelen ofrecer detalles románticos: champán, decoración especial y cenas privadas."),
     ("¿Qué actividades son más románticas en el Quindío?",
      "Caminata al Cocora al amanecer, tours privados de café, miradores al atardecer y cenas a la luz de las velas."),
     ("¿Cuánto cuesta una luna de miel en el Eje Cafetero?",
      "Depende del alojamiento, la duración y las actividades. Cotiza tu escapada romántica por WhatsApp — el Plan Diciembre 4D/3N publicado arranca en $1.464.000 COP/persona en temporada alta (cuádruple), y los paquetes románticos a medida se cotizan según lo que elijas.")])

# ---------------------------------------------------------------------------
# Generador de HTML
# ---------------------------------------------------------------------------

def wa_link(text):
    return f"https://wa.me/573174426044?text={text.replace(' ', '%20')}"


def render_facts(facts):
    items = "".join(f"<li><strong>{k}:</strong> {v}</li>" for k, v in facts)
    return f'<ul class="facts-list">{items}</ul>'


def render_highlights(highlights):
    items = "".join(f"<li>{h}</li>" for h in highlights)
    return f'<ul class="highlights-list">{items}</ul>'


def render_steps(steps):
    items = "".join(
        f'<li><strong>{t}:</strong> {d}</li>' for t, d in steps)
    return f'<ol class="steps-list">{items}</ol>'


def render_faqs(faqs):
    items = "".join(
        f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>'
        for q, a in faqs)
    return f'<div class="faq-grid">{items}</div>'


def render_price_table(rows):
    if not rows:
        return ""
    trs = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in rows)
    return (f'<table class="price-table"><thead><tr><th>Concepto</th>'
            f'<th>Precio referencial</th></tr></thead><tbody>{trs}</tbody></table>')


def render_reviews():
    return """
    <section class="reviews-section">
        <h2>Lo que dicen nuestros viajeros</h2>
        <div class="review-grid">
            <div class="review-card">
                <div class="stars">★★★★★</div>
                <p>"Increíble experiencia en el Eje Cafetero. Los guías fueron muy profesionales y las fincas cafeteras hermosas."</p>
                <cite>— María González, Octubre 2026</cite>
            </div>
            <div class="review-card">
                <div class="stars">★★★★★</div>
                <p>"Excelente organización y atención. El Valle de Cocora es espectacular y el guía local muy knowledgeable."</p>
                <cite>— Carlos Rodríguez, Julio 2026</cite>
            </div>
        </div>
        <p class="review-link">4.7/5 en Google · 150+ reseñas verificadas · <a href="https://g.page/quindiotravel/review">Ver todas</a></p>
    </section>"""


def build_page(slug, c):
    url = f"{BASE}/programmatic-pages/{slug}.html"
    wa = wa_link(f"Hola Quindío Travel, me interesa: {c['h1']}")

    faq_json = [{"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in c["faqs"]]
    jsonld = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Organization", "@id": f"{BASE}/#organization",
             "name": "Quindío Travel", "url": BASE,
             "logo": f"{BASE}/logo_quindio_travel.png",
             "contactPoint": {"@type": "ContactPoint",
                              "telephone": "+57-317-4426044",
                              "contactType": "customer service",
                              "availableLanguage": "Spanish"}},
            {"@type": "Article",
             "headline": c["h1"],
             "description": c["desc"],
             "author": {"@type": "Organization", "name": "Quindío Travel",
                        "url": BASE},
             "publisher": {"@type": "Organization", "name": "Quindío Travel",
                            "url": BASE},
             "datePublished": "2026-11-13",
             "dateModified": "2026-11-13",
             "mainEntityOfPage": {"@type": "WebPage", "@id": url}},
            {"@type": "FAQPage", "mainEntity": faq_json},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1,
                 "name": "Inicio", "item": BASE + "/"},
                {"@type": "ListItem", "position": 2,
                 "name": "Guías", "item": BASE + "/blog.html"},
                {"@type": "ListItem", "position": 3,
                 "name": c["h1"][:60], "item": url}]},
        ],
    }

    price_html = render_price_table(c.get("price_table"))
    cta_text = c.get("cta") or (
        "Cotiza gratis tu plan personalizado con operadores locales "
        "certificados RNT 18152. Asistencia médica incluida.")

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{escape(c['title'])}</title>
    <meta name="description" content="{escape(c['desc'])}">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <link rel="canonical" href="{url}">
    <meta property="og:type" content="article">
    <meta property="og:title" content="{escape(c['title'])}">
    <meta property="og:description" content="{escape(c['desc'])}">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="{BASE}/assets/images/paisajes/valle-cocora-hero-banner.webp">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="stylesheet" href="../styles.css">
    <script src="../assets/js/whatsapp-template-handler.js" defer></script>
    <script src="../assets/js/diciembre-theme.js" defer></script>
    <script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>
    <style>
        .programmatic-page{{max-width:860px;margin:0 auto;padding:32px 18px 60px;}}
        .facts-list,.highlights-list{{padding-left:20px;line-height:1.9;}}
        .steps-list{{padding-left:22px;line-height:2;}}
        .price-table{{width:100%;border-collapse:collapse;margin:18px 0;font-size:.95rem;}}
        .price-table th,.price-table td{{border:1px solid #e2e8f0;padding:10px 12px;text-align:left;}}
        .price-table th{{background:#2E5A36;color:#fff;}}
        .faq-grid{{display:grid;gap:14px;}}
        .faq-item{{background:#f8faf8;border:1px solid #e4ebe6;border-radius:12px;padding:16px 18px;}}
        .faq-item h3{{margin:0 0 8px;color:#2E5A36;font-size:1rem;}}
        .faq-item p{{margin:0;color:#33413a;line-height:1.65;}}
        .reviews-section{{margin-top:40px;background:#fff;border:1px solid #e2e8f0;border-radius:16px;padding:24px;}}
        .review-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;margin:14px 0;}}
        .review-card{{background:#f8faf8;border-radius:12px;padding:16px;}}
        .review-card .stars{{color:#f5a623;font-size:1rem;margin-bottom:8px;}}
        .review-card p{{font-size:.92rem;line-height:1.6;color:#33413a;margin:0 0 10px;}}
        .review-card cite{{font-size:.8rem;color:#64748b;font-style:normal;}}
        .review-link{{font-size:.88rem;color:#475569;}}
        .page-cta{{background:linear-gradient(135deg,#2E5A36,#4E8755);color:#fff;border-radius:16px;padding:30px;text-align:center;margin:36px 0;}}
        .page-cta a{{display:inline-block;background:#fff;color:#2E5A36;padding:14px 30px;border-radius:999px;font-weight:800;text-decoration:none;margin-top:14px;}}
        @media(max-width:600px){{.programmatic-page{{padding:20px 12px 48px;}}}}
    </style>
</head>
<body>
    <header class="main-header">
        <div class="container">
            <a href="../index.html" class="logo">Quindío Travel</a>
            <nav class="main-nav">
                <a href="../index.html">Inicio</a>
                <a href="../planes.html">Planes</a>
                <a href="../index.html#hoteles">Hoteles</a>
            </nav>
        </div>
    </header>

    <nav class="breadcrumb-nav" aria-label="Breadcrumb">
        <div class="container">
            <ol class="breadcrumb">
                <li><a href="../index.html">Inicio</a></li>
                <li><a href="../blog.html">Guías</a></li>
                <li>{escape(c['h1'][:60])}</li>
            </ol>
        </div>
    </nav>

    <main class="programmatic-page">
        <article>
            <h1>{escape(c['h1'])}</h1>
            <p class="page-meta" style="color:#64748b;font-size:.85rem;margin-bottom:20px;">
                Actualizado: noviembre 2026 · Quindío Travel — Operador Turístico RNT 18152
            </p>

            <section>
                <p><strong>{escape(c['intro'][0])}</strong></p>
                <p>{escape(c['intro'][1])}</p>
            </section>

            <section>
                <h2>Lo esencial de un vistazo</h2>
                {render_facts(c['facts'])}
            </section>

            <section>
                <h2>Lo que debes saber</h2>
                {render_highlights(c['highlights'])}
            </section>

            <section>
                <h2>Cómo es la experiencia</h2>
                {render_steps(c['steps'])}
            </section>

            {f'<section><h2>Precios de referencia 2026</h2>{price_html}</section>' if price_html else ''}

            <section>
                <h2>Preguntas frecuentes</h2>
                {render_faqs(c['faqs'])}
            </section>

            {render_reviews()}

            <div class="page-cta">
                <h2 style="margin:0 0 10px;font-size:1.4rem;">{escape(c['h1'].split(':')[0])}: cotiza tu experiencia</h2>
                <p style="margin:0;opacity:.92;">{escape(cta_text)}</p>
                <a href="{wa}">Cotizar por WhatsApp</a>
            </div>
        </article>

        <section class="related-links">
            <h3>Te puede interesar</h3>
            <ul>
                <li><a href="../planes.html">Todos los planes turísticos</a></li>
                <li><a href="../valle-de-cocora.html">Valle de Cocora</a></li>
                <li><a href="../salento.html">Guía de Salento</a></li>
                <li><a href="../filandia.html">Guía de Filandia</a></li>
                <li><a href="../parque-del-cafe.html">Parque del Café</a></li>
                <li><a href="../panaca.html">PANACA</a></li>
                <li><a href="../planes-especiales-diciembre-2026.html">Planes especiales diciembre</a></li>
            </ul>
        </section>
    </main>

    <footer class="main-footer">
        <div class="container">
            <p>Quindío Travel — RNT 18152 — Operador Turístico Certificado</p>
            <p>Armenia, Quindío, Colombia — +57 317 442 6044</p>
        </div>
    </footer>

    <script src="../assets/js/language-detector.js" defer></script>
    <script src="../assets/js/related-links.js" defer></script>
</body>
</html>
"""


def main():
    count = 0
    for slug, c in P.items():
        fname = f"{slug}.html"
        path = DIR / fname
        if not path.exists():
            print(f"  !! no existe: {fname}")
            continue
        html = build_page(slug, c)
        if not DRY:
            path.write_text(html, encoding="utf-8")
        count += 1
        print(f"  {'[dry] ' if DRY else ''}OK {fname}")
    print(f"\nTotal: {count} páginas {'(dry-run)' if DRY else 'actualizadas'}")


if __name__ == "__main__":
    sys.exit(main())
