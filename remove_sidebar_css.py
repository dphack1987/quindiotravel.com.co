from pathlib import Path

def remove_sidebar_css():
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Eliminar CSS de sidebar
    sidebar_css_pattern = r'/\* Don Chucho Sidebar \*/.*?@media \(max-width: 768px\) \{.*?\}'
    import re
    content = re.sub(sidebar_css_pattern, '', content, flags=re.DOTALL)
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("CSS de sidebar eliminado")

if __name__ == "__main__":
    remove_sidebar_css()