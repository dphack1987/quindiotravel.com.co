"""
Script para agregar configuración multilenguaje a todas las páginas
"""

import re
from pathlib import Path

def add_hreflang_tags(html_content, file_name):
    """Add hreflang tags to HTML"""
    
    # Generate base URL according to file location
    if '/' in file_name:
        # File in subdirectory
        base_url = f"https://quindiotravel.com.co/{file_name}"
    else:
        # File in root
        base_url = f"https://quindiotravel.com.co/{file_name}"
    
    hreflang_tags = f'''

    <!-- Alternate Language -->
    <link rel="alternate" hreflang="es" href="{base_url}">
    <link rel="alternate" hreflang="es-CO" href="{base_url}">
    <link rel="alternate" hreflang="en" href="{base_url}?lang=en">
    <link rel="alternate" hreflang="pt" href="{base_url}?lang=pt">
    <link rel="alternate" hreflang="fr" href="{base_url}?lang=fr">
    <link rel="alternate" hreflang="x-default" href="{base_url}">'''
    
    # Try to find og:site_name pattern first
    pattern = r'(<meta property="og:site_name" content="Quindío Travel">)'
    if re.search(pattern, html_content):
        html_content = re.sub(pattern, r'\1' + hreflang_tags, html_content)
    else:
        # If og:site_name not found, try to insert after other meta tags
        # Look for charset or viewport meta tags
        charset_pattern = r'(<meta charset="UTF-8">)'
        if re.search(charset_pattern, html_content):
            html_content = re.sub(charset_pattern, r'\1' + hreflang_tags, html_content)
        else:
            # Last resort: insert after title tag
            title_pattern = r'(</title>)'
            if re.search(title_pattern, html_content):
                html_content = re.sub(title_pattern, r'\1' + hreflang_tags, html_content)
    
    return html_content

def add_language_detector(html_content):
    """Agrega el script de language-detector antes de </body>"""
    
    # Primero verificar si ya tiene el script
    if 'language-detector.js' in html_content:
        return html_content
    
    # Patrón para encontrar </body>
    pattern = r'(</body>)'
    
    script_tag = r'''    <!-- Language Detector -->
    <script src="assets/js/language-detector.js" defer></script>
    
\1'''
    
    html_content = re.sub(pattern, script_tag, html_content)
    return html_content

def process_file(file_path):
    """Process individual HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Get relative file name and normalize path separators
        relative_path = str(file_path.relative_to(Path.cwd())).replace('\\', '/')
        
        # Add hreflang tags
        content = add_hreflang_tags(content, relative_path)
        
        # Add language detector script
        content = add_language_detector(content)
        
        # Save changes
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    base_dir = Path.cwd()
    
    print("Adding multilanguage configuration to all pages...")
    print("=" * 60)
    
    success_count = 0
    fail_count = 0
    
    # Process main pages in root
    print("\nProcessing main pages:")
    main_pages = ['valle-de-cocora.html', 'parque-del-cafe.html', 
                  'blog.html', 'blog-mejor-epoca-eje-cafetero.html',
                  'promo-agosto-2026.html', 'cabanas-la-esmeralda.html']
    
    for page in main_pages:
        page_path = base_dir / page
        if page_path.exists():
            if process_file(page_path):
                success_count += 1
                print(f"OK: {page}")
            else:
                fail_count += 1
                print(f"FAIL: {page}")
    
    # Process blog pages
    print("\nProcessing blog pages:")
    blog_dir = base_dir / 'blog'
    if blog_dir.exists():
        blog_files = list(blog_dir.glob('*.html'))
        print(f"Found {len(blog_files)} blog files")
        for html_file in blog_files:
            if process_file(html_file):
                success_count += 1
                print(f"OK: {html_file.name}")
            else:
                fail_count += 1
                print(f"FAIL: {html_file.name}")
    
    # Process programmatic pages
    print("\nProcessing programmatic pages:")
    programmatic_dir = base_dir / 'programmatic-pages'
    if programmatic_dir.exists():
        programmatic_files = list(programmatic_dir.glob('*.html'))
        print(f"Found {len(programmatic_files)} programmatic files")
        for html_file in programmatic_files:
            if process_file(html_file):
                success_count += 1
                print(f"OK: {html_file.name}")
            else:
                fail_count += 1
                print(f"FAIL: {html_file.name}")
    
    # Process hotel pages
    print("\nProcessing hotel pages:")
    hotel_pages = ['hotel-campestre-cafe-cafe.html', 'hotel-campestre-la-tata.html', 
                   'hotel-campestre-las-camelias.html', 'hotel-de-la-vega.html']
    for page in hotel_pages:
        page_path = base_dir / page
        if page_path.exists():
            if process_file(page_path):
                success_count += 1
                print(f"OK: {page}")
            else:
                fail_count += 1
                print(f"FAIL: {page}")
    
    print("\n" + "=" * 60)
    print(f"Completed: {success_count} successful, {fail_count} failed")

if __name__ == "__main__":
    main()