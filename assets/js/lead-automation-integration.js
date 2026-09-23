/**
 * Integración del Sistema de Automatización de Leads con Sitio Web
 * Conecta los formularios y botones del sitio con la API Python
 */

class LeadAutomationIntegration {
    constructor() {
        this.apiBaseUrl = 'http://localhost:5000/api'; // Cambiar a la URL de producción
        this.sessionData = this.initializeSessionData();
        this.init();
    }

    initializeSessionData() {
        // Inicializar datos de sesión para tracking
        return {
            sessionId: this.generateSessionId(),
            startTime: new Date().toISOString(),
            pageViews: 0,
            timeOnSite: 0,
            pagesVisited: [],
            interactions: []
        };
    }

    generateSessionId() {
        return 'session_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
    }

    init() {
        this.setupPageTracking();
        this.setupFormIntegration();
        this.setupWhatsAppIntegration();
        this.setupPeriodicSync();
    }

    setupPageTracking() {
        // Rastrear cada vista de página
        const currentPath = window.location.pathname;
        this.sessionData.pagesVisited.push({
            path: currentPath,
            timestamp: new Date().toISOString()
        });
        this.sessionData.pageViews++;

        // Rastrear tiempo en sitio
        this.timeOnSiteInterval = setInterval(() => {
            this.sessionData.timeOnSite++;
        }, 1000); // Actualizar cada segundo

        // Detectar tipo de dispositivo
        this.sessionData.device = this.detectDevice();
        this.sessionData.isReturnVisitor = this.checkReturnVisitor();
    }

    detectDevice() {
        const userAgent = navigator.userAgent.toLowerCase();
        if (/mobile|android|iphone|ipad|phone/i.test(userAgent)) {
            return 'mobile';
        } else if (/tablet|ipad/i.test(userAgent)) {
            return 'tablet';
        } else {
            return 'desktop';
        }
    }

    checkReturnVisitor() {
        return localStorage.getItem('quindio_return_visitor') === 'true';
    }

    setupFormIntegration() {
        // Integrar con formulario de cotización rápida existente
        const quoteForm = document.getElementById('quote-form');
        if (quoteForm) {
            this.enhanceQuoteForm(quoteForm);
        }

        // Integrar con cualquier formulario de contacto
        const contactForms = document.querySelectorAll('form[action*="contact"], form[action*="quote"]');
        contactForms.forEach(form => {
            this.enhanceContactForm(form);
        });
    }

