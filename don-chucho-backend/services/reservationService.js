const { ObjectId } = require('mongodb');
const { getDatabase } = require('../config/database');
const whatsappService = require('./whatsappService');

const DEFAULT_DEPOSIT_PERCENTAGE = Number(process.env.RESERVATION_DEPOSIT_PERCENTAGE || 30);

function normalizePhoneNumber(phone) {
    if (!phone) return '';
    return phone.toString().replace(/\D/g, '');
}

function calculateAmounts(category, transportation, adults, children) {
    const preciosBase = {
        economica: 570000,
        intermedia: 615000,
        intermedia_vip: 1000000,
        vip: 2305000
    };

    const multiplicadoresTransporte = {
        sin_transporte: 1,
        radio_taxi: 1.8,
        placa_blanca: 2.0
    };

    const precioBase = preciosBase[category] || preciosBase.economica;
    const multiplicador = multiplicadoresTransporte[transportation] || 1;
    const precioPersona = Math.round(precioBase * multiplicador);
    const precioNino = Math.round(precioPersona * 0.7);

    const totalAdultos = precioPersona * adults;
    const totalNinos = precioNino * children;
    const totalEstimado = totalAdultos + totalNinos;
    const depositAmount = Math.round((totalEstimado * DEFAULT_DEPOSIT_PERCENTAGE) / 100);

    return {
        precioPersona,
        precioNino,
        totalAdultos,
        totalNinos,
        totalEstimado,
        depositAmount,
        depositPercent: DEFAULT_DEPOSIT_PERCENTAGE
    };
}

async function checkAvailability({ travelDate, category }) {
    const db = getDatabase();
    const reservations = db.collection('reservations');

    const capacityByCategory = {
        economica: 40,
        intermedia: 30,
        intermedia_vip: 20,
        vip: 12
    };

    const date = new Date(travelDate);
    date.setHours(0, 0, 0, 0);

    const reservedCount = await reservations.countDocuments({
        travelDate: date,
        category,
        status: { $in: ['pending', 'confirmed'] }
    });

    const capacity = capacityByCategory[category] || 25;
    return {
        available: reservedCount < capacity,
        capacity,
        reservedCount
    };
}

function buildNotificationMessage(reservation) {
    const availabilityLabel = reservation.availability === 'available' ? 'DISPONIBLE' : 'NO DISPONIBLE / PENDIENTE DE REVISIÓN';
    return `📌 *Nueva Reserva Inteligente*\n\n` +
        `👤 *Cliente:* ${reservation.name}\n` +
        `📱 *WhatsApp:* +${reservation.whatsapp}\n` +
        `📧 *Email:* ${reservation.email}\n` +
        `🎯 *Plan:* ${reservation.plan}\n` +
        `🏨 *Categoría:* ${reservation.category}\n` +
        `🚗 *Transporte:* ${reservation.transportation}\n` +
        `📅 *Fecha:* ${reservation.travelDate.toISOString().split('T')[0]}\n` +
        `👥 *Adultos:* ${reservation.adults} · *Niños:* ${reservation.children}\n` +
        `💰 *Total estimado:* COP ${reservation.totalEstimated.toLocaleString('es-CO')}\n` +
        `💳 *Anticipo ${reservation.depositPercent}%:* COP ${reservation.depositAmount.toLocaleString('es-CO')}\n` +
        `⚠️ *Disponibilidad:* ${availabilityLabel}\n` +
        `📝 *Método de pago preferido:* ${reservation.paymentMethod}\n` +
        `💬 *Comentarios:* ${reservation.comments || 'Ninguno'}\n\n` +
        `📌 Reserva ID: ${reservation._id}`;
}

async function notifyAdmin(reservation) {
    try {
        if (!whatsappService.isWhatsAppConfigured()) {
            console.warn('WhatsApp no está configurado. No se enviará notificación al equipo.');
            return;
        }

        const adminPhone = process.env.QUINDIO_WHATSAPP;
        if (!adminPhone) {
            console.warn('QUINDIO_WHATSAPP no está definido. No se enviará notificación.');
            return;
        }

        const message = buildNotificationMessage(reservation);
        await whatsappService.sendMessage(adminPhone, message);
    } catch (error) {
        console.error('Error notificando al equipo sobre la reserva:', error.message || error);
    }
}

async function createReservation(payload) {
    const db = getDatabase();
    const reservations = db.collection('reservations');

    const adults = Number(payload.adults || 0);
    const children = Number(payload.children || 0);
    const normalizedWhatsApp = normalizePhoneNumber(payload.whatsapp);

    const priceData = calculateAmounts(payload.category, payload.transportation, adults, children);
    const availability = await checkAvailability({ travelDate: payload.date, category: payload.category });

    const reservation = {
        plan: payload.plan,
        category: payload.category,
        transportation: payload.transportation,
        travelDate: new Date(payload.date),
        adults,
        children,
        name: payload.name,
        whatsapp: normalizedWhatsApp,
        email: payload.email,
        paymentMethod: payload.paymentMethod,
        comments: payload.comments || '',
        pricePerPerson: priceData.precioPersona,
        totalAdults: priceData.totalAdultos,
        totalChildren: priceData.totalNinos,
        totalEstimated: priceData.totalEstimado,
        depositAmount: priceData.depositAmount,
        depositPercent: priceData.depositPercent,
        availability: availability.available ? 'available' : 'unavailable',
        availabilityMeta: {
            capacity: availability.capacity,
            reservedCount: availability.reservedCount
        },
        status: 'pending',
        paymentStatus: 'pending',
        createdAt: new Date(),
        updatedAt: new Date()
    };

    const result = await reservations.insertOne(reservation);
    reservation._id = result.insertedId;

    await notifyAdmin(reservation);

    return reservation;
}

async function getReservationById(reservationId) {
    const db = getDatabase();
    const reservations = db.collection('reservations');

    if (!ObjectId.isValid(reservationId)) {
        return null;
    }

    return reservations.findOne({ _id: new ObjectId(reservationId) });
}

async function confirmReservation(reservationId, paymentDetails = {}) {
    const db = getDatabase();
    const reservations = db.collection('reservations');

    if (!ObjectId.isValid(reservationId)) {
        throw new Error('Invalid reservation id');
    }

    const update = {
        status: 'confirmed',
        paymentStatus: 'paid',
        paymentDetails: {
            method: paymentDetails.paymentMethod || 'unknown',
            reference: paymentDetails.paymentReference || null,
            confirmedAt: new Date()
        },
        updatedAt: new Date()
    };

    await reservations.updateOne({ _id: new ObjectId(reservationId) }, { $set: update });
    return getReservationById(reservationId);
}

module.exports = {
    createReservation,
    checkAvailability,
    getReservationById,
    confirmReservation
};
