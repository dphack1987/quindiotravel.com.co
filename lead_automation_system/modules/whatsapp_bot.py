"""
Integración con WhatsApp Business API
Sistema automatizado de envío de mensajes y seguimiento
"""

import requests
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import time

class WhatsAppBusinessBot:
    """Bot de WhatsApp Business para automatización de comunicación"""
    
    def __init__(self, config: Dict):
        self.config = config["whatsapp"]
        self.api_url = f"https://graph.facebook.com/v19.0/{self.config.phone_number}"
        self.headers = {
            "Authorization": f"Bearer {self.config.api_token}",
            "Content-Type": "application/json"
        }
        self.message_queue = []
        self.daily_message_count = 0
    
    def send_text_message(self, phone_number: str, message: str) -> Dict:
        """Enviar mensaje de texto a través de WhatsApp Business API"""
        payload = {
            "messaging_product": "whatsapp_business_api",
            "to": phone_number,
            "type": "text",
            "text": {
                "body": message
            }
        }
        
        try:
            response = requests.post(
                f"{self.api_url}/messages",
                headers=self.headers,
                json=payload
            )
            
            self.daily_message_count += 1
            
            return {
                "success": response.status_code == 200,
                "status_code": response.status_code,
                "response": response.json() if response.text else None,
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def send_template_message(self, phone_number: str, template_name: str, components: List[Dict]) -> Dict:
        """Enviar mensaje usando template de WhatsApp"""
        payload = {
            "messaging_product": "whatsapp_business_api",
            "to": phone_number,
            "type": "template",
            "template": {
                "name": template_name,
                "language": {
                    "code": "es"
                },
                "components": components
            }
        }
        
        try:
            response = requests.post(
                f"{self.api_url}/messages",
                headers=self.headers,
                json=payload
            )
            
            self.daily_message_count += 1
            
            return {
                "success": response.status_code == 200,
                "status_code": response.status_code,
                "response": response.json() if response.text else None,
                "timestamp": datetime.now.now().isoformat()
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def send_media_message(self, phone_number: str, media_url: str, caption: str = "") -> Dict:
        """Enviar mensaje con media (imagen, documento, etc.)"""
        payload = {
            "messaging_product": "whatsapp_business_api",
            "to": phone_number,
            "type": "image",
            "image": {
                "link": media_url
            }
        }
        
        if caption:
            payload["image"]["caption"] = caption
        
        try:
            response = requests.post(
                f"{self.api_url}/messages",
                headers=self.headers,
                json=payload
            )
            
            self.daily_message_count += 1
            
            return {
                "success": response.status_code == 200,
                "status_code": response.status_code,
                "response": response.json() if response.text else None,
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def send_location_message(self, phone_number: str, latitude: float, longitude: float, name: str = "") -> Dict:
        """Enviar mensaje con ubicación"""
        payload = {
            "messaging_bproduct": "whatsapp_business_api",
            "to": phone_number,
            "type": "location",
            "location": {
                "latitude": latitude,
                "longitude": longitude,
                "name": name
            }
        }
        
        try:
            response = requests.post(
                f"{self.api_url}/messages",
                headers=self.headers,
                json=payload
            )
            
            self.daily_message_count += 1
            
            return {
                "success": response.status_code == 200,
                "status_code": response.status_code,
                "response": response.json() if response.text else None,
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "timestamp": datetime.now.isoformat()
            }
    
    def queue_message(self, phone_number: str, message: str, priority: str = "normal") -> None:
        """Agregar mensaje a la cola de envío"""
        self.message_queue.append({
            "phone_number": phone_number,
            "message": message,
            "priority": priority,
            "timestamp": datetime.now().isoformat(),
            "attempts": 0
        })
    
    def process_message_queue(self) -> List[Dict]:
        """Procesar cola de mensajes (respectando límites y horarios)"""
        results = []
        
        # Verificar límites diarios
        if self.daily_message_count >= self.config.max_messages_per_day:
            return results
        
        # Verificar horario laboral
        current_hour = datetime.now().hour
        if not (self.config.business_hours_start <= current_hour < self.config.business_hours_end):
            return results
        
        # Ordenar por prioridad
        self.message_queue.sort(key=lambda x: (
            0 if x["priority"] == "urgent" else 1 if x["priority"] == "high" else 2
        ))
        
        # Procesar mensajes
        for msg in self.message_queue[:5]:  # Procesar hasta 5 mensajes por batch
            if self.daily_message_count >= self.config.max_messages_per_day:
                break
            
            result = self.send_text_message(msg["phone_number"], msg["message"])
            results.append(result)
            
            if result["success"]:
                self.message_queue.remove(msg)
                time.sleep(self.config.message_delay_seconds)
            else:
                msg["attempts"] += 1
                if msg["attempts"] >= 3:
                    self.message_queue.remove(msg)
        
        return results
    
    def send_hot_lead_message(self, lead_data: Dict) -> Dict:
        """Enviar mensaje para lead caliente (hot lead)"""
        nombre = lead_data.get("nombre", "Cliente")
        plan_interes = lead_data.get("plan_interes", "un plan turístico")
        mensaje = f"""
🌟 *¡Hola {nombre}!*

Gracias por tu interés en {plan_interes} en el Eje Cafetero 🌿

He verificado nuestra disponibilidad y tenemos excelentes opciones para ti.

¿Podrías confirmarme:
📅 Fecha deseada de viaje?
👥 Número de personas?
🎯 Plan específico que te interesa?

Te envío cotización inmediata con disponibilidad actual.

📞 *Quindío Travel - RNT 18152*
📱 +57 317 442 6044
        """
        
        return self.send_text_message(lead_data["telefono"], mensaje)
    
    def send_warm_lead_message(self, lead_data: Dict) -> Dict:
        """Enviar mensaje para lead tibio (warm lead)"""
        nombre = lead_data.get("nombre", "Cliente")
        mensaje = f"""
🌿 *Hola {nombre} de Quindío Travel*

¿Cómo estás? Me interesé por tu consulta sobre planes al Eje Cafetero.

Tengo varias opciones disponibles que podrían ser perfectas para ti. ¿Podrías decirme:
1. ¿Cuándo planeas viajar?
2. ¿Cuántas personas serían?
3. ¿Algún destino específico te interesa más?

Con esta información te envío cotizaciones personalizadas con disponibilidad en tiempo real.

🏆 *Quindío Travel - RNT 18152*
        """
        
        return self.send_text_message(lead_data["telefono"], mensaje)
    
    def send_cold_lead_message(self, lead_data: Dict) -> Dict:
        """Enviar mensaje para lead frío (cold lead)"""
        mensaje = """
🌿 *Bienvenido a Quindío Travel*

Gracias por tu interés en conocer el hermoso Eje Cafetero colombiano 🇨🇴

Te comparto algunas de nuestras ofertas más populares:
• 🌾 Valle de Cocora - tours desde $425.000 COP
• ☕ Coffee Tours experiencial 
• 🏨 Fincas hotelería con piscina
• 🎯 Planes completos todo incluido

¿Te gustaría que te envíe información detallada sobre alguno de estos destinos?

🏆 *Quindío Travel - RNT 18152*
📱 +57 317 442 6044
        """
        
        return self.send_text_message(lead_data["telefono"], mensaje)
    
    def send_promo_message(self, lead_data: Dict, promo: Dict) -> Dict:
        """Enviar mensaje promocional"""
        nombre = lead_data.get("nombre", "Cliente")
        mensaje = f"""
🔥 *¡OFERTA ESPECIAL PARA TI {nombre}!*

{promo['titulo']}
💰 *Precio:* {promo['precio']}
⏰ *Válido hasta:* {promo['fecha_limite']}

{promo['descripcion']}

Esta oferta tiene cupos limitados. ¿Te gustaría asegurar tu lugar?

🏆 *Quindío Travel - RNT 18152*
📱 +57 317 442 6044
        """
        
        return self.send_text_message(lead_data["telefono"], mensaje)
    
    def send_quote_message(self, lead_data: Dict, quote: Dict) -> Dict:
        """Enviar cotización detallada"""
        nombre = lead_data.get("nombre", "Cliente")
        mensaje = f"""
🌟 *COTIZACIÓN PERSONALIZADA - {nombre}*

📋 *Plan:* {quote['plan']}
⏱️ *Duración:* {quote['duracion']}
💰 *Precio:* {quote['precio']} COP por persona

🎯 *Incluye:*
{chr(10).join(f"• {item}" for item in quote['incluye'])}

📅 *Disponibilidad:* {quote['disponibilidad']}
✅ *Válido hasta:* {quote['valido_hasta']}

Para confirmar tu reserva necesito:
📅 50% de anticipo
📋 Copia de documento de identidad
🏷️ Información de pasajeros

🏆 *Quindío Travel - RNT 18152*
📱 +57 317 442 6044
        """
        
        return self.send_text_message(lead_data["telefono"], mensaje)
    
    def get_message_status(self, message_id: str) -> Dict:
        """Verificar estado de un mensaje enviado"""
        try:
            response = requests.get(
                f"{self.api_url}/messages/{message_id}",
                headers=self.headers
            )
            
            return {
                "success": response.status_code == 200,
                "status_code": response.status_code,
                "response": response.json() if response.text else None
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def get_business_profile(self) -> Dict:
        """Obtener perfil del negocio de WhatsApp"""
        try:
            response = requests.get(
                f"{self.api_url}",
                headers=self.headers
            )
            
            return {
                "success": response.status_code == 200,
                "profile": response.json() if response.text else None
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }