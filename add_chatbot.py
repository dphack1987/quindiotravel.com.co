"""
Añadir Chatbot Básico para Atención 24/7
Integración con WhatsApp con respuestas automáticas
"""

from pathlib import Path

def add_chatbot_to_index():
    """Añade chatbot flotante a index.html"""
    
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Añadir chatbot flotante antes del footer
    chatbot_html = '''
    <!-- Chatbot Flotante -->
    <div class="chatbot-container" id="chatbot">
        <div class="chatbot-header" onclick="toggleChatbot()">
            <div class="chatbot-header-content">
                <i class="fas fa-robot"></i>
                <span>Asistente Quindío Travel</span>
            </div>
            <button class="chatbot-close"><i class="fas fa-times"></i></button>
        </div>
        
        <div class="chatbot-body" id="chatbot-body">
            <div class="chatbot-messages" id="chatbot-messages">
                <div class="message bot-message">
                    <div class="message-content">
                        <p>¡Hola! 👋 Soy el asistente virtual de Quindío Travel. ¿En qué puedo ayudarte hoy?</p>
                        <div class="quick-replies">
                            <button class="quick-reply" onclick="sendQuickReply('planes')">🗺️ Ver Planes</button>
                            <button class="quick-reply" onclick="sendQuickReply('precios')">💰 Precios</button>
                            <button class="quick-reply" onclick="sendQuickReply('contacto')">📞 Contacto</button>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="chatbot-input">
                <input type="text" id="chatbot-input" placeholder="Escribe tu mensaje..." onkeypress="handleKeyPress(event)">
                <button onclick="sendMessage()"><i class="fas fa-paper-plane"></i></button>
            </div>
        </div>
        
        <div class="chatbot-toggle" onclick="toggleChatbot()">
            <i class="fab fa-whatsapp"></i>
        </div>
    </div>
'''
    
    # Buscar el footer para añadir chatbot antes
    footer_start = '<footer'
    if footer_start in content:
        content = content.replace(footer_start, chatbot_html + '\n' + footer_start)
        print("[OK] Chatbot HTML añadido")
    
    # Añadir JavaScript para el chatbot
    chatbot_js = '''
    <script>
    let chatbotOpen = false;
    
    function toggleChatbot() {
        const chatbot = document.getElementById('chatbot');
        const chatbotBody = document.getElementById('chatbot-body');
        chatbotOpen = !chatbotOpen;
        
        if (chatbotOpen) {
            chatbotBody.style.display = 'block';
            chatbot.classList.add('chatbot-open');
        } else {
            chatbotBody.style.display = 'none';
            chatbot.classList.remove('chatbot-open');
        }
    }
    
    function sendMessage() {
        const input = document.getElementById('chatbot-input');
        const message = input.value.trim();
        
        if (message) {
            addMessage(message, 'user-message');
            input.value = '';
            
            // Simular respuesta del bot
            setTimeout(() => {
                const response = getBotResponse(message);
                addMessage(response, 'bot-message');
            }, 1000);
        }
    }
    
    function sendQuickReply(type) {
        let message = '';
        let response = '';
        
        switch(type) {
            case 'planes':
                message = 'Quiero ver los planes disponibles';
                response = 'Tenemos 6 planes increíbles desde 2 días hasta 5 días. Puedes ver todos los planes en nuestra sección de <a href="planes.html">Planes Turísticos</a>. ¿Te gustaría información sobre algún plan específico?';
                break;
            case 'precios':
                message = '¿Cuáles son los precios?';
                response = 'Nuestros precios varían según el plan, categoría de alojamiento y temporada. Desde $430.000 COP por persona para planes económicos hasta $3.420.000 COP para experiencias VIP. ¿Te gustaría cotizar un plan específico?';
                break;
            case 'contacto':
                message = 'Información de contacto';
                response = 'Puedes contactarnos por WhatsApp al +57 317 442 6044 o por email a gerencia@quindiotravel.net. También estamos disponibles 24/7 para atender tus consultas.';
                break;
        }
        
        addMessage(message, 'user-message');
        setTimeout(() => {
            addMessage(response, 'bot-message');
        }, 500);
    }
    
    function addMessage(text, className) {
        const messagesContainer = document.getElementById('chatbot-messages');
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${className}`;
        
        const messageContent = document.createElement('div');
        messageContent.className = 'message-content';
        messageContent.innerHTML = `<p>${text}</p>`;
        
        messageDiv.appendChild(messageContent);
        messagesContainer.appendChild(messageDiv);
        
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }
    
    function getBotResponse(message) {
        const lowerMessage = message.toLowerCase();
        
        if (lowerMessage.includes('precio') || lowerMessage.includes('costo') || lowerMessage.includes('tarifa')) {
            return 'Nuestros precios varían según el plan y categoría. Desde $430.000 COP hasta $3.420.000 COP por persona. Para una cotización exacta, te recomiendo usar nuestro <a href="https://wa.me/573174426044">WhatsApp</a> para atención personalizada.';
        } else if (lowerMessage.includes('plan') || lowerMessage.includes('paquete')) {
            return 'Tenemos 6 planes increíbles: Escapada Cafetera (2D/1N), Aventura Natural (3D/2N), Experiencia Completa (4D/3N), Relax y Aventura (4D/3N), Experiencia Premium (4D/3N) y La Experiencia Definitiva (5D/4N). ¿Te gustaría más detalles sobre alguno?';
        } else if (lowerMessage.includes('hotel') || lowerMessage.includes('alojamiento')) {
            return 'Trabajamos con hoteles certificados de diferentes categorías: estándar, intermedia y VIP. Algunos de nuestros alojamientos son Cabañas La Esmeralda, Finca Hotel Los Girasoles y Hotel Campestre Café Café.';
        } else if (lowerMessage.includes('contacto') || lowerMessage.includes('whatsapp')) {
            return 'Puedes contactarnos directamente por WhatsApp al +57 317 442 6044 para atención personalizada 24/7.';
        } else if (lowerMessage.includes('reserva') || lowerMessage.includes('cotizar')) {
            return 'Para realizar una reserva o cotización, te recomiendo usar nuestro <a href="https://wa.me/573174426044">WhatsApp</a> para atención inmediata con nuestros asesores.';
        } else {
            return 'Gracias por tu mensaje. Para una respuesta más detallada, te recomiendo contactarnos por WhatsApp al +57 317 442 6044 donde nuestros asesores te ayudarán personalmente.';
        }
    }
    
    function handleKeyPress(event) {
        if (event.key === 'Enter') {
            sendMessage();
        }
    }
    </script>
'''
    
    # Buscar </body> para añadir script antes
    body_end = '</body>'
    if body_end in content:
        content = content.replace(body_end, chatbot_js + '\n' + body_end)
        print("[OK] JavaScript del chatbot añadido")
    
    # Guardar cambios
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

if __name__ == "__main__":
    print("Añadiendo chatbot para atención 24/7...")
    print("=" * 70)
    
    add_chatbot_to_index()
    
    print("\n" + "=" * 70)
    print("Chatbot añadido exitosamente")