// Middleware de autenticación básico
// Para producción, considera implementar JWT o autenticación más robusta

const authMiddleware = (req, res, next) => {
    // Verificar API key básica
    const apiKey = req.headers['x-api-key'];
    const validApiKey = process.env.API_KEY || 'don-chucho-secret-key-2024';
    
    if (apiKey && apiKey === validApiKey) {
        next();
    } else {
        res.status(401).json({ error: 'Unauthorized' });
    }
};

// Rate limiting básico
const rateLimitMap = new Map();

const rateLimitMiddleware = (req, res, next) => {
    const ip = req.ip || req.connection.remoteAddress;
    const now = Date.now();
    const windowMs = 60 * 1000; // 1 minuto
    const maxRequests = 30;
    
    if (!rateLimitMap.has(ip)) {
        rateLimitMap.set(ip, { count: 1, resetTime: now + windowMs });
        next();
    } else {
        const data = rateLimitMap.get(ip);
        
        if (now > data.resetTime) {
            // Resetear contador
            rateLimitMap.set(ip, { count: 1, resetTime: now + windowMs });
            next();
        } else if (data.count < maxRequests) {
            data.count++;
            next();
        } else {
            res.status(429).json({ 
                error: 'Too many requests',
                retryAfter: Math.ceil((data.resetTime - now) / 1000)
            });
        }
    }
};

// Limpiar rate limit map periódicamente
setInterval(() => {
    const now = Date.now();
    for (const [ip, data] of rateLimitMap.entries()) {
        if (now > data.resetTime) {
            rateLimitMap.delete(ip);
        }
    }
}, 60 * 1000); // Cada minuto

module.exports = {
    authMiddleware,
    rateLimitMiddleware
};