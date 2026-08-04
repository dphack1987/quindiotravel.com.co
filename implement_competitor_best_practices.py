"""
Implementar Mejores Prácticas de Competidores
Aplica storytelling, categorización, autenticidad y sostenibilidad
"""

from pathlib import Path

def implement_storytelling_hero():
    """Mejora storytelling en hero section"""
    
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Mejorar hero content con storytelling emocional
    old_hero_content = '''<div class="hero-content">
                <h1>Guía de turismo en el Eje Cafetero y Quindío</h1>
                <p>Parques, Valle de Cocora, cafés, termales y hoteles campestres en un plan guiado con transporte, alojamiento y soporte local desde el primer mensaje.</p>'''
    
    new_hero_content = '''<div class="hero-content">
                <h1>Conectamos tu corazón con el Eje Cafetero: Experiencias auténticas que quedarán en tu memoria</h1>
                <p>No somos solo una guía de viajes; somos narradores de la cultura cafetera. Conectamos tu corazón con el Eje Cafetero a través de experiencias auténticas, grupos pequeños y conexiones reales con la tierra del mejor café del mundo.</p>'''
    
    if old_hero_content in content:
        content = content.replace(old_hero_content, new_hero_content)
        print("[OK] Hero storytelling mejorado con narrativa emocional")
    
    # Guardar cambios
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def add_authenticity_badges():
    """Añade badges de autenticidad y grupos pequeños"""
    
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Añadir badges de autenticidad después de hero highlights
    old_highlights = '''<div class="hero-highlights">
                <div class="hero-highlight-card"><i class="fas fa-route"></i><span>Planes todo incluido</span></div>
                <div class="hero-highlight-card"><i class="fas fa-hotel"></i><span>Hoteles y cabañas</span></div>
                <div class="hero-highlight-card"><i class="fas fa-users"></i><span>Grupos pequeños</span></div>
                <div class="hero-highlight-card"><i class="fas fa-leaf"></i><span>Turismo sostenible</span></div>
            </div>'''
    
    new_highlights = '''<div class="hero-highlights">
                <div class="hero-highlight-card"><i class="fas fa-route"></i><span>Planes todo incluido</span></div>
                <div class="hero-highlight-card"><i class="fas fa-hotel"></i><span>Hoteles y cabañas</span></div>
                <div class="hero-highlight-card"><i class="fas fa-users"></i><span>Grupos pequeños - Máximo 8 personas</span></div>
                <div class="hero-highlight-card"><i class="fas fa-leaf"></i><span>Turismo sostenible</span></div>
                <div class="hero-highlight-card"><i class="fas fa-heart"></i><span>Experiencias auténticas</span></div>
                <div class="hero-highlight-card"><i class="fas fa-certificate"></i><span>Operador certificado RNT 18152</span></div>
            </div>'''
    
    if old_highlights in content:
        content = content.replace(old_highlights, new_highlights)
        print("[OK] Badges de autenticidad añadidos a hero highlights")
    
    # Guardar cambios
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def add_sustainability_section():
    """Añade sección de sostenibilidad"""
    
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Buscar el footer para añadir sección antes
    footer_start = '<footer'
    
    sustainability_section = '''
    <!-- Sostenibilidad Turística -->
    <section class="sustainability-section" id="sostenibilidad" aria-label="Turismo Responsable y Sostenible">
        <div class="container">
            <div class="sustainability-content">
                <div class="sustainability-text">
                    <h2 class="sustainability-title">Turismo Responsable y Sostenible en el Eje Cafetero</h2>
                    <p class="sustainability-description">En Quindío Travel estamos comprometidos con el turismo responsable que genera beneficios sociales, ambientales, culturales y económicos para el medio ambiente. Cada experiencia está diseñada para respetar la cultura cafetera, proteger el medio ambiente y apoyar a las comunidades locales.</p>
                    
                    <div class="sustainability-values">
                        <div class="sustainability-value">
                            <i class="fas fa-recycle"></i>
                            <h3>Compromiso Ambiental</h3>
                            <p>Reducimos nuestro impacto ambiental con prácticas sostenibles y eco-amigables.</p>
                        </div>
                        <div class="sustainability-value">
                            <i class="fas fa-hands-helping"></i>
                            <h3>Apoyo a Comunidades</h3>
                            <p>Trabajamos directamente con guías locales, fincas cafeteras y hoteles familiares.</p>
                        </div>
                        <div class="sustainability-value">
                            <i class="fas fa-landmark"></i>
                            <h3>Preservación Cultural</h3>
                            <p>Promovemos y preservamos la cultura cafetera y tradiciones del Eje Cafetero.</p>
                        </div>
                    </div>
                </div>
                <div class="sustainability-image">
                    <div class="sustainability-img-wrapper" style="background-image: url('assets/images/paisajes/sostenibilidad.jpg');" alt="Turismo sostenible en el Eje Cafetero con prácticas responsables">
                        <div class="sustainability-overlay"></div>
                        <div class="sustainability-badge">
                            <i class="fas fa-leaf"></i>
                            <span>Turismo Sostenible</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
'''
    
    if footer_start in content:
        content = content.replace(footer_start, sustainability_section + '\n' + footer_start)
        print("[OK] Sección de sostenibilidad añadida antes del footer")
    
    # Guardar cambios
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def add_values_section():
    """Añade sección de valores y propuesta de valor"""
    
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Buscar la sección about para añadir valores después
    about_section_end = '</section>'
    
    # Buscar específicamente el final de la sección about
    about_pattern = '<section class="about"'
    
    if about_pattern in content:
        # Encontrar el cierre de la sección about
        about_start = content.find(about_pattern)
        section_count = 1
        current_pos = about_start + len(about_pattern)
        
        while section_count > 0 and current_pos < len(content):
            if content[current_pos:current_pos + 9] == '<section':
                section_count += 1
            elif content[current_pos:current_pos + 10] == '</section':
                section_count -= 1
                if section_count == 0:
                    # Añadir sección de valores después de esta sección
                    values_section = '''
    <!-- Valores y Propuesta de Valor -->
    <section class="values-section" id="valores" aria-label="Nuestros Valores y Propuesta de Valor">
        <div class="container">
            <div class="values-header">
                <h2 class="values-title">Nuestros Valores y Propuesta de Valor</h2>
                <p class="values-subtitle">Tenemos los Mejores Planes Turísticos en el Eje Cafetero porque creemos en conectar al visitante con el destino de manera auténtica y responsable.</p>
            </div>
            
            <div class="values-grid">
                <div class="value-card">
                    <div class="value-icon"><i class="fas fa-certificate"></i></div>
                    <h3 class="value-title">Experiencia Certificada</h3>
                    <p class="value-description">Operador turístico autorizado RNT 18152 con más de 10 años de experiencia en el Eje Cafetero.</p>
                </div>
                <div class="value-card">
                    <div class="value-icon"><i class="fas fa-user-check"></i></div>
                    <h3 class="value-title">Guías Certificados</h3>
                    <p class="value-description">Equipo profesional local certificado con profundo conocimiento de la cultura cafetera.</p>
                </div>
                <div class="value-card">
                    <div class="value-icon"><i class="fas fa-handshake"></i></div>
                    <h3 class="value-title">Red de Aliados</h3>
                    <p class="value-description">Mejores hoteles, fincas cafeteras y operadores locales del Eje Cafetero.</p>
                </div>
                <div class="value-card">
                    <div class="value-icon"><i class="fas fa-users"></i></div>
                    <h3 class="value-title">Grupos Pequeños</h3>
                    <p class="value-description">Grupos de máximo 8 personas para experiencias personalizadas y auténticas.</p>
                </div>
                <div class="value-card">
                    <div class="value-icon"><i class="fas fa-heart"></i></div>
                    <h3 class="value-title">Servicio Personalizado</h3>
                    <p class="value-description">Atención individual desde el primer mensaje hasta el final de tu experiencia.</p>
                </div>
                <div class="value-card">
                    <div class="value-icon"><i class="fas fa-shield-alt"></i></div>
                    <h3 class="value-title">Servicio Garantizado</h3>
                    <p class="value-description">Seguridad, confianza y satisfacción garantizada en cada experiencia.</p>
                </div>
            </div>
        </div>
    </section>
'''
                    content = content[:current_pos + 10] + values_section + content[current_pos + 10:]
                    print("[OK] Sección de valores añadida después de sección about")
                    break
            current_pos += 1
    
    # Guardar cambios
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

if __name__ == "__main__":
    print("Implementando mejores prácticas de competidores...")
    print("=" * 70)
    
    implement_storytelling_hero()
    add_authenticity_badges()
    add_sustainability_section()
    add_values_section()
    
    print("\n" + "=" * 70)
    print("Mejores prácticas de competidores implementadas exitosamente")