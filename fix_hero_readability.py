from pathlib import Path

def fix_hero_readability():
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Buscar y corregir el CSS del hero para mejorar legibilidad
    hero_css_fix = '''
    .hero {
        position: relative;
        overflow: hidden;
        min-height: 80vh;
        max-height: 600px;
        display: flex;
        align-items: center;
        text-align: center;
        color: var(--blanco);
        padding: 2rem 0;
    }
    
    .hero-bg-img {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
    }
    
    .hero-overlay {
        position: absolute;
        inset: 0;
        background: rgba(0,0,0,0.5);
    }
    
    .hero-content {
        position: relative;
        z-index: 2;
        max-width: 900px;
        margin: 0 auto;
        padding: 0 20px;
    }
    
    .hero-content h1 {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.6);
        line-height: 1.3;
        font-weight: 700;
    }
    
    .hero-content p {
        font-size: 1.2rem;
        margin-bottom: 1.5rem;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.5);
        line-height: 1.5;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
    }
    
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
    
    # Enfoque más simple: buscar y reemplazar el CSS directamente
    # Buscar y corregir el CSS existente del hero
    old_hero_css = '.hero{position:relative;overflow:hidden;min-height:72vh;display:flex;align-items:center;text-align:center;color:var(--blanco)}'
    new_hero_css = '.hero{position:relative;overflow:hidden;min-height:80vh;max-height:600px;display:flex;align-items:center;text-align:center;color:var(--blanco);padding:2rem 0}'
    content = content.replace(old_hero_css, new_hero_css)
    
    # Buscar y corregir el CSS de hero-content
    old_hero_content_css = '.hero-content{position:relative;z-index:2}'
    new_hero_content_css = '.hero-content{position:relative;z-index:2;max-width:900px;margin:0 auto;padding:0 20px}'
    content = content.replace(old_hero_content_css, new_hero_content_css)
    
    # Buscar y corregir el CSS de hero-content h1
    old_hero_h1_css = '.hero-content h1{font-size:2.8rem;margin-bottom:15px;text-shadow:2px 2px 4px rgba(0,0,0,0.6)}'
    new_hero_h1_css = '.hero-content h1{font-size:2.5rem;margin-bottom:1rem;text-shadow:2px 2px 4px rgba(0,0,0,0.6);line-height:1.3;font-weight:700}'
    content = content.replace(old_hero_h1_css, new_hero_h1_css)
    
    # Añadir CSS para hero-content p si no existe
    if '.hero-content p{' not in content:
        # Insertar después de hero-content h1
        hero_h1_idx = content.find('.hero-content h1{')
        if hero_h1_idx > 0:
            # Encontrar el cierre de la regla
            end_idx = content.find('}', hero_h1_idx) + 1
            hero_p_css = '.hero-content p{font-size:1.2rem;margin-bottom:1.5rem;text-shadow:1px 1px 3px rgba(0,0,0,0.5);line-height:1.5;max-width:700px;margin-left:auto;margin-right:auto}'
            content = content[:end_idx] + hero_p_css + content[end_idx:]
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("CSS de hero corregido para mejor legibilidad")

if __name__ == "__main__":
    fix_hero_readability()