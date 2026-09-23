"""
Sistema de Pruebas Unitarias - Analytics Module
Pruebas para verificar el funcionamiento del módulo de análisis
"""

import unittest
import sys
import os
import json
from datetime import datetime, timedelta

# Agregar directorio padre al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.analytics import LeadAnalytics
from config import config

class TestLeadAnalytics(unittest.TestCase):
    """Pruebas unitarias para el módulo de análisis"""
    
    def setUp(self):
        """Configuración inicial para cada prueba"""
        self.analytics = LeadAnalytics(config)
        
        # Crear datos de prueba si no existen
        if not self.analytics.conversion_data:
            self.analytics.conversion_data = self.create_test_conversion_data()
        
        if not self.analytics.leads_data:
            self.analytics.leads_data = self.create_test_leads_data()
    
    def create_test_conversion_data(self):
        """Crear datos de conversión de prueba"""
        now = datetime.now()
        return [
            {
                "lead_id": "lead_1",
                "conversion_date": (now - timedelta(days=5)).isoformat(),
                "amount": 1500000,
                "conversion_source": "whatsapp"
            },
            {
                "lead_id": "lead_2", 
                "conversion_date": (now - timedelta(days=15)).isoformat(),
                "amount": 2200000,
                "conversion_source": "website"
            },
            {
                "lead_id": "lead_3",
                "conversion_date": (now - timedelta(days=25)).isoformat(),
                "amount": 1800000,
                "conversion_source": "referral"
            }
        ]
    
    def create_test_leads_data(self):
        """Crear datos de leads de prueba"""
        now = datetime.now()
        return [
            {
                "id": "lead_1",
                "nombre": "Juan Pérez",
                "presupuesto": "1500000",
                "destino": "Valle de Cocora",
                "inquiry_time": (now - timedelta(days=6)).isoformat(),
                "converted": True,
                "conversion_date": (now - timedelta(days=5)).isoformat()
            },
            {
                "id": "lead_2",
                "nombre": "María García",
                "presupuesto": "2000000",
                "destino": "Eje Cafetero",
                "inquiry_time": (now - timedelta(days=16)).isoformat(),
                "converted": True,
                "conversion_date": (now - timedelta(days=15)).isoformat()
            },
            {
                "id": "lead_3",
                "nombre": "Carlos López",
                "presupuesto": "500000",
                "destino": "Salento",
                "inquiry_time": (now - timedelta(days=1)).isoformat(),
                "converted": False
            },
            {
                "id": "lead_4",
                "nombre": "Ana Martínez",
                "presupuesto": "3000000",
                "destino": "Filandia",
                "inquiry_time": (now - timedelta(days=2)).isoformat(),
                "converted": False
            }
        ]
    
    def test_conversion_rate_calculation(self):
        """Test de cálculo de tasa de conversión"""
        conversion_rate = self.analytics.calculate_conversion_rate(period_days=30)
        
        self.assertIn('conversion_rate', conversion_rate, "Debería incluir tasa de conversión")
        self.assertIn('total_leads', conversion_rate, "Debería incluir total de leads")
        self.assertIn('total_conversions', conversion_rate, "Debería incluir total de conversiones")
        self.assertGreaterEqual(conversion_rate['conversion_rate'], 0, "Tasa no debería ser negativa")
        self.assertLessEqual(conversion_rate['conversion_rate'], 100, "Tasa no debería exceder 100%")
    
    def test_conversion_probability_prediction(self):
        """Test de predicción de probabilidad de conversión"""
        lead_data = {
            "nombre": "Test User",
            "presupuesto": "1500000",
            "destino": "Valle de Cocora",
            "num_personas": "4",
            "inquiry_time": datetime.now().isoformat()
        }
        
        prediction = self.analytics.predict_conversion_probability(lead_data)
        
        self.assertIn('probability', prediction, "Debería incluir probabilidad")
        self.assertIn('confidence', prediction, "Debería incluir nivel de confianza")
        self.assertGreaterEqual(prediction['probability'], 0, "Probabilidad no debería ser negativa")
        self.assertLessEqual(prediction['probability'], 1, "Probabilidad no debería exceder 1")
        self.assertIn(prediction['confidence'], ['low', 'medium', 'high'], 
                     "Confianza debería ser low, medium o high")
    
    def test_revenue_potential_calculation(self):
        """Test de cálculo de potencial de ingresos"""
        leads = self.analytics.leads_data
        revenue_potential = self.analytics.calculate_revenue_potential(leads)
        
        self.assertIn('total_leads', revenue_potential, "Debería incluir total de leads")
        self.assertIn('high_value_leads_count', revenue_potential, "Debería incluir count de leads de alto valor")
        self.assertIn('total_potential', revenue_potential, "Debería incluir potencial total")
        self.assertGreaterEqual(revenue_potential['total_potential'], 0, "Potencial no debería ser negativo")
    
    def test_peak_periods_analysis(self):
        """Test de análisis de períodos pico"""
        peak_periods = self.analytics.analyze_peak_periods()
        
        self.assertIn('peak_month', peak_periods, "Debería incluir mes pico")
        self.assertIn('peak_day', peak_periods, "Debería incluir día pico")
        self.assertIn('peak_hour', peak_periods, "Debería incluir hora pico")
        self.assertIn('recommendations', peak_periods, "Debería incluir recomendaciones")
    
    def test_conversion_report_generation(self):
        """Test de generación de reporte de conversión"""
        report = self.analytics.generate_conversion_report()
        
        self.assertIn('report_date', report, "Debería incluir fecha del reporte")
        self.assertIn('conversion_rate', report, "Debería incluir tasa de conversión")
        self.assertIn('peak_periods', report, "Debería incluir períodos pico")
        self.assertIn('revenue_potential', report, "Debería incluir potencial de ingresos")
        self.assertIn('target_status', report, "Debería incluir estado del objetivo")
    
    def test_lead_lifecycle_tracking(self):
        """Test de rastreo de ciclo de vida de lead"""
        lead_id = "lead_1"
        lifecycle = self.analytics.track_lead_lifecycle(lead_id)
        
        self.assertIn('lead_id', lifecycle, "Debería incluir ID del lead")
        self.assertIn('stage', lifecycle, "Debería incluir etapa del lead")
        self.assertIn(lifecycle['stage'], ['new', 'followup', 'quoted', 'negotiation', 'converted'],
                     "Etapa debería ser válida")
    
    def test_budget_extraction(self):
        """Test de extracción de presupuesto"""
        # Test con diferentes formatos de presupuesto
        test_cases = [
            ("1500000", 1500000),
            ("$1,500,000", 1500000),
            ("1.5 millones", None),  # No debería extraer formato textual
            ("", None),
            ("invalid", None)
        ]
        
        for budget_str, expected in test_cases:
            result = self.analytics._extract_budget(budget_str)
            self.assertEqual(result, expected, 
                           f"Extracción de presupuesto falló para '{budget_str}'")

