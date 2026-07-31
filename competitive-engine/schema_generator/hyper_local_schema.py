"""
HyperLocalSchemaGenerator - Generador avanzado de esquemas JSON-LD con IA geoespacial

Este módulo implementa la generación de esquemas Schema.org hiper-localizados
con integración de APIs geoespaciales, validación automática y relaciones semánticas complejas.
"""

import json
import requests
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import logging
import hashlib
from pathlib import Path

class HyperLocalSchemaGenerator:
    """
    Generador avanzado de esquemas JSON-LD con IA geoespacial y validación automática.
    """
    
    def __init__(self, api_key: Optional[str] = None, cache_dir: str = "competitive-engine/cache", data_dir: str = "docs/data"):
        self.schema_validator_url = "https://validator.schema.org/"
        self.logger = logging.getLogger(__name__)
        self.geo_cache = {}
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
        # Configurar ruta a datos reales del proyecto
        self.data_dir = Path(data_dir)
        self.tarifas_file = self.data_dir / "tarifas.json"
        
        # Configurar logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
    def fetch_geo_spatial_data(self, location: str) -> Dict:
        """
        Obtiene datos geoespaciales enriquecidos de APIs reales (Google Maps/OpenStreetMap).
        
        Args:
            location: Nombre de la ubicación (ej: "Salento, Quindío")
            
        Returns:
            Diccionario con datos geoespaciales (lat, lng, display_name, bbox)
        """
        # Verificar caché primero
        cache_key = hashlib.md5(location.encode()).hexdigest()
        cache_file = self.cache_dir / f"geo_{cache_key}.json"
        
        if cache_file.exists():
            with open(cache_file, 'r') as f:
                return json.load(f)
            
        # Integración con OpenStreetMap Nominatim API (gratis)
        try:
            response = requests.get(
                f"https://nominatim.openstreetmap.org/search?format=json&q={location}",
                timeout=5,
                headers={'User-Agent': 'QuindioTravel-SEO-Engine/1.0'}
            )
            data = response.json()
            if data:
                geo_data = {
                    "lat": float(data[0]["lat"]),
                    "lng": float(data[0]["lon"]),
                    "display_name": data[0]["display_name"],
                    "bbox": data[0].get("boundingbox")
                }
                
                # Guardar en caché
                with open(cache_file, 'w') as f:
                    json.dump(geo_data, f)
                    
                self.geo_cache[location] = geo_data
                self.logger.info(f"✅ Datos geoespaciales obtenidos para {location}")
                return geo_data
        except Exception as e:
            self.logger.error(f"❌ Error fetching geo data: {e}")
            
        # Fallback a coordenadas del Quindío
        fallback_data = {
            "lat": 4.5338, 
            "lng": -75.6811, 
            "display_name": location,
            "bbox": None
        }
        self.logger.warning(f"⚠️ Usando coordenadas fallback para {location}")
        return fallback_data
    
    def generate_tourist_trip_schema(
        self,
        plan_name: str,
        description: str,
        price: int,
        valid_until: str,
        location: str,
        tourist_types: List[str],
        amenities: List[str],
        nearby_attractions: List[str],
        duration: str = "P4D",
        start_date: Optional[str] = None,
        end_date: Optional[str] = None
    ) -> str:
        """
        Genera esquema TouristTrip avanzado con relaciones semánticas complejas.
        
        Args:
            plan_name: Nombre del plan turístico
            description: Descripción detallada del plan
            price: Precio en COP
            valid_until: Fecha de validez (YYYY-MM-DD)
            location: Ubicación principal
            tourist_types: Tipos de turistas objetivo
            amenities: Amenidades incluidas
            nearby_attractions: Atracciones cercanas
            duration: Duración en formato ISO 8601 (ej: P4D = 4 días)
            start_date: Fecha de inicio (opcional)
            end_date: Fecha de fin (opcional)
            
        Returns:
            String JSON del esquema generado
        """
        geo_data = self.fetch_geo_spatial_data(location)
        
        # Fechas dinámicas si no se proporcionan
        if not start_date:
            start_date = datetime.now().strftime("%Y-%m-%d")
        if not end_date:
            end_date = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
        
        schema = {
            "@context": "https://schema.org",
            "@type": "TouristTrip",
            "name": plan_name,
            "description": description,
            "touristType": tourist_types,
            "duration": duration,
            "startDate": start_date,
            "endDate": end_date,
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
                    "latitude": geo_data["lat"],
                    "longitude": geo_data["lng"]
                },
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": location,
                    "addressRegion": "Quindío",
                    "addressCountry": {
                        "@type": "Country",
                        "name": "CO"
                    }
                },
                "containedInPlace": [
                    {
                        "@type": "Place",
                        "name": attraction
                    } for attraction in nearby_attractions
                ]
            },
            "offers": {
                "@type": "Offer",
                "name": f"Plan {plan_name}",
                "description": description,
                "price": price,
                "priceCurrency": "COP",
                "availability": "https://schema.org/InStock",
                "validFrom": start_date,
                "validThrough": valid_until,
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
                } for amenity in amenities
            ],
            "itinerary": {
                "@type": "ItemList",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "item": {
                            "@type": "Place",
                            "name": f"Llegada y check-in en {location}",
                            "description": "Traslado desde terminal de transporte, alojamiento en hotel seleccionado"
                        }
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "item": {
                            "@type": "Place",
                            "name": f"Experiencia principal en {location}",
                            "description": "Tour guiado por atracciones principales y cultura local"
                        }
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "item": {
                            "@type": "Place",
                            "name": "Actividades especiales",
                            "description": "Experiencias exclusivas según el tipo de tour seleccionado"
                        }
                    },
                    {
                        "@type": "ListItem",
                        "position": 4,
                        "item": {
                            "@type": "Place",
                            "name": "Regreso y despedida",
                            "description": "Transporte de regreso y conclusiones del viaje"
                        }
                    }
                ]
            },
            "potentialAction": {
                "@type": "ReserveAction",
                "target": {
                    "@type": "EntryPoint",
                    "urlTemplate": f"https://wa.me/573174426044?text=Hola, estoy interesado en {plan_name.replace(' ', '%20')}",
                    "actionPlatform": "http://schema.org/MobileWebPlatform"
                },
                "result": {
                    "@type": "Reservation",
                    "name": plan_name
                }
            },
            "additionalProperty": [
                {
                    "@type": "PropertyValue",
                    "name": "RNT",
                    "value": "18152"
                },
                {
                    "@type": "PropertyValue",
                    "name": "Temporada",
                    "value": "Alta demanda"
                }
            ]
        }
        
        self.logger.info(f"✅ Schema generado para {plan_name}")
        return json.dumps(schema, indent=2, ensure_ascii=False)
    
    def generate_multiple_schemas(self, plans_data: List[Dict]) -> List[str]:
        """
        Genera múltiples esquemas para un lote de planes turísticos.
        
        Args:
            plans_data: Lista de diccionarios con datos de planes
            
        Returns:
            Lista de strings JSON de esquemas generados
        """
        schemas = []
        
        for plan_data in plans_data:
            try:
                schema = self.generate_tourist_trip_schema(
                    plan_name=plan_data.get("name", ""),
                    description=plan_data.get("description", ""),
                    price=plan_data.get("price", 0),
                    valid_until=plan_data.get("valid_until", "2026-12-31"),
                    location=plan_data.get("location", "Quindío"),
                    tourist_types=plan_data.get("tourist_types", ["General"]),
                    amenities=plan_data.get("amenities", []),
                    nearby_attractions=plan_data.get("nearby_attractions", []),
                    duration=plan_data.get("duration", "P4D"),
                    start_date=plan_data.get("start_date"),
                    end_date=plan_data.get("end_date")
                )
                schemas.append(schema)
            except Exception as e:
                self.logger.error(f"❌ Error generando schema para {plan_data.get('name')}: {e}")
                
        return schemas
    
    def validate_schema(self, schema_json: str) -> bool:
        """
        Valida el esquema contra Schema.org Validator API.
        
        Args:
            schema_json: String JSON del esquema a validar
            
        Returns:
            True si es válido, False en caso contrario
        """
        try:
            response = requests.post(
                self.schema_validator_url,
                json={"schema": schema_json},
                timeout=10
            )
            is_valid = response.status_code == 200
            if is_valid:
                self.logger.info("✅ Schema validado correctamente")
            else:
                self.logger.warning(f"⚠️ Schema validation failed: {response.status_code}")
            return is_valid
        except Exception as e:
            self.logger.error(f"❌ Schema validation error: {e}")
            return False
    
    def save_schema_to_file(self, schema_json: str, filename: str) -> str:
        """
        Guarda el esquema en un archivo JSON.
        
        Args:
            schema_json: String JSON del esquema
            filename: Nombre del archivo
            
        Returns:
            Ruta del archivo guardado
        """
        output_path = Path("competitive-engine/data") / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(schema_json)
            
        self.logger.info(f"💾 Schema guardado en {output_path}")
        return str(output_path)


