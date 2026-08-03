const express = require('express');
const router = express.Router();
const WhatsAppService = require('../services/whatsappService');
const { getDatabase } = require('../config/database');

// Verificación del webhook de WhatsApp
router.get('/whatsapp', (req, res) => {
    const verifyToken = process.env.WHATSAPP_WEBHOOK_VERIFY_TOKEN;
    const mode = req.query['hub.mode'];
    const token = req.query['hub.verify_token'];
    const challenge = req.query['hub.challenge'];

    if (mode && token) {
        if (mode === 'subscribe' && token === verifyToken) {
            console.log('Webhook verificado con éxito.');
            return res.status(200).send(challenge);
        } else {
            console.warn('Webhook verification failed.');
            return res.sendStatus(403);
        }
    }

    res.sendStatus(400);
});

// Recepción de mensajes de WhatsApp
router.post('/whatsapp', async (req, res) => {
    try {
        const entry = req.body.entry?.[0];
        const changes = entry?.changes?.[0];
        const value = changes?.value;
        const messages = value?.messages;
        const metadata = value?.metadata;

        if (!messages || messages.length === 0) {
            return res.status(200).json({ success: true });
        }

        const message = messages[0];
        const from = message.from;
        const text = message.text?.body || '';

        console.log('WhatsApp webhook received message from:', from);

        if (text) {
            await WhatsAppService.processMessage(from, text);
        }

        res.status(200).json({ success: true });
    } catch (error) {
        console.error('WhatsApp webhook error:', error);
        res.status(500).json({ error: 'Webhook processing failed' });
    }
});

module.exports = router;
