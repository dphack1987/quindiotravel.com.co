const { MongoClient } = require('mongodb');
require('dotenv').config();

const uri = process.env.MONGODB_URI;
const client = new MongoClient(uri);

let db;

async function connectToDatabase() {
    try {
        await client.connect();
        console.log('✅ Connected to MongoDB');
        db = client.db(process.env.DB_NAME || 'don_chucho_db');
        
        // Crear índices automáticamente
        await createIndexes();
        
        return db;
    } catch (error) {
        console.error('❌ MongoDB connection error:', error);
        throw error;
    }
}

async function createIndexes() {
    try {
        const conversations = db.collection('conversations');
        const webConversations = db.collection('web_conversations');
        const escalations = db.collection('escalations');
        
        // Índices para conversaciones de WhatsApp
        await conversations.createIndex({ phoneNumber: 1, status: 1 });
        await conversations.createIndex({ startedAt: -1 });
        await conversations.createIndex({ lastMessageAt: -1 });
        
        // Índices para conversaciones web
        await webConversations.createIndex({ sessionId: 1 });
        await webConversations.createIndex({ lastUpdate: -1 });
        
        // Índices para escalaciones
        await escalations.createIndex({ timestamp: -1 });
        await escalations.createIndex({ status: 1 });
        
        console.log('✅ Database indexes created');
    } catch (error) {
        console.log('⚠️ Index creation warning:', error.message);
    }
}

function getDatabase() {
    if (!db) {
        throw new Error('Database not connected. Call connectToDatabase() first.');
    }
    return db;
}

async function closeDatabaseConnection() {
    await client.close();
    console.log('🔌 Database connection closed');
}

module.exports = { 
    connectToDatabase, 
    getDatabase,
    closeDatabaseConnection 
};