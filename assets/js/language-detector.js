// Sistema de detección y selección de idioma - Quindío Travel

const translations = {
    es: {
        nav: {
            inicio: "Inicio",
            planes: "Planes",
            hoteles: "Hoteles",
            experiencias: "Experiencias",
            mapa: "Mapa Turístico",
            empresas: "Empresas",
            blog: "Blog",
            nosotros: "Nosotros",
            contacto: "Contacto",
            promo: "🔥 Promoción"
        },
        hero: {
            badge: "🌿 Experiencias Auténticas 2026",
            title: "Planes Turísticos del Eje Cafetero",
            subtitle: "Descubre la magia del Quindío con nuestros 6 planes diseñados a tu medida. Desde escapadas cortas hasta experiencias completas de 5 días.",
            feature1: "Guías Certificados RNT 18152",
            feature2: "Transporte Incluido",
            feature3: "Asistencia Médica"
        },
        cta: {
            cotizar: "Cotizar Plan 4D/3N con alojamiento",
            whatsapp: "Solicitar cotización por WhatsApp"
        },
        experiences: {
            title: "Guía de turismo en Quindío: experiencias y rutas",
            subtitle: "Vive los atractivos más icónicos con la compañía de guías locales que conocen cada rincón del Quindío."
        },
        footer: {
            quindio_travel: "Quindío Travel",
            description: "No solo vendemos viajes; somos la guía oficial para descubrir el Quindío.",
            manager: "Gerente:",
            phone: "Celular / WhatsApp:",
            email: "Correo:",
            rnt: "RNT:",
            location: "Ubicación:",
            quick_links: "Enlaces Rápidos",
            destinations: "Destinos Populares",
            attractions: "Atractivos Principales"
        }
    },
    en: {
        nav: {
            inicio: "Home",
            planes: "Plans",
            hoteles: "Hotels",
            experiencias: "Experiences",
            mapa: "Tourist Map",
            empresas: "Corporate",
            blog: "Blog",
            nosotros: "About Us",
            contacto: "Contact",
            promo: "🔥 Promotion"
        },
        hero: {
            badge: "🌿 Authentic Experiences 2026",
            title: "Coffee Axis Tour Plans",
            subtitle: "Discover the magic of Quindío with our 6 plans designed to your measure. From short getaways to complete 5-day experiences.",
            feature1: "RNT 18152 Certified Guides",
            feature2: "Transport Included",
            feature3: "Medical Assistance"
        },
        cta: {
            cotizar: "Quote 4D/3N Plan with accommodation",
            whatsapp: "Request quote via WhatsApp"
        },
        experiences: {
            title: "Quindío tourism guide: experiences and routes",
            subtitle: "Experience the most iconic attractions with local guides who know every corner of Quindío."
        },
        footer: {
            quindio_travel: "Quindío Travel",
            description: "We don't just sell trips; we are the official guide to discover Quindío.",
            manager: "Manager:",
            phone: "Cell / WhatsApp:",
            email: "Email:",
            rnt: "RNT:",
            location: "Location:",
            quick_links: "Quick Links",
            destinations: "Popular Destinations",
            attractions: "Main Attractions"
        }
    },
    pt: {
        nav: {
            inicio: "Início",
            planes: "Planos",
            hoteles: "Hotéis",
            experiencias: "Experiências",
            mapa: "Mapa Turístico",
            empresas: "Empresas",
            blog: "Blog",
            nosotros: "Sobre Nós",
            contacto: "Contato",
            promo: "🔥 Promoção"
        },
        hero: {
            badge: "🌿 Experiências Autênticas 2026",
            title: "Planos Turísticos do Eixo Cafeeiro",
            subtitle: "Descubra a magia de Quindío com nossos 6 planos desenhados para você. De escapadas curtas até experiências completas de 5 dias.",
            feature1: "Guias Certificados RNT 18152",
            feature2: "Transporte Incluído",
            feature3: "Assistência Médica"
        },
        cta: {
            cotizar: "Cotizar Plano 4D/3N com acomodação",
            whatsapp: "Solicitar cotação via WhatsApp"
        },
        experiences: {
            title: "Guia de turismo em Quindío: experiências e rotas",
            subtitle: "Viva os atrativos mais icônicos com guias locais que conhecem cada canto de Quindío."
        },
        footer: {
            quindio_travel: "Quindío Travel",
            description: "Não apenas vendemos viagens; somos o guia oficial para descobrir Quindío.",
            manager: "Gerente:",
            phone: "Celular / WhatsApp:",
            email: "E-mail:",
            rnt: "RNT:",
            location: "Localização:",
            quick_links: "Links Rápidos",
            destinations: "Destinos Populares",
            attractions: "Atrações Principais"
        }
    }
};

// Detectar idioma del navegador
function detectBrowserLanguage() {
    const browserLang = navigator.language || navigator.userLanguage;
    const langCode = browserLang.split('-')[0]; // Obtener solo el código de idioma (es, en, pt)
    
    // Mapeo de idiomas soportados
    const supportedLangs = ['es', 'en', 'pt'];
    
    if (supportedLangs.includes(langCode)) {
        return langCode;
    }
    
    // Por defecto español para Colombia y América Latina
    return 'es';
}

