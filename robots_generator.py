"""
Generador de robots.txt optimizado para crawlers
Permite a los crawlers de Google y LLMs indexar correctamente
"""

from pathlib import Path

def generate_robots():
    """Genera robots.txt optimizado"""
    
    robots_content = """# Robots.txt para Quindío Travel
# Optimizado para crawlers de Google y LLMs

User-agent: *
Allow: /

# Permitir acceso a sitemap
Allow: /sitemap.xml
Allow: /llms.txt

# Permitir acceso a contenido programático
Allow: /programmatic-pages/
Allow: /blog/

# Bloquear archivos temporales y scripts
Disallow: /add_*.py
Disallow: /audit_*.py
Disallow: /blog_*.py
Disallow: /additional_*.py
Disallow: /check_*.py
Disallow: /gemini_*.py
Disallow: /list_*.py
Disallow: /optimize_*.py
Disallow: /programmatic_*.py
Disallow: /simple_*.py
Disallow: /topic_*.py
Disallow: /*_generator.py
Disallow: /llms_expanded.py
Disallow: /authority_content_generator.py
Disallow: /sitemap_generator.py
Disallow: /robots_generator.py

# Bloquear archivos de trabajo
Disallow: /interlinking_strategy.txt
Disallow: /TASKS_MANUALES_SEO_AVANZADO.md
Disallow: /FINAL_REPORT_SEO_AVANZADO.md
Disallow: /GEMINI_OPTIMIZATION_GUIDE.md
Disallow: /PROJECT_COMPLETION_REPORT.md
Disallow: /outreach_data/
Disallow: /directories_data/

# Sitemap
Sitemap: https://quindiotravel.com.co/sitemap.xml

# Crawl-delay para evitar sobrecarga
Crawl-delay: 1"""

    # Guardar robots.txt
    robots_file = Path(__file__).parent / "robots.txt"
    with open(robots_file, 'w', encoding='utf-8') as f:
        f.write(robots_content)
    
    print("Robots.txt optimizado creado")
    print("Permite a crawlers de Google y LLMs acceder a contenido optimizado")
    print("Bloquea archivos temporales y scripts de trabajo")
    
    return True

if __name__ == "__main__":
    print("Generando robots.txt optimizado...")
    print("=" * 60)
    
    success = generate_robots()
    
    if success:
        print("\n" + "=" * 60)
        print("Robots.txt optimizado con:")
        print("- Permisos para crawlers principales")
        print("- Acceso a sitemap.xml")
        print("- Acceso a llms.txt (para LLMs)")
        print("- Acceso a contenido programático y blog")
        print("- Bloqueo de archivos temporales")
        print("- Sitemap para crawlers")