"""
Sistema de Generación de Blog Automatizado - Quindío Travel
Genera artículos SEO-optimizados para turismo del Eje Cafetero
"""

import re
from pathlib import Path
from datetime import datetime
import json

class BlogGenerator:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.blog_dir = self.base_dir / "blog"
        self.blog_dir.mkdir(exist_ok=True)
        
        # Temas SEO-optimizados para el Eje Cafetero
        self.topics = [
            {
                "title": "Mejor época para visitar Quindío en 2026 - Guía Completa",
                "keywords": ["mejor época visitar quindío", "cuando ir quindío", "clima quindío", "temporada turística quindío"],
                "content_outline": [
                    "Introducción: Por qué elegir el Quindío en 2026",
                    "Temporada baja (enero-marzo): Ventajas y desventajas",
                    "Temporada media (abril-junio): Clima ideal",
                    "Temporada alta (julio-agosto): Vacaciones escolares",
                    "Temporada pico (diciembre-enero): Festividades",
                    "Eventos especiales por mes en 2026",
                    "Recomendaciones según tu tipo de viaje",
                    "Conclusión: Planifica tu viaje perfecto"
                ]
            },
            {
                "title": "Hoteles económicos en Salento para familias grandes - Guía 2026",
                "keywords": ["hoteles economicos salento", "alojamiento salento familias", "hoteles baratos salento", "donde quedarse salento"],
                "content_outline": [
                    "Introducción: Salento para familias",
                    "Top 5 hoteles económicos para familias",
                    "Comparativa de precios y servicios",
                    "Actividades familiares en Salento",
                    "Consejos para ahorrar en alojamiento",
                    "Reservas anticipadas vs última hora",
                    "Conclusión: Mejor opción según presupuesto"
                ]
            },
            {
                "title": "Guía completa de transporte al Eje Cafetero desde Bogotá 2026",
                "keywords": ["transporte bogota eje cafetero", "como llegar al quindío", "bus bogota armenia", "transporte particular eje cafetero"],
                "content_outline": [
                    "Introducción: Opciones de transporte",
                    "Transporte en bus desde Bogotá",
                    "Transporte particular: Ventajas y desventajas",
                    "Transporte aéreo: ¿Vale la pena?",
                    "Costos comparativos por opción",
                    "Tiempo de viaje y comodidad",
                    "Recomendaciones según presupuesto",
                    "Conclusión: Mejor opción para ti"
                ]
            },
            {
                "title": "Qué llevar en maleta para viaje al Quindío - Lista completa 2026",
                "keywords": ["que llevar al quindío", "maleta viaje eje cafetero", "ropa para quindío", "equipaje turismo quindío"],
                "content_outline": [
                    "Introducción: Preparación esencial",
                    "Ropa según temporada del año",
                    "Calzado recomendado para caminatas",
                    "Artículos de higiene personal",
                    "Electrónicos y accesorios",
                    "Documentos importantes",
                    "Botiquín de primeros auxilios",
                    "Lo que NO debes llevar",
                    "Conclusión: Lista de verificación final"
                ]
            },
            {
                "title": "Diferencias entre Salento y Filandia para elegir destino 2026",
                "keywords": ["salento vs filandia", "mejor destino quindío", "diferencias salento filandia", "elegir destino eje cafetero"],
                "content_outline": [
                    "Introducción: Dos joyas del Quindío",
                    "Salento: Características principales",
                    "Filandia: Características principales",
                    "Comparativa de actividades",
                    "Comparativa de costos",
                    "Comparativa de alojamiento",
                    "Para quién es cada destino",
                    "Recomendación según tipo de viajero",
                    "Conclusión: Tu destino ideal"
                ]
            }
        ]
    
    def generate_blog_article(self, topic):
        """Genera un artículo de blog completo basado en el tema"""
        
        # Generar HTML del artículo
        html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{topic['title']} | Quindío Travel</title>
    <meta name="description" content="Guía completa {topic['title']}. Tips, recomendaciones y precios para tu viaje al Eje Cafetero en 2026.">
    <meta name="keywords" content="{', '.join(topic['keywords'])}">
    <link rel="canonical" href="https://quindiotravel.com.co/blog/{self.slugify(topic['title'])}.html">
    <link rel="stylesheet" href="../styles.css">
