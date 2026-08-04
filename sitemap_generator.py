"""
Generador de Sitemap XML para Quindío Travel
Incluye todas las páginas optimizadas para IA generativa
"""

from pathlib import Path
from datetime import datetime

def generate_sitemap():
    """Genera sitemap XML completo del sitio"""
    
    base_url = "https://quindiotravel.com.co"
    
    # Obtener todas las páginas
    programmatic_dir = Path(__file__).parent / "programmatic-pages"
    blog_dir = Path(__file__).parent / "blog"
    root_dir = Path(__file__).parent
    
    # Páginas principales
    main_pages = [
        {"url": base_url, "priority": "1.0", "changefreq": "daily"},
        {"url": f"{base_url}/planes.html", "priority": "0.9", "changefreq": "weekly"},
        {"url": f"{base_url}/index.html#hoteles", "priority": "0.8", "changefreq": "daily"}
    ]
    
    # Páginas de hoteles principales
    hotel_pages = [
        {"url": f"{base_url}/hotel-campestre-cafe-cafe.html", "priority": "0.8", "changefreq": "weekly"},
        {"url": f"{base_url}/finca-hotel-la-dorada.html", "priority": "0.8", "changefreq": "weekly"},
        {"url": f"{base_url}/cabanas-la-esmeralda.html", "priority": "0.8", "changefreq": "weekly"},
        {"url": f"{base_url}/finca-hotel-los-girasoles.html", "priority": "0.8", "changefreq": "weekly"},
        {"url": f"{base_url}/hotel-campestre-la-tata.html", "priority": "0.8", "changefreq": "weekly"},
        {"url": f"{base_url}/hotel-campestre-las-camelias.html", "priority": "0.8", "changefreq": "weekly"},
        {"url": f"{base_url}/hotel-de-la-vega.html", "priority": "0.8", "changefreq": "weekly"}
    ]
    
    # Páginas programáticas
    programmatic_files = list(programmatic_dir.glob('*.html'))
    programmatic_urls = []
    for file in programmatic_files:
        programmatic_urls.append({
            "url": f"{base_url}/programmatic-pages/{file.name}",
            "priority": "0.6",
            "changefreq": "monthly"
        })
    
    # Páginas de blog
    blog_files = list(blog_dir.glob('*.html'))
    blog_urls = []
    for file in blog_files:
        blog_urls.append({
            "url": f"{base_url}/blog/{file.name}",
            "priority": "0.7",
            "changefreq": "weekly"
        })
    
    # Páginas de pueblos
    town_pages = [
        {"url": f"{base_url}/salento.html", "priority": "0.9", "changefreq": "daily"},
        {"url": f"{base_url}/filandia.html", "priority": "0.9", "changefreq": "daily"},
        {"url": f"{base_url}/armenia.html", "priority": "0.9", "changefreq": "daily"}
    ]
    
    # Combinar todas las URLs
    all_urls = main_pages + town_pages + hotel_pages + programmatic_urls + blog_urls
    
    # Generar sitemap XML
    sitemap_content = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
'''
    
    for page in all_urls:
        sitemap_content += f'''  <url>
    <loc>{page['url']}</loc>
    <lastmod>2026-08-03</lastmod>
    <changefreq>{page['changefreq']}</changefreq>
    <priority>{page['priority']}</priority>
  </url>
'''
    
    sitemap_content += '''</urlset>'''
    
    # Guardar sitemap
    sitemap_file = Path(__file__).parent / "sitemap.xml"
    with open(sitemap_file, 'w', encoding='utf-8') as f:
        f.write(sitemap_content)
    
    print(f"Sitemap generado con {len(all_urls)} URLs")
    print(f"Archivo guardado en: {sitemap_file}")
    
    return len(all_urls)

if __name__ == "__main__":
    print("Generando sitemap XML para Quindío Travel...")
    print("=" * 60)
    
    count = generate_sitemap()
    
    print(f"\nSitemap completo con {count} URLs")
    print("Incluye:")
    print("- Páginas principales")
    print("- Páginas de hoteles")
    print("- Páginas programáticas (93)")
    print("- Páginas de blog (20)")
    print("- Páginas de pueblos")
    print("\nEste sitemap ayudará a los crawlers de Google y LLMs a descubrir todas las páginas optimizadas.")