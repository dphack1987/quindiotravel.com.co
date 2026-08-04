from pathlib import Path

def add_hero_mobile_direct():
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Enfoque más directo: añadir el CSS móvil después del closing </style> del critical CSS
    hero_mobile_css = '''
        .hero {
            min-height: 70vh;
            max-height: 500px;
            padding: 1.5rem 0;
        }
        
        .hero-content h1 {
            font-size: 1.8rem;
            margin-bottom: 0.8rem;
        }
        
        .hero-content p {
            font-size: 1rem;
            margin-bottom: 1rem;
            max-width: 90%;
        }
'''
    
    # Verificar si ya existe la media query específica para hero
    if '.hero{' in content and 'min-height: 70vh' in content:
        print("Ya existe media query específica para hero en móviles")
        return
    
    # Buscar la media query existente en el critical CSS y añadir dentro de ella
    mobile_query_start = content.find('@media (max-width:768px){')
    if mobile_query_start > 0:
        # Encontrar el cierre de esta media query
        brace_count = 0
        found_start = False
        mobile_query_end = -1
        
        for i, char in enumerate(content[mobile_query_start:], mobile_query_start):
            if char == '{':
                brace_count += 1
                found_start = True
            elif char == '}':
                brace_count -= 1
                if found_start and brace_count == 0:
                    mobile_query_end = i
                    break
        
        if mobile_query_end > 0:
            # Insertar antes del cierre de la media query existente
            insert_pos = mobile_query_end
            content = content[:insert_pos] + hero_mobile_css + content[insert_pos:]
            print("Media query para hero móvil añadida a la media query existente")
        else:
            print("No se encontró el cierre de la media query existente")
    else:
        print("No se encontró media query existente en el critical CSS")
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    add_hero_mobile_direct()