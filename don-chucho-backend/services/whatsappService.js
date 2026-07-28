const axios = require('axios');
const openaiService = require('./openaiService');
const { getDatabase } = require('../config/database');

class WhatsAppService {
    async processMessage(phoneNumber, message) {
        try {
            // Obtener historial de conversación
            const db = getDatabase();
            const conversations = db.collection('conversations');
            
            // Buscar conversación existente
            let conversation = await conversations.findOne({
                phoneNumber: phoneNumber,
                status: 'active'
            });
            
            let conversationHistory = [];
            
            if (conversation) {
                conversationHistory = conversation.messages || [];
            } else {
                // Crear nueva conversación
                conversation = {
                    phoneNumber: phoneNumber,
                    status: 'active',
                    startedAt: new Date(),
                    messages: [],
                    metadata: {
                        firstContact: true,
                        source: 'whatsapp'
                    }
                };
                await conversations.insertOne(conversation);
            }
            
            // Agregar mensaje del usuario al historial
            conversationHistory.push({
                role: 'user',
                content: message,
                timestamp: new Date()
            });
            
            // Generar respuesta con IA
            const aiResponse = await openaiService.generateResponse(message, conversationHistory);
            
            // Agregar respuesta de Don Chucho al historial
            conversationHistory.push({
                role: 'assistant',
                content: aiResponse,
                timestamp: new Date()
            });
            
            // Actualizar conversación en base de datos
            await conversations.updateOne(
                { phoneNumber: phoneNumber },
                {
                    $set: {
                        messages: conversationHistory,
                        lastMessageAt: new Date(),
                        metadata: {
                            ...conversation.metadata,
                            firstContact: false
                        }
                    }
                }
            );
            
            // Enviar respuesta por WhatsApp
            await this.sendMessage(phoneNumber, aiResponse);
            
            // Detectar si necesita escalar a humano
            if (this.shouldEscalateToHuman(message, aiResponse)) {
                await this.escalateToHuman(phoneNumber, message, aiResponse);
            }
            
        } catch (error) {
            console.error('Error processing message:', error);
            // Enviar mensaje de error
            await this.sendMessage(phoneNumber, "Perdón, viajero. Tuve un pequeño problema, pero ya estoy mejor. ¿Podrías repetir tu pregunta?");
        }
    }

    async sendMessage(phoneNumber, message) {
        try {
            const url = `https://graph.facebook.com/${process.env.WHATSAPP_API_VERSION}/${process.env.WHATSAPP_PHONE_NUMBER_ID}/messages`;
            
            const response = await axios.post(url, {
                messaging_product: 'whatsapp',
                to: phoneNumber,
                text: {
                    body: message
                }
            }, {
                headers: {
                    'Authorization': `Bearer ${process.env.WHATSAPP_ACCESS_TOKEN}`,
                    'Content-Type': 'application/json'
                }
            });
            
            console.log(`✅ Message sent to ${phoneNumber}`);
            return response.data;
            
        } catch (error) {
            console.error('Error sending WhatsApp message:', error.response?.data || error.message);
            throw error;
        }
    }

    shouldEscalateToHuman(userMessage, aiResponse) {
        const escalationKeywords = ['humano', 'agente', 'persona', 'hablar con alguien', 'complejo', 'urgente'];
        const messageLower = userMessage.toLowerCase();
        
        return escalationKeywords.some(keyword => messageLower.includes(keyword));
    }

    async escalateToHuman(phoneNumber, userMessage, aiResponse) {
        try {
            const escalationMessage = `📞 *ESCOALAMIENTO A AGENTE HUMANO*\n\nHola, soy Don Chucho. Tu consulta: "${userMessage}"\n\nMi respuesta: "${aiResponse}"\n\nSi necesitas más ayuda, te conecto con un agente humano de Quindío Travel.`;
            
            await this.sendMessage(phoneNumber, escalationMessage);
            
            // Notificar al equipo humano (simulado)
            console.log(`🔔 ESCALATION: ${phoneNumber} - ${userMessage}`);
            
            // Enviar mensaje final con opción de contacto directo
            setTimeout(async () => {
                const finalMessage = `🤠 *Don Chucho - Arriero Guía*\n\nTe conecto directamente con WhatsApp de Quindío Travel:\n\n📱 https://wa.me/${process.env.QUINDIO_WHATSAPP}?text=Hola%20Quind%C3%ADo%20Travel,%20habl%C3%A9%20con%20Don%20Chucho%20y%20necesito%20ayuda%20urgente`;
                
                await this.sendMessage(phoneNumber, finalMessage);
            }, 2000);
            
        } catch (error) {
            console.error('Error in escalation:', error);
        }
    }

    async sendQuickReplyMessage(phoneNumber, message, quickReplies) {
        try {
            const url = `https://graph.facebook.com/${process.env.WHATSAPP_API_VERSION}/${process.env.WHATSAPP_PHONE_NUMBER_ID}/messages`;
            
            const buttons = quickReplies.map(reply => ({
                type: 'reply',
                reply: {
                    id: reply.id,
                    title: reply.title
                }
            }));
            
            const response = await axios.post(url, {
                messaging_product: 'whatsapp',
                to: phoneNumber,
                type: 'interactive',
                interactive: {
                    type: 'button',
                    body: {
                        text: message
                    },
                    action: {
                        buttons: buttons
                    }
                }
            }, {
                headers: {
                    'Authorization': `Bearer ${process.env.WHATSAPP_ACCESS_TOKEN}`,
                    'Content-Type': 'application/json'
                }
            });
            
            return response.data;
            
        } catch (error) {
            console.error('Error sending quick reply:', error);
            // Fallback a mensaje simple
            await this.sendMessage(phoneNumber, message);
        }
    }
}

module.exports = new WhatsAppService();