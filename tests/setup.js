// Configuración básica para tests
// Esta estructura permite agregar tests sin modificar el código existente

export const testConfig = {
    baseUrl: 'http://localhost:3000',
    timeout: 10000,
    retries: 2
};

// Helper para tests async
export async function waitFor(condition, timeout = 5000) {
    const start = Date.now();
    while (Date.now() - start < timeout) {
        if (condition()) return true;
        await new Promise(resolve => setTimeout(resolve, 100));
    }
    throw new Error('Condition not met within timeout');
}

// Helper para simular DOM
export function createMockElement(tag, attributes = {}) {
    const element = document.createElement(tag);
    Object.entries(attributes).forEach(([key, value]) => {
        element.setAttribute(key, value);
    });
    return element;
}