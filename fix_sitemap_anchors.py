"""
Corrección de URLs con Anchors en Sitemap
Elimina index.html#hoteles del sitemap para mejorar rastreo
"""

from pathlib import Path

def fix_sitemap_anchors():
    """Elimina URLs con anchors del sitemap"""
    
    sitemap_path = Path(__file__).parent / "sitemap.xml"
    
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Reemplazar URL con anchor
    old_url = 'https://quindiotravel.com.co/index.html#hoteles'
    new_url = 'https://quindiotravel.com.co/index.html'
    
    if old_url in content:
        content = content.replace(old_url, new_url)
        
        with open(sitemap_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("URL con anchor eliminada del sitemap")
        return True
    else:
        print("URL con anchor no encontrada o ya corregida")
        return False

if __name__ == "__main__":
    print("Corrigiendo URLs con anchors en sitemap...")
    print("=" * 60)
    
    fix_sitemap_anchors()
    
    print("\nSitemap corregido para mejor rastreo")