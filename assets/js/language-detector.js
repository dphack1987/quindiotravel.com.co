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
            destinos: "Destinos",
            promo: "🔥 Promoción"
        },
        breadcrumb: {
            home: "Inicio",
            hotels: "Hoteles"
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
        planes: {
            hero: {
                badge: "🌿 Experiencias Auténticas 2026",
                title: "Planes Turísticos del Eje Cafetero",
                subtitle: "Descubre la magia del Quindío con nuestros 6 planes diseñados a tu medida. Desde escapadas cortas hasta experiencias completas de 5 días.",
                feature1: "Guías Certificados RNT 18152",
                feature2: "Transporte Incluido",
                feature3: "Asistencia Médica",
                ctaQuote: "Cotizar mi viaje",
                ctaViewAll: "Ver todos los planes"
            },
            section: {
                badge: "🗺️ Experiencias Completas",
                title: "Paquetes turísticos completos en el Eje Cafetero",
                subtitle: "Planes turísticos en Quindío para recorrer el Eje Cafetero. 6 planes diseñados para descubrir la magia del Eje Cafetero. Todos incluyen transporte, asistencia local personalizada y asistencia médica."
            },
            cotizador: {
                badge: "🧮 Cotizador Oficial",
                title: "Cotizador de Precios Autorizados",
                subtitle: "Calcula tu cotización usando únicamente los precios oficiales del PORTAFOLIO PLANES NACIONALES 2026",
                planLabel: "Plan",
                hotelLabel: "Alojamiento",
                paxLabel: "Pasajeros",
                destinosLabel: "Destinos Adicionales",
                destinosHint: "Selecciona una o varias opciones",
                resultPriceLabel: "Precio por persona",
                resultTotalLabel: "TOTAL",
                resultDestinosLabel: "Destinos adicionales",
                whatsappButton: "Solicitar cotización por WhatsApp"
            }
        },
        hotel: {
            hero: {
                category: "⭐ Alojamiento Estándar",
                location: "Km. 5 Pueblo Tapao Vía a La Tebaida, Quindío"
            },
            gallery: {
                title: "📸 Galería de Fotos"
            },
            about: {
                title: "🏡 Sobre el alojamiento"
            },
            services: {
                title: "🛎️ Servicios Incluidos"
            },
            location: {
                title: "📍 Ubicación",
                address: "Dirección:",
                distance: "Distancia a Armenia:",
                nearby: "Cercano a:",
                cta: "Consultar disponibilidad"
            },
            operator: "Operador Turístico RNT 18152",
            plans: {
                title: "🗺️ Planes que incluyen este alojamiento",
                button: "Ver plan"
            }
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
            attractions: "Atractivos Principales",
            linkPlans: "Planes",
            linkHotels: "Hoteles",
            linkContact: "Contacto",
            linkMap: "Mapa Turístico",
            linkExperiences: "Experiencias",
            linkBlog: "Blog",
            copyright: "© 2026 Quindío Travel. Todos los derechos reservados. Diseñado con ❤ para el Eje Cafetero colombiano."
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
            destinos: "Destinations",
            promo: "🔥 Promotion"
        },
        breadcrumb: {
            home: "Home",
            hotels: "Hotels"
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
        planes: {
            hero: {
                badge: "🌿 Authentic Experiences 2026",
                title: "Coffee Axis Tour Plans",
                subtitle: "Discover the magic of Quindío with our 6 plans designed to your measure. From short getaways to complete 5-day experiences.",
                feature1: "RNT 18152 Certified Guides",
                feature2: "Transport Included",
                feature3: "Medical Assistance",
                ctaQuote: "Quote my trip",
                ctaViewAll: "See all plans"
            },
            section: {
                badge: "🗺️ Complete Experiences",
                title: "Complete tour packages in the Coffee Axis",
                subtitle: "Quindío tour plans to explore the Coffee Axis. 6 plans designed to discover the magic of the Coffee Axis. All include transport, personalized local assistance and medical support."
            },
            cotizador: {
                badge: "🧮 Official Quotation",
                title: "Authorized Price Calculator",
                subtitle: "Calculate your quote using only official prices from the 2026 NATIONAL PLANS PORTFOLIO",
                planLabel: "Plan",
                hotelLabel: "Accommodation",
                paxLabel: "Passengers",
                destinosLabel: "Additional Destinations",
                destinosHint: "Choose one or more options",
                resultPriceLabel: "Price per person",
                resultTotalLabel: "TOTAL",
                resultDestinosLabel: "Additional destinations",
                whatsappButton: "Request quote via WhatsApp"
            }
        },
        hotel: {
            hero: {
                category: "⭐ Standard Accommodation",
                location: "Km. 5 Pueblo Tapao Vía a La Tebaida, Quindío"
            },
            gallery: {
                title: "📸 Photo Gallery"
            },
            about: {
                title: "🏡 About the Accommodation"
            },
            services: {
                title: "🛎️ Included Services"
            },
            location: {
                title: "📍 Location",
                address: "Address:",
                distance: "Distance to Armenia:",
                nearby: "Near:",
                cta: "Check availability"
            },
            operator: "Tour operator RNT 18152",
            plans: {
                title: "🗺️ Plans that include this accommodation",
                button: "View plan"
            }
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
            attractions: "Main Attractions",
            linkPlans: "Plans",
            linkHotels: "Hotels",
            linkContact: "Contact",
            linkMap: "Tourist Map",
            linkExperiences: "Experiences",
            linkBlog: "Blog",
            copyright: "© 2026 Quindío Travel. All rights reserved. Designed with ❤ for the Colombian Coffee Axis."
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
        breadcrumb: {
            home: "Início",
            hotels: "Hotéis"
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
        planes: {
            hero: {
                badge: "🌿 Experiências Autênticas 2026",
                title: "Planos Turísticos do Eixo Cafeeiro",
                subtitle: "Descubra a magia de Quindío com nossos 6 planos desenhados para você. De escapadas curtas até experiências completas de 5 dias.",
                feature1: "Guias Certificados RNT 18152",
                feature2: "Transporte Incluído",
                feature3: "Assistência Médica",
                ctaQuote: "Cotizar mi viaje",
                ctaViewAll: "Ver todos los planes"
            },
            section: {
                badge: "🗺️ Experiências Completas",
                title: "Pacotes turísticos completos no Eixo Cafeeiro",
                subtitle: "Planos turísticos em Quindío para percorrer o Eixo Cafeeiro. 6 planos projetados para descobrir a magia do Eixo Cafeeiro. Todos incluem transporte, assistência local personalizada e assistência médica."
            },
            cotizador: {
                badge: "🧮 Cotador Oficial",
                title: "Calculadora de Preços Autorizados",
                subtitle: "Calcule sua cotação usando apenas preços oficiais do PORTFÓLIO PLANOS NACIONAIS 2026",
                planLabel: "Plano",
                hotelLabel: "Acomodação",
                paxLabel: "Passageiros",
                destinosLabel: "Destinos Adicionais",
                destinosHint: "Escolha uma ou mais opções",
                resultPriceLabel: "Preço por pessoa",
                resultTotalLabel: "TOTAL",
                resultDestinosLabel: "Destinos adicionais",
                whatsappButton: "Solicitar cotação via WhatsApp"
            }
        },
        hotel: {
            hero: {
                category: "⭐ Alojamento Padrão",
                location: "Km. 5 Pueblo Tapao Vía a La Tebaida, Quindío"
            },
            gallery: {
                title: "📸 Galeria de Fotos"
            },
            about: {
                title: "🏡 Sobre o Alojamento"
            },
            services: {
                title: "🛎️ Serviços Incluídos"
            },
            location: {
                title: "📍 Localização",
                address: "Endereço:",
                distance: "Distância para Armenia:",
                nearby: "Próximo a:",
                cta: "Consultar disponibilidade"
            },
            operator: "Operador Turístico RNT 18152",
            plans: {
                title: "🗺️ Planos que incluem este alojamento",
                button: "Ver plano"
            }
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
            attractions: "Atrações Principais",
            linkPlans: "Planos",
            linkHotels: "Hotéis",
            linkContact: "Contato",
            linkMap: "Mapa Turístico",
            linkExperiences: "Experiências",
            linkBlog: "Blog",
            copyright: "© 2026 Quindío Travel. Todos os direitos reservados. Projetado com ❤ para o Eixo Cafeeiro colombiano."
        }
    },
    fr: {
        nav: {
            inicio: "Accueil",
            planes: "Forfaits",
            hoteles: "Hôtels",
            experiencias: "Expériences",
            mapa: "Carte touristique",
            empresas: "Entreprises",
            blog: "Blog",
            nosotros: "À propos",
            contacto: "Contact",
            destinos: "Destinations",
            promo: "🔥 Promotion"
        },
        breadcrumb: {
            home: "Accueil",
            hotels: "Hôtels"
        },
        hero: {
            badge: "🌿 Expériences Authentiques 2026",
            title: "Forfaits touristiques de l'Eje Cafetero",
            subtitle: "Découvrez la magie de Quindío avec nos 6 forfaits conçus sur mesure. Des escapades courtes aux expériences complètes de 5 jours.",
            feature1: "Guides certifiés RNT 18152",
            feature2: "Transport inclus",
            feature3: "Assistance médicale"
        },
        cta: {
            cotizar: "Devis Plan 4D/3N avec hébergement",
            whatsapp: "Demander un devis via WhatsApp"
        },
        planes: {
            hero: {
                badge: "🌿 Expériences Authentiques 2026",
                title: "Forfaits touristiques de l'Eje Cafetero",
                subtitle: "Découvrez la magie de Quindío avec nos 6 forfaits conçus sur mesure. Des escapades courtes aux expériences complètes de 5 jours.",
                feature1: "Guides certifiés RNT 18152",
                feature2: "Transport inclus",
                feature3: "Assistance médicale",
                ctaQuote: "Demander un devis",
                ctaViewAll: "Voir tous les forfaits"
            },
            section: {
                badge: "🗺️ Expériences Complètes",
                title: "Forfaits touristiques complets dans l'Eje Cafetero",
                subtitle: "Forfaits touristiques à Quindío pour explorer l'Eje Cafetero. 6 forfaits conçus pour découvrir la magie de l'Eje Cafetero. Tous incluent le transport, l'assistance locale personnalisée et l'assistance médicale."
            },
            cotizador: {
                badge: "🧮 Devis officiel",
                title: "Calculateur de prix autorisé",
                subtitle: "Calculez votre devis en utilisant uniquement les prix officiels du PORTAIL DES FORFAITS NATIONAUX 2026",
                planLabel: "Forfait",
                hotelLabel: "Hébergement",
                paxLabel: "Passagers",
                destinosLabel: "Destinations supplémentaires",
                destinosHint: "Choisissez une ou plusieurs options",
                resultPriceLabel: "Prix par personne",
                resultTotalLabel: "TOTAL",
                resultDestinosLabel: "Destinations supplémentaires",
                whatsappButton: "Demander un devis via WhatsApp"
            }
        },
        hotel: {
            hero: {
                category: "⭐ Hébergement standard",
                location: "Km. 5 Pueblo Tapao Vía a La Tebaida, Quindío"
            },
            gallery: {
                title: "📸 Galerie de photos"
            },
            about: {
                title: "🏡 À propos de l'hébergement"
            },
            services: {
                title: "🛎️ Services inclus"
            },
            location: {
                title: "📍 Emplacement",
                address: "Adresse:",
                distance: "Distance jusqu'à Armenia:",
                nearby: "À proximité de:",
                cta: "Vérifier la disponibilité"
            },
            operator: "Opérateur touristique RNT 18152",
            plans: {
                title: "🗺️ Forfaits incluant cet hébergement",
                button: "Voir le forfait"
            }
        },
        experiences: {
            title: "Guide du tourisme à Quindío : expériences et itinéraires",
            subtitle: "Découvrez les attractions les plus emblématiques avec des guides locaux qui connaissent chaque recoin du Quindío."
        },
        footer: {
            quindio_travel: "Quindío Travel",
            description: "Nous ne vendons pas seulement des voyages ; nous sommes le guide officiel pour découvrir Quindío.",
            manager: "Directeur :",
            phone: "Téléphone / WhatsApp :",
            email: "E-mail :",
            rnt: "RNT :",
            location: "Emplacement :",
            quick_links: "Liens rapides",
            destinations: "Destinations populaires",
            attractions: "Principales attractions",
            linkPlans: "Forfaits",
            linkHotels: "Hôtels",
            linkContact: "Contact",
            linkMap: "Carte touristique",
            linkExperiences: "Expériences",
            linkBlog: "Blog",
            copyright: "© 2026 Quindío Travel. Tous droits réservés. Conçu avec ❤ pour l'Eje Cafetero colombien."
        }
    }
};

// Detectar idioma del navegador
function detectBrowserLanguage() {
    const browserLang = navigator.language || navigator.userLanguage;
    const langCode = browserLang.split('-')[0]; // Obtener solo el código de idioma (es, en, pt)
    
    // Mapeo de idiomas soportados
    const supportedLangs = ['es', 'en', 'pt', 'fr'];
    
    if (supportedLangs.includes(langCode)) {
        return langCode;
    }
    
    // Por defecto español para Colombia y América Latina
    return 'es';
}

// Obtener idioma almacenado, desde la URL o detectar
function getLanguage() {
    const urlParams = new URLSearchParams(window.location.search);
    const urlLang = urlParams.get('lang');
    const supportedLangs = ['es', 'en', 'pt', 'fr'];

    if (urlLang && supportedLangs.includes(urlLang)) {
        localStorage.setItem('quindio-language', urlLang);
        return urlLang;
    }

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
    document.documentElement.lang = lang === 'pt' ? 'pt-BR' : lang === 'en' ? 'en' : lang === 'fr' ? 'fr' : 'es';
    
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
        pt: 'pt_BR',
        fr: 'fr_FR'
    };
    
    const currentPath = window.location.pathname;
    const baseUrl = `${window.location.origin}${currentPath}`;
    const urlMap = {
        es: baseUrl,
        en: `${baseUrl}?lang=en`,
        pt: `${baseUrl}?lang=pt`,
        fr: `${baseUrl}?lang=fr`
    };
    
    document.querySelectorAll('link[rel="alternate"]').forEach(link => {
        const hreflang = link.getAttribute('hreflang');
        if (!hreflang) return;

        if (hreflang === 'x-default') {
            link.href = baseUrl;
            return;
        }

        if (hreflang.startsWith('es')) {
            link.href = urlMap.es;
        } else if (hreflang.startsWith('en')) {
            link.href = urlMap.en;
        } else if (hreflang.startsWith('pt')) {
            link.href = urlMap.pt;
        } else if (hreflang.startsWith('fr')) {
            link.href = urlMap.fr;
        }
    });
    
    const hreflangCode = langMap[lang] || 'es_CO';
    const existingLink = Array.from(document.querySelectorAll('link[rel="alternate"]')).find(link => link.getAttribute('hreflang') === hreflangCode || link.getAttribute('hreflang') === lang);

    if (!existingLink) {
        const link = document.createElement('link');
        link.rel = 'alternate';
        link.hreflang = lang;
        link.href = urlMap[lang] || urlMap.es;
        document.head.appendChild(link);
    }
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
    if (!headerActions || document.getElementById('language-selector')) {
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
    
    // Asegurar que funcione en redimensionamiento
    window.addEventListener('resize', function() {
        const existingSelector = document.getElementById('language-selector');
        if (existingSelector) {
            const container = existingSelector.parentElement;
            if (window.innerWidth <= 768) {
                const hamburgerBtn = document.getElementById('hamburger-btn');
                if (hamburgerBtn && container.nextElementSibling !== hamburgerBtn) {
                    headerActions.insertBefore(container, hamburgerBtn);
                }
            } else {
                if (container !== headerActions.firstChild) {
                    headerActions.insertBefore(container, headerActions.firstChild);
                }
            }
        }
    });
}

// Inicializar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', initLanguageSystem);