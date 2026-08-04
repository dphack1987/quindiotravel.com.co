from pathlib import Path

def add_multilanguage_support():
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Añadir selector de idioma en el header
    language_selector = '''
    <div class="language-selector">
        <button class="lang-btn active" data-lang="es" onclick="changeLanguage('es')">ES</button>
        <button class="lang-btn" data-lang="en" onclick="changeLanguage('en')">EN</button>
    </div>
'''
    
    # Buscar el nav para añadir selector
    nav_pattern = '<nav class="main-nav"'
    if nav_pattern in content:
        content = content.replace(nav_pattern, language_selector + '\n' + nav_pattern)
    
    # Añadir JavaScript para multilenguaje
    multilang_js = '''
    <script>
    const translations = {
        es: {
            'hero_title': 'Conectamos tu corazón con el Eje Cafetero: Experiencias auténticas que quedarán en tu memoria',
            'hero_subtitle': 'No somos solo una guía de viajes; somos narradores de la cultura cafetera',
            'plans_title': 'Planes turísticos en el Quindío (Eje Cafetero)',
            'contact_title': 'Contáctenos',
            'about_title': 'Nosotros'
        },
        en: {
            'hero_title': 'Connect your heart with the Coffee Region: Authentic experiences that will stay in your memory',
            'hero_subtitle': 'We are not just a travel guide; we are storytellers of coffee culture',
            'plans_title': 'Tourism Plans in Quindío (Coffee Region)',
            'contact_title': 'Contact Us',
            'about_title': 'About Us'
        }
    };
    
    let currentLang = 'es';
    
    function changeLanguage(lang) {
        currentLang = lang;
        
        // Actualizar botones
        document.querySelectorAll('.lang-btn').forEach(btn => {
            btn.classList.remove('active');
            if (btn.dataset.lang === lang) {
                btn.classList.add('active');
            }
        });
        
        // Actualizar textos
        const texts = translations[lang];
        for (const [key, value] of Object.entries(texts)) {
            const element = document.querySelector(`[data-i18n="${key}"]`);
            if (element) {
                element.textContent = value;
            }
        }
    }
    </script>
'''
    
    # Añadir data-i18n a elementos clave
    content = content.replace(
        '<h1 style="margin-top: 15px;">Conectamos tu corazón con el Eje Cafetero: Experiencias auténticas que quedarán en tu memoria</h1>',
        '<h1 style="margin-top: 15px;" data-i18n="hero_title">Conectamos tu corazón con el Eje Cafetero: Experiencias auténticas que quedarán en tu memoria</h1>'
    )
    
    # Añadir CSS para selector
    multilang_css = '''
    .language-selector {
        display: flex;
        gap: 5px;
        margin-left: 20px;
    }
    
    .lang-btn {
        background: rgba(255,255,255,0.1);
        border: 1px solid rgba(255,255,255,0.3);
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .lang-btn:hover, .lang-btn.active {
        background: var(--verde-cafe);
        border-color: var(--verde-cafe);
    }
'''
    
    # Buscar </style> para añadir CSS
    style_end = '</style>'
    if style_end in content:
        content = content.replace(style_end, multilang_css + '\n' + style_end)
    
    # Buscar </body> para añadir script
    body_end = '</body>'
    if body_end in content:
        content = content.replace(body_end, multilang_js + '\n' + body_end)
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    add_multilanguage_support()