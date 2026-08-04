"""
Actualizar Sitemap con Páginas Faltantes
Añade las páginas principales que faltan al sitemap
"""

from pathlib import Path

def get_sitemap_urls():
    """Extrae URLs del sitemap actual"""
    
    sitemap_path = Path(__file__).parent / "sitemap.xml"
    
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extraer URLs usando regex simple
    import re
    urls = re.findall(r'<loc>(https://quindiotravel\.com\.co/[^<]+)</loc>', content)
    
    return set(urls)

def get_main_html_files():
    """Obtiene archivos HTML principales"""
    
    project_root = Path(__file__).parent
    
    main_files = []
    
    # Directorio raíz
    main_files.extend(project_root.glob("*.html"))
    
    # Blog
    main_files.extend(project_root.glob("blog/*.html"))
    
    # Programmatic pages
    main_files.extend(project_root.glob("programmatic-pages/*.html"))
    
    # Planes
    main_files.extend(project_root.glob("plan-*.html"))
    
    # Hoteles (solo principales)
    hotel_files = [
        "hotel-campestre-cafe-cafe.html",
        "finca-hotel-la-dorada.html", 
        "cabanas-la-esmeralda.html",
        "finca-hotel-los-girasoles.html",
        "hotel-campestre-la-tata.html",
        "hotel-campestre-las-camelias.html",
        "hotel-de-la-vega.html"
    ]
    
    for hotel_file in hotel_files:
        hotel_path = project_root / hotel_file
        if hotel_path.exists():
            main_files.append(hotel_path)
    
    return main_files

def file_to_url(filepath):
    """Convierte filepath a URL"""
    
    project_root = Path(__file__).parent
    relative_path = filepath.relative_to(project_root)
    
    # Convertir a URL
    url = f"https://quindiotravel.com.co/{relative_path.as_posix()}"
    
    return url

def update_sitemap():
    """Actualiza sitemap con páginas faltantes"""
    
    sitemap_path = Path(__file__).parent / "sitemap.xml"
    
    # Obtener URLs actuales del sitemap
    sitemap_urls = get_sitemap_urls()
    print(f"URLs actuales en sitemap: {len(sitemap_urls)}")
    
    # Obtener archivos HTML principales
    html_files = get_main_html_files()
    print(f"Archivos HTML principales: {len(html_files)}")
    
    # Convertir archivos a URLs
    html_urls = set()
    for filepath in html_files:
        url = file_to_url(filepath)
        html_urls.add(url)
    
    # Encontrar URLs faltantes
    missing_urls = html_urls - sitemap_urls
    print(f"URLs faltantes: {len(missing_urls)}")
    
    if not missing_urls:
        print("No hay URLs faltantes para añadir")
        return False
    
    # Leer sitemap actual
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Encontrar posición antes de </urlset>
    urlset_end = content.find('</urlset>')
    
    if urlset_end == -1:
        print("Error: no se encontró </urlset>")
        return False
    
    # Generar entradas para URLs faltantes
    entries = []
    for url in sorted(missing_urls):
        entry = f'''  <url>
    <loc>{url}</loc>
    <lastmod>2026-08-04</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>'''
        entries.append(entry)
    
    # Insertar entradas antes de </urlset>
    new_content = content[:urlset_end] + '\n'.join(entries) + '\n' + content[urlset_end:]
    
    # Escribir sitemap actualizado
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Sitemap actualizado con {len(missing_urls)} URLs adicionales")
    
    # Verificar nuevo total
    new_url_count = new_content.count('<url>')
    print(f"Nuevo total de URLs: {new_url_count}")
    
    return True

if __name__ == "__main__":
    print("Actualizando sitemap con páginas faltantes...")
    print("=" * 70)
    
    update_sitemap()
    
    print("\n" + "=" * 70)
    print("Actualización de sitemap completada")