// Obtener idioma almacenado o detectar
function getLanguage() {
    const storedLang = localStorage.getItem('quindio-language');
    if (storedLang) {
        return storedLang;
    }
    
    const detectedLang = detectBrowserLanguage();
    localStorage.setItem('quindio-language', detectedLang);
    return detectedLang;
}

// Cambiar idioma
function setLanguage(lang) {
    localStorage.setItem('quindio-language', lang);
    applyLanguage(lang);
    updateLanguageSelector(lang);
}

// Aplicar idioma al contenido
function applyLanguage(lang) {
    const t = translations[lang];
    
    // Traducir navegación
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        const keys = key.split('.');
        let value = t;
        
        keys.forEach(k => {
            value = value[k];
        });
        
        if (value) {
            element.textContent = value;
        }
    });
    
    // Actualizar atributo lang del HTML
    document.documentElement.lang = lang === 'pt' ? 'pt-BR' : lang === 'en' ? 'en' : 'es';
    
    // Actualizar meta tags para SEO
    updateMetaTags(lang);
}

// Actualizar selector de idioma visual
function updateLanguageSelector(lang) {
    const selector = document.getElementById('language-selector');
    if (selector) {
        selector.value = lang;
    }
}

// Actualizar meta tags para SEO
function updateMetaTags(lang) {
    const langMap = {
        es: 'es_CO',
        en: 'en_US',
        pt: 'pt_BR'
    };
    
    const langCode = langMap[lang] || 'es_CO';
    
    // Actualizar hreflang
    let hreflang = document.querySelector('link[hreflang]');
    if (!hreflang) {
        hreflang = document.createElement('link');
        hreflang.rel = 'alternate';
        hreflang.hreflang = langCode;
        document.head.appendChild(hreflang);
    }
    hreflang.hreflang = langCode;
}

// Inicializar sistema de idioma
function initLanguageSystem() {
    const currentLang = getLanguage();
    applyLanguage(currentLang);
    updateLanguageSelector(currentLang);
    
    // Crear selector de idioma si no existe
    createLanguageSelector();
}

// Crear selector de idioma en el header
function createLanguageSelector() {
    const headerActions = document.querySelector('.header-actions');
    if (!headerActions) {
        console.log('header-actions not found, trying alternative method');
        // Try to find header and append there
        const header = document.querySelector('.main-header');
        if (header) {
            const navContainer = header.querySelector('.nav-container, .container');
            if (navContainer) {
                createLanguageSelectorInContainer(navContainer);
                return;
            }
        }
        return;
    }
    
    if (document.getElementById('language-selector')) {
        return;
    }
    
    const currentLang = getLanguage();
    
    const selectorContainer = document.createElement('div');
    selectorContainer.className = 'language-selector-container';
    selectorContainer.innerHTML = `
        <select id="language-selector" class="language-selector" aria-label="Seleccionar idioma / Select language">
            <option value="es" ${currentLang === 'es' ? 'selected' : ''}>🇪🇸 Español</option>
            <option value="en" ${currentLang === 'en' ? 'selected' : ''}>🇺🇸 English</option>
            <option value="pt" ${currentLang === 'pt' ? 'selected' : ''}>🇧🇷 Português</option>
            <option value="fr" ${currentLang === 'fr' ? 'selected' : ''}>🇫🇷 Français</option>
        </select>
    `;
    
    selectorContainer.querySelector('#language-selector').addEventListener('change', function() {
        setLanguage(this.value);
    });
    
    // Insertar antes del botón hamburguesa para mejor UX móvil
    const hamburgerBtn = document.getElementById('hamburger-btn');
    if (hamburgerBtn && window.innerWidth <= 768) {
        headerActions.insertBefore(selectorContainer, hamburgerBtn);
    } else {
        headerActions.insertBefore(selectorContainer, headerActions.firstChild);
    }
    
    console.log('Language selector created successfully');
}

function createLanguageSelectorInContainer(container) {
    if (document.getElementById('language-selector')) {
        return;
    }
    
    const currentLang = getLanguage();
    
    const selectorContainer = document.createElement('div');
    selectorContainer.className = 'language-selector-container';
    selectorContainer.style.marginRight = '15px';
    selectorContainer.innerHTML = `
        <select id="language-selector" class="language-selector" aria-label="Seleccionar idioma / Select language">
            <option value="es" ${currentLang === 'es' ? 'selected' : ''}>🇪🇸 Español</option>
            <option value="en" ${currentLang === 'en' ? 'selected' : ''}>🇺🇸 English</option>
            <option value="pt" ${currentLang === 'pt' ? 'selected' : ''}>🇧🇷 Português</option>
            <option value="fr" ${currentLang === 'fr' ? 'selected' : ''}>🇫🇷 Français</option>
        </select>
    `;
    
    selectorContainer.querySelector('#language-selector').addEventListener('change', function() {
        setLanguage(this.value);
    });
    
    // Insert at the beginning of container
    container.insertBefore(selectorContainer, container.firstChild);
    
    console.log('Language selector created in container');
}

// Inicializar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', initLanguageSystem);