</head>
<body>
    <!-- Header principal -->
    <header class="main-header">
        <div class="container">
            <a href="../index.html" class="logo">Quindío Travel</a>
            <nav class="main-nav">
                <a href="../index.html">Inicio</a>
                <a href="../planes.html">Planes</a>
                <a href="../index.html#hoteles">Hoteles</a>
                <a href="../blog/{self.slugify(topic['title'])}.html">Blog</a>
            </nav>
        </div>
    </header>

    <!-- Breadcrumb -->
    <nav class="breadcrumb-nav" aria-label="Breadcrumb">
        <div class="container">
            <ol class="breadcrumb" itemscope itemtype="https://schema.org/BreadcrumbList">
                <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                    <a href="../index.html" itemprop="item"><span itemprop="name">Inicio</span></a>
                    <meta itemprop="position" content="1" />
                </li>
                <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                    <a href="../blog.html" itemprop="item"><span itemprop="name">Blog</span></a>
                    <meta itemprop="position" content="2" />
                </li>
                <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                    <span itemprop="name">{topic['title']}</span>
                    <meta itemprop="position" content="3" />
                </li>
            </ol>
        </div>
    </nav>

    <!-- Contenido del artículo -->
    <main class="blog-post container">
        <article class="article-content">
            <h1>{topic['title']}</h1>
            
            <div class="article-meta">
                <p class="article-date">Publicado: {datetime.now().strftime('%d de %B de %Y')}</p>
                <p class="article-author">Por: Quindío Travel - Operador Turístico RNT 18152</p>
                <p class="article-reading-time">Tiempo de lectura: 8 minutos</p>
            </div>

            <div class="article-intro">
                <p>Descubre todo lo que necesitas saber para planificar tu viaje perfecto al Eje Cafetero con esta guía completa y actualizada para 2026.</p>
            </div>

            {self.generate_content_sections(topic)}

            <div class="article-cta">
                <h2>¿Listo para planificar tu viaje al Eje Cafetero?</h2>
                <p>Cotiza gratis tu plan personalizado con operadores locales certificados RNT 18152.</p>
                <a href="https://wa.me/573174426044?text=Hola%20Quindío%20Travel,%20estoy%20interesado%20en%20planificar%20mi%20viaje%20al%20Eje%20Cafetero" class="btn-cta">
                    Cotizar Plan Personalizado
                </a>
            </div>

            <div class="article-faq">
                <h2>Preguntas Frecuentes</h2>
                {self.generate_faq(topic)}
            </div>
        </article>

        <aside class="article-sidebar">
            <div class="sidebar-section">
                <h3>Artículos Relacionados</h3>
                <ul class="related-posts">
                    <li><a href="guia-completa-eje-cafetero.html">Guía Completa del Eje Cafetero</a></li>
                    <li><a href="mejores-hoteles-salento.html">Mejores Hoteles en Salento</a></li>
                    <li><a href="paquetes-economicos-eje-cafetero.html">Paquetes Económicos al Eje Cafetero</a></li>
                </ul>
            </div>

            <div class="sidebar-section">
                <h3>Planes Populares</h3>
                <ul class="popular-plans">
                    <li><a href="../plan-1.html">Plan 2 Días / 1 Noche</a></li>
                    <li><a href="../plan-3.html">Plan 4 Días / 3 Noches</a></li>
                    <li><a href="../plan-6.html">Plan 5 Días / 4 Noches</a></li>
                </ul>
            </div>
        </aside>
    </main>

    <!-- Footer -->
    <footer class="main-footer">
        <div class="container">
            <p>Quindío Travel - RNT 18152 - Operador Turístico Certificado</p>
            <p>Armenia, Quindío, Colombia - +57-317-4426044</p>
        </div>
    </footer>

    <!-- Schema.org Article -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "{topic['title']}",
        "author": {{
            "@type": "Organization",
            "name": "Quindío Travel",
            "url": "https://quindiotravel.com.co"
        }},
        "publisher": {{
            "@type": "Organization",
            "name": "Quindío Travel",
            "logo": {{
                "@type": "ImageObject",
                "url": "https://quindiotravel.com.co/logo_quindio_travel.png"
            }}
        }},
        "datePublished": "{datetime.now().strftime('%Y-%m-%d')}",
        "dateModified": "{datetime.now().strftime('%Y-%m-%d')}",
        "description": "Guía completa {topic['title']}. Tips, recomendaciones y precios para tu viaje al Eje Cafetero en 2026.",
        "keywords": "{', '.join(topic['keywords'])}"
    }}
    </script>
