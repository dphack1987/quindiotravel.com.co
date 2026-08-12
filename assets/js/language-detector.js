// Sistema de detección y selección de idioma - Quindío Travel
// Updated: 2026-08-06 - Simplificado para mejor funcionamiento

const translations = {
    es: {
        'nav.inicio': "Inicio",
        'nav.promo': "🔥 Promoción",
        'nav.planes': "Planes",
        'nav.hoteles': "Hoteles",
        'nav.experiencias': "Experiencias",
        'nav.destinos': "Destinos",
        'nav.blog': "Blog",
        'nav.nosotros': "Nosotros",
        'nav.contacto': "Contacto",
        'experiencias.title': "✨ Experiencias Inolvidables del Eje Cafetero",
        'experiencias.subtitle': "Vive los atractivos más icónicos con la compañía de guías locales que conocen cada rincón del Quindío.",
        'footer.quindio_travel': "Quindío Travel",
        'footer.description': "No solo vendemos viajes; somos la guía oficial para descubrir el Quindío auténtico.",
        'footer.manager': "Gerente:",
        'footer.phone': "Celular / WhatsApp:",
        'footer.email': "Correo:",
        'footer.rnt': "RNT:",
        'footer.location': "Ubicación:",
        'footer.quick_links': "Enlaces Rápidos",
        'footer.destinations': "Destinos Populares",
        'chat.greeting': "🤠 ¡Hola, compadre! Soy Don Chucho, tu guía del Eje Cafetero. Estoy aquí para ayudarte a planear el viaje perfecto al Quindío. ¿Qué te gustaría saber?",
        'chat.placeholder': "Escribe tu mensaje...",
        'chat.quick.planes': "🗺️ Ver Planes",
        'chat.quick.precios': "💰 Precios",
        'chat.quick.destinos': "🏛️ Destinos",
        'chat.quick.contacto': "📞 Contacto"
    },
    en: {
        'nav.inicio': "Home",
        'nav.promo': "🔥 Promotion",
        'nav.planes': "Plans",
        'nav.hoteles': "Hotels",
        'nav.experiencias': "Experiences",
        'nav.destinos': "Destinations",
        'nav.blog': "Blog",
        'nav.nosotros': "About Us",
        'nav.contacto': "Contact",
        'experiencias.title': "✨ Unforgettable Experiences of the Coffee Axis",
        'experiencias.subtitle': "Experience the most iconic attractions with local guides who know every corner of Quindío.",
        'footer.quindio_travel': "Quindío Travel",
        'footer.description': "We don't just sell trips; we are the official guide to discover Quindío.",
        'footer.manager': "Manager:",
        'footer.phone': "Cell / WhatsApp:",
        'footer.email': "Email:",
        'footer.rnt': "RNT:",
        'footer.location': "Location:",
        'footer.quick_links': "Quick Links",
        'footer.destinations': "Popular Destinations",
        'chat.greeting': "🤠 Hello, traveler! I'm Don Chucho, your Coffee Axis guide. I'm here to help you plan the perfect trip to Quindío. What would you like to know?",
        'chat.placeholder': "Type your message...",
        'chat.quick.planes': "🗺️ View Plans",
        'chat.quick.precios': "💰 Prices",
        'chat.quick.destinos': "🏛️ Destinations",
        'chat.quick.contacto': "📞 Contact"
    },
    pt: {
        'nav.inicio': "Início",
        'nav.promo': "🔥 Promoção",
        'nav.planes': "Planos",
        'nav.hoteles': "Hotéis",
        'nav.experiencias': "Experiências",
        'nav.destinos': "Destinos",
        'nav.blog': "Blog",
        'nav.nosotros': "Sobre Nós",
        'nav.contacto': "Contato",
        'experiencias.title': "✨ Experiências Inesquecíveis do Eixo Cafeeiro",
        'experiencias.subtitle': "Viva os atrativos mais icônicos com guias locais que conhecem cada canto de Quindío.",
        'footer.quindio_travel': "Quindío Travel",
        'footer.description': "Não apenas vendemos viagens; somos o guia oficial para descobrir Quindío.",
        'footer.manager': "Gerente:",
        'footer.phone': "Celular / WhatsApp:",
        'footer.email': "E-mail:",
        'footer.rnt': "RNT:",
        'footer.location': "Localização:",
        'footer.quick_links': "Links Rápidos",
        'footer.destinations': "Destinos Populares",
        'chat.greeting': "🤠 Olá, viajante! Sou Don Chucho, seu guia do Eixo Cafeeiro. Estou aqui para ajudar a planejar a viagem perfeita para Quindío. O que você gostaria de saber?",
        'chat.placeholder': "Escreva sua mensagem...",
        'chat.quick.planes': "🗺️ Ver Planos",
        'chat.quick.precios': "💰 Preços",
        'chat.quick.destinos': "🏛️ Destinos",
        'chat.quick.contacto': "📞 Contato"
    },
    fr: {
        'nav.inicio': "Accueil",
        'nav.promo': "🔥 Promotion",
        'nav.planes': "Plans",
        'nav.hoteles': "Hôtels",
        'nav.experiencias': "Expériences",
        'nav.destinos': "Destinations",
        'nav.blog': "Blog",
        'nav.nosotros': "À propos",
        'nav.contacto': "Contact",
        'experiencias.title': "✨ Expériences Inoubliables de l'Axe du Café",
        'experiencias.subtitle': "Vivez les attractions les plus emblématiques avec des guides locaux qui connaissent chaque coin de Quindío.",
        'footer.quindio_travel': "Quindío Travel",
        'footer.description': "Nous ne vendons pas seulement des voyages; nous sommes le guide officiel pour découvrir Quindío.",
        'footer.manager': "Gérant:",
        'footer.phone': "Cellulaire / WhatsApp:",
        'footer.email': "E-mail:",
        'footer.rnt': "RNT:",
        'footer.location': "Emplacement:",
        'footer.quick_links': "Liens Rapides",
        'footer.destinations': "Destinations Populaires",
        'chat.greeting': "🤠 Bonjour, voyageur ! Je suis Don Chucho, ton guide de l'Axe du Café. Je suis là pour t'aider à planifier le voyage parfait à Quindío. Que souhaites-tu savoir ?",
        'chat.placeholder': "Tapez votre message...",
        'chat.quick.planes': "🗺️ Voir les plans",
        'chat.quick.precios': "💰 Tarifs",
        'chat.quick.destinos': "🏛️ Destinations",
        'chat.quick.contacto': "📞 Contact"
    }
};

