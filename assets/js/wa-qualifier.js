/**
 * WhatsApp Qualifier Bot - Simula chatbot de WA.Expert
 * 4 preguntas con botones → mensaje estructurado → WhatsApp
 */
(function() {
    const WA_NUMBER = '573174426044';
    
    const plans = {
        'escapada': { name: 'Escapada Cafetera', days: '2D/1N', price: '$425K', emoji: '☕' },
        'aventura': { name: 'Aventura Natural', days: '3D/2N', price: '$562K', emoji: '🌿' },
        'completa': { name: 'Experiencia Completa', days: '4D/3N', price: '$777K', emoji: '⭐' },
        'granquindio': { name: 'Gran Quindío', days: '5D/4N', price: '$1.05M', emoji: '👑' }
    };

    const groups = {
        'pareja': 'Pareja',
        'familia': 'Familia (con niños)',
        'amigos': 'Grupo de amigos',
        'empresa': 'Empresa / Equipo'
    };

    const transports = {
        'propio': 'Vehículo propio',
        'taxi': 'Radio Taxi',
        'bus': 'Buseta privada'
    };

    let state = {
        step: 0,
        plan: null,
        group: null,
        people: null,
        transport: null
    };

    function buildMessage() {
        const p = plans[state.plan];
        const g = groups[state.group];
        const t = transports[state.transport];
        return `Hola Quindío Travel 🌿

Quiero información sobre:
📋 Plan ${p.name} (${p.days})
👥 ${state.people} personas (${g})
🚗 Transporte: ${t}
📅 Fechas: Por confirmar

¿Tienen disponibilidad?

RNT 18152`;
    }

    function getWhatsAppUrl() {
        return `https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(buildMessage())}`;
    }

    function renderChatbot() {
        const container = document.getElementById('wa-qualifier');
        if (!container) return;

        const steps = [
            {
                bot: '¡Hola! 👋 Soy tu asistente de viajes. Te ayudo a armar tu plan perfecto en 4 pasos.',
                question: '¿Qué plan te interesa?',
                options: Object.entries(plans).map(([k, v]) => ({ key: k, label: `${v.emoji} ${v.name} (${v.days})`, sub: `Desde ${v.price}/persona` }))
            },
            {
                bot: '¡Gran elección! ¿Viajas con quién?',
                question: '¿Cuál es tu grupo?',
                options: Object.entries(groups).map(([k, v]) => ({ key: k, label: v }))
            },
            {
                bot: 'Perfecto. ¿Cuántas personas serían?',
                question: '¿Cuántos viajan?',
                options: [
                    { key: '2', label: '2 personas' },
                    { key: '3-4', label: '3-4 personas' },
                    { key: '5-8', label: '5-8 personas' },
                    { key: '9+', label: '9+ personas (grupo)' }
                ]
            },
            {
                bot: 'Último paso. ¿Cómo llegan al Quindío?',
                question: 'Transporte:',
                options: Object.entries(transports).map(([k, v]) => ({ key: k, label: v }))
            }
        ];

        const currentStep = state.step;
        let html = '';

        if (currentStep >= steps.length) {
            // Show summary + WhatsApp CTA
            const p = plans[state.plan];
            const g = groups[state.group];
            const t = transports[state.transport];
            html = `
                <div class="wa-bot-message">
                    <div class="wa-bot-avatar">🌿</div>
                    <div class="wa-bot-bubble">
                        ¡Listo! Tu plan personalizado está armado. Te enviamos los detalles por WhatsApp con disponibilidad real y precio final.
                    </div>
                </div>
                <div class="wa-bot-summary">
                    <div class="wa-summary-item"><span>📋</span> <strong>${p.name}</strong> ${p.days}</div>
                    <div class="wa-summary-item"><span>👥</span> ${state.people} personas (${g})</div>
                    <div class="wa-summary-item"><span>🚗</span> ${t}</div>
                    <div class="wa-summary-item"><span>💰</span> Desde ${p.price}/persona</div>
                </div>
                <a href="${getWhatsAppUrl()}" target="_blank" rel="noopener" class="wa-bot-cta">
                    <i class="fab fa-whatsapp"></i> Enviar mi cotización por WhatsApp
                </a>
                <button class="wa-bot-restart" onclick="window.waQualifier.reset()">
                    <i class="fas fa-redo"></i> Empezar de nuevo
                </button>
            `;
        } else {
            const step = steps[currentStep];
            // Show previous bot messages
            for (let i = 0; i < currentStep; i++) {
                html += `<div class="wa-bot-message">
                    <div class="wa-bot-avatar">🌿</div>
                    <div class="wa-bot-bubble">${steps[i].bot}</div>
                </div>`;
            }
            // Current question
            html += `<div class="wa-bot-message">
                <div class="wa-bot-avatar">🌿</div>
                <div class="wa-bot-bubble">${step.bot}</div>
            </div>
            <div class="wa-bot-question">${step.question}</div>
            <div class="wa-bot-options">`;
            
            step.options.forEach(opt => {
                html += `<button class="wa-bot-btn" onclick="window.waQualifier.select('${currentStep}', '${opt.key}')">
                    ${opt.label}${opt.sub ? `<span class="wa-bot-sub">${opt.sub}</span>` : ''}
                </button>`;
            });
            
            html += `</div>`;
        }

        container.innerHTML = html;
    }

    window.waQualifier = {
        select: function(step, key) {
            switch(step) {
                case '0': state.plan = key; break;
                case '1': state.group = key; break;
                case '2': state.people = key; break;
                case '3': state.transport = key; break;
            }
            state.step++;
            renderChatbot();
        },
        reset: function() {
            state = { step: 0, plan: null, group: null, people: null, transport: null };
            renderChatbot();
        },
        init: function() {
            renderChatbot();
        }
    };

    document.addEventListener('DOMContentLoaded', function() {
        if (document.getElementById('wa-qualifier')) {
            renderChatbot();
        }
    });
})();