    enhanceQuoteForm(form) {
        // Agregar tracking al formulario existente
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const formData = new FormData(form);
            const leadData = this.formToLeadData(formData);
            
            // Enviar a sistema de automatización
            const result = await this.sendLeadToAutomation(leadData);
            
            if (result.success) {
                console.log('✅ Lead enviado al sistema de automatización:', result.lead_id);
                
                // Continuar con el comportamiento normal del formulario (abrir WhatsApp)
                this.proceedWithWhatsApp(leadData);
            } else {
                console.error('❌ Error al enviar lead:', result.error);
                // Continuar con el comportamiento normal aunque falle
                this.proceedWithWhatsApp(leadData);
            }
        });
    }

    enhanceContactForm(form) {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const formData = new FormData(form);
            const leadData = this.formToLeadData(formData);
            
            const result = await this.sendLeadToAutomation(leadData);
            
            if (result.success) {
                console.log('✅ Lead enviado al sistema de automatización:', result.lead_id);
            }
            
            // Continuar con el comportamiento normal del formulario
            form.submit();
        });
    }

    formToLeadData(formData) {
        return {
            nombre: formData.get('name') || formData.get('nombre') || '',
            telefono: formData.get('phone') || formData.get('telefono') || formData.get('telefono_whatsapp') || '',
            email: formData.get('email') || '',
            mensaje: formData.get('message') || formData.get('mensaje') || '',
            destino: formData.get('destination') || formData.get('destino') || '',
            fecha_deseada: formData.get('date') || formData.get('fecha_deseada') || '',
            num_personas: formData.get('passengers') || formData.get('num_personas') || '',
            presupuesto: formData.get('budget') || formData.get('presupuesto') || '',
            plan_interes: formData.get('plan') || formData.get('plan_interes') || '',
            // Datos de sesión
            session_data: this.sessionData,
            source: 'website',
            referral_source: document.referrer || 'direct'
        };
    }

    async sendLeadToAutomation(leadData) {
        try {
            const response = await fetch(`${this.apiBaseUrl}/lead`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(leadData)
            });

            const result = await response.json();
            return result;
        } catch (error) {
            console.error('Error al conectar con API de automatización:', error);
            return { success: false, error: error.message };
        }
    }

    proceedWithWhatsApp(leadData) {
        // Continuar con el comportamiento original de abrir WhatsApp
        const message = this.buildWhatsAppMessage(leadData);
        const whatsappUrl = `https://wa.me/573174426044?text=${encodeURIComponent(message)}`;
        window.open(whatsappUrl, '_blank');
    }

    buildWhatsAppMessage(leadData) {
        return `🌿 COTIZACIÓN RÁPIDA - Quindío Travel\n\n` +
               `👤 Nombre: ${leadData.nombre}\n` +
               `📅 Fecha deseada: ${leadData.fecha_deseada || 'Por definir'}\n` +
               `🎯 Destino: ${leadData.destino || 'Eje Cafetero'}\n` +
               `👥 Pasajeros: ${leadData.num_personas || 'Por definir'}\n\n` +
               `🏆 RNT 18152 - Operador Turístico Eje Cafetero\n\n` +
               `¿Me pueden dar información y precio disponible?`;
    }

    setupWhatsAppIntegration() {
        // Rastrear clics en enlaces de WhatsApp
        document.addEventListener('click', (e) => {
            const whatsappLink = e.target.closest('a[href*="wa.me"], a[href*="whatsapp"]');
            if (whatsappLink) {
                this.trackWhatsAppClick(whatsappLink);
            }
        });
    }

    trackWhatsAppClick(link) {
        const leadData = {
            nombre: 'Interesado WhatsApp',
            telefono: this.extractPhoneFromLink(link),
            mensaje: this.extractMessageFromLink(link),
            whatsapp_clicked: true,
            session_data: this.sessionData,
            source: 'whatsapp_click'
        };

        // Enviar click tracking al sistema
        this.sendLeadToAutomation(leadData);
    }

    extractPhoneFromLink(link) {
        const href = link.getAttribute('href');
        const match = href.match(/wa\.me\/(\d+)/);
        return match ? match[1] : '573174426044';
    }

    extractMessageFromLink(link) {
        const href = link.getAttribute('href');
        const url = new URL(href);
        const textParam = url.searchParams.get('text');
        return textParam ? decodeURIComponent(textParam) : 'Interés en planes turísticos';
    }

    setupPeriodicSync() {
        // Sincronizar datos de sesión periódicamente
        setInterval(() => {
            this.syncSessionData();
        }, 30000); // Cada 30 segundos

        // Sincronizar al salir de la página
        window.addEventListener('beforeunload', () => {
            this.syncSessionData();
            this.markAsReturnVisitor();
        });
    }

    async syncSessionData() {
        try {
            const response = await fetch(`${this.apiBaseUrl}/session`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.sessionData)
            });
            
            if (response.ok) {
                console.log('📊 Datos de sesión sincronizados');
            }
        } catch (error) {
            // Silencioso para no afectar la experiencia del usuario
            console.log('No se pudo sincronizar sesión (servidor no disponible)');
        }
    }

    markAsReturnVisitor() {
        localStorage.setItem('quindio_return_visitor', 'true');
    }

    // Método para predecir probabilidad de conversión (uso opcional)
    async predictConversion(leadData) {
        try {
            const response = await fetch(`${this.apiBaseUrl}/analytics/predict`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(leadData)
            });

            const result = await response.json();
            return result.success ? result.prediction : null;
        } catch (error) {
            console.error('Error al predecir conversión:', error);
            return null;
        }
    }

    // Método para obtener estadísticas del sistema (uso opcional)
    async getSystemStats() {
        try {
            const response = await fetch(`${this.apiBaseUrl}/stats`);
            const result = await response.json();
            return result.success ? result.stats : null;
        } catch (error) {
            console.error('Error al obtener estadísticas:', error);
            return null;
        }
    }
}

// Inicializar integración cuando el DOM esté listo
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        window.leadAutomation = new LeadAutomationIntegration();
    });
} else {
    window.leadAutomation = new LeadAutomationIntegration();
}

// Funciones helper globales para uso manual
window.createLead = async (leadData) => {
    if (window.leadAutomation) {
        return await window.leadAutomation.sendLeadToAutomation(leadData);
    }
    return { success: false, error: 'Sistema no inicializado' };
};

window.predictLeadConversion = async (leadData) => {
    if (window.leadAutomation) {
        return await window.leadAutomation.predictConversion(leadData);
    }
    return null;
};

window.getSystemStats = async () => {
    if (window.leadAutomation) {
        return await window.leadAutomation.getSystemStats();
    }
    return null;
};