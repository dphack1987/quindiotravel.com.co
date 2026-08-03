const nodemailer = require('nodemailer');
require('dotenv').config();

const SMTP_HOST = process.env.SMTP_HOST;
const SMTP_PORT = process.env.SMTP_PORT || 587;
const SMTP_USER = process.env.SMTP_USER;
const SMTP_PASS = process.env.SMTP_PASS;
const FROM_EMAIL = process.env.FROM_EMAIL || process.env.QUINDIO_EMAIL || 'noreply@quindiotravel.com';

let transporter = null;

if (SMTP_HOST && SMTP_USER && SMTP_PASS) {
    transporter = nodemailer.createTransport({
        host: SMTP_HOST,
        port: Number(SMTP_PORT),
        secure: Number(SMTP_PORT) === 465, // true for 465, false for other ports
        auth: {
            user: SMTP_USER,
            pass: SMTP_PASS
        }
    });
} else {
    console.warn('SMTP not configured. Email sending will be disabled. Set SMTP_HOST, SMTP_USER and SMTP_PASS.');
}

async function sendEmail(to, subject, text, html) {
    try {
        if (!transporter) {
            console.warn('Email transporter not configured. Skipping sendEmail.');
            return null;
        }

        const mailOptions = {
            from: FROM_EMAIL,
            to,
            subject,
            text,
            html
        };

        const info = await transporter.sendMail(mailOptions);
        console.log(`📧 Email sent to ${to}: ${info.messageId}`);
        return info;
    } catch (error) {
        console.error('Error sending email:', error);
        throw error;
    }
}

module.exports = {
    sendEmail
};