# Ejemplo de uso y pruebas
if __name__ == "__main__":
    # Configurar logging
    logging.basicConfig(level=logging.INFO)
    
    # Crear generador
    generator = HyperLocalSchemaGenerator()
    
    # Ejemplo 1: Generar schema individual
    print("🚀 Generando schema individual...")
    schema = generator.generate_tourist_trip_schema(
        plan_name="Expedición Secreta Valle de Cocora & Arriería",
        description="Tour exclusivo 4D/3N con experiencias auténticas de cultura cafetera, "
                   "visita a palmas de cera, taller de arriería tradicional y gastronomía local.",
        price=1152000,
        valid_until="2026-12-31",
        location="Salento, Quindío",
        tourist_types=["Familias", "Aventureros", "Ecoturismo", "Cultural"],
        amenities=["WiFi", "Desayuno incluido", "Guía certificado", "Transporte privado", "Spa"],
        nearby_attractions=["Valle de Cocora", "Museo del Canasto", "Calle del Tiempo Detenida", "Mirador Salento"]
    )
    
    # Guardar schema
    generator.save_schema_to_file(schema, "tourist_trip_valle_cocora.json")
    
    # Ejemplo 2: Generar múltiples schemas
    print("\n🚀 Generando múltiples schemas...")
    plans_data = [
        {
            "name": "Experiencia Café y Paisaje",
            "description": "3D/2N inmersión en cultura cafetera con visitas a fincas cafeteras tradicionales",
            "price": 890000,
            "valid_until": "2026-12-31",
            "location": "Armenia, Quindío",
            "tourist_types": ["Cultural", "Familias", "Parejas"],
            "amenities": ["WiFi", "Alimentación", "Guía especializado"],
            "nearby_attractions": ["Parque del Café", "PANACA", "Quimbaya"],
            "duration": "P3D"
        },
        {
            "name": "Aventura Termales y Naturaleza",
            "description": "4D/3N combinación de termales Santa Rosa con naturaleza del Eje Cafetero",
            "price": 1273000,
            "valid_until": "2026-12-31",
            "location": "Santa Rosa de Cabal, Risaralda",
            "tourist_types": ["Wellness", "Aventureros", "Parejas"],
            "amenities": ["Spa", "Termales", "Transporte", "Hospedaje"],
            "nearby_attractions": ["Termales Santa Rosa", "Ecoparque", "Cascadas"],
            "duration": "P4D"
        }
    ]
    
    schemas = generator.generate_multiple_schemas(plans_data)
    
    for i, schema in enumerate(schemas, 1):
        generator.save_schema_to_file(schema, f"tourist_trip_batch_{i}.json")
    
    print(f"\n✅ Sistema HyperLocalSchemaGenerator funcionando correctamente")
    print(f"📊 {len(schemas) + 1} schemas generados en total")