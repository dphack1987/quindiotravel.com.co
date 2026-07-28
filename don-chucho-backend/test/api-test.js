// Test Suite para Don Chucho Backend
const axios = require('axios');

const API_BASE_URL = process.env.API_BASE_URL || 'http://localhost:3000';

// Tests
async function runTests() {
    console.log('🧪 Iniciando tests de Don Chucho Backend...\n');
    
    let passed = 0;
    let failed = 0;
    
    // Test 1: Health Check
    try {
        console.log('Test 1: Health Check');
        const response = await axios.get(`${API_BASE_URL}/health`);
        
        if (response.data.status === 'ok') {
            console.log('✅ Health check passed');
            passed++;
        } else {
            console.log('❌ Health check failed');
            failed++;
        }
    } catch (error) {
        console.log('❌ Health check failed:', error.message);
        failed++;
    }
    
    // Test 2: Crear sesión de chat
    try {
        console.log('\nTest 2: Crear sesión de chat');
        const response = await axios.post(`${API_BASE_URL}/api/chat/session`, {
            source: 'web'
        });
        
        if (response.data.sessionId) {
            console.log('✅ Sesión creada:', response.data.sessionId);
            passed++;
        } else {
            console.log('❌ Creación de sesión falló');
            failed++;
        }
    } catch (error) {
        console.log('❌ Test de sesión falló:', error.message);
        failed++;
    }
    
    // Test 3: Enviar mensaje
    try {
        console.log('\nTest 3: Enviar mensaje');
        const response = await axios.post(`${API_BASE_URL}/api/chat/message`, {
            message: 'Hola Don Chucho, quiero información sobre planes',
            sessionId: 'test_session_123',
            conversationHistory: []
        });
        
        if (response.data.response) {
            console.log('✅ Respuesta recibida:', response.data.response.substring(0, 50) + '...');
            passed++;
        } else {
            console.log('❌ No se recibió respuesta');
            failed++;
        }
    } catch (error) {
        console.log('❌ Test de mensaje falló:', error.message);
        failed++;
    }
    
    // Test 4: Quick Replies
    try {
        console.log('\nTest 4: Obtener quick replies');
        const response = await axios.get(`${API_BASE_URL}/api/chat/quick-replies?context=initial`);
        
        if (response.data.quickReplies && response.data.quickReplies.length > 0) {
            console.log('✅ Quick replies obtenidos:', response.data.quickReplies.length);
            passed++;
        } else {
            console.log('❌ No se obtuvieron quick replies');
            failed++;
        }
    } catch (error) {
        console.log('❌ Test de quick replies falló:', error.message);
        failed++;
    }
    
    // Test 5: Escalado a humano
    try {
        console.log('\nTest 5: Escalado a humano');
        const response = await axios.post(`${API_BASE_URL}/api/chat/escalate`, {
            sessionId: 'test_session_123',
            message: 'Necesito hablar con un humano',
            context: 'urgent'
        });
        
        if (response.data.success) {
            console.log('✅ Escalado configurado');
            passed++;
        } else {
            console.log('❌ Escalado falló');
            failed++;
        }
    } catch (error) {
        console.log('❌ Test de escalado falló:', error.message);
        failed++;
    }
    
    // Resultados
    console.log('\n' + '='.repeat(50));
    console.log(`📊 Resultados: ${passed} passed, ${failed} failed`);
    console.log('='.repeat(50));
    
    if (failed === 0) {
        console.log('🎉 Todos los tests pasaron exitosamente!');
        process.exit(0);
    } else {
        console.log('⚠️  Algunos tests fallaron. Revisa la configuración.');
        process.exit(1);
    }
}

// Ejecutar tests
runTests();