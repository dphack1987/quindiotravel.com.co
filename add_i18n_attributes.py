"""
Add data-i18n attributes to main pages
"""

import re
from pathlib import Path

def add_i18n_to_navigation(html_content):
    """Add data-i18n attributes to navigation links"""
    
    # Navigation links mapping
    nav_mappings = {
        r'(<a href="index\.html">)(Inicio)(</a>)': r'\1\2 data-i18n="nav.inicio"\3',
        r'(<a href="planes\.html">)(Planes)(</a>)': r'\1\2 data-i18n="nav.planes"\3',
        r'(<a href="index\.html#hoteles">)(Hoteles)(</a>)': r'\1\2 data-i18n="nav.hoteles"\3',
        r'(<a href="index\.html#experiencias">)(Experiencias)(</a>)': r'\1\2 data-i18n="nav.experiencias"\3',
        r'(<a href="index\.html#destinos">)(Destinos)(</a>)': r'\1\2 data-i18n="nav.destinos"\3',
        r'(<a href="index\.html#contacto">)(Contacto)(</a>)': r'\1\2 data-i18n="nav.contacto"\3',
        r'(<a href="blog\.html">)(Blog)(</a>)': r'\1\2 data-i18n="nav.blog"\3',
    }
    
    for pattern, replacement in nav_mappings.items():
        html_content = re.sub(pattern, replacement, html_content)
    
    return html_content

def add_i18n_to_breadcrumb(html_content):
    """Add data-i18n attributes to breadcrumb"""
    
    breadcrumb_mappings = {
        r'(<span itemprop="name">)(Inicio)(</span>)': r'\1\2 data-i18n="breadcrumb.home"\3',
        r'(<span itemprop="name">)(Hoteles)(</span>)': r'\1\2 data-i18n="breadcrumb.hotels"\3',
    }
    
    for pattern, replacement in breadcrumb_mappings.items():
        html_content = re.sub(pattern, replacement, html_content)
    
    return html_content

def process_file(file_path):
    """Process individual HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add i18n attributes
        content = add_i18n_to_navigation(content)
        content = add_i18n_to_breadcrumb(content)
        
        # Save changes
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"Error processing {file_path.name}: {e}")
        return False

def main():
    base_dir = Path.cwd()
    
    # Main pages to process
    main_pages = [
        'valle-de-cocora.html',
        'parque-del-cafe.html',
        'blog.html',
        'blog-mejor-epoca-eje-cafetero.html',
        'promo-agosto-2026.html',
        'cabanas-la-esmeralda.html',
        'hotel-campestre-cafe-cafe.html',
        'hotel-campestre-la-tata.html',
        'hotel-campestre-las-camelias.html',
        'hotel-de-la-vega.html'
    ]
    
    print("Adding data-i18n attributes to main pages...")
    
    success_count = 0
    for page in main_pages:
        page_path = base_dir / page
        if page_path.exists():
            if process_file(page_path):
                success_count += 1
                print(f"OK: {page}")
            else:
                print(f"FAIL: {page}")
    
    print(f"Completed: {success_count} successful")

if __name__ == "__main__":
    main()