"""
Generación de 20 Páginas Programáticas Adicionales
Extendiendo el contenido programático para máxima visibilidad
"""

from pathlib import Path

def generate_additional_programmatic():
    """Genera 20 páginas programáticas adicionales"""
    
    programmatic_dir = Path(__file__).parent / "programmatic-pages"
    
    additional_pages = [
        {
            "file": "experiencias-romanticas-parejas-2026.html",
            "title": "Experiencias Románticas para Parejas Eje Cafetero 2026",
            "keywords": "experiencias romanticas eje cafetero, parejas salento, destinos romanticos quindio"
        },
        {
            "file": "turismo-gastronomico-aroma-cafe-2026.html",
            "title": "Turismo Gastronómico Aroma de Café Eje Cafetero 2026",
            "keywords": "turismo gastronomico eje cafetero, rutas cafe quindio, experiencias culinarias"
        },
        {
            "file": "senderismo-avanzado-quindio-2026.html",
            "title": "Senderismo Avanzado Quindío 2026 - Rutas Desafiantes",
            "keywords": "senderismo avanzado quindio, rutas dificiles eje cafetero, trekking salento"
        },
        {
            "file": "birdwatching-eje-cafetero-2026.html",
            "title": "Birdwatching Eje Cafetero 2026 - Observación de Aves",
            "keywords": "birdwatching eje cafetero, aves quindio, observacion aves salento"
        },
        {
            "file": "noches-estrellas-cocora-2026.html",
            "title": "Noches de Estrellas Valle de Cocora 2026",
            "keywords": "noches estrellas cocora, astronomia salento, cielo nocturno quindio"
        },
        {
            "file": "artesania-tradicional-quindio-2026.html",
            "title": "Artesanía Tradicional Quindío 2026 - Talleres Locales",
            "keywords": "artesania tradicional quindio, talleres artesanales salento, cultura local"
        },
        {
            "file": "mujeres-empresarias-cafe-2026.html",
            "title": "Mujeres Empresarias del Café Eje Cafetero 2026",
            "keywords": "mujeres empresarias cafe, mujeres caficultoras, empoderamiento rural"
        },
        {
            "file": "cultura-paisa-musica-2026.html",
            "title": "Cultura Paisa y Música Eje Cafetero 2026",
            "keywords": "cultura paisa musica, musica tipica eje cafetero, tradiciones quindio"
        },
        {
            "file": "fotografia-avanzada-palmas-2026.html",
            "title": "Fotografía Avanzada Palmas de Cera 2026",
            "keywords": "fotografia avanzada palmas cera, foto profesional cocora, tips fotograficos"
        },
        {
            "file": "rutas-moto-turismo-2026.html",
            "title": "Rutas en Moto Turismo Eje Cafetero 2026",
            "keywords": "rutas moto eje cafetero, mototurismo salento, viajes moto colombia"
        },
        {
            "file": "turismo-salud-bienestar-2026.html",
            "title": "Turismo Salud y Bienestar Eje Cafetero 2026",
            "keywords": "turismo salud eje cafetero, bienestar quindio, retreats colombia"
        },
        {
            "file": "festivales-musica-regionales-2026.html",
            "title": "Festivales de Música Regionales Eje Cafetero 2026",
            "keywords": "festivales musica eje cafetero, eventos musicales quindio, cultura musical"
        },
        {
            "file": "pueblos-magicos-quindio-2026.html",
            "title": "Pueblos Mágicos del Quindío 2026 - Pueblos Pueblitos",
            "keywords": "pueblos magicos quindio, pueblos pueblitos colombia, destinos encantadores"
        },
        {
            "file": "agricultura-sostenible-2026.html",
            "title": "Agricultura Sostenible Eje Cafetero 2026",
            "keywords": "agricultura sostenible eje cafetero, agricultura ecologica quindio, granjas sostenibles"
        },
        {
            "file": "turismo-negocios-2026.html",
            "title": "Turismo de Negocios Eje Cafetero 2026",
            "keywords": "turismo negocios eje cafetero, conferencias quindio, eventos corporativos"
        },
        {
            "file": "turismo-senior-2026.html",
            "title": "Turismo Senior Eje Cafetero 2026 - Viajes para Adultos Mayores",
            "keywords": "turismo senior eje cafetero, viajes adultos mayores, turismo accesible"
        },
        {
            "file": "deportes-extremos-controlados-2026.html",
            "title": "Deportes Extremos Controlados Eje Cafetero 2026",
            "keywords": "deportes extremos eje cafetero, aventura segura quindio, turismo adrenalina"
        },
        {
            "file": "artes-visuales-eje-cafetero-2026.html",
            "title": "Artes Visuales Eje Cafetero 2026 - Galerías y Talleres",
            "keywords": "artes visuales eje cafetero, galerias arte salento, talleres artisticos"
        },
        {
            "file": "produccion-cafe-organico-2026.html",
            "title": "Producción de Café Orgánico Eje Cafetero 2026",
            "keywords": "produccion cafe organico, cafes especiales quindio, agricultura organica"
        },
        {
            "file": "turismo-spiritual-2026.html",
            "title": "Turismo Espiritual Eje Cafetero 2026 - Retiros",
            "keywords": "turismo espiritual eje cafetero, retiros quindio, meditacion naturaleza"
        }
    ]
    
    # Template simplificado para generación rápida
    template = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{title} | Quindío Travel</title>
    <meta name="description" content="{title} en el Eje Cafetero colombiano. Experiencias auténticas con Quindío Travel RNT 18152.">
    <meta name="keywords" content="{keywords}">
    <link rel="stylesheet" href="../styles.css">
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
                <li><a href="../programmatic-pages.html">Programáticas</a></li>
                <li>{title_short}</li>
            </ol>
        </div>
    </nav>

    <main class="container">
        <article class="article-content">
            <h1>{title}</h1>
            
            <div class="article-meta">
                <p class="article-date">Actualizado: 3 de agosto de 2026</p>
                <p class="article-author">Por: Quindío Travel - RNT 18152</p>
            </div>

            <section class="article-section">
                <h2>Introducción: {title_short}</h2>
                <p>El Eje Cafetero ofrece experiencias únicas en {topic}, con Quindío Travel tu guía experto RNT 18152.</p>
            </section>

            <section class="article-section">
                <h2>Por qué elegir {topic_short}</h2>
                <p>Experiencias auténticas con operador local nativo, 15+ años de experiencia en turismo del Eje Cafetero.</p>
            </section>

            <div class="article-cta">
                <h2>¿Listo para {action}?</h2>
                <p>Cotiza gratis tu plan de {topic_short} con Quindío Travel.</p>
                <a href="https://wa.me/573174426044?text=Hola%20Quindío%20Travel,%20estoy%20interesado%20en%20{topic_underscore}" class="btn-cta">
                    Cotizar {topic_short}
                </a>
            </div>
        </article>
    </main>

    <footer class="main-footer">
        <div class="container">
            <p>Quindío Travel - RNT 18152 - Operador Turístico Certificado</p>
            <p>Armenia, Quindío, Colombia - +57-317-4426044</p>
        </div>
    </footer>
</body>
</html>"""
    
    generated_count = 0
    
    for page in additional_pages:
        try:
            # Extraer información para el template
            title = page["title"]
            keywords = page["keywords"]
            title_short = title.replace(" 2026", "").replace("Eje Cafetero", "").replace("Quindío", "").strip()
            topic = title_short
            topic_short = topic.split()[0] if topic.split() else topic
            topic_underscore = topic_short.replace(" ", "-").lower()
            action = topic_short.lower()
            
            # Reemplazar en template
            content = template.format(
                title=title,
                keywords=keywords,
                title_short=title_short,
                topic=topic,
                topic_short=topic_short,
                topic_underscore=topic_underscore,
                action=action
            )
            
            filepath = programmatic_dir / page["file"]
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            generated_count += 1
            print(f"Página generada: {page['file']}")
            
        except Exception as e:
            print(f"Error generando {page['file']}: {e}")
    
    return generated_count

if __name__ == "__main__":
    print("Generando 20 páginas programáticas adicionales...")
    print("=" * 60)
    
    count = generate_additional_programmatic()
    
    print(f"\nTotal páginas generadas: {count}")
    print(f"Total páginas programáticas: {93 + count}")
    print("\nProgreso despliegue contenido adicional: 30% completado")