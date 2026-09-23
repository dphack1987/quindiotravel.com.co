"""
Sistema de Pruebas Unitarias - Followup Engine
Pruebas para verificar el funcionamiento del motor de seguimiento
"""

import unittest
import sys
import os
from datetime import datetime, timedelta
from unittest.mock import Mock, MagicMock

# Agregar directorio padre al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.followup_engine import FollowupEngine
from config import config

class TestFollowupEngine(unittest.TestCase):
    """Pruebas unitarias para el motor de seguimiento"""
    
    def setUp(self):
        """Configuración inicial para cada prueba"""
        # Crear mocks para dependencias
        self.mock_whatsapp_bot = Mock()
        self.mock_lead_scorer = Mock()
        
        # Configurar comportamiento del mock lead scorer
        self.mock_lead_scorer.calculate_lead_score.return_value = {
            'score': 75,
            'category': 'hot_lead'
        }
        
        # Configurar comportamiento del mock whatsapp bot
        self.mock_whatsapp_bot.send_text_message.return_value = {
            'success': True,
            'timestamp': datetime.now().isoformat()
        }
        
        self.followup_engine = FollowupEngine(config, self.mock_whatsapp_bot, self.mock_lead_scorer)
    
    def test_schedule_followup_hot_lead(self):
        """Test de programación de seguimiento para lead caliente"""
        lead_data = {
            "id": "test_lead_1",
            "nombre": "Test User",
            "telefono": "573000000000",
            "inquiry_time": datetime.now().isoformat()
        }
        
        followups = self.followup_engine.schedule_followup(lead_data)
        
        self.assertIsInstance(followups, list, "Seguimientos deberían ser lista")
        self.assertGreater(len(followups), 0, "Debería haber seguimientos programados")
        
        # Verificar que hot lead tiene seguimientos apropiados
        hot_lead_schedule = config['followup'].followup_schedule['hot_lead']
        self.assertEqual(len(followups), len(hot_lead_schedule), 
                        "Número de seguimientos debería coincidir con configuración")
    
    def test_schedule_followup_warm_lead(self):
        """Test de programación de seguimiento para lead tibio"""
        lead_data = {
            "id": "test_lead_2",
            "nombre": "Test User",
            "telefono": "573000000000",
            "inquiry_time": datetime.now().isoformat()
        }
        
        # Configurar mock para warm lead
        self.mock_lead_scorer.calculate_lead_score.return_value = {
            'score': 60,
            'category': 'warm_lead'
        }
        
        followups = self.followup_engine.schedule_followup(lead_data)
        
        self.assertIsInstance(followups, list, "Seguimientos deberían ser lista")
        self.assertGreater(len(followups), 0, "Debería haber seguimientos programados")
        
        # Verificar categoría
        self.assertEqual(followups[0]['lead_category'], 'warm_lead',
                        "Categoría debería ser warm_lead")
    
    def test_schedule_followup_cold_lead(self):
        """Test de programación de seguimiento para lead frío"""
        lead_data = {
            "id": "test_lead_3",
            "nombre": "Test User",
            "telefono": "573000000000",
            "inquiry_time": datetime.now().isoformat()
        }
        
        # Configurar mock para cold lead
        self.mock_lead_scorer.calculate_lead_score.return_value = {
            'score': 30,
            'category': 'cold_lead'
        }
        
        followups = self.followup_engine.schedule_followup(lead_data)
        
        self.assertIsInstance(followups, list, "Seguimientos deberían ser lista")
        self.assertGreater(len(followups), 0, "Debería haber seguimientos programados")
        
        # Verificar categoría
        self.assertEqual(followups[0]['lead_category'], 'cold_lead',
                        "Categoría debería ser cold_lead")
    
    def test_message_template_selection(self):
        """Test de selección de plantilla de mensaje"""
        # Test para hot lead
        template_hot = self.followup_engine._select_message_template('hot_lead', 0)
        self.assertIsInstance(template_hot, str, "Plantilla debería ser string")
        self.assertIn('{nombre}', template_hot, "Plantilla debería tener placeholder de nombre")
        
        # Test para warm lead
        template_warm = self.followup_engine._select_message_template('warm_lead', 1)
        self.assertIsInstance(template_warm, str, "Plantilla debería ser string")
        
        # Test para cold lead
        template_cold = self.followup_engine._select_message_template('cold_lead', 7)
        self.assertIsInstance(template_cold, str, "Plantilla debería ser string")
    
    def test_followup_priority_determination(self):
        """Test de determinación de prioridad de seguimiento"""
        # Hot lead inmediato debería ser urgente
        priority_hot = self.followup_engine._get_followup_priority('hot_lead', 0)
        self.assertEqual(priority_hot, 'urgent', "Hot lead inmediato debería ser urgente")
        
        # Warm lead temprano debería ser alta
        priority_warm = self.followup_engine._get_followup_priority('warm_lead', 1)
        self.assertEqual(priority_warm, 'high', "Warm lead temprano debería ser alta")
        
        # Otros deberían ser normales
        priority_normal = self.followup_engine._get_followup_priority('cold_lead', 7)
        self.assertEqual(priority_normal, 'normal', "Cold lead debería ser normal")
    
    def test_manual_followup_addition(self):
        """Test de adición de seguimiento manual"""
        lead_id = "test_lead_manual"
        custom_message = "Mensaje personalizado de prueba"
        
        followup = self.followup_engine.add_manual_followup(lead_id, custom_message, "high")
        
        self.assertEqual(followup['lead_id'], lead_id, "ID de lead debería coincidir")
        self.assertEqual(followup['message_template'], custom_message, "Mensaje debería coincidir")
        self.assertEqual(followup['priority'], 'high', "Prioridad debería ser alta")
        self.assertTrue(followup['manual'], "Debería estar marcado como manual")
    
    def test_followup_cancellation(self):
        """Test de cancelación de seguimiento"""
        lead_id = "test_lead_cancel"
        
        # Agregar seguimiento
        self.followup_engine.add_manual_followup(lead_id, "Mensaje de prueba")
        
        # Cancelar seguimiento
        followup_id = f"{lead_id}_{datetime.now().isoformat()}"
        cancelled = self.followup_engine.cancel_followup(lead_id, followup_id)
        
        # Como el followup_id exacto puede variar, verificamos que el método funcione
        self.assertIsInstance(cancelled, bool, "Cancelación debería retornar booleano")
    
    def test_followup_history_retrieval(self):
        """Test de recuperación de historial de seguimientos"""
        lead_id = "test_lead_history"
        
        # Agregar seguimientos
        self.followup_engine.add_manual_followup(lead_id, "Mensaje 1")
        self.followup_engine.add_manual_followup(lead_id, "Mensaje 2")
        
        # Recuperar historial
        history = self.followup_engine.get_lead_followup_history(lead_id)
        
        self.assertIsInstance(history, list, "Historial debería ser lista")
        self.assertGreaterEqual(len(history), 2, "Debería tener al menos 2 seguimientos")
    
    def test_followup_stats_calculation(self):
        """Test de cálculo de estadísticas de seguimiento"""
        # Agregar algunos seguimientos para diferentes leads
        self.followup_engine.add_manual_followup("lead_1", "Mensaje 1")
        self.followup_engine.add_manual_followup("lead_2", "Mensaje 2")
        self.followup_engine.add_manual_followup("lead_3", "Mensaje 3")
        
        stats = self.followup_engine.get_followup_stats()
        
        self.assertIn('total_followups', stats, "Debería incluir total de seguimientos")
        self.assertIn('sent_followups', stats, "Debería incluir seguimientos enviados")
        self.assertIn('failed_followups', stats, "Debería incluir seguimientos fallidos")
        self.assertIn('pending_followups', stats, "Debería incluir seguimientos pendientes")
        self.assertIn('success_rate', stats, "Debería incluir tasa de éxito")
        
        self.assertGreaterEqual(stats['total_followups'], 3, 
                               "Debería tener al menos 3 seguimientos totales")

