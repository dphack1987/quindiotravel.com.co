"""
Motor de Lead Scoring Avanzado
Sistema inteligente para calificar leads por probabilidad de conversión
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional
import json
import re

class LeadScoringEngine:
    """Motor de calificación de leads"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.scoring_rules = self.load_scoring_rules()
    
    def load_scoring_rules(self) -> Dict:
        """Cargar reglas de scoring desde archivo JSON"""
        try:
            with open('data/scoring_rules.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            # Reglas por defecto si no existe archivo
            return {
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
            }
    
    def calculate_lead_score(self, lead_data: Dict) -> Dict:
        """Calcular score completo de un lead"""
        score = 0
        signals = []
        
        # 1. Señales de interés
        interest_score = self._calculate_interest_signals(lead_data)
        score += interest_score
        signals.append({"category": "interest", "score": interest_score})
        
        # 2. Señales de calidad
        quality_score = self._calculate_quality_signals(lead_data)
        score += quality_score
        signals.append({"category": "quality", "score": quality_score})
        
        # 3. Señales de comportamiento
        behavior_score = self._calculate_behavioral_signals(lead_data)
        score += behavior_score
        signals.append({"category": "behavior", "score": behavior_score})
        
        # 4. Señales de timing
        timing_score = self._calculate_timing_signals(lead_data)
        score += timing_score
        signals.append({"category": "timing", "score": timing_score})
        
        # Normalizar score a 0-100
        normalized_score = min(100, max(0, score))
        
        # Determinar categoría del lead
        lead_category = self._categorize_lead(normalized_score)
        
        return {
            "score": normalized_score,
            "category": lead_category,
            "signals": signals,
            "priority": self._get_priority_level(lead_category),
            "recommended_actions": self._get_recommended_actions(lead_category)
        }
    
    def _calculate_interest_signals(self, lead_data: Dict) -> int:
        """Calcular señales de interés del lead"""
        score = 0
        message = lead_data.get("message", "").lower()
        
        interest_signals = self.scoring_rules["interest_signals"]
        
        # Verificar si menciona plan específico
        if any(plan in message for plan in ["plan", "paquete", "viaje", "tour"]):
            score += interest_signals["specific_plan_mentioned"]
        
        # Verificar si proporciona fecha
        if lead_data.get("fecha_deseada") or any(fecha in message for fecha in ["fecha", "cuando", "día", "mes"]):
            score += interest_signals["date_range_provided"]
        
        # Verificar si proporciona número de personas
        if lead_data.get("num_personas") or any(personas in message for personas in ["persona", "gente", "pareja", "familia", "grupo"]):
            score += interest_signals["guest_count_provided"]
        
        # Verificar si menciona presupuesto
        if lead_data.get("presupuesto") or any(presupuesto in message for presupuesto in ["presupuesto", "dinero", "costo", "precio"]):
            score += interest_signals["budget_mentioned"]
        
        # Verifica si hace preguntas
        if "?" in message or any(question in message for question in ["?", "cómo", "dónde", "cuánto"]):
            score += interest_signals["question_asked"]
        
        # Verifica si hubo clic en WhatsApp
        if lead_data.get("whatsapp_clicked"):
            score += interest_signals["whatsapp_clicked"]
        
        return score
    
    def _calculate_quality_signals(self, lead_data: Dict) -> int:
        """Calcular señales de calidad del lead"""
        score = 0
        message = lead_data.get("message", "")
        
        quality_signals = self.scoring_rules["quality_signals"]
        
        # Verificar si el mensaje es una oración completa
        if len(message.split()) > 3 and message.count(' ') > 2:
            score += quality_signals["complete_sentence"]
        
        # Verificar si menciona destinos relevantes
        relevant_destinations = ["salento", "cocora", "café", "quindío", "armenia", "filandia", "eje cafetero"]
        if any(dest in message.lower() for dest in relevant_destinations):
            score += quality_signals["relevant_destination"]
        
        # Verificar si el presupuesto es razonable
        presupuesto = lead_data.get("presupuesto", "")
        if presupuesto:
            try:
                presupuesto_num = int(re.sub(r'[^0-9]', '', presupuesto))
                if 300000 <= presupuesto_num <= 5000000:  # Rango razonable para turismo Eje Cafetero
                    score += quality_signals["reasonable_budget"]
            except:
                pass
        
        # Verificar si las fechas son realistas
        fecha_deseada = lead_data.get("fecha_deseada", "")
        if fecha_deseada:
            try:
                fecha = datetime.strptime(fecha_deseada, "%Y-%m-%d")
                hoy = datetime.now()
                # Verificar que la fecha sea en el futuro y no más de 6 meses
                if hoy < fecha <= hoy + timedelta(days=180):
                    score += quality_signals["realistic_dates"]
            except:
                pass
        
        # Verificar si proporciona información de contacto
        if lead_data.get("nombre") and (lead_data.get("telefono") or lead_data.get("email")):
            score += quality_signals["contact_provided"]
        
        return score
    
    def _calculate_behavioral_signals(self, lead_data: Dict) -> int:
        """Calcular señales de comportamiento del lead"""
        score = 0
        behavioral_signals = self.scoring_rules["behavioral_signals"]
        
        # Páginas vistas
        page_views = lead_data.get("page_views", 0)
        if page_views >= 3:
            score += behavioral_signals["page_views"] * min(page_views, 5)
        
        # Tiempo en el sitio (en minutos)
        time_on_site = lead_data.get("time_on_site", 0)
        if time_on_site >= 2:
            score += behavioral_signals["time_on_site"] * min(int(time_on_site / 2), 5)
        
        # Visitante recurrente
        if lead_data.get("is_return_visitor"):
            score += behavioral_signals["return_visitor"]
        
        # Tipo de dispositivo
        device = lead_data.get("device", "")
        if device == "desktop":
            score += behavioral_signals["desktop_device"]
        elif device == "mobile":
            score += behavioral_signals["mobile_device"]
        
        return score
    
    def _calculate_timing_signals(self, lead_data: Dict) -> int:
        """Calcular señales de timing del lead"""
        score = 0
        timing_signals = self.scoring_rules["timing_signals"]
        
        # Tiempo de respuesta
        inquiry_time = lead_data.get("inquiry_time")
        if inquiry_time:
            now = datetime.now()
            if isinstance(inquiry_time, str):
                inquiry_time = datetime.fromisoformat(inquiry_time)
            
            time_diff = (now - inquiry_time).total_seconds() / 3600  # en horas
            
            if time_diff < 1:
                score += timing_signals["response_under_1hr"]
            elif time_diff < 24:
                score += timing_signals["response_1_24hr"]
            elif time_diff < 72:
                score += timing_signals["response_24_72hr"]
        
        # Día de la semana
        inquiry_day = lead_data.get("inquiry_day", "")
        if inquiry_day in ["saturday", "sunday"]:
            score += timing_signals["weekend_inquiry"]
        
        # Temporada (asumimos que estamos en temporada alta si es julio-agosto o diciembre-enero)
        current_month = datetime.now().month
        if current_month in [7, 8, 12, 1]:  # Temporada alta
            score += timing_signals["holiday_season"]
        
        return score
    
    def _categorize_lead(self, score: int) -> str:
        """Categorizar lead según su score"""
        if score >= self.config["scoring"].min_score_for_hot_lead:
            return "hot_lead"
        elif score >= self.config["scoring"].min_score_for_warm_lead:
            return "warm_lead"
        else:
            return "cold_lead"
    
    def _get_priority_level(self, category: str) -> str:
        """Obtener nivel de prioridad"""
        priorities = {
            "hot_lead": "URGENTE",
            "warm_lead": "ALTA",
            "cold_lead": "MEDIA"
        }
        return priorities.get(category, "BAJA")
    
    def _get_recommended_actions(self, category: str) -> List[str]:
        """Obtener acciones recomendadas según categoría"""
        actions = {
            "hot_lead": [
                "Llamada inmediata (dentro de 15 minutos)",
                "Mensaje WhatsApp personalizado con disponibilidad",
                "Enviar cotización detallada con 2-3 opciones",
                "Oferta de seguimiento en 2 horas si no responde"
            ],
            "warm_lead": [
                "Mensaje WhatsApp dentro de 1 hora",
                "Llamada en 4-6 horas",
                "Enviar información adicional sobre destinos",
                "Follow-up al día siguiente"
            ],
            "cold_lead": [
                "Mensaje WhatsApp informativo en 24 horas",
                "Newsletter con planes promocionales",
                "Retargeting en redes sociales",
                "Seguimiento semanal durante 2 meses"
            ]
        }
        return actions.get(category, [])
    
    def get_top_leads(self, leads: List[Dict], limit: int = 10) -> List[Dict]:
        """Obtener los leads con mayor score"""
        scored_leads = []
        
        for lead in leads:
            scored_lead = self.calculate_lead_score(lead)
            scored_lead["original_data"] = lead
            scored_leads.append(scored_lead)
        
        # Ordenar por score descendente
        scored_leads.sort(key=lambda x: x["score"], reverse=True)
        
        return scored_leads[:limit]