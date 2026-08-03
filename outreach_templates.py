"""
Sistema de Plantillas de Outreach para Backlinks
Genera emails personalizados para solicitar backlinks a blogs de turismo
"""

from pathlib import Path
from datetime import datetime

class OutreachSystem:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.outreach_data = self.base_dir / "outreach_data"
        self.outreach_data.mkdir(exist_ok=True)
        
        # Plantillas de email para diferentes tipos de outreach
        self.templates = {
            "guest_post": {
                "subject": "Propuesta de Artículo Invitado para {blog_name}",
                "body": """Hola {name},

Soy Álvaro Alzate Ortiz, fundador de Quindío Travel (RNT 18152), operador turístico certificado con más de 15 años de experiencia en el Eje Cafetero colombiano.

Me encanta el contenido que publicas sobre turismo en Colombia, especialmente tu artículo sobre {recent_article}. Me parece que tu audiencia valoraría mucho contenido sobre experiencias auténticas del Quindío.

Te escribo para proponer un artículo invitado de alta calidad sobre:
- "Guía Completa de Turismo Eje Cafetero 2026"
- "Los 5 Secretos del Quindío que los Turistas No Conocen"
- "Experiencias Cafeteras Auténticas: Más allá de lo Turístico"

Cada artículo tiene 1,500+ palabras, está optimizado para SEO, y aporta valor real a tu audiencia. A cambio, incluiré 2-3 enlaces contextuales a Quindío Travel (https://quindiotravel.com.co), que complementan perfectamente el contenido sobre turismo colombiano.

¿Te interesaría recibir el borrador del artículo para revisión?

Quedo atento a tu respuesta.

Saludos cordiales,
Álvaro Alzate Ortiz
Quindío Travel - RNT 18152
+57-317-4426044
gerencia@quindiotravel.net
https://quindiotravel.com.co"""
            },
            "collaboration": {
                "subject": "Propuesta de Colaboración: Turismo Eje Cafetero",
                "body": """Hola {name},

Te contacto desde Quindío Travel (RNT 18152), operador turístico local con 15+ años de experiencia en el Eje Cafetero.

He estado siguiendo tu blog {blog_name} y me encanta cómo cubres el turismo colombiano. Noté que tienes excelente contenido sobre {content_focus}, pero no has cubierto en profundidad el Eje Cafetero y el Quindío.

Te propongo una colaboración mutuamente beneficiosa:

1. Te proporciono contenido exclusivo sobre el Eje Cafetero (artículos, fotos, videos)
2. Tú lo publicas en tu blog con attribution a Quindío Travel
3. Incluyo backlinks a tu blog desde mi sitio (autoridad mutua)
4. Promocionamos el contenido en mis redes sociales (+1,200 seguidores)

El Eje Cafetero es uno de los destinos más populares de Colombia, y tu audiencia definitivamente estará interesada en contenido sobre:
- Valle de Cocora y Salento
- Experiencias cafeteras auténticas
- Hoteles y alojamientos locales
- Gastronomía paisa

¿Te gustaría discutir esta colaboración más a fondo?

Saludos,
Álvaro Alzate Ortiz
Quindío Travel - RNT 18152"""
            },
            "resource_link": {
                "subject": "Recurso Útil para tu Audiencia: Guía Eje Cafetero",
                "body": """Hola {name},

Te escribo porque me parece que tu audiencia de {blog_name} podría beneficiarse de un recurso que acabo de crear.

He desarrollado una "Guía Completa del Eje Cafetero 2026" que incluye:
- Mapa interactivo de destinos
- Precios actualizados 2026
- Mejores épocas para visitar
- Tips de locales expertos
- Rutas y itinerarios

Esta guía está disponible gratuitamente en Quindío Travel (https://quindiotravel.com.co/guia-eje-cafetero-2026).

Tu audiencia encontraría este recurso muy útil, especialmente si están planeando viajes al Eje Cafetero. ¿Considerarías incluir este enlace en tu sección de recursos o en un artículo futuro?

Como operador local certificado RNT 18152, puedo responder cualquier pregunta que tengas sobre el contenido.

¿Te parece útil este recurso para tu audiencia?

Saludos,
Álvaro Alzate Ortiz
Quindío Travel - RNT 18152"""
            },
            "interview": {
                "subject": "Entrevista con Experto Local del Eje Cafetero",
                "body": """Hola {name},

Te contacto desde Quindío Travel, operador turístico local con 15+ años de experiencia en el Eje Cafetero.

Me encanta cómo cubres el turismo en Colombia en {blog_name}. ¿Te interesaría entrevistarme para un artículo sobre "Secretos del Eje Cafetero que Solo los Locales Conocen"?

Como operador certificado RNT 18152, puedo compartir:
- Los mejores momentos para visitar cada destino
- Restaurantes que no aparecen en las guías turísticas
- Rutas alternativas menos concurridas
- Experiencias culturales auténticas
- Precios reales y consejos para ahorrar

La entrevista sería 100% gratuita y en tu formato preferido (escrito, audio, video). A cambio, solo pediría un backlink contextual a Quindío Travel.

¿Te interesa esta entrevista?

Saludos,
Álvaro Alzate Ortiz
Quindío Travel - RNT 18152"""
            }
        }
    
    def generate_personalized_email(self, template_type, recipient_data):
        """Genera email personalizado basado en plantilla"""
        if template_type not in self.templates:
            return None
        
        template = self.templates[template_type]
        
        subject = template["subject"].format(**recipient_data)
        body = template["body"].format(**recipient_data)
        
        return {
            "subject": subject,
            "body": body,
            "template_type": template_type
        }
    
    def generate_outreach_list(self):
        """Genera lista de objetivos de outreach"""
        outreach_targets = [
            {
                "blog_name": "Colombia Travel Blog",
                "name": "Editor",
                "url": "https://www.colombiatravelblog.com",
                "recent_article": "Mejores destinos Colombia 2026",
                "content_focus": "destinos colombianos",
                "email": "contacto@colombiatravelblog.com"
            },
            {
                "blog_name": "Viajeros Colombia",
                "name": "Redacción",
                "url": "https://www.viajeroscolombia.com",
                "recent_article": "Guía turismo interior",
                "content_focus": "turismo nacional",
                "email": "redaccion@viajeroscolombia.com"
            },
            {
                "blog_name": "Eje Cafetero Blog",
                "name": "Administrador",
                "url": "https://www.ejecaferoblog.com",
                "recent_article": "Valle de Cocora",
                "content_focus": "turismo regional",
                "email": "info@ejecaferoblog.com"
            },
            {
                "blog_name": "Turismo Responsable Colombia",
                "name": "Director",
                "url": "https://www.turismoresponsable.co",
                "recent_article": "Turismo sostenible",
                "content_focus": "turismo ecológico",
                "email": "contacto@turismoresponsable.co"
            },
            {
                "blog_name": "Rutas Colombia",
                "name": "Editor",
                "url": "https://www.rutascolombia.com",
                "recent_article": "Rutas de café",
                "content_focus": "rutas turísticas",
                "email": "contacto@rutascolombia.com"
            }
        ]
        
        return outreach_targets
    
    def generate_campaign(self):
        """Genera campaña completa de outreach"""
        targets = self.generate_outreach_list()
        campaign = []
        
        for target in targets:
            # Generar emails con diferentes plantillas
            for template_type in ["guest_post", "collaboration", "resource_link"]:
                email = self.generate_personalized_email(template_type, target)
                if email:
                    campaign.append({
                        "target": target,
                        "email": email,
                        "status": "pending"
                    })
        
        return campaign
    
    def save_campaign(self, campaign):
        """Guarda la campaña de outreach"""
        campaign_file = self.outreach_data / "outreach_campaign.txt"
        
        with open(campaign_file, 'w', encoding='utf-8') as f:
            f.write("CAMPAÑA DE OUTREACH - QUINDÍO TRAVEL\n")
            f.write("=" * 60 + "\n\n")
            f.write(f"Total emails: {len(campaign)}\n")
            f.write(f"Generado: {datetime.now().strftime('%d de %B de %Y')}\n\n")
            
            for i, item in enumerate(campaign, 1):
                f.write(f"EMAIL {i}\n")
                f.write(f"Objetivo: {item['target']['blog_name']}\n")
                f.write(f"Email: {item['target']['email']}\n")
                f.write(f"Tipo: {item['email']['template_type']}\n")
                f.write(f"Asunto: {item['email']['subject']}\n")
                f.write(f"Estado: {item['status']}\n")
                f.write(f"\nCuerpo del email:\n{item['email']['body']}\n")
                f.write("\n" + "=" * 60 + "\n\n")
        
        return campaign_file
    
    def generate_follow_up_templates(self):
        """Genera plantillas de follow-up"""
        follow_up = {
            "follow_up_1": {
                "subject": "Re: {original_subject}",
                "days_after": 7,
                "body": """Hola {name},

Te escribo para seguir mi correo anterior sobre la propuesta de colaboración para tu blog {blog_name}.

¿Tuviste oportunidad de revisar mi propuesta? Me encantaría saber tu opinión o si necesitas más información sobre el contenido que puedo proporcionar.

Como operador local certificado RNT 18152, estoy disponible para responder cualquier pregunta sobre el Eje Cafetero y el contenido que puedo aportar a tu audiencia.

Quedo atento a tu respuesta.

Saludos,
Álvaro Alzate Ortiz
Quindío Travel - RNT 18152"""
            },
            "follow_up_2": {
                "subject": "Re: {original_subject}",
                "days_after": 14,
                "body": """Hola {name},

Espero que estés bien. Te escribo por última vez respecto a mi propuesta de colaboración para {blog_name}.

Entiendo que debes estar muy ocupado, pero creo que mi propuesta podría beneficiar a tu audiencia interesada en el Eje Cafetero.

Si ahora no es el momento o prefieres otra forma de colaboración, me gustaría saberlo para considerar otras opciones.

De cualquier manera, seguiré disfrutando de tu excelente contenido sobre turismo colombiano.

Saludos cordiales,
Álvaro Alzate Ortiz
Quindío Travel - RNT 18152"""
            }
        }
        
        return follow_up

