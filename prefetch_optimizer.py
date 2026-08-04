"""
Implementación de Prefetch de Recursos Críticos
Añade prefetch para páginas importantes y recursos
"""

from pathlib import Path

def add_prefetch_to_index():
    """Añade prefetch a index.html"""
    
    index_path = Path(__file__).parent / "index.html"
    
    if not index_path.exists():
        print("index.html no encontrado")
        return False
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Prefetch de páginas importantes
    prefetch_links = [
        '<link rel="prefetch" href="planes.html">',
        '<link rel="prefetch" href="blog.html">',
        '<link rel="prefetch" href="salento.html">',
        '<link rel="prefetch" href="filandia.html">',
        '<link rel="prefetch" href="styles.css">',
        '<link rel="prefetch" href="logo_quindio_travel.png">'
    ]
    
    # Buscar </head> para insertar antes
    if '</head>' in content:
        # Verificar si ya existe prefetch
        if 'rel="prefetch"' not in content:
            # Insertar prefetch links antes de </head>
            prefetch_section = '\n    '.join(prefetch_links)
            content = content.replace('</head>', f'    {prefetch_section}\n</head>')
            
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print("Prefetch añadido a index.html")
            return True
        else:
            print("Prefetch ya existe en index.html")
            return True
    else:
        print("</head> no encontrado en index.html")
        return False

def add_prefetch_to_other_pages():
    """Añade prefetch a otras páginas principales"""
    
    pages = ["planes.html", "blog.html", "salento.html", "filandia.html"]
    
    for page in pages:
        filepath = Path(__file__).parent / page
        if filepath.exists():
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Prefetch básico para cada página
            basic_prefetch = [
                '<link rel="prefetch" href="index.html">',
                '<link rel="prefetch" href="styles.css">'
            ]
            
            if '</head>' in content and 'rel="prefetch"' not in content:
                prefetch_section = '\n    '.join(basic_prefetch)
                content = content.replace('</head>', f'    {prefetch_section}\n</head>')
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"Prefetch añadido a {page}")

if __name__ == "__main__":
    print("Implementando prefetch de recursos críticos...")
    print("=" * 60)
    
    add_prefetch_to_index()
    add_prefetch_to_other_pages()
    
    print("\nPrefetch implementado en páginas principales")
    print("Impacto esperado: +10-15% velocidad de navegación")