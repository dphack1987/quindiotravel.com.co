from pathlib import Path

def remove_don_chucho_sidebar():
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Eliminar todo el CSS relacionado con Don Chucho sidebar
    don_chucho_css_pattern = r'/\* Don Chucho Sidebar \*/.*?@media \(max-width: 768px\) \{.*?\}'
    import re
    content = re.sub(don_chucho_css_pattern, '', content, flags=re.DOTALL)
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("CSS de Don Chucho sidebar eliminado")

if __name__ == "__main__":
    remove_don_chucho_sidebar()