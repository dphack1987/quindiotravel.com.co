/**
 * Sistema de Seguimiento Automático en WhatsApp
 * Sistema que simplifica el proceso de reserva y proporciona seguimiento automático
 */

(function() {
    'use strict';

    class WhatsAppAutoFollowup {
        constructor() {
            this.init();
        }

        init() {
            this.setupAutoMessages();
            this.setupTracking();
            this.optimizeWhatsAppLinks();
        }

        setupAutoMessages() {
            // Configurar mensajes automáticos para diferentes escenarios
            this.autoMessages = {
                initial: "¡Gracias por contactar a Quindío Travel! 🌿\n\nSoy tu asistente virtual. Recibí tu solicitud y un especialista te responderá en menos de 15 minutos.\n\nMientras tanto, ¿te gustaría ver nuestros planes disponibles?\n👉 https://quindiotravel.com.co/planes.html\n\nRNT 18152 - Operador Turístico Eje Cafetero",
                followup: "Hola de nuevo 🌿\n\nVeo que estabas interesado en nuestros planes del Eje Cafetero. ¿Tienes alguna pregunta adicional o necesitas más información?\n\nEstamos aquí para ayudarte a planificar tu viaje perfecto.\n\nWhatsApp: +57 317 442 6044",
                urgent: "¡ÚLTIMA OPORTUNIDAD! 🔥\n\nSolo quedan 3 cupos disponibles para esta semana en nuestros planes del Eje Cafetero.\n\n¿Te gustaría reservar uno de los últimos cupos?\n\nResponde AHORA para asegurar tu lugar:\n👉 https://wa.me/573174426044?text=RESERVAR%20CUPO%20URGENTE"
            };
        }

        setupTracking() {
            // Tracking de clics en enlaces de WhatsApp
            document.addEventListener('click', (e) => {
                const link = e.target.closest('a[href*="wa.me"]');
                if (link) {
                    this.trackWhatsAppClick(link);
                }
            });
        }

        trackWhatsAppClick(link) {
            // Extraer información del enlace
            const href = link.getAttribute('href');
            const message = this.extractWhatsAppMessage(href);
            const context = this.getClickContext(link);

            // Tracking de conversión
            if (typeof gtag !== 'undefined') {
                gtag('event', 'whatsapp_click', {
                    'event_category': 'conversion',
                    'event_label': context,
                    'value': message.length
                });
            }

            console.log(`WhatsApp click tracked: ${context}`);
        }

        extractWhatsAppMessage(href) {
            try {
                const url = new URL(href);
                const textParam = url.searchParams.get('text');
                return textParam ? decodeURIComponent(textParam) : '';
            } catch (e) {
                return '';
            }
        }

        getClickContext(link) {
            // Determinar el contexto del clic
            if (link.classList.contains('btn-whatsapp-hero')) {
                return 'hero_cta';
            } else if (link.id === 'urgency-banner') {
                return 'urgency_banner';
            } else if (link.closest('.hero-buttons')) {
                return 'hero_section';
            } else if (link.closest('.footer')) {
                return 'footer';
            } else {
                return 'other';
            }
        }

        optimizeWhatsAppLinks() {
            // Optimizar todos los enlaces de WhatsApp
            const whatsappLinks = document.querySelectorAll('a[href*="wa.me"]');
            
            whatsappLinks.forEach(link => {
                // Agregar atributos para mejor tracking
                link.setAttribute('data-whatsapp-tracking', 'true');
                
                // Agregar parámetro de timestamp
                const href = link.getAttribute('href');
                const timestamp = new Date().getTime();
                
                if (!href.includes('timestamp=')) {
                    const separator = href.includes('?') ? '&' : '?';
                    link.setAttribute('href', `${href}${separator}timestamp=${timestamp}`);
                }
                
                // Mejorar accesibilidad
                link.setAttribute('aria-label', 'Contactar por WhatsApp');
            });
        }

        generateQuickQuoteMessage(formData) {
            // Generar mensaje optimizado para cotización rápida
            const { name, date, destination, passengers } = formData;
            
            return `🌿 COTIZACIÓN RÁPIDA - Quindío Travel\n\n` +
                   `👤 Nombre: ${name}\n` +
                   `📅 Fecha deseada: ${date}\n` +
                   `🎯 Destino: ${destination}\n` +
                   `👥 Pasajeros: ${passengers || 'Por definir'}\n\n` +
                   `🏆 RNT 18152 - Operador Turístico Eje Cafetero\n\n` +
                   `¿Me pueden dar información y precio disponible?`;
        }

        generateUrgencyMessage(cupsAvailable) {
            // Generar mensaje de urgencia
            return `🔥 URGENTE - ÚLTIMOS ${cupsAvailable} CUPOS\n\n` +
                   `¡No te pierdas esta oportunidad!\n\n` +
                   `Solo quedan ${cupsAvailable} cupos disponibles para esta semana en nuestros planes del Eje Cafetero.\n\n` +
                   `📅 Esta oferta expira en 48 horas\n` +
                   `💰 Precios desde $1.152.000 COP\n\n` +
                   `Responde AHORA para asegurar tu lugar:\n` +
                   `👉 RESERVAR CUPO URGENTE`;
        }
    }

    // Función global para generar mensajes de WhatsApp
    window.WhatsAppAutoFollowup = {
        generateQuickQuote: (formData) => {
            const system = new WhatsAppAutoFollowup();
            return system.generateQuickQuoteMessage(formData);
        },
        
        generateUrgency: (cupsAvailable) => {
            const system = new WhatsAppAutoFollowup();
            return system.generateUrgencyMessage(cupsAvailable);
        },
        
        openWhatsApp: (message) => {
            const url = `https://wa.me/573174426044?text=${encodeURIComponent(message)}`;
            window.open(url, '_blank');
        }
    };

    // Inicializar sistema
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => {
            new WhatsAppAutoFollowup();
        });
    } else {
        new WhatsAppAutoFollowup();
    }

})();