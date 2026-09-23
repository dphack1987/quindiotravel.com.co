"""
Wizard de Configuración Inicial - Lead Automation System
Asistente interactivo para configuración inicial del sistema
"""

import os
import json
from typing import Dict, Optional

class SetupWizard:
    """Wizard interactivo para configuración inicial"""
    
    def __init__(self):
        self.config_data = {}
        self.steps = [
            'welcome',
            'whatsapp_config',
            'business_info',
            'scoring_config',
            'followup_config',
            'review',
            'save'
        ]
        self.current_step = 0
    
    def print_header(self, title: str):
        """Imprimir encabezado del wizard"""
        print("\n" + "=" * 60)
        print(f"🧙 {title}")
        print("=" * 60)
    
    def print_step(self, step_num: int, total_steps: int, title: str):
        """Imprimir información del paso actual"""
        print(f"\n📍 Paso {step_num}/{total_steps}: {title}")
        print("-" * 60)
    
    def step_welcome(self) -> Dict:
        """Paso de bienvenida"""
        self.print_header("WIZARD DE CONFIGURACIÓN INICIAL")
        
        print("""
🎯 Bienvenido al Wizard de Configuración del Sistema de Automatización de Leads

Este wizard te guiará a través de la configuración inicial del sistema para lograr
tu objetivo de 4+ reservas mensuales.

⚠️  IMPORTANTE:
- Puedes presionar Ctrl+C en cualquier momento para cancelar
- Puedes usar los valores por defecto presionando Enter
- La configuración se guardará en config.py
        """)
        
        response = input("\n¿Deseas continuar con la configuración? (s/n): ").strip().lower()
        
        if response in ['s', 'si', 'y', 'yes']:
            return {'continue': True}
        else:
            print("❌ Configuración cancelada por el usuario")
            return {'continue': False}
    
    def step_whatsapp_config(self) -> Dict:
        """Configuración de WhatsApp Business API"""
        self.print_step(1, len(self.steps), "Configuración de WhatsApp Business API")
        
        print("""
📱 CONFIGURACIÓN DE WHATSAPP BUSINESS API

El sistema puede enviar mensajes automáticos a través de WhatsApp Business API.
Esto requiere obtener un token de Facebook Developers.

🔗 Instrucciones:
1. Ve a https://developers.facebook.com/
2. Crea una aplicación WhatsApp Business
3. Obtén el Access Token y Business ID
4. Ingresa los datos abajo

⚠️  Si no tienes el token ahora, puedes dejar estos campos vacíos y
configurarlos más tarde editando el archivo .env
        """)
        
        phone_number = input("Número de WhatsApp Business (ej: 573174426044): ").strip()
        api_token = input("WhatsApp API Token (opcional, dejar vacío): ").strip()
        business_id = input("Business ID (opcional, dejar vacío): ").strip()
        
        # Valores por defecto
        if not phone_number:
            phone_number = "573174426044"
        
        self.config_data['whatsapp'] = {
            'phone_number': phone_number,
            'api_token': api_token or '',
            'business_profile_id': business_id or '',
            'max_messages_per_day': 100,
            'message_delay_seconds': 30,
            'business_hours_start': 8,
            'business_hours_end': 20
        }
        
        print(f"✅ Configuración de WhatsApp guardada")
        return {'success': True}
    
    def step_business_info(self) -> Dict:
        """Configuración de información del negocio"""
        self.print_step(2, len(self.steps), "Información del Negocio")
        
        print("""
🏢 INFORMACIÓN DEL NEGOCIO

Configura la información de tu negocio que se usará en los mensajes
automatizados y en el sistema de lead scoring.
        """)
        
        business_name = input("Nombre del negocio (Quindío Travel): ").strip() or "Quindío Travel"
        rnt_number = input("Número RNT (18152): ").strip() or "18152"
        contact_phone = input("Teléfono de contacto (+57-317-4426044): ").strip() or "+57-317-4426044"
        contact_email = input("Email de contacto (gerencia@quindiotravel.net): ").strip() or "gerencia@quindiotravel.net"
        
        self.config_data['business'] = {
            'name': business_name,
            'rnt': rnt_number,
            'phone': contact_phone,
            'email': contact_email
        }
        
        print(f"✅ Información del negocio guardada")
        return {'success': True}
    
    def step_scoring_config(self) -> Dict:
        """Configuración del sistema de lead scoring"""
        self.print_step(3, len(self.steps), "Configuración de Lead Scoring")
        
        print("""
🎯 CONFIGURACIÓN DE LEAD SCORING

El sistema califica los leads automáticamente según varios factores.
Puedes ajustar los umbrales de calificación.
        """)
        
        min_hot_score = input("Puntuación mínima para Hot Lead (70): ").strip()
        min_warm_score = input("Puntuación mínima para Warm Lead (50): ").strip()
        
        # Convertir a enteros con valores por defecto
        try:
            min_hot_score = int(min_hot_score) if min_hot_score else 70
        except ValueError:
            min_hot_score = 70
        
        try:
            min_warm_score = int(min_warm_score) if min_warm_score else 50
        except ValueError:
            min_warm_score = 50
        
        self.config_data['scoring'] = {
            'min_score_for_hot_lead': min_hot_score,
            'min_score_for_warm_lead': min_warm_score,
            'cold_lead_score': 30
        }
        
        print(f"✅ Configuración de lead scoring guardada")
        print(f"   Hot Lead: {min_hot_score}+ puntos")
        print(f"   Warm Lead: {min_warm_score}+ puntos")
        print(f"   Cold Lead: <{min_warm_score} puntos")
        
        return {'success': True}
    
    def step_followup_config(self) -> Dict:
        """Configuración del sistema de seguimiento"""
        self.print_step(4, len(self.steps), "Configuración de Seguimiento Automatizado")
        
        print("""
📅 CONFIGURACIÓN DE SEGUIMIENTO AUTOMATIZADO

El sistema programará seguimientos automáticos según la categoría del lead.
Puedes personalizar los días de seguimiento para cada categoría.
        """)
        
        print("\n🔥 Días de seguimiento para Hot Lead (separados por coma):")
        print("   Por defecto: 0,2,7,14 (hoy, 2 días, 1 semana, 2 semanas)")
        hot_schedule = input("   Días (0,2,7,14): ").strip() or "0,2,7,14"
        
        print("\n⏰ Días de seguimiento para Warm Lead (separados por coma):")
        print("   Por defecto: 1,3,7,14,30 (mañana, 3 días, 1 semana, 2 semanas, 1 mes)")
        warm_schedule = input("   Días (1,3,7,14,30): ").strip() or "1,3,7,14,30"
        
        print("\n❄️  Días de seguimiento para Cold Lead (separados por coma):")
        print("   Por defecto: 7,14,30,60 (1 semana, 2 semanas, 1 mes, 2 meses)")
        cold_schedule = input("   Días (7,14,30,60): ").strip() or "7,14,30,60"
        
        # Convertir strings a listas de enteros
        try:
            hot_days = [int(d.strip()) for d in hot_schedule.split(',')]
            warm_days = [int(d.strip()) for d in warm_schedule.split(',')]
            cold_days = [int(d.strip()) for d in cold_schedule.split(',')]
        except ValueError:
            print("⚠️  Error en formato de días, usando valores por defecto")
            hot_days = [0, 2, 7, 14]
            warm_days = [1, 3, 7, 14, 30]
            cold_days = [7, 14, 30, 60]
        
        self.config_data['followup'] = {
            'followup_schedule': {
                'hot_lead': hot_days,
                'warm_lead': warm_days,
                'cold_lead': cold_days
            }
        }
        
        print(f"✅ Configuración de seguimiento guardada")
        return {'success': True}
    
    def step_analytics_config(self) -> Dict:
        """Configuración de análisis y objetivos"""
        self.print_step(5, len(self.steps), "Configuración de Análisis y Objetivos")
        
        print("""
📊 CONFIGURACIÓN DE ANÁLISIS Y OBJETIVOS

Configura los objetivos del sistema y las métricas que deseas rastrear.
        """)
        
        target_conversions = input("Objetivo de conversiones mensuales (4): ").strip()
        target_conversion_rate = input("Tasa de conversión objetivo en % (8): ").strip()
        leads_needed = input("Leads necesarios por mes (50): ").strip()
        
        # Convertir a números con valores por defecto
        try:
            target_conversions = int(target_conversions) if target_conversions else 4
        except ValueError:
            target_conversions = 4
        
        try:
            target_conversion_rate = float(target_conversion_rate) / 100 if target_conversion_rate else 0.08
        except ValueError:
            target_conversion_rate = 0.08
        
        try:
            leads_needed = int(leads_needed) if leads_needed else 50
        except ValueError:
            leads_needed = 50
        
        self.config_data['analytics'] = {
            'conversion_target_monthly': target_conversions,
            'target_conversion_rate': target_conversion_rate,
            'leads_needed_per_month': leads_needed,
            'high_value_lead_threshold': 1000000  # 1M COP
        }
        
        print(f"✅ Configuración de análisis guardada")
        print(f"   Objetivo mensual: {target_conversions} conversiones")
        print(f"   Tasa objetivo: {target_conversion_rate*100:.1f}%")
        print(f"   Leads necesarios: {leads_needed}/mes")
        
        return {'success': True}
    
    def step_review(self) -> Dict:
        """Revisión de la configuración"""
        self.print_step(6, len(self.steps), "Revisión de Configuración")
        
        print("""
📋 REVISIÓN DE CONFIGURACIÓN

Por favor revisa la configuración antes de guardar:
        """)
        
        print("\n📱 WhatsApp:")
        print(f"   Número: {self.config_data['whatsapp']['phone_number']}")
        print(f"   API Token: {'Configurado' if self.config_data['whatsapp']['api_token'] else 'No configurado'}")
        
        print("\n🏢 Negocio:")
        print(f"   Nombre: {self.config_data['business']['name']}")
        print(f"   RNT: {self.config_data['business']['rnt']}")
        print(f"   Teléfono: {self.config_data['business']['phone']}")
        
        print("\n🎯 Lead Scoring:")
        print(f"   Hot Lead: {self.config_data['scoring']['min_score_for_hot_lead']}+ puntos")
        print(f"   Warm Lead: {self.config_data['scoring']['min_score_for_warm_lead']}+ puntos")
        
        print("\n📅 Seguimiento:")
        print(f"   Hot Lead: {self.config_data['followup']['followup_schedule']['hot_lead']}")
        print(f"   Warm Lead: {self.config_data['followup']['followup_schedule']['warm_lead']}")
        print(f"   Cold Lead: {self.config_data['followup']['followup_schedule']['cold_lead']}")
        
        print("\n📊 Objetivos:")
        print(f"   Conversiones mensuales: {self.config_data['analytics']['conversion_target_monthly']}")
        print(f"   Tasa de conversión: {self.config_data['analytics']['target_conversion_rate']*100:.1f}%")
        print(f"   Leads necesarios: {self.config_data['analytics']['leads_needed_per_month']}/mes")
        
        response = input("\n¿Estás satisfecho con esta configuración? (s/n): ").strip().lower()
        
        if response in ['s', 'si', 'y', 'yes']:
            return {'approved': True}
        else:
            response_edit = input("¿Qué deseas editar? (whatsapp/scoring/followup/analytics): ").strip().lower()
            
            if response_edit == 'whatsapp':
                return self.step_whatsapp_config()
            elif response_edit == 'scoring':
                return self.step_scoring_config()
            elif response_edit == 'followup':
                return self.step_followup_config()
            elif response_edit == 'analytics':
                return self.step_analytics_config()
            else:
                print("❌ Opción no válida, usando configuración actual")
                return {'approved': True}
    
    def step_save(self) -> Dict:
        """Guardar configuración"""
        self.print_step(7, len(self.steps), "Guardar Configuración")
        
        try:
            # Guardar configuración en archivo JSON
            config_file = 'config_user.json'
            
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config_data, f, indent=2, ensure_ascii=False)
            
            print(f"✅ Configuración guardada en {config_file}")
            
            # Guardar variables de entorno
            env_file = '.env'
            env_content = f"""# WhatsApp Business API Configuration
WHATSAPP_API_TOKEN={self.config_data['whatsapp']['api_token']}
WHATSAPP_BUSINESS_ID={self.config_data['whatsapp']['business_profile_id']}

# Sistema Configuration
LEAD_AUTOMATION_MODE=interactive
LOG_LEVEL=INFO
DEBUG=False
"""
            
            with open(env_file, 'w', encoding='utf-8') as f:
                f.write(env_content)
            
            print(f"✅ Variables de entorno guardadas en {env_file}")
            
            print("\n🎉 CONFIGURACIÓN COMPLETADA EXITOSAMENTE!")
            print("\n📝 PRÓXIMOS PASOS:")
            print("1. Ejecutar: python main.py")
            print("2. Seleccionar modo interactivo")
            print("3. Procesar tu primer lead de prueba")
            print("4. Abrir dashboard.html para monitoreo")
            
            return {'success': True, 'config_file': config_file}
        
        except Exception as e:
            print(f"❌ Error al guardar configuración: {str(e)}")
            return {'success': False, 'error': str(e)}
    
    def run_wizard(self) -> Dict:
        """Ejecutar el wizard completo"""
        try:
            # Paso 1: Bienvenida
            welcome_result = self.step_welcome()
            if not welcome_result.get('continue'):
                return {'success': False, 'reason': 'user_cancelled'}
            
            # Paso 2: WhatsApp
            self.step_whatsapp_config()
            
            # Paso 3: Negocio
            self.step_business_info()
            
            # Paso 4: Scoring
            self.step_scoring_config()
            
            # Paso 5: Followup
            self.step_followup_config()
            
            # Paso 6: Analytics
            self.step_analytics_config()
            
            # Paso 7: Revisión
            review_result = self.step_review()
            if not review_result.get('approved'):
                return {'success': False, 'reason': 'user_not_approved'}
            
            # Paso 8: Guardar
            save_result = self.step_save()
            
            return save_result
        
        except KeyboardInterrupt:
            print("\n\n❌ Configuración cancelada por el usuario")
            return {'success': False, 'reason': 'user_interrupted'}
        except Exception as e:
            print(f"\n❌ Error durante configuración: {str(e)}")
            return {'success': False, 'error': str(e)}

def main():
    """Función principal"""
    print("🧙 SISTEMA DE CONFIGURACIÓN INICIAL")
    print("=" * 60)
    
    wizard = SetupWizard()
    result = wizard.run_wizard()
    
    if result.get('success'):
        print("\n✅ El sistema está listo para usar")
        print("🚀 Ejecuta 'python main.py' para comenzar")
    else:
        print("\n⚠️  La configuración no se completó")
        print("💡 Puedes ejecutar el wizard nuevamente cuando estés listo")
    
    return result

if __name__ == '__main__':
    main()