"""
Generador de Artículos de Blog SEO - Quindío Travel
"""

from pathlib import Path
from datetime import datetime

def create_blog_directory():
    """Crea directorio de blog"""
    base_dir = Path(__file__).parent
    blog_dir = base_dir / "blog"
    blog_dir.mkdir(exist_ok=True)
    return blog_dir

def generate_article(title, keywords, content_outline):
    """Genera un artículo de blog completo"""
    
    current_date = datetime.now().strftime('%d de %B de %Y')
    
    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Quindío Travel</title>
    <meta name="description" content="Guía completa {title}. Tips, recomendaciones y precios para tu viaje al Eje Cafetero en 2026.">
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
                <p class="article-date">Publicado: {current_date}</p>
                <p class="article-author">Por: Quindío Travel - RNT 18152</p>
                <p class="article-reading-time">Tiempo de lectura: 8 minutos</p>
            </div>

            <div class="article-intro">
                <p>Descubre todo lo que necesitas saber para planificar tu viaje perfecto al Eje Cafetero con esta guía completa y actualizada para 2026.</p>
            </div>

            {content_outline}

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
    
    return html_content

def get_articles_data():
    """Retorna datos de los artículos a generar"""
    return [
        {
            "title": "Mejor época para visitar Quindío en 2026 - Guía Completa",
            "filename": "mejor-epoca-visitar-quindio-2026",
            "keywords": ["mejor época visitar quindío", "cuando ir quindío", "clima quindío", "temporada turística quindío"],
            "content": """
            <section class="article-section">
                <h2>Introducción: Por qué visitar el Quindío en 2026</h2>
                <p>El Quindío es una de las regiones más hermosas de Colombia, con paisajes únicos como el Valle de Cocora, pueblos mágicos como Salento y Filandia, y una cultura cafetera auténtica.</p>
                
                <p>Como operador turístico certificado RNT 18152, Quindío Travel te ofrece planes desde $425.000 COP hasta $3.420.000 COP por persona, adaptados a cualquier presupuesto.</p>
            </section>

            <section class="article-section">
                <h2>Temporada baja (enero-marzo): Ventajas y desventajas</h2>
                <p>La temporada baja es ideal para quienes buscan precios más económicos y menos turistas. Los precios de los planes pueden ser hasta un 30% más bajos que en temporada alta.</p>
                
                <ul>
                    <li><strong>Ventajas:</strong> Mejores precios, menos multitudes, disponibilidad inmediata</li>
                    <li><strong>Desventajas:</strong> Algunos servicios reducidos, clima más variable</li>
                </ul>
            </section>

            <section class="article-section">
                <h2>Temporada alta (diciembre-enero): Festividades</h2>
                <p>La temporada alta coincide con las vacaciones y festividades. Es el momento perfecto para disfrutar del clima seco y los eventos especiales de la región.</p>
                
                <ul>
                    <li><strong>Ventajas:</strong> Clima ideal, eventos especiales, ambiente festivo</li>
                    <li><strong>Desventajas:</strong> Precios más altos, mayor turismo, requiere reserva anticipada</li>
                </ul>
            </section>

            <section class="article-section">
                <h2>Eventos especiales por mes en 2026</h2>
                <p>El Quindío tiene eventos durante todo el año:</p>
                
                <ul>
                    <li><strong>Enero:</strong> Festividades de Año Nuevo</li>
                    <li><strong>Marzo:</strong> Festival de la Canción</li>
                    <li><strong>Julio:</strong> Feria de las Flores (regionales)</li>
                    <li><strong>Diciembre:</strong> Navidad y Año Nuevo</li>
                </ul>
            </section>

            <section class="article-section">
                <h2>Recomendaciones según tu tipo de viaje</h2>
                <p>Elige según tu estilo:</p>
                
                <ul>
                    <li><strong>Presupuesto limitado:</strong> Temporada baja, planes económicos</li>
                    <li><strong>Familias con niños:</strong> Temporada alta, días festivos</li>
                    <li><strong>Parejas:</strong> Temporada media, menos turismo</li>
                    <li><strong>Grupos grandes:</strong> Temporada media, mejores tarifas grupales</li>
                </ul>
            </section>
            """
        },
        {
            "title": "Hoteles económicos en Salento para familias grandes - Guía 2026",
            "filename": "hoteles-economicos-salento-familias-2026",
            "keywords": ["hoteles economicos salento", "alojamiento salento familias", "hoteles baratos salento", "donde quedarse salento"],
            "content": """
            <section class="article-section">
                <h2>Introducción: Salento para familias</h2>
                <p>Salento es uno de los destinos más populares del Eje Cafetero, ideal para familias gracias a su clima, seguridad y actividades variadas.</p>
                
                <p>Quindío Travel ofrece alojamiento en Salento desde $425.000 COP por persona en planes económicos, perfectos para familias grandes.</p>
            </section>

            <section class="article-section">
                <h2>Top 5 hoteles económicos para familias</h2>
                <p>Los mejores alojamientos económicos en Salento:</p>
                
                <ol>
                    <li><strong>Cabañas La Esmeralda:</strong> Desde $1.152.000 COP, ideal para familias</li>
                    <li><strong>Hotel Los Girasoles:</strong> Desde $1.588.000 COP, con piscina</li>
                    <li><strong>Hotel Café Café:</strong> Desde $1.770.000 COP, servicios completos</li>
                    <li><strong>Hostales familiares:</strong> Desde $430.000 COP, opción económica</li>
                    <li><strong>Fincas campestres:</strong> Desde $570.000 COP, experiencia rural</li>
                </ol>
            </section>

            <section class="article-section">
                <h2>Comparativa de precios y servicios</h2>
                <p>Análisis de opciones:</p>
                
                <ul>
                    <li><strong>Económico ($425.000 - $820.000 COP):</strong> Hostales, alojamiento básico</li>
                    <li><strong>Intermedio ($820.000 - $1.500.000 COP):</strong> Hoteles 3 estrellas, servicios completos</li>
                    <li><strong>VIP ($1.500.000 - $3.420.000 COP):</strong> Hoteles 4-5 estrellas, lujo</li>
                </ul>
            </section>

            <section class="article-section">
                <h2>Actividades familiares en Salento</h2>
                <p>Salento ofrece muchas actividades para familias:</p>
                
                <ul>
                    <li>Valle de Cocora: Caminata con niños, vistas espectaculares</li>
                    <li>Salento histórico: Calle del Tiempo Detenida, Museo del Canasto</li>
                    <li>Cafeterías: Experiencias cafeteras para familias</li>
                    <li>Naturaleza: Miradores, caminatas fáciles</li>
                </ul>
            </section>

            <section class="article-section">
                <h2>Consejos para ahorrar en alojamiento</h2>
                <p>Consejos de expertos:</p>
                
                <ul>
                    <li>Reservar con 2-3 meses de anticipación</li>
                    <li>Viajar en temporada baja (enero-marzo)</li>
                    <li>Optar por planes todo incluido</li>
                    <li>Considerar tarifas grupales (4+ personas)</li>
                </ul>
            </section>
            """
        },
        {
            "title": "Guía completa de transporte al Eje Cafetero desde Bogotá 2026",
            "filename": "guia-transporte-eje-cafetero-bogota-2026",
            "keywords": ["transporte bogota eje cafetero", "como llegar al quindío", "bus bogota armenia", "transporte particular eje cafetero"],
            "content": """
            <section class="article-section">
                <h2>Introducción: Opciones de transporte</h2>
                <p>Desde Bogotá hasta el Eje Cafetero hay varias opciones de transporte, cada una con sus ventajas según tu presupuesto y preferencias.</p>
                
                <p>Quindío Travel incluye transporte en sus planes desde $820.000 COP, facilitando tu viaje sin preocupaciones logísticas.</p>
            </section>

            <section class="article-section">
                <h2>Transporte en bus desde Bogotá</h2>
                <p>La opción más económica:</p>
                
                <ul>
                    <li><strong>Costo:</strong> $80.000 - $120.000 COP por persona</li>
                    <li><strong>Tiempo:</strong> 6-8 horas</li>
                    <li><strong>Compañías:</strong> Bolivariano, Expreso Bolivariano</li>
                    <li><strong>Ventajas:</strong> Económico, seguro, cómodo</li>
                </ul>
            </section>

            <section class="article-section">
                <h2>Transporte particular: Ventajas y desventajas</h2>
                <p>Opción para mayor comodidad:</p>
                
                <ul>
                    <li><strong>Costo:</strong> $200.000 - $400.000 COP por persona</li>
                    <li><strong>Tiempo:</strong> 4-5 horas</li>
                    <li><strong>Ventajas:</strong> Rápido, flexible, privado</li>
                    <li><strong>Desventajas:</strong> Más costoso, requiere coordinación</li>
                </ul>
            </section>

            <section class="article-section">
                <h2>Transporte aéreo: ¿Vale la pena?</h2>
                <p>Opción más rápida pero limitada:</p>
                
                <ul>
                    <li><strong>Costo:</strong> $300.000 - $600.000 COP</li>
                    <li><strong>Tiempo:</strong> 1 hora vuelo + traslado</li>
                    <li><strong>Limitaciones:</strong> Vuelos limitados a Armenia</li>
                    <li><strong>Recomendación:</strong> Solo para viajes cortos o presupuesto alto</li>
                </ul>
            </section>

            <section class="article-section">
                <h2>Costos comparativos por opción</h2>
                <p>Tabla comparativa:</p>
                
                <ul>
                    <li><strong>Bus:</strong> $80.000 - $120.000 COP (6-8 horas)</li>
                    <li><strong>Particular:</strong> $200.000 - $400.000 COP (4-5 horas)</li>
                    <li><strong>Aéreo:</strong> $300.000 - $600.000 COP (2-3 horas total)</li>
                </ul>
            </section>
            """
        },
        {
            "title": "Qué llevar en maleta para viaje al Quindío - Lista completa 2026",
            "filename": "que-llevar-maleta-viaje-quindio-2026",
            "keywords": ["que llevar al quindío", "maleta viaje eje cafetero", "ropa para quindío", "equipaje turismo quindío"],
            "content": """
            <section class="article-section">
                <h2>Introducción: Preparación esencial</h2>
                <p>Una buena preparación de tu maleta es fundamental para disfrutar al máximo tu viaje al Eje Cafetero.</p>
                
                <p>Quindío Travel te proporciona esta guía completa para que no olvides nada importante en tu viaje.</p>
            </section>

            <section class="article-section">
                <h2>Ropa según temporada del año</h2>
                <p>La ropa que debes llevar:</p>
                
                <ul>
                    <li><strong>Temporada seca:</strong> Ropa ligera, protector solar, sombrero</li>
                    <li><strong>Temporada lluviosa:</strong> Impermeable, botas, ropa abrigada</li>
                    <li><strong>General:</strong> Ropa cómoda para caminatas, calzado resistente</li>
                </ul>
            </section>

            <section class="article-section">
                <h2>Calzado recomendado para caminatas</h2>
                <p>El calzado es fundamental:</p>
                
                <ul>
                    <li>Botas de caminata (para Valle de Cocora)</li>
                    <li>Zapatillas cómodas (para pueblos)</li>
                    <li>Sandalias (para hotel/descanso)</li>
                    <li>Calzado impermeable (si lluvias)</li>
                </ul>
            </section>

            <section class="article-section">
                <h2>Artículos de higiene personal</h2>
                <p>No olvides:</p>
                
                <ul>
                    <li>Protector solar (muy importante)</li>
                    <li>Repelente de mosquitos</li>
                    <li>Medicamentos personales</li>
                    <li>Kit de aseo básico</li>
                </ul>
            </section>

            <section class="article-section">
                <h2>Electrónicos y accesorios</h2>
                <p>Tecnología esencial:</p>
                
                <ul>
                    <li>Cámara fotográfica / smartphone</li>
                    <li>Baterías extra / power bank</li>
                    <li>Cargadores universales</li>
                    <li>Adaptador eléctrico (si necesario)</li>
                </ul>
            </section>
            """
        },
        {
            "title": "Diferencias entre Salento y Filandia para elegir destino 2026",
            "filename": "diferencias-salento-filandia-destino-2026",
            "keywords": ["salento vs filandia", "mejor destino quindío", "diferencias salento filandia", "elegir destino eje cafetero"],
            "content": """
            <section class="article-section">
                <h2>Introducción: Dos joyas del Quindío</h2>
                <p>Salento y Filandia son dos de los destinos más hermosos del Eje Cafetero, cada uno con su propio encanto y características únicas.</p>
                
                <p>Quindío Travel te ayuda a elegir el destino perfecto según tus preferencias y presupuesto.</p>
            </section>

            <section class="article-section">
                <h2>Salento: Características principales</h2>
                <p>Salento es conocido por:</p>
                
                <ul>
                    <li>Valle de Cocora (principal atractivo)</li>
                    <li>Arquitectura tradicional bahareque</li>
                    <li>Calle del Tiempo Detenida</li>
                    <li>Mayor desarrollo turístico</li>
                    <li>Más opciones de alojamiento</li>
                </ul>
            </section>

            <section class="article-section">
                <h2>Filandia: Características principales</h2>
                <p>Filandia destaca por:</p>
                
                <ul>
                    <li>Vistas panorámicas del Quindío</li>
                    <li>Artesanías de alta calidad</li>
                    <li>Menos turismo masivo</li>
                    <li>Clima más fresco</li>
                    <li>Experiencia más auténtica</li>
                </ul>
            </section>

            <section class="article-section">
                <h2>Comparativa de actividades</h2>
                <p>Actividades en cada destino:</p>
                
                <ul>
                    <li><strong>Salento:</strong> Valle de Cocora, cafeterías, pueblos cercanos</li>
                    <li><strong>Filandia:</strong> Miradores, artesanías, clima más tranquilo</li>
                </ul>
            </section>

            <section class="article-section">
                <h2>Comparativa de costos</h2>
                <p>Costos aproximados:</p>
                
                <ul>
                    <li><strong>Salento:</strong> $425.000 - $2.000.000 COP (más opciones)</li>
                    <li><strong>Filandia:</strong> $570.000 - $1.800.000 COP (similar)</li>
                </ul>
            </section>

            <section class="article-section">
                <h2>Para quién es cada destino</h2>
                <p>Recomendaciones:</p>
                
                <ul>
                    <li><strong>Salento:</strong> Familias, grupos grandes, primera vez</li>
                    <li><strong>Filandia:</strong> Parejas, tranquilidad, artesanía</li>
                </ul>
            </section>
            """
        }
    ]

def main():
    """Función principal"""
    print("Sistema de Generación de Blog - Quindío Travel")
    print("=" * 50)
    
    blog_dir = create_blog_directory()
    articles_data = get_articles_data()
    
    generated_count = 0
    
    for article in articles_data:
        try:
            html_content = generate_article(
                article['title'], 
                article['keywords'], 
                article['content']
            )
            
            filename = f"{article['filename']}.html"
            filepath = blog_dir / filename
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            generated_count += 1
            print(f"✅ Artículo generado: {filename}")
            
        except Exception as e:
            print(f"❌ Error generando {article['title']}: {e}")
    
    print(f"\n🎉 {generated_count} artículos de blog generados exitosamente")
    print(f"📁 Ubicación: {blog_dir}")
    print(f"🔍 Keywords optimizadas para SEO")
    print(f"📄 Total de páginas SEO: {generated_count}")

if __name__ == "__main__":
    main()