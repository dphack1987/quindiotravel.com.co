"""
Process blog files in smaller batches
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
    
    # Process in batches of 5 files
    all_files = sorted(list(blog_dir.glob('*.html')))
    print(f"Found {len(all_files)} blog files")
    
    batch_size = 5
    success_count = 0
    fail_count = 0
    
    for batch_num in range(0, len(all_files), batch_size):
        batch = all_files[batch_num:batch_num + batch_size]
        print(f"\nProcessing batch {batch_num//batch_size + 1}: files {batch_num+1}-{min(batch_num+batch_size, len(all_files))}")
        
        for html_file in batch:
            print(f"  Processing {html_file.name}...")
            if process_file(html_file):
                success_count += 1
                print(f"    OK")
            else:
                fail_count += 1
                print(f"    FAIL")
    
    print(f"\nCompleted: {success_count} successful, {fail_count} failed out of {len(all_files)} total")

if __name__ == "__main__":
    main()