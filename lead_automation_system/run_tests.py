"""
Script de Ejecución de Pruebas - Lead Automation System
Ejecuta todas las pruebas unitarias del sistema
"""

import sys
import os
import unittest
from datetime import datetime

# Agregar directorio actual al path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

def run_all_tests():
    """Ejecutar todas las pruebas del sistema"""
    print("🧪 Ejecutando Pruebas Unitarias - Lead Automation System")
    print("=" * 60)
    print(f"📅 Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    # Crear suite de pruebas
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Descubrir y agregar todas las pruebas
    from tests import test_lead_scoring, test_analytics, test_followup_engine
    
    # Agregar pruebas de lead scoring
    suite.addTests(loader.loadTestsFromModule(test_lead_scoring))
    
    # Agregar pruebas de analytics
    suite.addTests(loader.loadTestsFromModule(test_analytics))
    
    # Agregar pruebas de followup engine
    suite.addTests(loader.loadTestsFromModule(test_followup_engine))
    
    # Ejecutar pruebas
    print("🔍 Iniciando ejecución de pruebas...\n")
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Mostrar resumen
    print("\n" + "=" * 60)
    print("📊 RESUMEN DE PRUEBAS")
    print("=" * 60)
    print(f"Total pruebas ejecutadas: {result.testsRun}")
    print(f"✅ Pruebas exitosas: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"❌ Pruebas fallidas: {len(result.failures)}")
    print(f"⚠️  Pruebas con errores: {len(result.errors)}")
    print(f"⏱️  Tiempo de ejecución: {result.duration:.2f} segundos")
    print("=" * 60)
    
    if result.wasSuccessful():
        print("🎉 ¡TODAS LAS PRUEBAS PASARON EXITOSAMENTE!")
        return True
    else:
        print("⚠️  ALGUNAS PRUEBAS FALLARON - Revisar detalles arriba")
        return False

def run_specific_test(test_module):
    """Ejecutar pruebas de un módulo específico"""
    print(f"🧪 Ejecutando pruebas de módulo: {test_module}")
    print("=" * 60)
    
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromName(test_module)
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()

def run_quick_tests():
    """Ejecutar solo pruebas rápidas (smoke tests)"""
    print("🧪 Ejecutando Pruebas Rápidas (Smoke Tests)")
    print("=" * 60)
    
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Cargar solo pruebas esenciales
    from tests.test_lead_scoring import TestLeadScoringEngine
    from tests.test_analytics import TestLeadAnalytics
    
    # Agregar solo pruebas críticas
    suite.addTest(TestLeadScoringEngine('test_hot_lead_scoring'))
    suite.addTest(TestLeadScoringEngine('test_warm_lead_scoring'))
    suite.addTest(TestLeadScoringEngine('test_cold_lead_scoring'))
    suite.addTest(TestLeadAnalytics('test_conversion_rate_calculation'))
    suite.addTest(TestLeadAnalytics('test_conversion_probability_prediction'))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Ejecutar pruebas del sistema de automatización de leads')
    parser.add_argument('--module', type=str, help='Ejecutar pruebas de un módulo específico')
    parser.add_argument('--quick', action='store_true', help='Ejecutar solo pruebas rápidas')
    
    args = parser.parse_args()
    
    try:
        if args.module:
            success = run_specific_test(args.module)
        elif args.quick:
            success = run_quick_tests()
        else:
            success = run_all_tests()
        
        sys.exit(0 if success else 1)
    
    except KeyboardInterrupt:
        print("\n⚠️  Ejecución de pruebas interrumpida por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error durante ejecución de pruebas: {str(e)}")
        sys.exit(1)