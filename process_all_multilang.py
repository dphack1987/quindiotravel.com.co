"""
Process all files for multilanguage configuration - simplified version
"""

import re
from pathlib import Path

def add_hreflang_tags(html_content, file_name):
    """Add hreflang tags to HTML"""
    
    # Generate base URL according to file location
    if '/' in file_name:
        base_url = f"https://quindiotravel.com.co/{file_name}"
    else:
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
        return False

def main():
    base_dir = Path.cwd()
    
    # Collect all files to process
    all_files = []
    
    # Blog files
    blog_dir = base_dir / 'blog'
    if blog_dir.exists():
        all_files.extend(blog_dir.glob('*.html'))
    
    # Programmatic files
    prog_dir = base_dir / 'programmatic-pages'
    if prog_dir.exists():
        all_files.extend(prog_dir.glob('*.html'))
    
    # Hotel files
    hotel_files = ['hotel-campestre-cafe-cafe.html', 'hotel-campestre-la-tata.html', 
                   'hotel-campestre-las-camelias.html', 'hotel-de-la-vega.html']
    for hotel in hotel_files:
        hotel_path = base_dir / hotel
        if hotel_path.exists():
            all_files.append(hotel_path)
    
    print(f"Total files to process: {len(all_files)}")
    
    success_count = 0
    fail_count = 0
    
    for i, file_path in enumerate(all_files, 1):
        if i % 10 == 0:
            print(f"Progress: {i}/{len(all_files)} processed")
        
        if process_file(file_path):
            success_count += 1
        else:
            fail_count += 1
    
    print(f"Completed: {success_count} successful, {fail_count} failed")

if __name__ == "__main__":
    main()