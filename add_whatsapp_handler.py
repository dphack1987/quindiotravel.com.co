"""
Add WhatsApp Template Handler script to all HTML files
"""

import re
from pathlib import Path

def add_whatsapp_handler(html_content):
    """Add WhatsApp Template Handler script to HTML files"""
    
    # Check if already has the script
    if 'whatsapp-template-handler.js' in html_content:
        return html_content, False
    
    # Pattern to find stylesheets before other scripts
    pattern = r'(<link rel="stylesheet"[^>]*>)'
    matches = list(re.finditer(pattern, html_content))
    
    if not matches:
        return html_content, False
    
    # Find the last stylesheet reference
    last_stylesheet = matches[-1]
    insert_position = last_stylesheet.end()
    
    # Insert the WhatsApp Template Handler script
    script_tag = '\n    <!-- WhatsApp Template Handler -->\n    <script src="assets/js/whatsapp-template-handler.js" defer></script>'
    
    new_content = html_content[:insert_position] + script_tag + html_content[insert_position:]
    
    return new_content, True

def process_file(file_path):
    """Process individual HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content, modified = add_whatsapp_handler(content)
        
        if modified:
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
    
    print(f"Total files to check: {len(all_files)}")
    
    modified_count = 0
    for file_path in all_files:
        if process_file(file_path):
            modified_count += 1
            print(f"Updated: {file_path.name}")
    
    print(f"Completed: {modified_count} files modified")

if __name__ == "__main__":
    main()