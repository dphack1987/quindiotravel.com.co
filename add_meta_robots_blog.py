"""
Añadir Meta Robots a Páginas de Blog
Mejora el rastreo de páginas de blog añadiendo meta robots explícitos
"""

from pathlib import Path

def add_meta_robots_to_blog():
    """Añade meta robots a páginas de blog"""
    
    blog_dir = Path(__file__).parent / "blog"
    
    # Meta robots a añadir
    meta_robots = '''    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
    <meta name="googlebot" content="index, follow">
    <meta name="bingbot" content="index, follow">
    
    '''
    
    blog_files = [
        "senderismo-rutas-seguras-eje-cafetero-2026.html",
        "gastronomia-autentica-quindio-2026.html",
        "turismo-romantico-luna-miel-2026.html",
        "turismo-accesible-discapacitados-2026.html",
        "turismo-sostenible-eco-2026.html",
        "mejores-fotos-influencers-eje-cafetero-2026.html",
        "turismo-familiar-ninos-2026.html",
        "turismo-solo-soltera-2026.html",
        "conferencias-eventos-quindio-2026.html",
        "ofertas-temporada-agosto-2026.html"
    ]
    
    modified_count = 0
    
    for filename in blog_files:
        filepath = blog_dir / filename
        if filepath.exists():
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Verificar si ya tiene meta robots
            if '<meta name="robots"' not in content:
                # Añadir después de </title>
                content = content.replace('</title>', f'</title>\n{meta_robots}')
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                modified_count += 1
                print(f"Meta robots añadido: {filename}")
            else:
                print(f"Ya tiene meta robots: {filename}")
    
    return modified_count

if __name__ == "__main__":
    print("Añadiendo meta robots a páginas de blog...")
    print("=" * 60)
    
    count = add_meta_robots_to_blog()
    
    print(f"\nTotal páginas modificadas: {count}")
    print("Meta robots añadidos para mejor rastreo")