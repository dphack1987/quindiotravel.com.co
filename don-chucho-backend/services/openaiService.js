const { Configuration, OpenAIApi } = require('openai');
require('dotenv').config();

const apiKey = process.env.OPENAI_API_KEY;
const configuration = new Configuration({ apiKey });
const openai = apiKey ? new OpenAIApi(configuration) : null;

class OpenAIService {
    async generateResponse(message, conversationHistory = []) {
        try {
            if (!apiKey || !openai) {
                console.warn('OpenAI API key not configured. Returning fallback response.');
                return 'Perdón, viajero. El servicio de IA no está disponible en este momento. Intenta más tarde.';
            }

            const messages = [];

            if (Array.isArray(conversationHistory) && conversationHistory.length > 0) {
                conversationHistory.forEach(item => {
                    if (item.role && item.content) {
                        messages.push({
                            role: item.role,
                            content: item.content
                        });
                    }
                });
            }

            messages.push({
                role: 'user',
                content: message
            });

            const response = await openai.createChatCompletion({
                model: process.env.OPENAI_MODEL || 'gpt-3.5-turbo',
                messages,
                temperature: 0.8,
                max_tokens: 500
            });

            const aiMessage = response.data?.choices?.[0]?.message?.content;

            if (!aiMessage) {
                return 'Perdón, viajero. No pude procesar tu solicitud en este momento. ¿Puedes intentar de nuevo?';
            }

            return aiMessage.trim();
        } catch (error) {
            console.error('OpenAI Service Error:', error.response?.data || error.message || error);
            return 'Perdón, viajero. Tuve un problema al conectar con el motor de IA. Intenta de nuevo en unos minutos.';
        }
    }
}

module.exports = new OpenAIService();
