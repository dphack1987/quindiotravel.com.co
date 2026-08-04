from pathlib import Path

def add_hero_mobile_responsive():
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Añadir media query específica para el hero en móviles
    hero_mobile_css = '''
    @media (max-width: 768px) {
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
    }
'''
    
    # Buscar la media query existente en el critical CSS y añadir después
    # Primero verificar si ya existe la media query específica para hero móvil
    if 'hero-content h1' in content and 'font-size: 1.8rem' in content:
        print("Ya existe media query específica para hero en móviles")
        return
    
    # Enfoque más directo: añadir al final de la media query existente en el critical CSS
    # Buscar la media query existente en el critical CSS
    mobile_query_start = content.find('@media (max-width:768px){')
    if mobile_query_start > 0:
        # Encontrar el cierre de esta media query
        mobile_query_end = content.find('}', mobile_query_start + 1)
        if mobile_query_end > 0:
            # Encontrar el cierre real (el primer cierre que cierra la media query)
            # Necesitamos encontrar el cierre correcto contando las llaves
            brace_count = 0
            search_start = mobile_query_start
            for i, char in enumerate(content[mobile_query_start:], mobile_query_start):
                if char == '{':
                    brace_count += 1
                elif char == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        mobile_query_end = i
                        break
            
            # Insertar antes del cierre de la media query existente
            insert_pos = mobile_query_end
            content = content[:insert_pos] + hero_mobile_css + content[insert_pos:]
            print("Media query para hero móvil añadida")
        else:
            print("No se encontró el cierre de la media query existente")
    else:
        print("No se encontró media query existente en el critical CSS")
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    add_hero_mobile_responsive()