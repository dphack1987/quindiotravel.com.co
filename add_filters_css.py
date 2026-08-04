"""
Añadir CSS para Filtros Avanzados
Estilos modernos inspirados en Booking.com
"""

from pathlib import Path

def add_filters_css():
    """Añade CSS para la sección de filtros"""
    
    planes_path = Path(__file__).parent / "planes.html"
    
    with open(planes_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Buscar </style> para añadir CSS antes
    style_end = '</style>'
    
    filters_css = '''
    
    /* Advanced Filters Section Styles */
    .filters-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 0;
        margin: 2rem 0;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .filters-header {
        text-align: center;
        margin-bottom: 2rem;
        color: white;
    }
    
    .filters-title {
        font-size: 2rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    
    .filters-subtitle {
        font-size: 1.1rem;
        opacity: 0.9;
    }
    
    .filters-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 1rem;
        margin-bottom: 1.5rem;
    }
    
    .filter-group {
        display: flex;
        flex-direction: column;
    }
    
    .filter-label {
        color: white;
        font-weight: 600;
        margin-bottom: 0.5rem;
        font-size: 0.9rem;
    }
    
    .filter-select {
        padding: 0.75rem;
        border-radius: 10px;
        border: none;
        background: rgba(255,255,255,0.2);
        backdrop-filter: blur(10px);
        color: white;
        font-size: 0.9rem;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .filter-select:hover {
        background: rgba(255,255,255,0.3);
        transform: translateY(-2px);
    }
    
    .filter-select option {
        background: #667eea;
        color: white;
    }
    
    .filter-reset {
        padding: 0.75rem;
        border-radius: 10px;
        border: 2px solid rgba(255,255,255,0.3);
        background: rgba(255,255,255,0.1);
        color: white;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
    }
    
    .filter-reset:hover {
        background: rgba(255,255,255,0.2);
        transform: translateY(-2px);
    }
    
    .filters-results {
        text-align: center;
        color: white;
        font-size: 1rem;
        padding: 1rem;
        background: rgba(255,255,255,0.1);
        border-radius: 10px;
        backdrop-filter: blur(10px);
    }
    
    .results-label {
        opacity: 0.8;
        margin-left: 0.5rem;
    }
    
    @media (max-width: 768px) {
        .filters-container {
            grid-template-columns: 1fr;
        }
        
        .filters-title {
            font-size: 1.5rem;
        }
    }
'''
    
    if style_end in content:
        content = content.replace(style_end, filters_css + '\n' + style_end)
        print("[OK] CSS para filtros avanzados añadido")
    
    # Guardar cambios
    with open(planes_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

if __name__ == "__main__":
    print("Añadiendo CSS para filtros avanzados...")
    print("=" * 70)
    
    add_filters_css()
    
    print("\n" + "=" * 70)
    print("CSS para filtros añadido exitosamente")