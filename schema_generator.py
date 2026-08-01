#!/usr/bin/env python3
"""
Schema Generator & Validator for Quindío Travel
Genera y valida esquemas JSON-LD Schema.org automáticamente para SEO técnico avanzado.
"""

import json
import re
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional
import hashlib

class QuindioTravelSchemaGenerator:
    """Generador de esquemas JSON-LD especializado para Quindío Travel."""
    
    def __init__(self):
        self.quindio_coords = {"lat": 4.5338, "lng": -75.6811}
        self.quindio_locations = {
            "armenia": {"lat": 4.5351, "lng": -75.6754},
            "salento": {"lat": 4.6378, "lng": -75.5702},
            "filandia": {"lat": 4.6719, "lng": -75.6217},
            "valle_cocora": {"lat": 4.6336, "lng": -75.5532}
        }
        
    def generate_tourist_trip_schema(self, plan_data: Dict) -> str:
        """Genera esquema TouristTrip completo y validado."""
        
        location = plan_data.get("location", "Quindío")
        coords = self.quindio_locations.get(location.lower().replace(" ", "_"), self.quindio_coords)
        
        schema = {
            "@context": "https://schema.org",
            "@type": "TouristTrip",
            "name": plan_data["name"],
            "description": plan_data["description"],
            "touristType": plan_data.get("tourist_types", ["Cultural", "Adventure"]),
            "duration": plan_data.get("duration", "P4D"),
            "startDate": plan_data.get("start_date", datetime.now().strftime("%Y-%m-%d")),
            "endDate": plan_data.get("end_date", (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")),
            "provider": {
                "@type": "TravelAgency",
                "name": "Quindío Travel",
                "telephone": "+57-317-4426044",
                "url": "https://quindiotravel.com.co",
                "priceRange": "$$ - $$$",
                "image": "https://quindiotravel.com.co/logo_quindio_travel.png",
                "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": "4.9",
                    "reviewCount": "1200",
                    "bestRating": "5",
                    "worstRating": "1"
                }
            },
            "location": {
                "@type": "Place",
                "name": location,
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": coords["lat"],
                    "longitude": coords["lng"]
                },
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": location,
                    "addressRegion": "Quindío",
                    "addressCountry": {
                        "@type": "Country",
                        "name": "CO"
                    }
                }
            },
            "offers": {
                "@type": "Offer",
                "name": f"Plan {plan_data['name']}",
                "description": plan_data["description"],
                "price": plan_data["price"],
                "priceCurrency": "COP",
                "availability": "https://schema.org/InStock",
                "validFrom": datetime.now().strftime("%Y-%m-%d"),
                "validThrough": plan_data.get("valid_until", "2026-12-31"),
                "seller": {
                    "@type": "TravelAgency",
                    "name": "Quindío Travel",
                    "telephone": "+57-317-4426044"
                },
                "inventoryLevel": {
                    "@type": "QuantitativeValue",
                    "value": "15",
                    "unitText": "spaces"
                }
            },
            "amenityFeature": [
                {
                    "@type": "LocationFeatureSpecification",
                    "name": amenity,
                    "value": "True"
                } for amenity in plan_data.get("amenities", [])
            ],
            "potentialAction": {
                "@type": "ReserveAction",
                "target": {
                    "@type": "EntryPoint",
                    "urlTemplate": f"https://wa.me/573174426044?text=Hola, estoy interesado en {plan_data['name'].replace(' ', '%20')}",
                    "actionPlatform": "http://schema.org/MobileWebPlatform"
                },
                "result": {
                    "@type": "Reservation",
                    "name": plan_data["name"]
                }
            },
            "additionalProperty": [
                {
                    "@type": "PropertyValue",
                    "name": "RNT",
                    "value": "18152"
                }
            ]
        }
        
        return json.dumps(schema, indent=2, ensure_ascii=False)
    
    def validate_schema_structure(self, schema_json: str) -> Dict:
        """Valida estructura básica del schema."""
        try:
            schema = json.loads(schema_json)
            
            validation = {
                "valid": True,
                "errors": [],
                "warnings": []
            }
            
            # Validaciones básicas
            if "@context" not in schema:
                validation["valid"] = False
                validation["errors"].append("Missing @context")
            
            if "@type" not in schema:
                validation["valid"] = False
                validation["errors"].append("Missing @type")
            
            if schema.get("@type") not in ["TouristTrip", "TravelAgency", "Product", "Place"]:
                validation["warnings"].append(f"Unusual @type: {schema.get('@type')}")
            
            if "name" not in schema:
                validation["valid"] = False
                validation["errors"].append("Missing required field: name")
            
            if "image" not in schema and schema.get("@type") == "TravelAgency":
                validation["valid"] = False
                validation["errors"].append("TravelAgency requires image field")
            
            return validation
            
        except json.JSONDecodeError as e:
            return {
                "valid": False,
                "errors": [f"Invalid JSON: {str(e)}"],
                "warnings": []
            }
    
    def inject_schema_to_html(self, html_file: str, schema_json: str, output_file: str = None):
        """Inyecta schema JSON-LD en archivo HTML."""
        html_path = Path(html_file)
        
        if not html_path.exists():
            raise FileNotFoundError(f"HTML file not found: {html_file}")
        
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Insertar schema antes de </head>
        schema_block = f'\n    <script type="application/ld+json">\n{schema_json}\n    </script>\n'
        html_with_schema = re.sub(r'(</head>)', f'{schema_block}\\1', html_content)
        
        output_path = Path(output_file) if output_file else html_path
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_with_schema)
        
        return str(output_path)

def main():
    """Función principal para ejecutar el generador."""
    generator = QuindioTravelSchemaGenerator()
    
    # Plan de ejemplo
    plan_data = {
        "name": "Expedición Premium Eje Cafetero",
        "description": "Tour exclusivo 4D/3N con guía privada, experiencias VIP y acceso premium a los mejores destinos del Quindío",
        "price": 1890000,
        "valid_until": "2026-12-31",
        "location": "Salento",
        "tourist_types": ["Lujo", "Parejas", "Cultural"],
        "amenities": ["WiFi", "Desayuno incluido", "Guía certificado", "Transporte privado", "Spa"],
        "duration": "P4D"
    }
    
    # Generar schema
    print("Generando schema JSON-LD...")
    schema = generator.generate_tourist_trip_schema(plan_data)
    
    # Validar schema
    print("Validando estructura...")
    validation = generator.validate_schema_structure(schema)
    
    if validation["valid"]:
        print("Schema validado correctamente")
        
        # Guardar schema en archivo
        schema_file = Path("generated_schema.json")
        with open(schema_file, 'w', encoding='utf-8') as f:
            f.write(schema)
        
        print(f"Schema guardado en {schema_file}")
        
        print("Home oficial consolidado en index.html")
        print("No se genera index_enhanced.html para evitar duplicidad de homepage")
    else:
        print("Errores de validación:")
        for error in validation["errors"]:
            print(f"  - {error}")
        
        for warning in validation["warnings"]:
            print(f"  Advertencia: {warning}")

if __name__ == "__main__":
    main()
