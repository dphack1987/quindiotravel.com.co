"""
Process remaining blog files that weren't processed
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
    """Add language detector script before </body>"""
    
    # First check if it already has the script
    if 'language-detector.js' in html_content:
        return html_content
    
    # Pattern to find </body>
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
        print(f"Error processing {file_path.name}: {e}")
        return False

def main():
    base_dir = Path.cwd()
    blog_dir = base_dir / 'blog'
    
    if not blog_dir.exists():
        print("Blog directory not found")
        return
    
    # Get all blog files
    all_files = sorted(list(blog_dir.glob('*.html')))
    print(f"Found {len(all_files)} blog files")
    
    # Files already processed (first 11)
    processed_files = {
        'conferencias-eventos-quindio-2026.html',
        'diferencias-salento-filandia-destino-2026.html',
        'experiencias-cafeteras-autenticas-quindio-2026.html',
        'festividades-temporada-quindio-2026.html',
        'festividades-tradicionales-quindio-2026.html',
        'gastronomia-autentica-quindio-2026.html',
        'guia-compras-salento-2026.html',
        'guia-fotografia-eje-cafetero-2026.html',
        'guia-transporte-eje-cafetero-bogota-2026.html',
        'hoteles-economicos-salento-familias-2026.html',
        'mejor-epoca-visitar-quindio-2026.html'
    }
    
    # Get remaining files
    remaining_files = [f for f in all_files if f.name not in processed_files]
    print(f"Remaining files to process: {len(remaining_files)}")
    
    success_count = 0
    fail_count = 0
    
    for i, html_file in enumerate(remaining_files, 1):
        print(f"[{i}/{len(remaining_files)}] Processing {html_file.name}...")
        if process_file(html_file):
            success_count += 1
            print(f"  OK")
        else:
            fail_count += 1
            print(f"  FAIL")
    
    print(f"\nCompleted: {success_count} successful, {fail_count} failed out of {len(remaining_files)} total")

if __name__ == "__main__":
    main()