class TestAnalyticsEdgeCases(unittest.TestCase):
    """Pruebas de casos extremos para analytics"""
    
    def setUp(self):
        """Configuración inicial para cada prueba"""
        self.analytics = LeadAnalytics(config)
    
    def test_empty_data_conversion_rate(self):
        """Test de tasa de conversión con datos vacíos"""
        self.analytics.conversion_data = []
        self.analytics.leads_data = []
        
        conversion_rate = self.analytics.calculate_conversion_rate()
        
        self.assertEqual(conversion_rate['total_leads'], 0, "Total leads debería ser 0")
        self.assertEqual(conversion_rate['total_conversions'], 0, "Total conversiones debería ser 0")
        self.assertEqual(conversion_rate['conversion_rate'], 0, "Tasa de conversión debería ser 0")
    
    def test_prediction_with_no_similar_leads(self):
        """Test de predicción sin leads similares"""
        lead_data = {
            "nombre": "Unique User",
            "presupuesto": "99999999",  # Presupuesto muy atípico
            "destino": "Unknown Destination",
            "inquiry_time": datetime.now().isoformat()
        }
        
        prediction = self.analytics.predict_conversion_probability(lead_data)
        
        self.assertIn('probability', prediction, "Debería incluir probabilidad")
        self.assertGreater(prediction['probability'], 0, "Probabilidad debería ser mayor a 0")
        self.assertIn(prediction['confidence'], ['low', 'medium', 'high'],
                     "Debería tener nivel de confianza")
    
    def test_revenue_potential_with_no_high_value_leads(self):
        """Test de potencial de ingresos sin leads de alto valor"""
        leads = [
            {
                "id": "lead_1",
                "presupuesto": "500000",  # Bajo valor
                "inquiry_time": datetime.now().isoformat()
            },
            {
                "id": "lead_2",
                "presupuesto": "300000",  # Bajo valor
                "inquiry_time": datetime.now().isoformat()
            }
        ]
        
        revenue_potential = self.analytics.calculate_revenue_potential(leads)
        
        self.assertEqual(revenue_potential['high_value_leads_count'], 0, 
                        "No debería haber leads de alto valor")
        self.assertEqual(revenue_potential['total_potential'], 0, 
                        "Potencial total debería ser 0")
    
    def test_nonexistent_lead_lifecycle(self):
        """Test de ciclo de vida de lead inexistente"""
        lifecycle = self.analytics.track_lead_lifecycle("nonexistent_lead")
        
        self.assertIn('error', lifecycle, "Debería incluir error")
        self.assertEqual(lifecycle['error'], "Lead no encontrado", 
                        "Debería indicar lead no encontrado")

def run_tests():
    """Ejecutar todas las pruebas"""
    # Crear suite de pruebas
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Agregar pruebas
    suite.addTests(loader.loadTestsFromTestCase(TestLeadAnalytics))
    suite.addTests(loader.loadTestsFromTestCase(TestAnalyticsEdgeCases))
    
    # Ejecutar pruebas
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Retornar resultado
    return result.wasSuccessful()

if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)