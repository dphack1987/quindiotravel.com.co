from pathlib import Path

def add_don_chucho_sidebar_css():
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Añadir CSS para el sidebar de Don Chucho
    sidebar_css = '''
    
    /* Don Chucho Sidebar */
    .don-chucho-sidebar {
        position: fixed;
        left: 20px;
        top: 50%;
        transform: translateY(-50%);
        z-index: 999;
        background: white;
        border-radius: 50%;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        padding: 5px;
        transition: all 0.3s ease;
    }
    
    .don-chucho-sidebar:hover {
        transform: translateY(-50%) scale(1.1);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    
    .don-chucho-small-avatar {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        object-fit: cover;
        display: block;
    }
    
    @media (max-width: 768px) {
        .don-chucho-sidebar {
            left: 10px;
        }
        
        .don-chucho-small-avatar {
            width: 40px;
            height: 40px;
        }
    }
'''
    
    # Buscar </style> para añadir CSS
    style_end = '</style>'
    if style_end in content:
        content = content.replace(style_end, sidebar_css + '\n' + style_end)
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("CSS para sidebar Don Chucho añadido")

if __name__ == "__main__":
    add_don_chucho_sidebar_css()