const supportedLangs = ['es', 'en', 'pt', 'fr'];

// Detectar idioma del navegador
function detectBrowserLanguage() {
    const browserLang = navigator.language || navigator.userLanguage;
    const langCode = browserLang.split('-')[0]; // Obtener solo el código de idioma
    
    if (supportedLangs.includes(langCode)) {
        return langCode;
    }
    
    // Por defecto español para Colombia y América Latina
    return 'es';
}

// Obtener idioma almacenado, query param o detectar
function getLanguage() {
    const urlParams = new URLSearchParams(window.location.search);
    const requestedLang = urlParams.get('lang');
    if (requestedLang && supportedLangs.includes(requestedLang)) {
        localStorage.setItem('quindio-language', requestedLang);
        return requestedLang;
    }

    const storedLang = localStorage.getItem('quindio-language');
    if (storedLang && supportedLangs.includes(storedLang)) {
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
    
    if (!t) {
        console.error('No translations found for language:', lang);
        return;
    }
    
    // Traducir elementos con data-i18n
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        const value = t[key];
        
        if (value) {
            element.textContent = value;
            console.log(`Translated ${key} to: ${value}`);
        } else {
            console.warn(`No translation found for key: ${key}`);
        }
    });
    
    // Actualizar atributo lang del HTML
    document.documentElement.lang = lang === 'pt' ? 'pt-BR' : lang === 'en' ? 'en' : lang === 'fr' ? 'fr' : 'es';
    
    console.log(`Language applied: ${lang}`);
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
    console.log('Initializing language system with:', currentLang);
    
    // Esperar a que el DOM esté completamente cargado
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => {
            applyLanguage(currentLang);
            updateLanguageSelector(currentLang);
            setupLanguageSelector();
        });
    } else {
        applyLanguage(currentLang);
        updateLanguageSelector(currentLang);
        setupLanguageSelector();
    }
}

// Configurar selector de idioma existente
function setupLanguageSelector() {
    const selector = document.getElementById('language-selector');
    if (selector) {
        // Remover event listeners anteriores
        const newSelector = selector.cloneNode(true);
        selector.parentNode.replaceChild(newSelector, selector);
        
        // Agregar nuevo event listener
        newSelector.addEventListener('change', function() {
            const newLang = this.value;
            console.log('Language changed to:', newLang);
            setLanguage(newLang);
        });
        
        console.log('Language selector setup complete');
    } else {
        console.warn('Language selector not found');
    }
}

// Inicializar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', initLanguageSystem);

console.log("Language detector script loaded");