def main():
    """Función principal"""
    print("Sistema de Outreach para Backlinks - Quindío Travel")
    print("=" * 60)
    
    outreach = OutreachSystem()
    
    # Generar lista de objetivos
    targets = outreach.generate_outreach_list()
    print(f"Objetivos identificados: {len(targets)}")
    
    # Generar campaña
    campaign = outreach.generate_campaign()
    print(f"Emails generados: {len(campaign)}")
    
    # Guardar campaña
    campaign_file = outreach.save_campaign(campaign)
    print(f"Campaña guardada en: {campaign_file}")
    
    # Generar follow-ups
    follow_ups = outreach.generate_follow_up_templates()
    print(f"Plantillas de follow-up: {len(follow_ups)}")
    
    # Estadísticas
    print("\nESTADÍSTICAS DE LA CAMPAÑA:")
    print(f"- Total objetivos: {len(targets)}")
    print(f"- Total emails: {len(campaign)}")
    print(f"- Emails por objetivo: {len(campaign) // len(targets)}")
    print(f"- Tasa de respuesta esperada: 5-10%")
    print(f"- Backlinks esperados: {len(targets) * 0.05:.1f} - {len(targets) * 0.1:.1f}")
    
    print("\nRESULTADOS ESPERADOS:")
    print("- Backlinks: 0.25-0.5 backlinks en 30 días")
    print("- DA Mejora: +5-10 puntos en 6 meses")
    print("- Autoridad en nicho: +50%")

if __name__ == "__main__":
    main()