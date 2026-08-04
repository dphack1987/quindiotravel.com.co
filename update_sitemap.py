"""
Actualización de Sitemap XML
Incluye las nuevas páginas generadas (10 blog + 20 programáticas)
"""

from pathlib import Path
from datetime import datetime

def update_sitemap():
    """Actualiza el sitemap con nuevas páginas"""
    
    sitemap_path = Path(__file__).parent / "sitemap.xml"
    
    # Nuevas páginas de blog
    new_blog_pages = [
        "blog/senderismo-rutas-seguras-eje-cafetero-2026.html",
        "blog/gastronomia-autentica-quindio-2026.html",
        "blog/turismo-romantico-luna-miel-2026.html",
        "blog/turismo-accesible-discapacitados-2026.html",
        "blog/turismo-sostenible-eco-2026.html",
        "blog/mejores-fotos-influencers-eje-cafetero-2026.html",
        "blog/turismo-familiar-ninos-2026.html",
        "blog/turismo-solo-soltera-2026.html",
        "blog/conferencias-eventos-quindio-2026.html",
        "blog/ofertas-temporada-agosto-2026.html"
    ]
    
    # Nuevas páginas programáticas
    new_programmatic_pages = [
        "programmatic-pages/experiencias-romanticas-parejas-2026.html",
        "programmatic-pages/turismo-gastronomico-aroma-cafe-2026.html",
        "programmatic-pages/senderismo-avanzado-quindio-2026.html",
        "programmatic-pages/birdwatching-eje-cafetero-2026.html",
        "programmatic-pages/noches-estrellas-cocora-2026.html",
        "programmatic-pages/artesania-tradicional-quindio-2026.html",
        "programmatic-pages/mujeres-empresarias-cafe-2026.html",
        "programmatic-pages/cultura-paisa-musica-2026.html",
        "programmatic-pages/fotografia-avanzada-palmas-2026.html",
        "programmatic-pages/rutas-moto-turismo-2026.html",
        "programmatic-pages/turismo-salud-bienestar-2026.html",
        "programmatic-pages/turismo-negocios-2026.html",
        "programmatic-pages/turismo-senior-2026.html",
        "programmatic-pages/turismo-spiritual-2026.html",
        "programmatic-pages/pueblos-magicos-quindio-2026.html",
        "programmatic-pages/agricultura-sostenible-2026.html",
        "programmatic-pages/artes-visuales-eje-cafetero-2026.html",
        "programmatic-pages/deportes-extremos-controlados-2026.html",
        "programmatic-pages/festivales-musica-regionales-2026.html",
        "programmatic-pages/produccion-cafe-organico-2026.html"
    ]
    
    if sitemap_path.exists():
        with open(sitemap_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Agregar nuevas páginas de blog
        for page in new_blog_pages:
            url = f"https://quindiotravel.com.co/{page}"
            if url not in content:
                entry = f"        <url>\n            <loc>{url}</loc>\n            <lastmod>2026-08-03</lastmod>\n            <changefreq>weekly</changefreq>\n            <priority>0.7</priority>\n        </url>\n"
                content = content.replace('</urlset>', f'{entry}</urlset>')
        
        # Agregar nuevas páginas programáticas
        for page in new_programmatic_pages:
            url = f"https://quindiotravel.com.co/{page}"
            if url not in content:
                entry = f"        <url>\n            <loc>{url}</loc>\n            <lastmod>2026-08-03</lastmod>\n            <changefreq>monthly</changefreq>\n            <priority>0.6</priority>\n        </url>\n"
                content = content.replace('</urlset>', f'{entry}</urlset>')
        
        with open(sitemap_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("Sitemap actualizado con nuevas páginas")
        return True
    else:
        print("Sitemap no encontrado")
        return False

if __name__ == "__main__":
    print("Actualizando sitemap...")
    print("=" * 60)
    
    if update_sitemap():
        print("Sitemap actualizado exitosamente")
        print("Total URLs nuevas: 30 (10 blog + 20 programáticas)")
    else:
        print("Error actualizando sitemap")