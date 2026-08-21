"""
Remove duplicate hreflang tags from files
"""

import re
from pathlib import Path

def remove_duplicate_hreflang(html_content):
    """Remove duplicate hreflang tags"""
    
    # Find all hreflang link blocks
    pattern = r'<!-- Alternate Language -->[\s\S]*?(?=</head>|<meta|<link[^>]*/>)'
    matches = re.findall(pattern, html_content)
    
    if len(matches) <= 1:
        return html_content
    
    # Keep only the first occurrence
    first_match = matches[0]
    
    # Remove all hreflang blocks
    for match in matches:
        html_content = html_content.replace(match, '')
    
    # Insert the first one back after charset meta tag
    charset_pattern = r'(<meta charset="UTF-8">)'
    if re.search(charset_pattern, html_content):
        html_content = re.sub(charset_pattern, r'\1' + first_match, html_content)
    
    return html_content

def process_file(file_path):
    """Process individual HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove duplicates
        new_content = remove_duplicate_hreflang(content)
        
        # Only save if content changed
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path.name}: {e}")
        return False

def main():
    base_dir = Path.cwd()
    
    # Process all HTML files
    all_files = []
    
    # Blog files
    blog_dir = base_dir / 'blog'
    if blog_dir.exists():
        all_files.extend(blog_dir.glob('*.html'))
    
    # Programmatic files
    prog_dir = base_dir / 'programmatic-pages'
    if prog_dir.exists():
        all_files.extend(prog_dir.glob('*.html'))
    
    # Main files
    main_files = ['valle-de-cocora.html', 'parque-del-cafe.html', 'blog.html', 
                  'blog-mejor-epoca-eje-cafetero.html', 'promo-agosto-2026.html', 
                  'cabanas-la-esmeralda.html', 'hotel-campestre-cafe-cafe.html', 
                  'hotel-campestre-la-tata.html', 'hotel-campestre-las-camelias.html', 
                  'hotel-de-la-vega.html']
    for main_file in main_files:
        main_path = base_dir / main_file
        if main_path.exists():
            all_files.append(main_path)
    
    print(f"Total files to check: {len(all_files)}")
    
    modified_count = 0
    for file_path in all_files:
        if process_file(file_path):
            modified_count += 1
            print(f"Cleaned: {file_path.name}")
    
    print(f"Completed: {modified_count} files modified")

if __name__ == "__main__":
    main()