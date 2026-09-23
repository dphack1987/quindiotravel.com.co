"""
Motor de Follow-up Automatizado
Sistema inteligente de seguimiento personalizado según tipo de lead
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional
import json
import random

class FollowupEngine:
    """Motor de seguimiento automatizado de leads"""
    
    def __init__(self, config: Dict, whatsapp_bot, lead_scorer):
        self.config = config["followup"]
        self.whatsapp_bot = whatsapp_bot
        self.lead_scorer = lead_scorer
        self.followup_history = {}
        self.message_templates = self.load_message_templates()
    
    def load_message_templates(self) -> Dict:
        """Cargar plantillas de mensajes desde archivo"""
        try:
            with open('utils/message_templates.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            # Plantillas por defecto
            return {
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
    
    def schedule_followup(self, lead_data: Dict) -> List[Dict]:
        """Programar seguimientos automáticos para un lead"""
        lead_score = self.lead_scorer.calculate_lead_score(lead_data)
        lead_category = lead_score["category"]
        
        schedule = self.config.followup_schedule.get(lead_category, [])
        followups = []
        
        base_date = datetime.now()
        
        for day_offset in schedule:
            followup_date = base_date + timedelta(days=day_offset)
            
            followup = {
                "lead_id": lead_data.get("id", "unknown"),
                "lead_category": lead_category,
                "scheduled_date": followup_date.isoformat(),
                "day_offset": day_offset,
                "message_template": self._select_message_template(lead_category, day_offset),
                "priority": self._get_followup_priority(lead_category, day_offset),
                "status": "scheduled"
            }
            
            followups.append(followup)
        
        # Guardar en historial
        if lead_data.get("id") not in self.followup_history:
            self.followup_history[lead_data["id"]] = []
        
        self.followup_history[lead_data["id"]].extend(followups)
        
        return followups
    
    def _select_message_template(self, lead_category: str, day_offset: int) -> str:
        """Seleccionar plantilla de mensaje apropiada"""
        if lead_category == "hot_lead":
            if day_offset == 0:
                return random.choice(self.message_templates["hot_lead"]["immediate"])
            elif day_offset == 2:
                return random.choice(self.message_templates["hot_lead"]["2_days"])
            elif day_offset == 7:
                return random.choice(self.message_templates["hot_lead"]["1_week"])
            elif day_offset == 14:
                return random.choice(self.message_templates["hot_lead"]["2_weeks"])
        
        elif lead_category == "warm_lead":
            if day_offset == 1:
                return random.choice(self.message_templates["warm_lead"]["1_day"])
            elif day_offset == 3:
                return random.choice(self.message_templates["warm_lead"]["3_days"])
            elif day_offset == 7:
                return random.choice(self.message_templates["warm_lead"]["1_week"])
            elif day_offset == 14:
                return random.choice(self.message_templates["warm_lead"]["2_weeks"])
            elif day_offset == 30:
                return random.choice(self.message_templates["warm_lead"]["1_month"])
        
        elif lead_category == "cold_lead":
            if day_offset == 7:
                return random.choice(self.message_templates["cold_lead"]["1_week"])
            elif day_offset == 14:
                return random.choice(self.message_templates["cold_lead"]["2_weeks"])
            elif day_offset == 30:
                return random.choice(self.message_templates["cold_lead"]["1_month"])
            elif day_offset == 60:
                return random.choice(self.message_templates["cold_lead"]["2_months"])
        
        return "Hola, te saluda Quindío Travel. ¿En qué podemos ayudarte?"
    
    def _get_followup_priority(self, lead_category: str, day_offset: int) -> str:
        """Determinar prioridad del seguimiento"""
        if lead_category == "hot_lead" and day_offset == 0:
            return "urgent"
        elif lead_category == "hot_lead" and day_offset <= 2:
            return "high"
        elif lead_category == "warm_lead" and day_offset <= 3:
            return "high"
        else:
            return "normal"
    
    def execute_pending_followups(self) -> List[Dict]:
        """Ejecutar seguimientos pendientes"""
        results = []
        now = datetime.now()
        
        for lead_id, followups in self.followup_history.items():
            for followup in followups:
                if followup["status"] == "scheduled":
                    scheduled_date = datetime.fromisoformat(followup["scheduled_date"])
                    
                    if scheduled_date <= now:
                        # Ejecutar seguimiento
                        result = self._execute_followup(followup)
                        results.append(result)
        
        return results
    
    def _execute_followup(self, followup: Dict) -> Dict:
        """Ejecutar un seguimiento específico"""
        lead_id = followup["lead_id"]
        message_template = followup["message_template"]
        
        # Aquí deberías obtener los datos del lead desde tu base de datos
        # Por ahora, usamos datos de ejemplo
        lead_data = {
            "id": lead_id,
            "nombre": "Cliente",
            "telefono": "573000000000"  # Deberías obtener esto de tu DB
        }
        
        # Personalizar mensaje
        personalized_message = message_template.format(
            nombre=lead_data.get("nombre", "Cliente")
        )
        
        # Enviar mensaje
        result = self.whatsapp_bot.send_text_message(
            lead_data["telefono"],
            personalized_message
        )
        
        # Actualizar estado
        followup["status"] = "sent" if result["success"] else "failed"
        followup["sent_date"] = datetime.now().isoformat()
        followup["result"] = result
        
        return {
            "followup_id": f"{lead_id}_{followup['scheduled_date']}",
            "lead_id": lead_id,
            "success": result["success"],
            "message": personalized_message,
            "sent_date": datetime.now().isoformat()
        }
    
    def get_followup_stats(self) -> Dict:
        """Obtener estadísticas de seguimientos"""
        total_followups = sum(len(followups) for followups in self.followup_history.values())
        sent_followups = sum(
            len([f for f in followups if f["status"] == "sent"])
            for followups in self.followup_history.values()
        )
        failed_followups = sum(
            len([f for f in followups if f["status"] == "failed"])
            for followups in self.followup_history.values()
        )
        pending_followups = sum(
            len([f for f in followups if f["status"] == "scheduled"])
            for followups in self.followup_history.values()
        )
        
        return {
            "total_followups": total_followups,
            "sent_followups": sent_followups,
            "failed_followups": failed_followups,
            "pending_followups": pending_followups,
            "success_rate": (sent_followups / total_followups * 100) if total_followups > 0 else 0
        }
    
    def add_manual_followup(self, lead_id: str, message: str, priority: str = "normal") -> Dict:
        """Agregar seguimiento manual"""
        now = datetime.now()
        
        followup = {
            "lead_id": lead_id,
            "lead_category": "manual",
            "scheduled_date": now.isoformat(),
            "day_offset": 0,
            "message_template": message,
            "priority": priority,
            "status": "scheduled",
            "manual": True
        }
        
        if lead_id not in self.followup_history:
            self.followup_history[lead_id] = []
        
        self.followup_history[lead_id].append(followup)
        
        return followup
    
    def cancel_followup(self, lead_id: str, followup_id: str) -> bool:
        """Cancelar un seguimiento programado"""
        if lead_id in self.followup_history:
            for followup in self.followup_history[lead_id]:
                if f"{lead_id}_{followup['scheduled_date']}" == followup_id:
                    followup["status"] = "cancelled"
                    return True
        return False
    
    def get_lead_followup_history(self, lead_id: str) -> List[Dict]:
        """Obtener historial de seguimientos de un lead"""
        return self.followup_history.get(lead_id, [])