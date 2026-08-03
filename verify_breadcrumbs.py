"""
Script para verificar la visualización y estructura de breadcrumbs
"""

import re
from pathlib import Path

def verify_breadcrumb_structure(file_path):
    """
    Verifica la estructura de breadcrumbs en un archivo HTML
    
    Args:
        file_path: Ruta del archivo HTML
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Buscar breadcrumb-nav
    breadcrumb_pattern = r'<nav class="breadcrumb-nav"[^>]*>(.*?)</nav>'
    breadcrumb_match = re.search(breadcrumb_pattern, content, re.DOTALL)
    
    if not breadcrumb_match:
        return {
            'file': file_path.name,
            'has_breadcrumb': False,
            'placement': 'none',
            'schema': False
        }
    
    breadcrumb_content = breadcrumb_match.group(1)
    
    # Verificar si tiene Schema.org
    has_schema = 'itemscope itemtype="https://schema.org/BreadcrumbList"' in breadcrumb_content
    
    # Verificar posición (antes de header, entre header y hero, después de hero)
    header_pos = content.find('<header')
    hero_pos = content.find('class="hotel-hero"')
    breadcrumb_pos = breadcrumb_match.start()
    
    placement = 'unknown'
    if header_pos < breadcrumb_pos < hero_pos:
        placement = 'correct'  # Entre header y hero
    elif breadcrumb_pos < header_pos:
        placement = 'before_header'
    elif breadcrumb_pos > hero_pos:
        placement = 'after_hero'
    
    # Verificar estructura interna
    has_ol = '<ol class="breadcrumb"' in breadcrumb_content
    has_li = '<li' in breadcrumb_content
    has_links = '<a href=' in breadcrumb_content
    
    return {
        'file': file_path.name,
        'has_breadcrumb': True,
        'placement': placement,
        'schema': has_schema,
        'has_ol': has_ol,
        'has_li': has_li,
        'has_links': has_links
    }

def main():
    """Función principal"""
    base_dir = Path(__file__).parent
    
    print("Verificacion de visualizacion de breadcrumbs")
    print("=" * 60)
    
    # Verificar archivos principales de hoteles
    hotel_files = [
        "hotel-campestre-cafe-cafe.html",
        "finca-hotel-la-dorada.html",
        "cabanas-la-esmeralda.html",
        "finca-hotel-los-girasoles.html",
        "hotel-campestre-la-tata.html",
        "hotel-campestre-las-camelias.html",
        "hotel-de-la-vega.html"
    ]
    
    print("\nArchivos de hoteles principales:")
    hotel_results = []
    for hotel_file in hotel_files:
        file_path = base_dir / hotel_file
        if file_path.exists():
            result = verify_breadcrumb_structure(file_path)
            hotel_results.append(result)
            
            status = "OK" if result['has_breadcrumb'] and result['placement'] == 'correct' else "ERROR"
            print(f"  {status} {result['file']}: {result['placement']}, Schema: {result['schema']}")
    
    # Verificar archivos generated-pages
    generated_dir = base_dir / "generated-pages" / "alojamiento"
    if generated_dir.exists():
        print("\nArchivos generated-pages:")
        generated_files = list(generated_dir.glob('*.html'))
        
        for gen_file in generated_files[:3]:  # Solo verificar los primeros 3
            result = verify_breadcrumb_structure(gen_file)
            
            status = "OK" if result['has_breadcrumb'] and result['placement'] == 'correct' else "ERROR"
            print(f"  {status} {result['file']}: {result['placement']}, Schema: {result['schema']}")
    
    # Resumen
    print("\n" + "=" * 60)
    print("RESUMEN")
    print("=" * 60)
    
    correct_placement = sum(1 for r in hotel_results if r['placement'] == 'correct')
    with_schema = sum(1 for r in hotel_results if r['schema'])
    
    print(f"Hoteles con breadcrumbs: {len(hotel_results)}/7")
    print(f"Colocacion correcta: {correct_placement}/7")
    print(f"Con Schema.org: {with_schema}/7")
    
    if correct_placement == len(hotel_results) and with_schema == len(hotel_results):
        print("\nTodos los breadcrumbs estan correctamente colocados y con Schema")
    else:
        print("\nAlgunos breadcrumbs necesitan correccion")

if __name__ == "__main__":
    main()