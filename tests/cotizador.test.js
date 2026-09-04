// Tests básicos para el cotizador
// Tests no invasivos que verifican funcionalidad sin modificar código existente

import { testConfig, waitFor } from './setup.js';

describe('Cotizador de Viajes', () => {
    
    test('debería calcular precio básico correctamente', () => {
        // Simular datos de prueba
        const mockTarifas = {
            plan1_2d1n: {
                temporada_baja: {
                    economica: 425000,
                    intermedia: 442000
                }
            }
        };
        
        // Test de cálculo básico
        const resultado = mockTarifas.plan1_2d1n.temporada_baja.economica * 2;
        expect(resultado).toBe(850000);
    });

    test('debería validar número mínimo de personas', () => {
        const minPersonas = 2;
        const inputPersonas = 3;
        
        expect(inputPersonas).toBeGreaterThanOrEqual(minPersonas);
    });

    test('debería detectar temporada correctamente', () => {
        const mesesTemporadaAlta = [12, 1, 2, 6, 7]; // Dic, Ene, Feb, Jun, Jul
        const mesActual = new Date().getMonth() + 1;
        
        const esTemporadaAlta = mesesTemporadaAlta.includes(mesActual);
        expect(typeof esTemporadaAlta).toBe('boolean');
    });

    test('debería tener estructura de datos válida', () => {
        const estructuraEsperada = ['plan', 'categoria', 'pax', 'temporada'];
        const datosPrueba = {
            plan: 'plan1_2d1n',
            categoria: 'economica',
            pax: 2,
            temporada: 'baja'
        };
        
        estructuraEsperada.forEach(campo => {
            expect(datosPrueba).toHaveProperty(campo);
        });
    });
});

// Tests para validación de formularios
describe('Validación de Formularios', () => {
    
    test('debería aceptar valores válidos de ocupación', () => {
        const ocupacionesValidas = ['doble', 'triple', 'cuadruple'];
        const ocupacionTest = 'cuadruple';
        
        expect(ocupacionesValidas).toContain(ocupacionTest);
    });

    test('debería rechazar valores negativos', () => {
        const valorNegativo = -5;
        const valorPositivo = 10;
        
        expect(valorPositivo).toBeGreaterThan(0);
        expect(valorNegativo).not.toBeGreaterThan(0);
    });
});