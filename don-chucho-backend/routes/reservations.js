const express = require('express');
const router = express.Router();
const reservationService = require('../services/reservationService');

function validateReservationPayload(payload) {
    const requiredFields = ['plan', 'category', 'transportation', 'date', 'adults', 'name', 'whatsapp', 'email', 'paymentMethod'];
    const missing = requiredFields.filter((field) => !payload[field]);
    return missing;
}

router.post('/', async (req, res) => {
    try {
        const missingFields = validateReservationPayload(req.body);
        if (missingFields.length > 0) {
            return res.status(400).json({
                success: false,
                error: 'Missing required reservation fields',
                missingFields
            });
        }

        const reservation = await reservationService.createReservation(req.body);

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
