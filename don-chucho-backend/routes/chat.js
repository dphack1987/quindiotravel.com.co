const express = require('express');
const router = express.Router();
const openaiService = require('../services/openaiService');
const knowledgeBase = require('../services/knowledgeBase');
const { getDatabase } = require('../config/database');

// API para chat desde el frontend web
router.post('/message', async (req, res) => {
    try {
        const { message, sessionId, conversationHistory = [] } = req.body;
        
        if (!message) {
            return res.status(400).json({ error: 'Message is required' });
        }

        console.log(`💬 Web Chat Message: ${message}`);

        // Generar respuesta con IA
        const aiResponse = await openaiService.generateResponse(message, conversationHistory);
        
        // Buscar información adicional en base de conocimiento
        const searchResults = knowledgeBase.buscarPorPalabraClave(message);
        let additionalInfo = null;
        
        if (searchResults.length > 0) {
            additionalInfo = knowledgeBase.formatearRespuesta(searchResults);
        }

        // Guardar conversación en base de datos
        const db = getDatabase();
        const conversations = db.collection('web_conversations');
        const now = new Date();
        const savedHistory = Array.isArray(conversationHistory) ? conversationHistory : [];

        const historyEntries = savedHistory.map(item => ({
            role: item.role || 'user',
            content: item.content || '',
            timestamp: item.timestamp ? new Date(item.timestamp) : now
        }));

        historyEntries.push({ role: 'user', content: message, timestamp: now });
        historyEntries.push({ role: 'assistant', content: aiResponse, timestamp: now });

        await conversations.updateOne(
            { sessionId: sessionId },
            {
                $set: {
                    sessionId,
                    lastMessage: message,
                    lastResponse: aiResponse,
                    lastUpdate: now,
                    source: 'web',
                    history: historyEntries
                },
                $inc: { messageCount: 1 }
            },
            { upsert: true }
        );

        // Responder
        res.json({
            response: aiResponse,
            additionalInfo: additionalInfo,
            timestamp: now
        });

    } catch (error) {
        console.error('Chat API Error:', error);
        res.status(500).json({ 
            error: 'Error processing message',
            fallback: 'Perdón, viajero. Tuve un pequeño problema, pero ya estoy mejor. ¿Podrías repetir tu pregunta?'
        });
    }
});

// Obtener historial de conversación
router.get('/history/:sessionId', async (req, res) => {
    try {
        const { sessionId } = req.params;
        const db = getDatabase();
        const conversations = db.collection('web_conversations');
        
        const conversation = await conversations.findOne({ sessionId });
        
        if (!conversation) {
            return res.json({ history: [] });
        }

        res.json({ 
            history: conversation.history || [],
            lastUpdate: conversation.lastUpdate
        });

    } catch (error) {
        console.error('History Error:', error);
        res.status(500).json({ error: 'Error fetching history' });
    }
});

// Iniciar nueva sesión de chat
router.post('/session', async (req, res) => {
    try {
        const { source = 'web' } = req.body;
        const sessionId = `session_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
        
        const db = getDatabase();
        const conversations = db.collection('web_conversations');
        
        await conversations.insertOne({
            sessionId,
            source,
            startedAt: new Date(),
            messageCount: 0,
            history: []
        });

        res.json({ 
            sessionId,
            message: '¡Buenos días, viajero! 👋 Soy Don Chucho, el asistente virtual de Quindío Travel. ¿En qué puedo ayudarte hoy?'
        });

    } catch (error) {
        console.error('Session Error:', error);
        res.status(500).json({ error: 'Error creating session' });
    }
});

// Endpoint para obtener quick replies
router.get('/quick-replies', (req, res) => {
    const { context } = req.query;
    
    const quickReplies = {
        initial: [
            { id: 'planes', title: '🗺️ Ver planes turísticos' },
            { id: 'destinos', title: '🏛️ Destinos populares' },
            { id: 'cotizar', title: '💰 Cotizar viaje' },
            { id: 'consejos', title: '💡 Consejos locales' }
        ],
        planes: [
            { id: '3d', title: 'Plan 3D/2N' },
            { id: '4d', title: 'Plan 4D/3N' },
            { id: '5d', title: 'Plan 5D/4N' },
            { id: 'premium', title: 'Premium VIP' }
        ],
        destinos: [
            { id: 'salento', title: 'Salento' },
            { id: 'valle', title: 'Valle de Cocora' },
            { id: 'cafe', title: 'Parque del Café' },
            { id: 'termales', title: 'Termales' }
        ],
        cotizar: [
            { id: '1-2', title: '1-2 personas' },
            { id: '3-4', title: '3-4 personas' },
            { id: '5+', title: '5+ personas' },
            { id: 'empresas', title: 'Empresas' }
        ],
        consejos: [
            { id: 'clima', title: 'Clima' },
            { id: 'que llevar', title: 'Qué llevar' },
            { id: 'seguridad', title: 'Seguridad' },
            { id: 'fotos', title: 'Fotos' }
        ]
    };

    const replies = quickReplies[context] || quickReplies.initial;
    res.json({ quickReplies: replies });
});

// Escalar a humano
router.post('/escalate', async (req, res) => {
    try {
        const { sessionId, message, context } = req.body;
        
        const db = getDatabase();
        const escalations = db.collection('escalations');
        
        await escalations.insertOne({
            sessionId,
            message,
            context,
            timestamp: new Date(),
            status: 'pending'
        });

        res.json({
            success: true,
            whatsappLink: `https://wa.me/${process.env.QUINDIO_WHATSAPP}?text=Hola%20Quind%C3%ADo%20Travel,%20necesito%20ayuda%20de%20un%20agente%20humano`
        });

    } catch (error) {
        console.error('Escalation Error:', error);
        res.status(500).json({ error: 'Error processing escalation' });
    }
});

module.exports = router;