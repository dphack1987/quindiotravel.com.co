// Don Chucho Chat System - Frontend Integration
// Conecta el chat web con el backend de Don Chucho

class DonChuchoChat {
    constructor() {
        this.chatOpen = false;
        this.sessionId = null;
        this.conversationHistory = [];
        
        // Configuración dinámica basada en entorno
        this.backendUrl = this.getBackendUrl();
        this.apiKey = this.getApiKey();
        
        this.init();
    }
    
    getBackendUrl() {
        // Prioridad: variable de entorno > configuración dinámica > localhost
        if (window.DON_CHUCHO_BACKEND_URL) {
            return window.DON_CHUCHO_BACKEND_URL;
        }
        
        // Detectar entorno automáticamente
        const hostname = window.location.hostname;
        if (hostname === 'localhost' || hostname === '127.0.0.1') {
            return 'http://localhost:3000';
        } else if (hostname.includes('quindiotravel.com.co')) {
            return 'https://api.quindiotravel.com.co';
        } else {
            // Fallback a localhost para desarrollo
            return 'http://localhost:3000';
        }
    }
    
    getApiKey() {
        // No exponer API key en código cliente
        // En producción, la autenticación debería manejarse del lado del servidor
        // o usando un sistema de tokens temporales
        if (window.DON_CHUCHO_API_KEY) {
            return window.DON_CHUCHO_API_KEY;
        }
        
        // Para desarrollo, usar una key genérica que el backend debería validar
        // En producción, esto debería ser null o un token temporal
        return null;
    }
    
    async init() {
        try {
            // Crear sesión
            const headers = {
                'Content-Type': 'application/json'
            };
            
            // Solo agregar API key si está configurada
            if (this.apiKey) {
                headers['x-api-key'] = this.apiKey;
            }
            
            const response = await fetch(`${this.backendUrl}/api/chat/session`, {
                method: 'POST',
                headers: headers,
                body: JSON.stringify({ source: 'web' })
            });
            
            if (response.ok) {
                const data = await response.json();
                this.sessionId = data.sessionId;
                console.log('Don Chucho session created:', this.sessionId);
            } else {
                console.error('Failed to create Don Chucho session');
                this.useFallbackMode();
            }
        } catch (error) {
            console.error('Don Chucho backend not available, using fallback mode:', error);
            this.useFallbackMode();
        }
    }
    
    useFallbackMode() {
        this.fallbackMode = true;
        this.sessionId = 'fallback-' + Date.now();
        console.log('Don Chucho running in fallback mode');
    }
    
    async sendMessage(message) {
        if (!message || !message.trim()) return;
        
        // Abrir chat si se envía desde un quick reply o input cuando está cerrado
        if (!this.chatOpen) {
            this.toggleChat();
        }

        // Agregar mensaje del usuario
        this.addMessage(message, 'user-message');
        
        // Mostrar indicador de escritura
        const typingIndicator = this.addTypingIndicator();
        
        try {
            let response;
            
            if (this.fallbackMode) {
                response = await this.getFallbackResponse(message);
            } else {
                const headers = {
                    'Content-Type': 'application/json'
                };
                
                // Solo agregar API key si está configurada
                if (this.apiKey) {
                    headers['x-api-key'] = this.apiKey;
                }
                
                const apiResponse = await fetch(`${this.backendUrl}/api/chat/message`, {
                    method: 'POST',
                    headers: headers,
                    body: JSON.stringify({
                        message: message,
                        sessionId: this.sessionId,
                        conversationHistory: this.conversationHistory
                    })
                });
                
                if (apiResponse.ok) {
                    const data = await apiResponse.json();
                    response = data.response || await this.getFallbackResponse(message);
                } else {
                    throw new Error('Backend error');
                }
            }
            
            // Agregar respuesta del bot
            await new Promise(resolve => setTimeout(resolve, 700));
            if (typingIndicator && typingIndicator.parentNode) {
                typingIndicator.remove();
            }
            this.addMessage(response, 'bot-message');
            
        } catch (error) {
            console.error('Error sending message:', error);
            if (typingIndicator && typingIndicator.parentNode) {
                typingIndicator.remove();
            }
            const fallbackResponse = await this.getFallbackResponse(message);
            this.addMessage(fallbackResponse, 'bot-message');
        }
    }