</body>
</html>"""
        
        return html_content
    
    def generate_content_sections(self, topic):
        """Genera las secciones de contenido basadas en el outline"""
        sections_html = ""
        
        for i, section_title in enumerate(topic['content_outline'], 1):
            section_content = self.generate_section_content(section_title, topic['keywords'])
            sections_html += f"""
            <section class="article-section">
                <h2>{i}. {section_title}</h2>
                {section_content}
            </section>
            """
        
        return sections_html
    
    def generate_section_content(self, section_title, keywords):
        """Genera contenido para una sección específica"""
        # Aquí podrías integrar un LLM para generar contenido real
        # Por ahora, generamos contenido placeholder optimizado
        
        content = f"""
        <p>Esta sección detalla {section_title.lower()} con información actualizada para 2026.</p>
        
        <p>En el contexto del turismo del Eje Cafetero, {section_title.lower()} es fundamental para planificar tu viaje. Considerando los precios actuales que van desde $425.000 COP hasta $3.420.000 COP por persona, es importante tomar decisiones informadas.</p>
        
        <h3>Puntos clave a considerar:</h3>
        <ul>
            <li><strong>Precio:</strong> Varía según temporada y tipo de servicio</li>
            <li><strong>Disponibilidad:</strong> Mejor reservar con anticipación</li>
            <li><strong>Calidad:</strong> Operadores certificados RNT 18152 garantizan servicio</li>
            <li><strong>Ubicación:</strong> Proximidad a principales atractivos</li>
        </ul>
        
        <p>Para más información sobre {keywords[0]}, te recomendamos contactar directamente con operadores locales como Quindío Travel.</p>
        """
        
        return content
    
    def generate_faq(self, topic):
        """Genera FAQ basado en el tema"""
        faq_html = ""
        
        faq_questions = [
            f"¿Cuál es el mejor momento para {topic['keywords'][0]}?",
            f"¿Cuánto cuesta {topic['keywords'][0]} en 2026?",
            f"¿Qué incluye {topic['keywords'][0]}?",
            f"¿Es seguro {topic['keywords'][0]}?"
        ]
        
        for i, question in enumerate(faq_questions, 1):
            answer = f"Esta respuesta detalla información sobre {question.lower()} basada en la experiencia de operadores turísticos locales certificados."
            
            faq_html += f"""
            <div class="faq-item">
                <h3>{i}. {question}</h3>
                <p>{answer}</p>
            </div>
            """
        
        return faq_html
    
    def slugify(self, text):
        """Convierte texto a slug URL-friendly"""
        text = text.lower()
        text = re.sub(r'[^\w\s-]', '', text)
        text = re.sub(r'[-\s]+', '-', text)
        return text[:100]  # Limitar longitud
    
    def generate_all_articles(self):
        """Genera todos los artículos de blog"""
        generated_count = 0
        
        try:
            for topic in self.topics:
                try:
                    html_content = self.generate_blog_article(topic)
                    filename = f"{self.slugify(topic['title'])}.html"
                    filepath = self.blog_dir / filename
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(html_content)
                    
                    generated_count += 1
                    print(f"✅ Artículo generado: {filename}")
                    
                except Exception as e:
                    print(f"❌ Error generando {topic['title']}: {e}")
        
        except Exception as e:
            print(f"❌ Error general: {e}")
        
        return generated_count

def main():
    """Función principal"""
    print("Sistema de Generación de Blog - Quindío Travel")
    print("=" * 50)
    
    generator = BlogGenerator()
    count = generator.generate_all_articles()
    
    print(f"\n🎉 {count} artículos de blog generados exitosamente")
    print(f"📁 Ubicación: {generator.blog_dir}")
    print(f"🔍 Keywords optimizadas para SEO")

if __name__ == "__main__":
    main()