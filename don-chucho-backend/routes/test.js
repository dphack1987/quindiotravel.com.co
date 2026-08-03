const express = require('express');
const router = express.Router();
const { authMiddleware } = require('../middleware/auth');
const emailService = require('../services/emailService');

// Endpoint protegido para enviar email de prueba
router.post('/email', authMiddleware, async (req, res) => {
    try {
        const { to, subject, text, html } = req.body;
        if (!to) return res.status(400).json({ success: false, error: 'Missing `to` field' });

        const info = await emailService.sendEmail(to, subject || 'Prueba de correo', text || '', html || null);
        res.json({ success: true, messageId: info?.messageId || null });
    } catch (error) {
        console.error('Test email error:', error);
        res.status(500).json({ success: false, error: error.message || 'Error sending test email' });
    }
});

module.exports = router;
