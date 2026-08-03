const express = require('express');
const cors = require('cors');
require('dotenv').config();

const { connectToDatabase } = require('./config/database');
const webhookRoutes = require('./routes/webhook');
const chatRoutes = require('./routes/chat');
const { rateLimitMiddleware } = require('./middleware/auth');

const requiredEnv = [
    'MONGODB_URI',
    'DB_NAME',
    'API_KEY',
    'QUINDIO_WHATSAPP'
];

const missingEnv = requiredEnv.filter((key) => !process.env[key]);

if (missingEnv.length > 0) {
    console.error('❌ Missing required environment variables:', missingEnv.join(', '));
    process.exit(1);
}

const app = express();
const PORT = Number(process.env.PORT || 3000);

// Middleware
app.use(cors({ origin: process.env.FRONTEND_URL || '*' }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(rateLimitMiddleware);

// Conectar a base de datos
connectToDatabase().catch(console.error);

// Routes
app.use('/webhook', webhookRoutes);
app.use('/api/chat', chatRoutes);
app.use('/api/reservations', require('./routes/reservations'));
app.use('/api/test', require('./routes/test'));

// Health check
app.get('/health', (req, res) => {
    res.json({ 
        status: 'ok', 
        message: 'Don Chucho Backend Running',
        timestamp: new Date()
    });
});

// Error handling
app.use((err, req, res, next) => {
    console.error('Server Error:', err);
    res.status(500).json({ 
        error: 'Internal Server Error',
        message: process.env.NODE_ENV === 'development' ? err.message : 'Something went wrong'
    });
});

// Graceful shutdown
process.on('SIGTERM', async () => {
    console.log('SIGTERM signal received: closing HTTP server');
    const { closeDatabaseConnection } = require('./config/database');
    await closeDatabaseConnection();
    process.exit(0);
});

// Start server
app.listen(PORT, () => {
    console.log(`🤠 Don Chucho Backend running on port ${PORT}`);
    console.log(`🌐 Environment: ${process.env.NODE_ENV || 'development'}`);
});