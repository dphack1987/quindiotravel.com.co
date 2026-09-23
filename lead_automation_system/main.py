"""
Sistema Principal de Automatización de Leads
Quindío Travel - Sistema para lograr 4+ reservas mensuales
Orquestador que integra todos los módulos del sistema
"""

import sys
import os
import json
from datetime import datetime, timedelta
from typing import Dict, List
import schedule
import time

# Agregar directorio actual al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import config
from modules.lead_scoring import LeadScoringEngine
from modules.whatsapp_bot import WhatsAppBusinessBot
from modules.followup_engine import FollowupEngine
from modules.analytics import LeadAnalytics

class LeadAutomationSystem:
    """Sistema principal de automatización de leads"""
    
    def __init__(self):
        self.config = config
        self.lead_scorer = LeadScoringEngine(config)
        self.whatsapp_bot = WhatsAppBusinessBot(config)
        self.followup_engine = FollowupEngine(config, self.whatsapp_bot, self.lead_scorer)
        self.analytics = LeadAnalytics(config)
        
        # Cargar datos iniciales
        self.leads_db = self.load_leads_database()
        self.conversion_data = self.analytics.conversion_data
        
        print("🚀 Sistema de Automatización de Leads - Quindío Travel")
        print(f"📊 Objetivo: {config['analytics'].conversion_target_monthly} reservas/mes")
        print(f"🎯 Tasa objetivo: {config['analytics'].target_conversion_rate*100:.1f}%")
        print(f"📱 WhatsApp: {config['whatsapp'].phone_number}")
        print("✅ Sistema inicializado correctamente\n")
    
    def load_leads_database(self) -> List[Dict]:
        """Cargar base de datos de leads"""
        try:
            with open('data/leads_db.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            # Crear estructura inicial si no existe
            self.initialize_data_structure()
            return []
    
    def initialize_data_structure(self):
        """Inicializar estructura de datos si no existe"""
        # Crear directorios necesarios
        os.makedirs('data', exist_ok=True)
        os.makedirs('utils', exist_ok=True)
        
        # Crear archivos de datos vacíos
        with open('data/leads_db.json', 'w', encoding='utf-8') as f:
            json.dump([], f)
        
        with open('data/conversion_data.json', 'w', encoding='utf-8') as f:
            json.dump([], f)
        
        with open('data/scoring_rules.json', 'w', encoding='utf-8') as f:
            json.dump({
                "interest_signals": {
                    "specific_plan_mentioned": 15,
                    "date_range_provided": 12,
                    "guest_count_provided": 10,
                    "budget_mentioned": 12,
                    "question_asked": 8,
                    "whatsapp_clicked": 20
                },
                "quality_signals": {
                    "complete_sentence": 5,
                    "relevant_destination": 10,
                    "reasonable_budget": 15,
                    "realistic_dates": 10,
                    "contact_provided": 8
                },
                "behavioral_signals": {
                    "page_views": 2,
                    "time_on_site": 3,
                    "return_visitor": 15,
                    "mobile_device": 5,
                    "desktop_device": 7
                },
                "timing_signals": {
                    "response_under_1hr": 10,
                    "response_1_24hr": 5,
                    "response_24_72hr": 2,
                    "weekend_inquiry": 8,
                    "holiday_season": 12
                }
            }, f, indent=2)
        
        # Crear plantillas de mensajes
        message_templates = {
            "hot_lead": {
                "immediate": [
                    "🌟 ¡Hola {nombre}! Gracias por tu interés. Tengo disponibilidad inmediata para tu viaje al Eje Cafetero. ¿Podrías confirmarme tu fecha preferida?",
                    "🎯 ¡Excelente elección {nombre}! Estoy revisando nuestra disponibilidad para tu viaje. ¿Te interesa alguna fecha específica?",
                    "🌿 Hola {nombre}, te escribo de Quindío Travel. Tengo excelentes opciones disponibles para tu plan. ¿Podrías decirme cuándo prefieres viajar?"
                ],
                "2_days": [
                    "🌟 Hola {nombre}, ¿cómo estás? Quería seguir contigo sobre tu viaje al Eje Cafetero. ¿Tienes alguna pregunta adicional?",
                    "🎯 {nombre}, te recuerdo que tengo disponibilidad confirmada para tu fechas de interés. ¿Te gustaría proceder con la reserva?",
                    "🌿 {nombre}, encontré una opción especial que podría ser perfecta para tu grupo. ¿Te interesa verla?"
                ],
                "1_week": [
                    "🌟 {nombre}, espero que estés bien. Quería saber si todavía estás interesado en tu viaje al Eje Cafetero. Tengo algunas promociones activas.",
                    "🎯 Hola {nombre}, te escribo para seguir con tu consulta. Si decides viajar en las próximas semanas, tengo disponibilidad garantizada.",
                    "🌿 {nombre}, recuerda que la temporada alta está cerca. Si reservas ahora, aseguras los mejores precios y disponibilidad."
                ],
                "2_weeks": [
                    "🌟 {nombre}, última oportunidad para las fechas que mencionaste. ¿Te gustaría que te reserve provisionalmente?",
                    "🎯 Hola {nombre}, quería ofrecerte una oferta especial por tiempo limitado. Solo válida hasta fin de semana.",
                    "🌿 {nombre}, te recuerdo que estamos aquí para ayudarte a planificar tu viaje perfecto. ¿En qué puedo asistirte?"
                ]
            },
            "warm_lead": {
                "1_day": [
                    "🌿 Hola {nombre} de Quindío Travel. ¿Cómo estás? Te interesé por tu consulta sobre planes turísticos.",
                    "🎯 {nombre}, espero que estés bien. Me gustaría seguir con tu consulta sobre el Eje Cafetero.",
                    "🌟 Hola {nombre}, quería preguntarte si seguías interesado en conocer nuestros planes del Eje Cafetero."
                ],
                "3_days": [
                    "🌿 {nombre}, encontré algunos planes que podrían ser perfectos para ti. ¿Te gustaría que te envíe la información?",
                    "🎯 Hola {nombre}, tengo algunas opciones especiales disponibles para tu temporada de interés.",
                    "🌟 {nombre}, te comparto nuestros planes más populares para que puedas comparar y elegir el ideal."
                ],
                "1_week": [
                    "🌿 {nombre}, ¿cómo está tu búsqueda de viaje? Tengo nuevas promociones disponibles.",
                    "🎯 Hola {nombre}, quería recordarte que estamos aquí para ayudarte a planificar tu viaje perfecto.",
                    "🌟 {nombre}, te invito a conocer nuestras experiencias exclusivas en el Eje Cafetero."
                ],
                "2_weeks": [
                    "🌿 {nombre}, temporada alta se acerca. Si reservas ahora, aseguras los mejores precios.",
                    "🎯 Hola {nombre}, tengo disponibilidad confirmada para fechas cercanas. ¿Te interesa?",
                    "🌟 {nombre}, te recuerdo que nuestra misión es que tengas la mejor experiencia en el Eje Cafetero."
                ],
                "1_month": [
                    "🌿 {nombre}, espero que te encuentres bien. ¿Has pensado en tu próximo viaje?",
                    "🎯 Hola {nombre}, quería saber si seguías interesado en descubrir el Eje Cafetero.",
                    "🌟 {nombre}, te compartimos nuevas experiencias que hemos agregado a nuestros planes."
                ]
            },
            "cold_lead": {
                "1_week": [
                    "🌿 Hola {nombre}, te saluda Quindío Travel. ¿Te gustaría recibir información sobre nuestros planes?",
                    "🎯 {nombre}, te invitamos a descubrir los tesoros del Eje Cafetero con nosotros.",
                    "🌟 Hola {nombre}, tenemos experiencias especiales que podrían interesarte."
                ],
                "2_weeks": [
                    "🌿 {nombre}, ¿te gustaría conocer nuestros destinos más populares?",
                    "🎯 Hola {nombre}, te compartimos testimonios de viajeros felices.",
                    "🌟 {nombre}, tenemos planes que se adaptan a diferentes presupuestos."
                ],
                "1_month": [
                    "🌿 {nombre}, temporada especial de promociones. ¿Te gustaría ver nuestras ofertas?",
                    "🎯 Hola {nombre}, recuerda que el Eje Cafetero te espera todo el año.",
                    "🌟 {nombre}, te invitamos a formar parte de la familia Quindío Travel."
                ],
                "2_months": [
                    "🌿 {nombre}, ¿planeas viajes especiales este año? Podemos ayudarte.",
                    "🎯 Hola {nombre}, el café colombiano te espera en Quindío Travel.",
                    "🌟 {nombre}, esperamos verte pronto en el hermoso Eje Cafetero."
                ]
            }
        }
        
        with open('utils/message_templates.json', 'w', encoding='utf-8') as f:
            json.dump(message_templates, f, indent=2, ensure_ascii=False)
        
        print("📁 Estructura de datos inicializada")
    
    def process_new_lead(self, lead_data: Dict) -> Dict:
        """Procesar un nuevo lead a través del sistema completo"""
        print(f"📥 Procesando nuevo lead: {lead_data.get('nombre', 'Desconocido')}")
        
        # 1. Calcular score del lead
        lead_score = self.lead_scorer.calculate_lead_score(lead_data)
        print(f"🎯 Score: {lead_score['score']}/100 - Categoría: {lead_score['category']}")
        
        # 2. Predecir probabilidad de conversión
        prediction = self.analytics.predict_conversion_probability(lead_data)
        print(f"🔮 Probabilidad de conversión: {prediction['probability']*100:.1f}%")
        
        # 3. Programar seguimientos automáticos
        followups = self.followup_engine.schedule_followup(lead_data)
        print(f"📅 Seguimientos programados: {len(followups)}")
        
        # 4. Enviar mensaje inicial según categoría
        if lead_score['category'] == 'hot_lead':
            result = self.whatsapp_bot.send_hot_lead_message(lead_data)
            print(f"📱 Mensaje lead caliente enviado: {result['success']}")
        elif lead_score['category'] == 'warm_lead':
            result = self.whatsapp_bot.send_warm_lead_message(lead_data)
            print(f"📱 Mensaje lead tibio enviado: {result['success']}")
        else:
            result = self.whatsapp_bot.send_cold_lead_message(lead_data)
            print(f"📱 Mensaje lead frío enviado: {result['success']}")
        
        # 5. Guardar lead en base de datos
        lead_id = f"lead_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        lead_data['id'] = lead_id
        lead_data['score'] = lead_score
        lead_data['prediction'] = prediction
        lead_data['processed_date'] = datetime.now().isoformat()
        
        self.leads_db.append(lead_data)
        self.save_leads_database()
        
        print(f"✅ Lead procesado y guardado: {lead_id}\n")
        
        return {
            "lead_id": lead_id,
            "score": lead_score,
            "prediction": prediction,
            "followups_scheduled": len(followups),
            "initial_message_sent": result['success']
        }
    
    def execute_daily_tasks(self):
        """Ejecutar tareas diarias del sistema"""
        print(f"🔄 Ejecutando tareas diarias - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # 1. Ejecutar seguimientos pendientes
        followup_results = self.followup_engine.execute_pending_followups()
        print(f"📧 Seguimientos ejecutados: {len(followup_results)}")
        
        # 2. Procesar cola de mensajes de WhatsApp
        message_results = self.whatsapp_bot.process_message_queue()
        print(f"📱 Mensajes enviados: {len(message_results)}")
        
        # 3. Generar reporte diario
        daily_report = self.generate_daily_report()
        print(f"📊 Reporte diario generado")
        
        # 4. Identificar leads de alta prioridad
        high_priority_leads = self.identify_high_priority_leads()
        print(f"🚨 Leads de alta prioridad: {len(high_priority_leads)}")
        
        return {
            "followups_executed": len(followup_results),
            "messages_sent": len(message_results),
            "high_priority_leads": len(high_priority_leads),
            "daily_report": daily_report
        }
    
    def generate_daily_report(self) -> Dict:
        """Generar reporte diario del sistema"""
        conversion_rate = self.analytics.calculate_conversion_rate()
        followup_stats = self.followup_engine.get_followup_stats()
        
        report = {
            "date": datetime.now().strftime('%Y-%m-%d'),
            "total_leads": len(self.leads_db),
            "conversion_rate": conversion_rate,
            "followup_stats": followup_stats,
            "whatsapp_messages_sent": self.whatsapp_bot.daily_message_count,
            "target_progress": {
                "target": self.config['analytics'].conversion_target_monthly,
                "current_month_conversions": conversion_rate['total_conversions'],
                "percentage": (conversion_rate['total_conversions'] / self.config['analytics'].conversion_target_monthly * 100) if self.config['analytics'].conversion_target_monthly > 0 else 0
            }
        }
        
        # Guardar reporte
        report_filename = f"data/reports/daily_{datetime.now().strftime('%Y%m%d')}.json"
        os.makedirs('data/reports', exist_ok=True)
        
        with open(report_filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        return report
    
    def identify_high_priority_leads(self) -> List[Dict]:
        """Identificar leads de alta prioridad para acción inmediata"""
        high_priority_leads = []
        
        for lead in self.leads_db:
            if lead.get('score', {}).get('category') == 'hot_lead':
                # Verificar si necesita acción inmediata
                processed_date = datetime.fromisoformat(lead.get('processed_date', datetime.now().isoformat()))
                hours_since_processed = (datetime.now() - processed_date).total_seconds() / 3600
                
                if hours_since_processed < 24:  # Leads calientes de las últimas 24 horas
                    high_priority_leads.append({
                        "lead_id": lead.get('id'),
                        "nombre": lead.get('nombre'),
                        "score": lead.get('score', {}).get('score'),
                        "phone": lead.get('telefono'),
                        "hours_since_processed": hours_since_processed,
                        "recommendation": "Llamada inmediata dentro de 15 minutos"
                    })
        
        return high_priority_leads
    
    def generate_monthly_report(self) -> Dict:
        """Generar reporte mensual completo"""
        print("📊 Generando reporte mensual completo...")
        
        report = self.analytics.generate_conversion_report()
        
        # Agregar estadísticas del sistema
        report["system_stats"] = {
            "total_leads_in_system": len(self.leads_db),
            "hot_leads": len([l for l in self.leads_db if l.get('score', {}).get('category') == 'hot_lead']),
            "warm_leads": len([l for l in self.leads_db if l.get('score', {}).get('category') == 'warm_lead']),
            "cold_leads": len([l for l in self.leads_db if l.get('score', {}).get('category') == 'cold_lead']),
            "followup_stats": self.followup_engine.get_followup_stats(),
            "whatsapp_messages_monthly": self.whatsapp_bot.daily_message_count
        }
        
        # Guardar reporte mensual
        report_filename = f"data/reports/monthly_{datetime.now().strftime('%Y%m')}.json"
        os.makedirs('data/reports', exist_ok=True)
        
        with open(report_filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"📄 Reporte mensual guardado: {report_filename}")
        
        return report
    
    def save_leads_database(self):
        """Guardar base de datos de leads"""
        with open('data/leads_db.json', 'w', encoding='utf-8') as f:
            json.dump(self.leads_db, f, indent=2, ensure_ascii=False)
    
    def run_scheduled_tasks(self):
        """Ejecutar tareas programadas automáticamente"""
        # Programar tarea diaria
        schedule.every().day.at("09:00").do(self.execute_daily_tasks)
        schedule.every().day.at("14:00").do(self.execute_daily_tasks)
        schedule.every().day.at("18:00").do(self.execute_daily_tasks)
        
        # Programar reporte mensual
        schedule.every().month.do(self.generate_monthly_report)
        
        print("⏰ Tareas programadas configuradas:")
        print("   - Ejecución diaria: 09:00, 14:00, 18:00")
        print("   - Reporte mensual: Primer día de cada mes")
        print("🔄 Sistema en modo de ejecución programada...")
        
        while True:
            schedule.run_pending()
            time.sleep(60)  # Verificar cada minuto
    
    def run_interactive_mode(self):
        """Ejecutar sistema en modo interactivo"""
        print("🎮 Sistema en modo interactivo")
        print("Comandos disponibles:")
        print("  1. Procesar nuevo lead")
        print("  2. Ejecutar tareas diarias")
        print("  3. Generar reporte mensual")
        print("  4. Ver leads de alta prioridad")
        print("  5. Ver estadísticas")
        print("  6. Salir")
        
        while True:
            try:
                command = input("\n🔹 Ingrese comando (1-6): ").strip()
                
                if command == "1":
                    self.interactive_process_lead()
                elif command == "2":
                    results = self.execute_daily_tasks()
                    print(f"✅ Tareas ejecutadas: {results}")
                elif command == "3":
                    report = self.generate_monthly_report()
                    print(f"📊 Reporte generado: {report['target_status']['current_conversions']}/{report['target_status']['target_conversions']} conversiones")
                elif command == "4":
                    leads = self.identify_high_priority_leads()
                    print(f"🚨 Leads de alta prioridad: {len(leads)}")
                    for lead in leads:
                        print(f"   - {lead['nombre']}: {lead['recommendation']}")
                elif command == "5":
                    self.show_statistics()
                elif command == "6":
                    print("👋 Saliendo del sistema...")
                    break
                else:
                    print("❌ Comando no válido")
            
            except KeyboardInterrupt:
                print("\n👋 Interrupción detectada. Saliendo...")
                break
            except Exception as e:
                print(f"❌ Error: {str(e)}")
    
    def interactive_process_lead(self):
        """Procesar lead en modo interactivo"""
        print("📝 Ingrese datos del nuevo lead:")
        
        lead_data = {
            "nombre": input("Nombre: "),
            "telefono": input("Teléfono (con código país): "),
            "mensaje": input("Mensaje: "),
            "destino": input("Destino (opcional): "),
            "fecha_deseada": input("Fecha deseada (YYYY-MM-DD, opcional): "),
            "num_personas": input("Número de personas (opcional): "),
            "presupuesto": input("Presupuesto (opcional): "),
            "inquiry_time": datetime.now().isoformat(),
            "device": "desktop",  # Por defecto
            "page_views": 3,  # Por defecto
            "time_on_site": 5,  # Por defecto
            "is_return_visitor": False  # Por defecto
        }
        
        result = self.process_new_lead(lead_data)
        print(f"✅ Lead procesado: {result}")
    
    def show_statistics(self):
        """Mostrar estadísticas del sistema"""
        conversion_rate = self.analytics.calculate_conversion_rate()
        followup_stats = self.followup_engine.get_followup_stats()
        
        print("\n📊 ESTADÍSTICAS DEL SISTEMA")
        print("=" * 50)
        print(f"Total leads en sistema: {len(self.leads_db)}")
        print(f"Tasa de conversión: {conversion_rate['conversion_rate']:.1f}%")
        print(f"Conversiones este mes: {conversion_rate['total_conversions']}")
        print(f"Objetivo mensual: {self.config['analytics'].conversion_target_monthly}")
        print(f"Progreso: {conversion_rate['total_conversions']}/{self.config['analytics'].conversion_target_monthly} ({(conversion_rate['total_conversions']/self.config['analytics'].conversion_target_monthly*100) if self.config['analytics'].conversion_target_monthly > 0 else 0:.1f}%)")
        print(f"\nSeguimientos:")
        print(f"  Total: {followup_stats['total_followups']}")
        print(f"  Enviados: {followup_stats['sent_followups']}")
        print(f"  Fallidos: {followup_stats['failed_followups']}")
        print(f"  Pendientes: {followup_stats['pending_followups']}")
        print(f"  Tasa éxito: {followup_stats['success_rate']:.1f}%")
        print(f"\nWhatsApp:")
        print(f"  Mensajes enviados hoy: {self.whatsapp_bot.daily_message_count}")
        print("=" * 50)

def main():
    """Función principal"""
    # Inicializar sistema
    system = LeadAutomationSystem()
    
    # Menú de modo de ejecución
    print("Seleccione modo de ejecución:")
    print("1. Modo interactivo")
    print("2. Modo programado (automático)")
    
    mode = input("Seleccione modo (1-2): ").strip()
    
    if mode == "1":
        system.run_interactive_mode()
    elif mode == "2":
        system.run_scheduled_tasks()
    else:
        print("❌ Modo no válido. Iniciando modo interactivo por defecto...")
        system.run_interactive_mode()

if __name__ == "__main__":
    main()