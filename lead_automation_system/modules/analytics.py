"""
Módulo de Análisis y Métricas
Sistema para análisis de datos, predicción de conversión y optimización
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional
import json
import statistics
from collections import defaultdict

class LeadAnalytics:
    """Sistema de análisis de leads y conversiones"""
    
    def __init__(self, config: Dict):
        self.config = config["analytics"]
        self.conversion_data = self.load_conversion_data()
        self.leads_data = self.load_leads_data()
    
    def load_conversion_data(self) -> List[Dict]:
        """Cargar datos históricos de conversiones"""
        try:
            with open('data/conversion_data.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def load_leads_data(self) -> List[Dict]:
        """Cargar datos de leads"""
        try:
            with open('data/leads_db.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def calculate_conversion_rate(self, period_days: int = 30) -> Dict:
        """Calcular tasa de conversión para un período específico"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=period_days)
        
        # Filtrar leads del período
        period_leads = [
            lead for lead in self.leads_data
            if start_date <= datetime.fromisoformat(lead.get("inquiry_time", start_date.isoformat())) <= end_date
        ]
        
        # Filtrar conversiones del período
        period_conversions = [
            conv for conv in self.conversion_data
            if start_date <= datetime.fromisoformat(conv.get("conversion_date", start_date.isoformat())) <= end_date
        ]
        
        total_leads = len(period_leads)
        total_conversions = len(period_conversions)
        
        conversion_rate = (total_conversions / total_leads * 100) if total_leads > 0 else 0
        
        return {
            "period_days": period_days,
            "total_leads": total_leads,
            "total_conversions": total_conversions,
            "conversion_rate": conversion_rate,
            "target_rate": self.config.target_conversion_rate,
            "target_met": conversion_rate >= self.config.target_conversion_rate,
            "leads_needed": self.config.leads_needed_per_month,
            "conversions_needed": self.config.conversion_target_monthly
        }
    
    def predict_conversion_probability(self, lead_data: Dict) -> Dict:
        """Predecir probabilidad de conversión de un lead específico"""
        # Usar datos históricos para encontrar patrones similares
        similar_leads = self._find_similar_leads(lead_data)
        
        if not similar_leads:
            return {
                "probability": 0.1,  # Probabilidad base para leads nuevos
                "confidence": "low",
                "factors": []
            }
        
        # Calcular probabilidad basada en leads similares
        converted_similar = sum(1 for lead in similar_leads if lead.get("converted", False))
        probability = converted_similar / len(similar_leads)
        
        # Factores que aumentan la probabilidad
        factors = self._identify_conversion_factors(lead_data, similar_leads)
        
        confidence = "high" if len(similar_leads) >= 10 else "medium" if len(similar_leads) >= 5 else "low"
        
        return {
            "probability": probability,
            "confidence": confidence,
            "similar_leads_count": len(similar_leads),
            "factors": factors,
            "recommendation": self._get_probability_recommendation(probability)
        }
    
    def _find_similar_leads(self, lead_data: Dict) -> List[Dict]:
        """Encontrar leads similares basado en características"""
        similar_leads = []
        
        for lead in self.leads_data:
            similarity_score = 0
            
            # Similaridad en destino
            if lead.get("destino") == lead_data.get("destino"):
                similarity_score += 2
            
            # Similaridad en presupuesto
            lead_budget = self._extract_budget(lead.get("presupuesto", ""))
            data_budget = self._extract_budget(lead_data.get("presupuesto", ""))
            if lead_budget and data_budget:
                budget_diff = abs(lead_budget - data_budget)
                if budget_diff < 500000:  # Diferencia menor a 500k COP
                    similarity_score += 2
            
            # Similaridad en número de personas
            if lead.get("num_personas") == lead_data.get("num_personas"):
                similarity_score += 1
            
            # Similaridad en temporada
            lead_month = datetime.fromisoformat(lead.get("inquiry_time", "")).month
            data_month = datetime.fromisoformat(lead_data.get("inquiry_time", "")).month
            if lead_month == data_month:
                similarity_score += 1
            
            if similarity_score >= 3:  # Umbral de similitud
                similar_leads.append(lead)
        
        return similar_leads
    
    def _extract_budget(self, budget_str: str) -> Optional[int]:
        """Extraer valor numérico del presupuesto"""
        import re
        numbers = re.findall(r'\d+', budget_str)
        if numbers:
            return int(numbers[0])
        return None
    
    def _identify_conversion_factors(self, lead_data: Dict, similar_leads: List[Dict]) -> List[str]:
        """Identificar factores que aumentan la probabilidad de conversión"""
        factors = []
        
        # Analizar leads similares que se convirtieron
        converted_leads = [lead for lead in similar_leads if lead.get("converted", False)]
        
        if not converted_leads:
            return factors
        
        # Presupuesto adecuado
        if any(lead.get("presupuesto") for lead in converted_leads):
            factors.append("Presupuesto indicado")
        
        # Fecha específica
        if any(lead.get("fecha_deseada") for lead in converted_leads):
            factors.append("Fecha específica proporcionada")
        
        # Número de personas
        if any(lead.get("num_personas") for lead in converted_leads):
            factors.append("Número de personas definido")
        
        # Dispositivo de escritorio
        if any(lead.get("device") == "desktop" for lead in converted_leads):
            factors.append("Búsqueda desde desktop")
        
        # Visitante recurrente
        if any(lead.get("is_return_visitor") for lead in converted_leads):
            factors.append("Visitante recurrente")
        
        return factors
    
    def _get_probability_recommendation(self, probability: float) -> str:
        """Obtener recomendación basada en probabilidad"""
        if probability >= 0.7:
            return "PRIORIDAD ALTA - Llamada inmediata y seguimiento intensivo"
        elif probability >= 0.4:
            return "PRIORIDAD MEDIA - Seguimiento personalizado en 24 horas"
        elif probability >= 0.2:
            return "PRIORIDAD BAJA - Seguimiento estándar"
        else:
            return "PRIORIDAD MÍNIMA - Campañas de nurturing"
    
    def analyze_peak_periods(self) -> Dict:
        """Analizar períodos de alta conversión"""
        month_conversions = defaultdict(int)
        day_conversions = defaultdict(int)
        hour_conversions = defaultdict(int)
        
        for conversion in self.conversion_data:
            conv_date = datetime.fromisoformat(conversion.get("conversion_date", ""))
            
            month_conversions[conv_date.month] += 1
            day_conversions[conv_date.weekday()] += 1
            hour_conversions[conv_date.hour] += 1
        
        # Encontrar picos
        peak_month = max(month_conversions.items(), key=lambda x: x[1]) if month_conversions else (1, 0)
        peak_day = max(day_conversions.items(), key=lambda x: x[1]) if day_conversions else (0, 0)
        peak_hour = max(hour_conversions.items(), key=lambda x: x[1]) if hour_conversions else (0, 0)
        
        month_names = {
            1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
            5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
            9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
        }
        
        day_names = {
            0: "Lunes", 1: "Martes", 2: "Miércoles", 3: "Jueves",
            4: "Viernes", 5: "Sábado", 6: "Domingo"
        }
        
        return {
            "peak_month": {
                "month": peak_month[0],
                "name": month_names.get(peak_month[0], "Desconocido"),
                "conversions": peak_month[1]
            },
            "peak_day": {
                "day": peak_day[0],
                "name": day_names.get(peak_day[0], "Desconocido"),
                "conversions": peak_day[1]
            },
            "peak_hour": {
                "hour": peak_hour[0],
                "conversions": peak_hour[1]
            },
            "recommendations": self._get_peak_period_recommendations(peak_month, peak_day, peak_hour)
        }
    
    def _get_peak_period_recommendations(self, peak_month, peak_day, peak_hour) -> List[str]:
        """Obtener recomendaciones basadas en períodos pico"""
        recommendations = []
        
        # Recomendaciones mensuales
        if peak_month[0] in [7, 8, 12, 1]:  # Temporada alta
            recommendations.append("Incrementar disponibilidad durante temporada alta")
            recommendations.append("Preparar promociones especiales para temporada alta")
        
        # Recomendaciones diarias
        if peak_day[0] in [5, 6]:  # Fin de semana
            recommendations.append("Asegurar respuesta rápida los fines de semana")
        
        # Recomendaciones horarias
        if 9 <= peak_hour[0] <= 17:  # Horario laboral
            recommendations.append("Priorizar respuesta inmediata durante horario laboral")
        elif 18 <= peak_hour[0] <= 21:  # Horario tarde/noche
            recommendations.append("Habilitar atención extendida en horarios de alta consulta")
        
        return recommendations
    
    def calculate_revenue_potential(self, leads: List[Dict]) -> Dict:
        """Calcular potencial de ingresos de leads actuales"""
        total_potential = 0
        high_value_leads = []
        
        for lead in leads:
            presupuesto = self._extract_budget(lead.get("presupuesto", ""))
            if presupuesto and presupuesto >= self.config.high_value_lead_threshold:
                total_potential += presupuesto
                high_value_leads.append({
                    "lead_id": lead.get("id"),
                    "presupuesto": presupuesto,
                    "estimated_conversion": presupuesto * 0.3  # Estimación conservadora
                })
        
        return {
            "total_leads": len(leads),
            "high_value_leads_count": len(high_value_leads),
            "total_potential": total_potential,
            "estimated_revenue": sum(lead["estimated_conversion"] for lead in high_value_leads),
            "high_value_leads": high_value_leads[:10]  # Top 10
        }
    
    def generate_conversion_report(self) -> Dict:
        """Generar reporte completo de conversión"""
        conversion_rate = self.calculate_conversion_rate()
        peak_periods = self.analyze_peak_periods()
        revenue_potential = self.calculate_revenue_potential(self.leads_data)
        
        return {
            "report_date": datetime.now().isoformat(),
            "conversion_rate": conversion_rate,
            "peak_periods": peak_periods,
            "revenue_potential": revenue_potential,
            "target_status": {
                "target_conversions": self.config.conversion_target_monthly,
                "current_conversions": conversion_rate["total_conversions"],
                "progress_percentage": (conversion_rate["total_conversions"] / self.config.conversion_target_monthly * 100) if self.config.conversion_target_monthly > 0 else 0,
                "on_track": conversion_rate["total_conversions"] >= self.config.conversion_target_monthly
            },
            "recommendations": self._generate_monthly_recommendations(conversion_rate, peak_periods)
        }
    
    def _generate_monthly_recommendations(self, conversion_rate: Dict, peak_periods: Dict) -> List[str]:
        """Generar recomendaciones mensuales"""
        recommendations = []
        
        # Análisis de tasa de conversión
        if not conversion_rate["target_met"]:
            recommendations.append(f"Tasa de conversión actual ({conversion_rate['conversion_rate']:.1f}%) está por debajo del objetivo ({self.config.target_conversion_rate*100:.1f}%)")
            recommendations.append("Revisar y optimizar proceso de seguimiento de leads")
            recommendations.append("Implementar lead scoring para priorizar leads de alta conversión")
        
        # Análisis de períodos pico
        recommendations.extend(peak_periods["recommendations"])
        
        # Recomendaciones generales
        if conversion_rate["total_leads"] < self.config.leads_needed_per_month:
            recommendations.append(f"Incrementar generación de leads (actuales: {conversion_rate['total_leads']}, objetivo: {self.config.leads_needed_per_month})")
        
        return recommendations
    
    def track_lead_lifecycle(self, lead_id: str) -> Dict:
        """Rastrear ciclo de vida de un lead específico"""
        lead = next((l for l in self.leads_data if l.get("id") == lead_id), None)
        
        if not lead:
            return {"error": "Lead no encontrado"}
        
        lifecycle = {
            "lead_id": lead_id,
            "inquiry_time": lead.get("inquiry_time"),
            "first_response_time": lead.get("first_response_time"),
            "followup_count": len(lead.get("followups", [])),
            "conversion_date": lead.get("conversion_date"),
            "conversion_time_days": None,
            "stage": self._determine_lead_stage(lead),
            "total_time_in_stage": self._calculate_time_in_stage(lead)
        }
        
        if lead.get("conversion_date"):
            inquiry_time = datetime.fromisoformat(lead["inquiry_time"])
            conversion_time = datetime.fromisoformat(lead["conversion_date"])
            lifecycle["conversion_time_days"] = (conversion_time - inquiry_time).days
        
        return lifecycle
    
    def _determine_lead_stage(self, lead: Dict) -> str:
        """Determinar etapa actual del lead"""
        if lead.get("converted"):
            return "converted"
        elif lead.get("in_negotiation"):
            return "negotiation"
        elif lead.get("quoted"):
            return "quoted"
        elif lead.get("followed_up"):
            return "followup"
        else:
            return "new"
    
    def _calculate_time_in_stage(self, lead: Dict) -> Dict:
        """Calcular tiempo en cada etapa"""
        stages = {}
        current_time = datetime.now()
        
        inquiry_time = datetime.fromisoformat(lead.get("inquiry_time", current_time.isoformat()))
        stages["new"] = (current_time - inquiry_time).days
        
        if lead.get("first_response_time"):
            response_time = datetime.fromisoformat(lead["first_response_time"])
            stages["new"] = (response_time - inquiry_time).days
            stages["followup"] = (current_time - response_time).days
        
        return stages