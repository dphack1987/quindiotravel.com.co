"""
Sistema Simplificado de Generación de Blog - Quindío Travel
"""

import re
from pathlib import Path
from datetime import datetime

def slugify(text):
    """Convierte texto a slug URL-friendly"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text[:100]

def generate_simple_article(title, keywords):
    """Genera un artículo simple de blog"""
    
    slug = slugify(title)
    
    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Quindío Travel</title>
    <meta name="description" content="Guía completa {title}. Tips y recomendaciones para tu viaje al Eje Cafetero en 2026.">
    <meta name="keywords" content="{', '.join(keywords)}">
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
                <li><a href="../blog.html">Blog</a></li>
                <li>{title}</li>
            </ol>
        </div>
    </nav>

    <main class="blog-post container">
        <article class="article-content">
            <h1>{title}</h1>
            
            <div class="article-meta">
                <p class="article-date">Publicado: {datetime.now().strftime('%d de %B de %Y')}</p>
                <p class="article-author">Por: Quindío Travel - RNT 18152</p>
            </div>

            <div class="article-intro">
                <p>Descubre todo lo que necesitas saber para planificar tu viaje perfecto al Eje Cafetero con esta guía completa y actualizada para 2026.</p>
            </div>

            <section class="article-section">
                <h2>Introducción</h2>
                <p>El turismo en el Eje Cafetero colombiano es una experiencia única. En esta guía completa te contamos todo lo que necesitas saber sobre {keywords[0]} para planificar tu viaje perfecto en 2026.</p>
                
                <p>Como operador turístico certificado RNT 18152 con más de 15 años de experiencia, Quindío Travel te ofrece planes desde $425.000 COP hasta $3.420.000 COP por persona, dependiendo de tu presupuesto y preferencias.</p>
            </section>

            <section class="article-section">
                <h2>Por qué visitar el Eje Cafetero en 2026</h2>
                <p>El Eje Cafetero ofrece paisajes únicos como el Valle de Cocora con sus palmas de cera, experiencias culturales en Salento y Filandia, y parques temáticos como el Parque del Café y PANACA.</p>
                
                <p>Además, la región ofrece una excelente gastronomía, clima perfecto todo el año, y la hospitalidad característica de los paisas.</p>
            </section>

            <section class="article-section">
                <h2>Mejor época para visitar</h2>
                <p>El Eje Cafetero es hermoso todo el año, pero cada temporada tiene sus ventajas:</p>
                
                <ul>
                    <li><strong>Temporada baja (enero-marzo, mayo-junio, septiembre-noviembre):</strong> Mejores precios, menos turistas, clima ideal para actividades.</li>
                    <li><strong>Temporada alta (diciembre-enero, Semana Santa, julio):</strong> Clima seco, festividades, más eventos.</li>
                </ul>
            </section>

            <section class="article-section">
                <h2>Costos y Presupuesto</h2>
                <p>Los planes turísticos varían según:</p>
                
                <ul>
                    <li>Duración del viaje (2-5 días)</li>
                    <li>Tipo de alojamiento (económico, intermedio, VIP)</li>
                    <li>Transporte (sin transporte, radio taxi, placa blanca)</li>
                    <li>Número de personas</li>
                </ul>
                
                <p>Rango de precios: $425.000 COP (económico sin transporte) hasta $3.420.000 COP (VIP sin transporte).</p>
            </section>

            <section class="article-section">
                <h2>Recomendaciones de Quindío Travel</h2>
                <p>Como operador local certificado, recomendamos:</p>
                
                <ul>
                    <li>Reservar con anticipación en temporada alta</li>
                    <li>Elegir operadores certificados RNT</li>
                    <li>Considerar transporte seguro y legal</li>
                    <li>Incluir experiencia en fincas cafeteras</li>
                </ul>
            </section>

            <div class="article-cta">
                <h2>¿Listo para planificar tu viaje al Eje Cafetero?</h2>
                <p>Cotiza gratis tu plan personalizado con operadores locales certificados RNT 18152.</p>
                <a href="https://wa.me/573174426044?text=Hola%20Quindío%20Travel,%20estoy%20interesado%20en%20planificar%20mi%20viaje%20al%20Eje%20Cafetero" class="btn-cta">
                    Cotizar Plan Personalizado
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
    
    return html_content, slug

def main():
    """Función principal"""
    print("Sistema de Generación de Blog - Quindío Travel")
    print("=" * 50)
    
    base_dir = Path(__file__).parent
    blog_dir = base_dir / "blog"
    blog_dir.mkdir(exist_ok=True)
    
    topics = [
        {
            "title": "Mejor época para visitar Quindío en 2026 - Guía Completa",
            "keywords": ["mejor época visitar quindío", "cuando ir quindío", "clima quindío", "temporada turística quindío"]
        },
        {
            "title": "Hoteles económicos en Salento para familias grandes - Guía 2026",
            "keywords": ["hoteles economicos salento", "alojamiento salento familias", "hoteles baratos salento", "donde quedarse salento"]
        },
        {
            "title": "Guía completa de transporte al Eje Cafetero desde Bogotá 2026",
            "keywords": ["transporte bogota eje cafetero", "como llegar al quindío", "bus bogota armenia", "transporte particular eje cafetero"]
        },
        {
            "title": "Qué llevar en maleta para viaje al Quindío - Lista completa 2026",
            "keywords": ["que llevar al quindío", "maleta viaje eje cafetero", "ropa para quindío", "equipaje turismo quindío"]
        },
        {
            "title": "Diferencias entre Salento y Filandia para elegir destino 2026",
            "keywords": ["salento vs filandia", "mejor destino quindío", "diferencias salento filandia", "elegir destino eje cafetero"]
        }
    ]
    
    generated_count = 0
    
    for topic in topics:
        try:
            html_content, slug = generate_simple_article(topic['title'], topic['keywords'])
            filename = f"{slug}.html"
            filepath = blog_dir / filename
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            generated_count += 1
            print(f"✅ Artículo generado: {filename}")
            
        except Exception as e:
            print(f"❌ Error generando {topic['title']}: {e}")
    
    print(f"\n🎉 {generated_count} artículos de blog generados exitosamente")
    print(f"📁 Ubicación: {blog_dir}")
    print(f"🔍 Keywords optimizadas para SEO")

if __name__ == "__main__":
    main()