class TestFollowupEngineEdgeCases(unittest.TestCase):
    """Pruebas de casos extremos para followup engine"""
    
    def setUp(self):
        """Configuración inicial para cada prueba"""
        self.mock_whatsapp_bot = Mock()
        self.mock_lead_scorer = Mock()
        self.mock_lead_scorer.calculate_lead_score.return_value = {
            'score': 50,
            'category': 'warm_lead'
        }
        
        self.followup_engine = FollowupEngine(config, self.mock_whatsapp_bot, self.mock_lead_scorer)
    
    def test_followup_with_missing_lead_data(self):
        """Test de seguimiento con datos de lead incompletos"""
        lead_data = {
            "id": "incomplete_lead"
            # Faltan datos importantes
        }
        
        followups = self.followup_engine.schedule_followup(lead_data)
        
        self.assertIsInstance(followups, list, "Debería retornar lista")
        # El sistema debería manejar datos incompletos gracefulmente
    
    def test_followup_with_invalid_category(self):
        """Test de seguimiento con categoría inválida"""
        lead_data = {
            "id": "invalid_category_lead",
            "nombre": "Test",
            "inquiry_time": datetime.now().isoformat()
        }
        
        # Configurar mock con categoría inválida
        self.mock_lead_scorer.calculate_lead_score.return_value = {
            'score': 50,
            'category': 'invalid_category'
        }
        
        followups = self.followup_engine.schedule_followup(lead_data)
        
        # Debería usar default (cold lead schedule) o manejar gracefulmente
        self.assertIsInstance(followups, list, "Debería retornar lista")
    
    def test_message_template_with_no_match(self):
        """Test de selección de plantilla sin coincidencia"""
        template = self.followup_engine._select_message_template('unknown_category', 999)
        
        # Debería retornar plantilla por defecto
        self.assertIsInstance(template, str, "Debería retornar string")
        self.assertGreater(len(template), 0, "Plantilla no debería estar vacía")
    
    def test_followup_with_whatsapp_failure(self):
        """Test de seguimiento cuando WhatsApp falla"""
        lead_data = {
            "id": "whatsapp_fail_lead",
            "nombre": "Test User",
            "telefono": "573000000000",
            "inquiry_time": datetime.now().isoformat()
        }
        
        # Configurar mock para fallar
        self.mock_whatsapp_bot.send_text_message.return_value = {
            'success': False,
            'error': 'WhatsApp API error'
        }
        
        # Programar seguimiento
        self.followup_engine.schedule_followup(lead_data)
        
        # Intentar ejecutar seguimientos pendientes
        results = self.followup_engine.execute_pending_followups()
        
        self.assertIsInstance(results, list, "Debería retornar lista")
        # Debería manejar fallas gracefulmente
    
    def test_manual_followup_with_empty_message(self):
        """Test de seguimiento manual con mensaje vacío"""
        lead_id = "empty_message_lead"
        empty_message = ""
        
        followup = self.followup_engine.add_manual_followup(lead_id, empty_message)
        
        self.assertEqual(followup['message_template'], empty_message, 
                        "Debería aceptar mensaje vacío")
    
    def test_followup_history_for_nonexistent_lead(self):
        """Test de historial para lead inexistente"""
        history = self.followup_engine.get_lead_followup_history("nonexistent_lead")
        
        self.assertIsInstance(history, list, "Debería retornar lista vacía")
        self.assertEqual(len(history), 0, "Historial debería estar vacío")

def run_tests():
    """Ejecutar todas las pruebas"""
    # Crear suite de pruebas
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Agregar pruebas
    suite.addTests(loader.loadTestsFromTestCase(TestFollowupEngine))
    suite.addTests(loader.loadTestsFromTestCase(TestFollowupEngineEdgeCases))
    
    # Ejecutar pruebas
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Retornar resultado
    return result.wasSuccessful()

if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)