    addTypingIndicator() {
        const messagesContainer = document.getElementById('don-chucho-messages');
        if (!messagesContainer) return null;

        const typingDiv = document.createElement('div');
        typingDiv.className = 'message bot-message typing-indicator';
        typingDiv.innerHTML = `
            <div class="message-content">
                <p>🤠 Don Chucho está escribiendo...</p>
            </div>
        `;

        messagesContainer.appendChild(typingDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
        return typingDiv;
    }
    
    async getFallbackResponse(message) {
        const lowerMessage = message.toLowerCase();
        
        // Respuestas de Don Chucho basadas en conocimiento local mejorado
        if (lowerMessage.includes('precio') || lowerMessage.includes('costo') || lowerMessage.includes('tarifa')) {
            return '🤠 ¡Vaya, viajero! Nuestros precios varían según el plan:\n\n• Plan 2D/1N: Desde $425.000 COP\n• Plan 3D/2N: Desde $562.000 COP\n• Plan 4D/3N: Desde $777.000 COP\n• Plan 5D/4N: Desde $788.000 COP\n• Plan 6D/4N: Desde $1.008.000 COP\n\nTodo incluye alojamiento, transporte y guías locales RNT 18152. ¿Te gustaría cotizar un plan específico?';
        } else if (lowerMessage.includes('plan') || lowerMessage.includes('paquete')) {
            return '🤠 ¡Excelente elección, compadre! Tenemos varios planes:\n\n🗺️ **Plan 2D/1N**: Escapada rápida - Parque del Café y PANACA\n🗺️ **Plan 3D/2N**: Aventura natural - Incluye PANACA y Parque del Café\n🗺️ **Plan 4D/3N**: Termales y relax - Termales Santa Rosa incluidos\n🗺️ **Plan 5D/4N**: Experiencia cultural - RECUCA y cultura cafetera\n🗺️ **Plan 6D/4N**: Experiencia definitiva - Todo el Eje Cafetero incluido\n\n¿Cuál te llama más la atención?';
        } else if (lowerMessage.includes('hotel') || lowerMessage.includes('alojamiento') || lowerMessage.includes('finca')) {
            return '🤠 ¡Para descansar como en casa! Trabajamos con fincas hoteles certificadas:\n\n🏡 Cabañas La Esmeralda (Estándar) - $1.152.000 cuádruple\n🏡 Finca Hotel Los Girasoles (Intermedia) - $1.588.000 cuádruple\n🏡 Hotel Campestre Café Café (VIP) - $1.770.000 cuádruple\n\nTodas con desayuno incluido y guías locales. ¿Prefieres categoría estándar, intermedia o VIP?';
        } else if (lowerMessage.includes('salento')) {
            return '🤠 ¡Salento es joya del Quindío! Pueblo patrimonio con balcones coloridos y mirador al Valle de Cocora.\n\n✨ Must-see: Mirador Cóndor, Calle Real, artesanías en guadua\n💡 Tips: Sube al mirador al atardecer, lleva cámara para fotos increíbles\n\n¿Quieres incluir Salento en tu viaje?';
        } else if (lowerMessage.includes('valle') || lowerMessage.includes('cocora')) {
            return '🤠 ¡El Valle de Cocora es espectacular! Palmas de cera de hasta 60 metros de altura, el árbol nacional de Colombia.\n\n✨ Actividades: Senderismo, fotografía, naturaleza, observación de colibríes\n💡 Tips: Lleva botas antideslizantes, agua y protector solar\n\n¿Te gustaría caminar por el bosque nuboso?';
        } else if (lowerMessage.includes('cafe') || lowerMessage.includes('parque')) {
            return '🤠 ¡El Parque del Café es imperdible! Atracciones mecánicas, shows culturales y el mejor café del mundo.\n\n✨ Incluye: Museo interactivo, shows, 30 atracciones mecánicas\n💡 Tips: Dedica todo el día, compra pasaporte múltiple\n\n¿Eres amante del café, compadre?';
        } else if (lowerMessage.includes('panaca')) {
            return '🤠 ¡PANACA es increíble! Parque agropecuario con 4.500 animales y 10 estaciones temáticas.\n\n✨ Actividades: Interacción con animales, shows educativos, recorridos\n💡 Tips: Planifica mínimo 4 horas, ideal para familias\n\n¿Te gustaría conocer PANACA?';
        } else if (lowerMessage.includes('termales') || lowerMessage.includes('santa rosa')) {
            return '🤠 ¡Los Termales Santa Rosa son medicina natural! Aguas volcánicas de 45°C ricas en minerales.\n\n✨ Beneficios: Relajación, propiedades terapéuticas, spa\n💡 Tips: Lleva toalla, protector solar, hidratación\n\n¿Quieres un día de relax en los termales?';
        } else if (lowerMessage.includes('recuca')) {
            return '🤠 ¡RECUCA es tradición cafetera pura! Experiencia vivencial del proceso del café.\n\n✨ Actividades: Recolección, beneficio tradicional, cata de café\n💡 Tips: Usa ropa cómoda, cámara para fotos del proceso\n\n¿Te interesa la cultura cafetera?';
        } else if (lowerMessage.includes('mariposario') || lowerMessage.includes('mariposa')) {
            return '🤠 ¡El Mariposario es mágico! Más de 50 especies de mariposas tropicales en jardines botánicos.\n\n✨ Actividades: Observación, ciclo de vida, conservación\n💡 Tips: Ideal para fotografía macro, visite temprano\n\n¿Te gustan las mariposas?';
        } else if (lowerMessage.includes('cabalgata') || lowerMessage.includes('caballo')) {
            return '🤠 ¡Las cabalgatas son experiencia auténtica! Recorridos a caballo por paisajes cafeteros.\n\n✨ Rutas: Valles, cafetales, pueblos\n💡 Tips: Ropa cómoda, experiencia previa no necesaria\n\n¿Te animas a montar a caballo?';
        } else if (lowerMessage.includes('contacto') || lowerMessage.includes('whatsapp')) {
            return '🤠 ¡Para atención personalizada, compadre! Contáctanos:\n\n📱 WhatsApp: +57 317 442 6044\n📧 Email: gerencia@quindiotravel.net\n🌐 Web: www.quindiotravel.com.co\n\nEstamos disponibles 24/7 para ayudarte a planear tu viaje al Eje Cafetero.';
        } else if (lowerMessage.includes('reserva') || lowerMessage.includes('cotizar')) {
            return '🤠 ¡Perfecto, viajero! Para cotizar tu viaje necesito:\n\n👤 ¿Cuántas personas viajan?\n📅 ¿Cuándo quieres viajar?\n🎯 ¿Qué te interesa más? (café, naturaleza, pueblos, termales)\n💰 ¿Qué presupuesto tienes en mente?\n\nCuéntame estos detalles y te preparo una cotización especial con descuento.';
        } else if (lowerMessage.includes('hola') || lowerMessage.includes('buenos') || lowerMessage.includes('buenas')) {
            return '🤠 ¡Hola, compadre! Soy Don Chucho, el asistente virtual de Quindío Travel. Estoy aquí para ayudarte a explorar planes, destinos y opciones de viaje por el Quindío.\n\nPuedo ayudarte con:\n• Planes turísticos\n• Precios y cotizaciones\n• Destinos y atractivos\n• Alojamiento y transporte\n\n¿Qué te gustaría saber?';
        } else if (lowerMessage.includes('gracias') || lowerMessage.includes('muchas gracias')) {
            return '🤠 ¡De nada, compadre! Es un placer ayudarte a descubrir la magia del Eje Cafetero.\n\n¿Hay algo más en lo que pueda ayudarte para tu viaje?';
        } else if (lowerMessage.includes('filandia')) {
            return '🤠 ¡Filandia es encantadora! Pueblo con el mejor mirador del Quindío y artesanías en guadua premium.\n\n✨ Must-see: Mirador 360°, talleres artesanales, gastronomía\n💡 Tips: Compra artesanías de calidad, visita mirador al amanecer\n\n¿Quieres conocer Filandia?';
        } else if (lowerMessage.includes('armenia')) {
            return '🤠 ¡Armenia es la capital del Quindío! Ciudad moderna con acceso a todos los destinos.\n\n✨ Base para: Salento, Filandia, Parque del Café, PANACA\n💡 Tips: Centro de operaciones perfecta, aeropuerto cercano\n\n¿Necesitas información sobre Armenia?';
        } else {
            return '🤠 ¡Gracias por escribir, compadre! Para darte la mejor respuesta, cuéntame:\n\n• ¿Buscas información sobre planes, destinos o precios?\n• ¿Tienes alguna fecha en mente?\n• ¿Cuántas personas viajan?\n• ¿Qué te interesa más? (café, naturaleza, pueblos, termales)\n\nO contáctanos directamente por WhatsApp al +57 317 442 6044 para atención inmediata.';
        }
    }
    
    addMessage(text, className) {
        const messagesContainer = document.getElementById('don-chucho-messages');
        if (!messagesContainer) return;
        
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${className}`;
        
        const messageContent = document.createElement('div');
        messageContent.className = 'message-content';
        
        // Procesar formato markdown simple
        let formattedText = text
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\n/g, '<br>');
        
        messageContent.innerHTML = `<p>${formattedText}</p>`;
        
        messageDiv.appendChild(messageContent);
        messagesContainer.appendChild(messageDiv);
        
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
        
        // Guardar en historial
        this.conversationHistory.push({
            role: className === 'user-message' ? 'user' : 'assistant',
            content: text
        });
    }
    
    toggleChat() {
        this.chatOpen = !this.chatOpen;
        const chatContainer = document.getElementById('don-chucho-chat');
        const chatBody = document.getElementById('don-chucho-body');
        const chatInput = document.getElementById('don-chucho-input');
        
        if (chatContainer && chatBody) {
            chatBody.style.display = this.chatOpen ? 'block' : 'none';
            chatBody.classList.toggle('opened', this.chatOpen);
            chatContainer.classList.toggle('don-chucho-open', this.chatOpen);

            if (this.chatOpen && chatInput) {
                setTimeout(() => chatInput.focus(), 120);
            }
        }
    }

    handleDocumentClick(event) {
        const chatContainer = document.getElementById('don-chucho-chat');
        if (!this.chatOpen || !chatContainer) return;

        if (!chatContainer.contains(event.target)) {
            this.toggleChat();
        }
    }

    handleKeyDown(event) {
        if (event.key === 'Escape' && this.chatOpen) {
            this.toggleChat();
        }
    }
    
    sendQuickReply(type) {
        if (!this.chatOpen) {
            this.toggleChat();
        }

        let message = '';
        
        switch(type) {
            case 'planes':
                message = 'Quiero ver los planes disponibles';
                break;
            case 'precios':
                message = '¿Cuáles son los precios?';
                break;
            case 'contacto':
                message = 'Información de contacto';
                break;
            case 'destinos':
                message = '¿Qué destinos puedo visitar?';
                break;
        }
        
        this.sendMessage(message);
    }
}

// Inicializar Don Chucho cuando el DOM esté listo
let donChucho;

document.addEventListener('DOMContentLoaded', () => {
    donChucho = new DonChuchoChat();
    
    // Exponer funciones globalmente para los onclick del HTML
    window.toggleDonChucho = () => donChucho.toggleChat();
    window.sendDonChuchoMessage = (message) => donChucho.sendMessage(message);
    window.sendDonChuchoQuickReply = (type) => donChucho.sendQuickReply(type);
    window.handleDonChuchoKeyPress = (event) => {
        if (event.key === 'Enter') {
            const input = document.getElementById('don-chucho-input');
            if (input) {
                donChucho.sendMessage(input.value);
                input.value = '';
            }
        }
    };

    document.addEventListener('click', (event) => donChucho.handleDocumentClick(event));
    document.addEventListener('keydown', (event) => donChucho.handleKeyDown(event));
});

console.log('Don Chucho chat system loaded');