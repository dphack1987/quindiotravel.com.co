const express = require('express');
const router = express.Router();
const { body, validationResult } = require('express-validator');
const reservationService = require('../services/reservationService');

const reservationValidation = [
    body('plan').notEmpty().withMessage('Plan is required'),
    body('category').notEmpty().withMessage('Category is required'),
    body('transportation').notEmpty().withMessage('Transportation is required'),
    body('date').isISO8601().withMessage('Date must be valid ISO8601'),
    body('adults').isInt({ min: 1 }).withMessage('Adults must be at least 1'),
    body('name').trim().notEmpty().withMessage('Name is required'),
    body('whatsapp').trim().notEmpty().withMessage('WhatsApp is required'),
    body('email').isEmail().withMessage('Valid email is required'),
    body('paymentMethod').notEmpty().withMessage('Payment method is required')
];

router.post('/', reservationValidation, async (req, res) => {
    try {
        const errors = validationResult(req);
        if (!errors.isEmpty()) {
            return res.status(400).json({ success: false, errors: errors.array() });
        }

        // Optional idempotencyKey in body to prevent duplicates
        const payload = req.body;

        const reservation = await reservationService.createReservation(payload);

        res.json({
            success: true,
            reservationId: reservation._id,
            availability: reservation.availability,
            depositAmount: reservation.depositAmount,
            totalEstimated: reservation.totalEstimated,
            message: reservation.availability === 'available'
                ? 'Tu reserva ha sido recibida. Nuestro equipo te contactará para confirmar disponibilidad y pago del anticipo.'
                : 'Tu reserva está en revisión. Te contactaremos para confirmar disponibilidad o ajustar la fecha.'
        });
    } catch (error) {
        console.error('Reservation error:', error);
        res.status(500).json({
            success: false,
            error: 'Error processing reservation',
            details: error.message
        });
    }
});

router.get('/:id', async (req, res) => {
    try {
        const reservation = await reservationService.getReservationById(req.params.id);
        if (!reservation) {
            return res.status(404).json({ success: false, error: 'Reservation not found' });
        }

        res.json({ success: true, reservation });
    } catch (error) {
        console.error('Get reservation error:', error);
        res.status(500).json({ success: false, error: 'Error fetching reservation' });
    }
});

router.post('/:id/confirm', async (req, res) => {
    try {
        const { paymentReference, paymentMethod } = req.body;
        const reservation = await reservationService.confirmReservation(req.params.id, { paymentReference, paymentMethod });

        res.json({ success: true, reservation, message: 'Reserva confirmada y pago registrado.' });
    } catch (error) {
        console.error('Confirm reservation error:', error);
        res.status(500).json({ success: false, error: 'Error confirming reservation' });
    }
});

module.exports = router;
