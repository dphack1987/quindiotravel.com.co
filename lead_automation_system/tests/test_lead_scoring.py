"""
Sistema de Pruebas Unitarias - Lead Scoring Engine
Pruebas para verificar el funcionamiento del sistema de calificación de leads
"""

import unittest
import sys
import os
import json
from datetime import datetime, timedelta

# Agregar directorio padre al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.lead_scoring import LeadScoringEngine
from config import config

class TestLeadScoringEngine(unittest.TestCase):
    """Pruebas unitarias para el motor de lead scoring"""
    
    def setUp(self):
        """Configuración inicial para cada prueba"""
        self.lead_scorer = LeadScoringEngine(config)
    
    def test_hot_lead_scoring(self):
        """Test de calificación de lead caliente"""
        lead_data = {
            "nombre": "Juan Pérez",
            "telefono": "573000000000",
            "mensaje": "Hola, estoy interesado en un plan turístico al Valle de Cocora para 4 personas. Mi presupuesto es de 2 millones de pesos. ¿Tienen disponibilidad para el próximo fin de semana?",
            "destino": "Valle de Cocora",
            "fecha_deseada": (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d"),
            "num_personas": "4",
            "presupuesto": "2000000",
            "inquiry_time": datetime.now().isoformat(),
            "device": "desktop",
            "page_views": 5,
            "time_on_site": 10,
            "is_return_visitor": True,
            "whatsapp_clicked": True
        }
        
        result = self.lead_scorer.calculate_lead_score(lead_data)
        
        self.assertGreaterEqual(result['score'], 70, "Lead con datos completos debería ser hot lead")
        self.assertEqual(result['category'], 'hot_lead', "Categoría debería ser hot_lead")
        self.assertEqual(result['priority'], 'URGENTE', "Prioridad debería ser URGENTE")
    
    def test_warm_lead_scoring(self):
        """Test de calificación de lead tibio"""
        lead_data = {
            "nombre": "María García",
            "telefono": "573000000000",
            "mensaje": "Hola, me gustaría información sobre planes al Eje Cafetero",
            "destino": "Eje Cafetero",
            "fecha_deseada": "",
            "num_personas": "",
            "presupuesto": "",
            "inquiry_time": datetime.now().isoformat(),
            "device": "mobile",
            "page_views": 2,
            "time_on_site": 3,
            "is_return_visitor": False,
            "whatsapp_clicked": False
        }
        
        result = self.lead_scorer.calculate_lead_score(lead_data)
        
        self.assertGreaterEqual(result['score'], 50, "Lead con interés básico debería ser warm lead")
        self.assertLess(result['score'], 70, "No debería alcanzar hot lead")
        self.assertEqual(result['category'], 'warm_lead', "Categoría debería ser warm_lead")
    
    def test_cold_lead_scoring(self):
        """Test de calificación de lead frío"""
        lead_data = {
            "nombre": "Carlos López",
            "telefono": "573000000000",
            "mensaje": "Hola",
            "destino": "",
            "fecha_deseada": "",
            "num_personas": "",
            "presupuesto": "",
            "inquiry_time": datetime.now().isoformat(),
            "device": "mobile",
            "page_views": 1,
            "time_on_site": 1,
            "is_return_visitor": False,
            "whatsapp_clicked": False
        }
        
        result = self.lead_scorer.calculate_lead_score(lead_data)
        
        self.assertLess(result['score'], 50, "Lead con información mínima debería ser cold lead")
        self.assertEqual(result['category'], 'cold_lead', "Categoría debería ser cold_lead")
    
    def test_interest_signals(self):
        """Test de señales de interés"""
        lead_with_plan = {
            "mensaje": "Estoy interesado en un plan turístico",
            "presupuesto": "1000000",
            "num_personas": "2"
        }
        
        lead_without_plan = {
            "mensaje": "Hola",
            "presupuesto": "",
            "num_personas": ""
        }
        
        score_with_plan = self.lead_scorer._calculate_interest_signals(lead_with_plan)
        score_without_plan = self.lead_scorer._calculate_interest_signals(lead_without_plan)
        
        self.assertGreater(score_with_plan, score_without_plan, 
                          "Lead con información de plan debería tener mayor score")
    
    def test_quality_signals(self):
        """Test de señales de calidad"""
        lead_complete = {
            "message": "Hola, estoy interesado en visitar Salento y Valle de Cocora. Mi presupuesto es de 1.5 millones de pesos para 3 personas.",
            "presupuesto": "1500000",
            "fecha_deseada": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d"),
            "nombre": "Test User",
            "telefono": "573000000000"
        }
        
        lead_incomplete = {
            "message": "Hola",
            "presupuesto": "",
            "fecha_deseada": "",
            "nombre": "",
            "telefono": ""
        }
        
        score_complete = self.lead_scorer._calculate_quality_signals(lead_complete)
        score_incomplete = self.lead_scorer._calculate_quality_signals(lead_incomplete)
        
        self.assertGreater(score_complete, score_incomplete,
                          "Lead con información completa debería tener mayor score de calidad")
    
    def test_top_leads_sorting(self):
        """Test de ordenamiento de leads por score"""
        leads = [
            {
                "nombre": "Lead 1",
                "mensaje": "Hola",
                "inquiry_time": datetime.now().isoformat()
            },
            {
                "nombre": "Lead 2",
                "mensaje": "Estoy interesado en un plan para 4 personas con presupuesto de 2 millones",
                "presupuesto": "2000000",
                "num_personas": "4",
                "whatsapp_clicked": True,
                "inquiry_time": datetime.now().isoformat()
            },
            {
                "nombre": "Lead 3",
                "mensaje": "Información sobre Eje Cafetero",
                "inquiry_time": datetime.now().isoformat()
            }
        ]
        
        top_leads = self.lead_scorer.get_top_leads(leads, limit=2)
        
        self.assertEqual(len(top_leads), 2, "Debería retornar top 2 leads")
        self.assertGreaterEqual(top_leads[0]['score'], top_leads[1]['score'],
                              "Primer lead debería tener mayor score")
    
    def test_scoring_rules_loading(self):
        """Test de carga de reglas de scoring"""
        rules = self.lead_scorer.scoring_rules
        
        self.assertIn('interest_signals', rules, "Debería tener señales de interés")
        self.assertIn('quality_signals', rules, "Debería tener señales de calidad")
        self.assertIn('behavioral_signals', rules, "Debería tener señales de comportamiento")
        self.assertIn('timing_signals', rules, "Debería tener señales de timing")
    
    def test_recommended_actions(self):
        """Test de acciones recomendadas por categoría"""
        hot_actions = self.lead_scorer._get_recommended_actions('hot_lead')
        warm_actions = self.lead_scorer._get_recommended_actions('warm_lead')
        cold_actions = self.lead_scorer._get_recommended_actions('cold_lead')
        
        self.assertIsInstance(hot_actions, list, "Acciones hot lead deberían ser lista")
        self.assertGreater(len(hot_actions), 0, "Debería tener acciones para hot lead")
        self.assertIn("Llamada inmediata", hot_actions[0], "Hot lead debería requerir llamada inmediata")
        
        self.assertIsInstance(warm_actions, list, "Acciones warm lead deberían ser lista")
        self.assertGreater(len(warm_actions), 0, "Debería tener acciones para warm lead")
        
        self.assertIsInstance(cold_actions, list, "Acciones cold lead deberían ser lista")
        self.assertGreater(len(cold_actions), 0, "Debería tener acciones para cold lead")

class TestLeadScoringEdgeCases(unittest.TestCase):
    """Pruebas de casos extremos para lead scoring"""
    
    def setUp(self):
        """Configuración inicial para cada prueba"""
        self.lead_scorer = LeadScoringEngine(config)
    
    def test_empty_lead_data(self):
        """Test con datos de lead vacíos"""
        lead_data = {}
        
        result = self.lead_scorer.calculate_lead_score(lead_data)
        
        self.assertGreaterEqual(result['score'], 0, "Score no debería ser negativo")
        self.assertLessEqual(result['score'], 100, "Score no debería exceder 100")
        self.assertEqual(result['category'], 'cold_lead', "Lead vacío debería ser cold lead")
    
    def test_very_long_message(self):
        """Test con mensaje muy largo"""
        lead_data = {
            "mensaje": "Hola " * 1000,  # Mensaje muy largo
            "inquiry_time": datetime.now().isoformat()
        }
        
        result = self.lead_scorer.calculate_lead_score(lead_data)
        
        self.assertGreaterEqual(result['score'], 0, "Score no debería ser negativo")
        self.assertLessEqual(result['score'], 100, "Score no debería exceder 100")
    
    def test_future_date(self):
        """Test con fecha muy futura"""
        future_date = (datetime.now() + timedelta(days=365)).strftime("%Y-%m-%d")
        lead_data = {
            "fecha_deseada": future_date,
            "inquiry_time": datetime.now().isoformat()
        }
        
        result = self.lead_scorer.calculate_lead_score(lead_data)
        
        # Fecha muy futura no debería dar puntos de realismo
        self.assertLessEqual(result['score'], 100, "Score no debería exceder 100")
    
    def test_past_date(self):
        """Test con fecha pasada"""
        past_date = (datetime.now() - timedelta(days=10)).strftime("%Y-%m-%d")
        lead_data = {
            "fecha_deseada": past_date,
            "inquiry_time": datetime.now().isoformat()
        }
        
        result = self.lead_scorer.calculate_lead_score(lead_data)
        
        # Fecha pasada no debería dar puntos de realismo
        self.assertLessEqual(result['score'], 100, "Score no debería exceder 100")
    
    def test_very_high_budget(self):
        """Test con presupuesto muy alto"""
        lead_data = {
            "presupuesto": "100000000",  # 100 millones de pesos
            "inquiry_time": datetime.now().isoformat()
        }
        
        result = self.lead_scorer.calculate_lead_score(lead_data)
        
        # Presupuesto muy alto no debería dar puntos de razonabilidad
        self.assertLessEqual(result['score'], 100, "Score no debería exceder 100")
    
    def test_very_low_budget(self):
        """Test con presupuesto muy bajo"""
        lead_data = {
            "presupuesto": "10000",  # 10 mil pesos
            "inquiry_time": datetime.now().isoformat()
        }
        
        result = self.lead_scorer.calculate_lead_score(lead_data)
        
        # Presupuesto muy bajo no debería dar puntos de razonabilidad
        self.assertLessEqual(result['score'], 100, "Score no debería exceder 100")

def run_tests():
    """Ejecutar todas las pruebas"""
    # Crear suite de pruebas
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Agregar pruebas
    suite.addTests(loader.loadTestsFromTestCase(TestLeadScoringEngine))
    suite.addTests(loader.loadTestsFromTestCase(TestLeadScoringEdgeCases))
    
    # Ejecutar pruebas
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Retornar resultado
    return result.wasSuccessful()

if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)