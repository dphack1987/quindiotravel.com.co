"""
Hreflang Utils - Common functions for language detection and hreflang tags
Provides reusable functionality for multilingual SEO
"""

import re
from pathlib import Path


def add_hreflang_tags(html_content: str, file_name: str, base_domain: str = "quindiotravel.com.co") -> str:
    """
    Add hreflang tags to HTML content for multilingual SEO
    
    Args:
        html_content: HTML content to modify
        file_name: Relative file path/name
        base_domain: Base domain for URLs (default: quindiotravel.com.co)
        
    Returns:
        Modified HTML content with hreflang tags
    """
    # Generate base URL according to file location
    if '/' in file_name:
        # File in subdirectory
        base_url = f"https://{base_domain}/{file_name}"
    else:
        # File in root
        base_url = f"https://{base_domain}/{file_name}"
    
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


def add_language_detector(html_content: str, script_path: str = "assets/js/language-detector.js") -> str:
    """
    Add language detector script before </body> tag
    
    Args:
        html_content: HTML content to modify
        script_path: Path to the language detector script (default: assets/js/language-detector.js)
        
    Returns:
        Modified HTML content with language detector script
    """
    # First check if it already has the script
    if 'language-detector.js' in html_content:
        return html_content
    
    # Pattern to find </body>
    pattern = r'(</body>)'
    
    script_tag = f'''    <!-- Language Detector -->
    <script src="{script_path}" defer></script>
    
\\1'''
    
    html_content = re.sub(pattern, script_tag, html_content)
    return html_content


def has_hreflang_tags(html_content: str) -> bool:
    """
    Check if HTML content already has hreflang tags
    
    Args:
        html_content: HTML content to check
        
    Returns:
        True if hreflang tags exist, False otherwise
    """
    return bool(re.search(r'<link rel="alternate" hreflang=', html_content))


def has_language_detector(html_content: str) -> bool:
    """
    Check if HTML content already has language detector script
    
    Args:
        html_content: HTML content to check
        
    Returns:
        True if language detector script exists, False otherwise
    """
    return 'language-detector.js' in html_content


def process_file_with_hreflang(file_path: Path, base_domain: str = "quindiotravel.com.co") -> bool:
    """
    Process a single HTML file to add hreflang tags and language detector
    
    Args:
        file_path: Path to the HTML file
        base_domain: Base domain for URLs (default: quindiotravel.com.co)
        
    Returns:
        True if successful, False otherwise
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Get relative file name and normalize path separators
        relative_path = str(file_path.relative_to(Path.cwd())).replace('\\', '/')
        
        # Add hreflang tags
        content = add_hreflang_tags(content, relative_path, base_domain)
        
        # Add language detector script
        content = add_language_detector(content)
        
        # Save changes
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"Error processing {file_path.name}: {e}")
        return False