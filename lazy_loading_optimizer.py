"""
Implementación de Lazy Loading de Imágenes
Añade loading="lazy" a imágenes below-the-fold para mejorar velocidad de carga
"""

from pathlib import Path
import re

def add_lazy_loading_to_index():
    """Añade lazy loading a imágenes en index.html"""
    
    index_path = Path(__file__).parent / "index.html"
    
    if not index_path.exists():
        print("index.html no encontrado")
        return False
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Encontrar todas las etiquetas <img>
    img_pattern = r'<img([^>]*?)(?:\s+loading="[^"]*")?([^>]*?)>'
    
    def add_lazy_loading(match):
        attrs = match.group(1) + match.group(2)
        
        # No añadir lazy loading a imágenes con ciertos patrones
        skip_patterns = [
            'logo',          # Logos deben cargar inmediatamente
            'hero',          # Imágenes hero deben cargar inmediatamente
            'above-fold',    # Imágenes above-fold
            'critical',      # Imágenes críticas
            'avatar',        # Avatares
            'favicon'        # Favicon
        ]
        
        if any(pattern in attrs.lower() for pattern in skip_patterns):
            return match.group(0)
        
        # Si ya tiene loading, no modificar
        if 'loading=' in attrs.lower():
            return match.group(0)
        
        # Añadir loading="lazy"
        if 'src=' in attrs:
            # Insertar loading="lazy" después de src
            attrs = re.sub(r'(src=["\'][^"\']*["\'])', r'\1 loading="lazy"', attrs)
            return f'<img{attrs}>'
        
        return match.group(0)
    
    # Aplicar la transformación
    content = re.sub(img_pattern, add_lazy_loading, content)
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Lazy loading añadido a imágenes de index.html")
    return True

def add_lazy_loading_to_files():
    """Añade lazy loading a otras páginas principales"""
    
    main_files = [
        "planes.html",
        "salento.html", 
        "filandia.html",
        "armenia.html"
    ]
    
    for filename in main_files:
        filepath = Path(__file__).parent / filename
        if filepath.exists():
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Aplicar la misma lógica de lazy loading
            img_pattern = r'<img([^>]*?)(?:\s+loading="[^"]*")?([^>]*?)>'
            
            def add_lazy_loading(match):
                attrs = match.group(1) + match.group(2)
                
                skip_patterns = ['logo', 'hero', 'above-fold', 'critical', 'avatar', 'favicon']
                
                if any(pattern in attrs.lower() for pattern in skip_patterns):
                    return match.group(0)
                
                if 'loading=' in attrs.lower():
                    return match.group(0)
                
                if 'src=' in attrs:
                    attrs = re.sub(r'(src=["\'][^"\']*["\'])', r'\1 loading="lazy"', attrs)
                    return f'<img{attrs}>'
                
                return match.group(0)
            
            content = re.sub(img_pattern, add_lazy_loading, content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"Lazy loading añadido a {filename}")

if __name__ == "__main__":
    print("Implementando lazy loading de imágenes...")
    print("=" * 60)
    
    add_lazy_loading_to_index()
    add_lazy_loading_to_files()
    
    print("\nLazy loading implementado en páginas principales")
    print("Impacto esperado: +20-30% velocidad de carga inicial")