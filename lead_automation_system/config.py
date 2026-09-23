"""
Configuración del Sistema de Automatización de Leads
Quindío Travel - Sistema para lograr 4+ reservas mensuales
"""

import os
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class WhatsAppConfig:
    """Configuración de WhatsApp Business API"""
    phone_number: str = "573174426044"
    api_token: str = os.getenv("WHATSAPP_API_TOKEN", "")
    business_profile_id: str = os.getenv("WHATSAPP_BUSINESS_ID", "")
    
    # Configuración de envío
    max_messages_per_day: int = 100
    message_delay_seconds: int = 30
    business_hours_start: int = 8  # 8 AM
    business_hours_end: int = 20  # 8 PM

@dataclass 
class LeadScoringConfig:
    """Configuración del sistema de lead scoring"""
    min_score_for_hot_lead: int = 70
    min_score_for_warm_lead: int = 50
    cold_lead_score: int = 30
    
    # Pesos de factores de scoring
    weight_interested_plan: float = 0.25
    weight_provided_date: float = 0.20
    weight_provided_guests: float = 0.15
    weight_budget_indicated: float = 0.15
    weight_message_quality: float = 0.15
    weight_response_time: float = 0.10

@dataclass
class FollowupConfig:
    """Configuración del sistema de follow-up"""
    followup_schedule: Dict[str, List[int]] = None
    
    def __post_init__(self):
        if self.followup_schedule is None:
            self.followup_schedule = {
                "hot_lead": [0, 2, 7, 14],  # Días: hoy, 2 días, 1 semana, 2 semanas
                "warm_lead": [1, 3, 7, 14, 30],  # Días: mañana, 3 días, 1 semana, 2 semanas, 1 mes
                "cold_lead": [7, 14, 30, 60]  # Días: 1 semana, 2 semanas, 1 mes, 2 meses
            }

@dataclass
class AnalyticsConfig:
    """Configuración de análisis y métricas"""
    conversion_target_monthly: int = 4
    target_conversion_rate: float = 0.08  # 8% de conversión esperado
    leads_needed_per_month: int = 50  # Leads necesarios para 4 conversiones
    high_value_lead_threshold: int = 1000000  # COP presupuesto mínimo para lead de alto valor

# Instancia de configuración
config = {
    "whatsapp": WhatsAppConfig(),
    "scoring": LeadScoringConfig(),
    "followup": FollowupConfig(),
    "analytics": AnalyticsConfig()
}