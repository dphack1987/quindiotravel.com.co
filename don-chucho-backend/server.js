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
    console.warn('⚠️ Missing environment variables:', missingEnv.join(', '));
    console.warn('⚠️ Server will start in degraded mode. Please configure .env file for full functionality.');
    
    // Set default values for development
    if (!process.env.MONGODB_URI) {
        process.env.MONGODB_URI = 'mongodb://localhost:27017/don_chucho_db';
        console.warn('⚠️ Using default MongoDB URI for development');
    }
    if (!process.env.DB_NAME) {
        process.env.DB_NAME = 'don_chucho_db';
        console.warn('⚠️ Using default database name for development');
    }
    if (!process.env.API_KEY) {
        process.env.API_KEY = 'dev-key-' + Date.now();
        console.warn('⚠️ Using generated API key for development');
    }
    if (!process.env.QUINDIO_WHATSAPP) {
        process.env.QUINDIO_WHATSAPP = '573000000000';
        console.warn('⚠️ Using default WhatsApp number for development');
    }
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