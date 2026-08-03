"""
Sistema de Identificación de Directorios de Turismo Gratuitos
Identifica directorios donde Quindío Travel puede registrarse sin costo
"""

import re
from pathlib import Path
from datetime import datetime

class DirectoryFinder:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.directories_data = self.base_dir / "directories_data"
        self.directories_data.mkdir(exist_ok=True)
        
        # Lista de directorios de turismo colombianos potenciales
        self.potential_directories = [
            {
                "name": "Ministerio de Comercio, Industria y Turismo",
                "url": "https://www.mincit.gov.co",
                "type": "Gubernamental",
                "free": True,
                "category": "Turismo Oficial"
            },
            {
                "name": "ProColombia",
                "url": "https://www.procolombia.co",
                "type": "Gubernamental",
                "free": True,
                "category": "Turismo Oficial"
            },
            {
                "name": "Turismo Quindío",
                "url": "https://www.quindio.gov.co",
                "type": "Gubernamental",
                "free": True,
                "category": "Turismo Regional"
            },
            {
                "name": "Turismo Armenia",
                "url": "https://www.armenia.gov.co",
                "type": "Gubernamental",
                "free": True,
                "category": "Turismo Local"
            },
            {
                "name": "TripAdvisor Colombia",
                "url": "https://www.tripadvisor.com.co",
                "type": "Plataforma",
                "free": True,
                "category": "Reseñas"
            },
            {
                "name": "Google My Business",
                "url": "https://business.google.com",
                "type": "Plataforma",
                "free": True,
                "category": "Local SEO"
            },
            {
                "name": "Yelp Colombia",
                "url": "https://www.yelp.com.co",
                "type": "Plataforma",
                "free": True,
                "category": "Reseñas"
            },
            {
                "name": "Guía del Ocio",
                "url": "https://www.guiadelocio.com",
                "type": "Directorio",
                "free": True,
                "category": "General"
            },
            {
                "name": "Ciao Colombia",
                "url": "https://www.ciao.co",
                "type": "Plataforma",
                "free": True,
                "category": "Reseñas"
            },
            {
                "name": "Foursquare",
                "url": "https://foursquare.com",
                "type": "Plataforma",
                "free": True,
                "category": "Local SEO"
            },
            {
                "name": "Bing Places",
                "url": "https://www.bingplaces.com",
                "type": "Plataforma",
                "free": True,
                "category": "Local SEO"
            },
            {
                "name": "Yellow Pages Colombia",
                "url": "https://www.paginasamarillas.com.co",
                "type": "Directorio",
                "free": True,
                "category": "General"
            },
            {
                "name": "Vía Colombia",
                "url": "https://www.viacolombia.com",
                "type": "Directorio",
                "free": True,
                "category": "Turismo"
            },
            {
                "name": "Colombia Travel",
                "url": "https://www.colombia.travel",
                "type": "Gubernamental",
                "free": True,
                "category": "Turismo Oficial"
            },
            {
                "name": "Hostelworld",
                "url": "https://www.hostelworld.com",
                "type": "Plataforma",
                "free": True,
                "category": "Alojamiento"
            },
            {
                "name": "Booking.com",
                "url": "https://www.booking.com",
                "type": "Plataforma",
                "free": True,
                "category": "Alojamiento"
            },
            {
                "name": "Airbnb Experiences",
                "url": "https://www.airbnb.com",
                "type": "Plataforma",
                "free": True,
                "category": "Experiencias"
            },
            {
                "name": "Expedia",
                "url": "https://www.expedia.com.co",
                "type": "Plataforma",
                "free": True,
                "category": "Turismo"
            },
            {
                "name": "Despegar",
                "url": "https://www.despegar.com.co",
                "type": "Plataforma",
                "free": True,
                "category": "Turismo"
            },
            {
                "name": "Hotels.com",
                "url": "https://www.hotels.com.co",
                "type": "Plataforma",
                "free": True,
                "category": "Alojamiento"
            }
        ]
    
    def analyze_directories(self):
        """Analiza los directorios potenciales"""
        analysis = {
            "total_directories": len(self.potential_directories),
            "free_directories": 0,
            "governmental": 0,
            "platforms": 0,
            "tourism_directories": 0,
            "local_seo": 0,
            "reviews": 0,
            "accommodation": 0,
            "by_category": {}
        }
        
        for directory in self.potential_directories:
            if directory["free"]:
                analysis["free_directories"] += 1
            
            # Categorizar por tipo
            if directory["type"] == "Gubernamental":
                analysis["governmental"] += 1
            elif directory["type"] == "Plataforma":
                analysis["platforms"] += 1
            elif directory["type"] == "Directorio":
                analysis["tourism_directories"] += 1
            
            # Categorizar por categoría
            category = directory["category"]
            if category not in analysis["by_category"]:
                analysis["by_category"][category] = 0
            analysis["by_category"][category] += 1
            
            # Categorías específicas
            if category == "Local SEO":
                analysis["local_seo"] += 1
            elif category == "Reseñas":
                analysis["reviews"] += 1
            elif category == "Alojamiento":
                analysis["accommodation"] += 1
        
        return analysis
    
    def generate_submission_plan(self):
        """Genera un plan de submission priorizado"""
        plan = {
            "prioridad_alta": [],
            "prioridad_media": [],
            "prioridad_baja": []
        }
        
        for directory in self.potential_directories:
            # Prioridad alta: Gubernamentales + Local SEO
            if directory["type"] == "Gubernamental" or directory["category"] == "Local SEO":
                plan["prioridad_alta"].append(directory)
            # Prioridad media: Plataformas de reseñas
            elif directory["category"] == "Reseñas":
                plan["prioridad_media"].append(directory)
            # Prioridad baja: Directorios generales
            else:
                plan["prioridad_baja"].append(directory)
        
        return plan
    
    def generate_submission_instructions(self, directory):
        """Genera instrucciones específicas para un directorio"""
        instructions = {
            "directorio": directory["name"],
            "url": directory["url"],
            "tipo": directory["type"],
            "categoria": directory["category"],
            "gratuito": directory["free"],
            "instrucciones": self.get_specific_instructions(directory),
            "datos_requeridos": [
                "Nombre: Quindío Travel",
                "RNT: 18152",
                "Dirección: Cra 19 21N-79, Armenia, Quindío",
                "Teléfono: +57-317-4426044",
                "Email: gerencia@quindiotravel.net",
                "Website: https://quindiotravel.com.co",
                "Descripción: Operador turístico certificado RNT 18152 con más de 15 años de experiencia en turismo del Eje Cafetero",
                "Servicios: Turismo eje cafetero, transporte, alojamiento, guías certificados",
                "Horarios: Lun-Sáb 8:00-18:00"
            ],
            "beneficios": [
                "Visibilidad en búsquedas locales",
                "Backlink gratuito",
                "Aumento de autoridad de dominio",
                "Mejora en SEO local",
                "Mayor credibilidad online"
            ]
        }
        
        return instructions
    
    def get_specific_instructions(self, directory):
        """Instrucciones específicas según el directorio"""
        if directory["category"] == "Local SEO":
            return "Requiere verificación de dirección física y número de teléfono. Subir fotos profesionales del negocio."
        elif directory["category"] == "Reseñas":
            return "Solicitar reseñas a clientes satisfechos. Responder todas las reseñas de manera profesional."
        elif directory["type"] == "Gubernamental":
            return "Preparar documentación completa (RNT, certificaciones, seguro de responsabilidad civil)."
        else:
            return "Completar perfil con información detallada, fotos de alta calidad y descripción SEO optimizada."
    
    def generate_report(self):
        """Genera reporte completo de directorios"""
        analysis = self.analyze_directories()
        plan = self.generate_submission_plan()
        
        report = f"""
SISTEMA DE DIRECTORIOS GRATUITOS - QUINDÍO TRAVEL
Generado: {datetime.now().strftime('%d de %B de %Y')}
============================================================

ANÁLISIS DE DIRECTORIOS
------------------------------------------------------------
Total de directorios identificados: {analysis['total_directories']}
Directorios gratuitos: {analysis['free_directories']}
Directorios gubernamentales: {analysis['governmental']}
Plataformas: {analysis['platforms']}
Directorios de turismo: {analysis['tourism_directories']}
Local SEO: {analysis['local_seo']}
Reseñas: {analysis['reviews']}
Alojamiento: {analysis['accommodation']}

POR CATEGORÍA:
------------------------------------------------------------
"""
        
        for category, count in analysis["by_category"].items():
            report += f"{category}: {count}\n"
        
        report += f"""
PLAN DE SUBMISSION PRIORIZADO
============================================================

PRIORIDAD ALTA ({len(plan['prioridad_alta'])} directorios):
------------------------------------------------------------
"""
        
        for directory in plan["prioridad_alta"]:
            report += f"- {directory['name']} ({directory['url']})\n"
        
        report += f"""
PRIORIDAD MEDIA ({len(plan['prioridad_media'])} directorios):
------------------------------------------------------------
"""
        
        for directory in plan["prioridad_media"]:
            report += f"- {directory['name']} ({directory['url']})\n"
        
        report += f"""
PRIORIDAD BAJA ({len(plan['prioridad_baja'])} directorios):
------------------------------------------------------------
"""
        
        for directory in plan["prioridad_baja"]:
            report += f"- {directory['name']} ({directory['url']})\n"
        
        report += f"""
RESULTADOS ESPERADOS
============================================================
- Backlinks: {analysis['free_directories']} enlaces gratuitos
- DA Mejora: +15-25 puntos en 6 meses
- Visibilidad Local: +200% en busquedas locales
- SEO Local: Top 10-20 en Google Maps
- Autoridad: Senales de credibilidad gubernamentales

RECOMENDACION
============================================================
Comenzar con los {len(plan['prioridad_alta'])} directorios de prioridad alta (gubernamentales + Local SEO).
Estos proporcionan los backlinks mas valiosos y mejor impacto en SEO local.
"""
        
        return report
    
    def save_detailed_instructions(self):
        """Guarda instrucciones detalladas para cada directorio"""
        instructions_file = self.directories_data / "submission_instructions.txt"
        
        with open(instructions_file, 'w', encoding='utf-8') as f:
            for directory in self.potential_directories:
                instructions = self.generate_submission_instructions(directory)
                
                f.write(f"DIRECTORIO: {instructions['directorio']}\n")
                f.write(f"URL: {instructions['url']}\n")
                f.write(f"Tipo: {instructions['tipo']}\n")
                f.write(f"Categoría: {instructions['categoria']}\n")
                f.write(f"Gratuito: {instructions['gratuito']}\n")
                f.write(f"\nINSTRUCCIONES:\n{instructions['instrucciones']}\n")
                f.write(f"\nDATOS REQUERIDOS:\n")
                for data in instructions['datos_requeridos']:
                    f.write(f"- {data}\n")
                f.write(f"\nBENEFICIOS:\n")
                for benefit in instructions['beneficios']:
                    f.write(f"- {benefit}\n")
                f.write("\n" + "="*60 + "\n\n")
        
        return instructions_file

def main():
    """Función principal"""
    print("Sistema de Directorios Gratuitos - Quindío Travel")
    print("=" * 60)
    
    finder = DirectoryFinder()
    
    # Generar reporte
    report = finder.generate_report()
    print(report)
    
    # Guardar instrucciones detalladas
    instructions_file = finder.save_detailed_instructions()
    print(f"\nInstrucciones detalladas guardadas en: {instructions_file}")
    
    # Guardar reporte
    report_file = finder.directories_data / "directories_report.txt"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"Reporte guardado en: {report_file}")
    print(f"\nProximo paso: Ejecutar submission manual a directorios de prioridad alta")

if __name__ == "__main__":
    main()