const { Schema } = require('mongoose');

// Nota: Si usas MongoDB directo (sin Mongoose), este archivo es referencia
// Para implementación simple con MongoDB directo, usa la estructura de datos

const conversationSchema = new Schema({
    sessionId: {
        type: String,
        required: true,
        unique: true
    },
    phoneNumber: {
        type: String,
        sparse: true // Permite null para conversaciones web
    },
    source: {
        type: String,
        enum: ['whatsapp', 'web'],
        default: 'web'
    },
    status: {
        type: String,
        enum: ['active', 'escalated', 'completed'],
        default: 'active'
    },
    messages: [{
        role: {
            type: String,
            enum: ['user', 'assistant']
        },
        content: String,
        timestamp: {
            type: Date,
            default: Date.now
        },
        metadata: {
            type: Object,
            default: {}
        }
    }],
    metadata: {
        firstContact: {
            type: Boolean,
            default: true
        },
        lastTopic: String,
        interestedIn: [String],
        conversionStage: {
            type: String,
            enum: ['awareness', 'consideration', 'decision', 'retention'],
            default: 'awareness'
        }
    },
    startedAt: {
        type: Date,
        default: Date.now
    },
    lastMessageAt: {
        type: Date,
        default: Date.now
    },
    messageCount: {
        type: Number,
        default: 0
    },
    escalatedAt: Date,
    completedAt: Date
});

// Índices para optimización
conversationSchema.index({ phoneNumber: 1, status: 1 });
conversationSchema.index({ sessionId: 1 });
conversationSchema.index({ startedAt: -1 });
conversationSchema.index({ lastMessageAt: -1 });

// Métodos del modelo
conversationSchema.methods.escalate = function() {
    this.status = 'escalated';
    this.escalatedAt = new Date();
    return this.save();
};

conversationSchema.methods.complete = function() {
    this.status = 'completed';
    this.completedAt = new Date();
    return this.save();
};

conversationSchema.methods.addMessage = function(role, content, metadata = {}) {
    this.messages.push({
        role,
        content,
        timestamp: new Date(),
        metadata
    });
    this.lastMessageAt = new Date();
    this.messageCount += 1;
    return this.save();
};

conversationSchema.statics.getActiveConversations = function() {
    return this.find({ status: 'active' })
        .sort({ lastMessageAt: -1 })
        .limit(100);
};

conversationSchema.statics.getStatistics = function() {
    return this.aggregate([
        {
            $group: {
                _id: '$source',
                count: { $sum: 1 },
                avgMessages: { $avg: '$messageCount' }
            }
        }
    ]);
};

module.exports = conversationSchema;