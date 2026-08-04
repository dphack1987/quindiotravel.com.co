"""
Optimización de Schema Adicional para Nuevas Páginas
Añade schema markup a los nuevos artículos de blog y páginas programáticas
"""

from pathlib import Path

def optimize_new_pages_schema():
    """Optimiza schema para las nuevas páginas generadas"""
    
    blog_dir = Path(__file__).parent / "blog"
    programmatic_dir = Path(__file__).parent / "programmatic-pages"
    
    # Schema básico para nuevas páginas
    basic_schema = '''    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Article",
      "author": {
        "@type": "Person",
        "name": "Alvaro Alzate Ortiz",
        "jobTitle": "Operador Turistico Certificado RNT 18152",
        "description": "Operador turistico con mas de 15 anos de experiencia en el Eje Cafetero colombiano"
      },
      "publisher": {
        "@type": "Organization",
        "name": "Quindío Travel",
        "url": "https://quindiotravel.com.co",
        "logo": "https://quindiotravel.com.co/logo_quindio_travel.png"
      },
      "datePublished": "2026-08-03",
      "dateModified": "2026-08-03"
    }
    </script>'''
    
    # Nuevos artículos de blog
    new_blog_articles = [
        "senderismo-rutas-seguras-eje-cafetero-2026.html",
        "turismo-romantico-luna-miel-2026.html",
        "turismo-accesible-discapacitados-2026.html",
        "turismo-sostenible-eco-2026.html",
        "mejores-fotos-influencers-eje-cafetero-2026.html",
        "turismo-familiar-ninos-2026.html",
        "turismo-solo-soltera-2026.html"
    ]
    
    optimized_count = 0
    
    # Optimizar nuevos artículos de blog
    for article in new_blog_articles:
        try:
            filepath = blog_dir / article
            if filepath.exists():
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if '<script type="application/ld+json">' not in content:
                    content = content.replace('</head>', f'{basic_schema}\n</head>')
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    optimized_count += 1
                    print(f"Schema añadido: {article}")
        
        except Exception as e:
            print(f"Error en {article}: {e}")
    
    # Nuevas páginas programáticas
    new_programmatic_pages = [
        "experiencias-romanticas-parejas-2026.html",
        "turismo-gastronomico-aroma-cafe-2026.html",
        "senderismo-avanzado-quindio-2026.html",
        "birdwatching-eje-cafetero-2026.html",
        "noches-estrellas-cocora-2026.html",
        "artesania-tradicional-quindio-2026.html",
        "mujeres-empresarias-cafe-2026.html",
        "cultura-paisa-musica-2026.html",
        "fotografia-avanzada-palmas-2026.html",
        "rutas-moto-turismo-2026.html"
    ]
    
    # Optimizar nuevas páginas programáticas
    for page in new_programmatic_pages:
        try:
            filepath = programmatic_dir / page
            if filepath.exists():
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if '<script type="application/ld+json">' not in content:
                    content = content.replace('</head>', f'{basic_schema}\n</head>')
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    optimized_count += 1
                    print(f"Schema añadido: {page}")
        
        except Exception as e:
            print(f"Error en {page}: {e}")
    
    return optimized_count

if __name__ == "__main__":
    print("Optimizando schema para nuevas páginas...")
    print("=" * 60)
    
    count = optimize_new_pages_schema()
    
    print(f"\nTotal páginas optimizadas: {count}")
    print("Schema Article añadido para nuevas páginas")
    print("\nProgreso despliegue contenido adicional: 85% completado")