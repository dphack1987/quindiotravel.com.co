"""
SchemaABTestSystem - Sistema de A/B Testing para Schema.org

Este módulo implementa sistema de testing A/B para esquemas Schema.org
con análisis de rendimiento en SERPs y optimización automática.
"""

import json
import hashlib
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import logging
from pathlib import Path
from collections import defaultdict
import random

class SchemaABTestSystem:
    """
    Sistema de A/B testing para esquemas Schema.org con 
    análisis de rendimiento en SERPs.
    """
    
    def __init__(self, data_dir: str = "competitive-engine/data"):
        self.schema_variants = {}
        self.performance_metrics = {}
        self.user_assignments = {}
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        # Configurar logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
        # Configuración de testing
        self.test_config = {
            'traffic_split': 0.5,  # 50% del tráfico para cada variante
            'min_sample_size': 100,  # Mínimo de usuarios por variante
            'confidence_level': 0.95,  # Nivel de confianza para significancia
            'test_duration_days': 14  # Duración del test en días
        }
        
    def create_schema_variant(
        self, 
        base_schema: dict, 
        variant_name: str, 
        modifications: dict,
        description: str = ""
    ) -> str:
        """
        Crea variante de schema con modificaciones específicas.
        
        Args:
            base_schema: Schema base (diccionario)
            variant_name: Nombre descriptivo de la variante
            modifications: Diccionario de modificaciones (soporta notación de puntos)
            description: Descripción de la variante
            
        Returns:
            ID único de la variante
        """
        variant_schema = base_schema.copy()
        
        # Aplicar modificaciones profundas
        for key, value in modifications.items():
            if '.' in key:
                # Soporte para notación de puntos (ej: "provider.name")
                keys = key.split('.')
                current = variant_schema
                for k in keys[:-1]:
                    current = current.setdefault(k, {})
                current[keys[-1]] = value
            else:
                variant_schema[key] = value
        
        # Generar ID único para la variante
        variant_id = hashlib.md5(
            json.dumps(variant_schema, sort_keys=True).encode()
        ).hexdigest()[:8]
        
        self.schema_variants[variant_id] = {
            'name': variant_name,
            'description': description,
            'schema': variant_schema,
            'created_at': datetime.now().isoformat(),
            'modifications': modifications,
            'is_active': True
        }
        
        self.logger.info(f"✅ Variante creada: {variant_name} (ID: {variant_id})")
        
        return variant_id
    
    def assign_user_to_variant(self, user_id: str, test_id: str = None) -> Optional[str]:
        """
        Asigna usuario a variante de schema de forma consistente.
        
        Args:
            user_id: Identificador único del usuario
            test_id: ID del test específico (opcional)
            
        Returns:
            ID de la variante asignada o None
        """
        variant_ids = [vid for vid, v in self.schema_variants.items() if v['is_active']]
        
        if not variant_ids:
            self.logger.warning("⚠️ No hay variantes activas disponibles")
            return None
        
        # Asignación consistente basada en hash del usuario
        user_hash = int(hashlib.md5(f"{user_id}_{test_id}".encode()).hexdigest(), 16)
        variant_index = user_hash % len(variant_ids)
        
        assigned_variant = variant_ids[variant_index]
        
        # Guardar asignación
        if user_id not in self.user_assignments:
            self.user_assignments[user_id] = {}
        
        self.user_assignments[user_id][test_id or 'default'] = assigned_variant
        
        return assigned_variant
    
    def track_performance(
        self, 
        variant_id: str, 
        metric: str, 
        value: float,
        timestamp: Optional[str] = None
    ):
        """
        Registra métricas de rendimiento para cada variante.
        
        Args:
            variant_id: ID de la variante
            metric: Nombre de la métrica (ctr, position, impressions, etc.)
            value: Valor numérico de la métrica
            timestamp: Timestamp opcional (default: ahora)
        """
        if variant_id not in self.performance_metrics:
            self.performance_metrics[variant_id] = {}
            
        if metric not in self.performance_metrics[variant_id]:
            self.performance_metrics[variant_id][metric] = []
        
        timestamp = timestamp or datetime.now().isoformat()
        
        self.performance_metrics[variant_id][metric].append({
            'value': value,
            'timestamp': timestamp
        })
        
        self.logger.debug(f"📊 Métrica registrada: {variant_id} - {metric} = {value}")
    
    def track_user_interaction(
        self, 
        user_id: str, 
        variant_id: str, 
        interaction_type: str,
        metadata: dict = None
    ):
        """
        Registra interacción de usuario con una variante.
        
        Args:
            user_id: ID del usuario
            variant_id: ID de la variante
            interaction_type: Tipo de interacción (click, view, conversion, etc.)
            metadata: Metadatos adicionales (opcional)
        """
        interaction = {
            'user_id': user_id,
            'variant_id': variant_id,
            'interaction_type': interaction_type,
            'timestamp': datetime.now().isoformat(),
            'metadata': metadata or {}
        }
        
        # Guardar en métricas específicas
        metric_key = f"{interaction_type}_count"
        self.track_performance(variant_id, metric_key, 1)
        
        self.logger.debug(f"👤 Interacción registrada: {user_id} - {interaction_type}")
    
    def calculate_variant_statistics(self, variant_id: str) -> Dict:
        """
        Calcula estadísticas descriptivas para una variante.
        
        Args:
            variant_id: ID de la variante
            
        Returns:
            Diccionario con estadísticas
        """
        if variant_id not in self.performance_metrics:
            return {}
        
        stats = {}
        metrics = self.performance_metrics[variant_id]
        
        for metric_name, values in metrics.items():
            if not values:
                continue
                
            numeric_values = [v['value'] for v in values]
            
            stats[metric_name] = {
                'count': len(numeric_values),
                'mean': sum(numeric_values) / len(numeric_values),
                'min': min(numeric_values),
                'max': max(numeric_values),
                'total': sum(numeric_values)
            }
        
        return stats
    
    def analyze_results(self, test_id: str = None) -> Dict:
        """
        Analiza resultados del A/B testing y recomienda ganador.
        
        Args:
            test_id: ID del test específico (opcional)
            
        Returns:
            Diccionario con análisis completo de resultados
        """
        results = {}
        
        for variant_id, variant_data in self.schema_variants.items():
            if not variant_data['is_active']:
                continue
                
            stats = self.calculate_variant_statistics(variant_id)
            
            results[variant_id] = {
                'name': variant_data['name'],
                'description': variant_data['description'],
                'statistics': stats,
                'avg_ctr': stats.get('ctr', {}).get('mean', 0),
                'avg_position': stats.get('position', {}).get('mean', 0),
                'total_impressions': stats.get('impressions', {}).get('total', 0),
                'total_clicks': stats.get('click_count', {}).get('total', 0),
                'conversions': stats.get('conversion_count', {}).get('total', 0)
            }
        
        # Encontrar ganador basado en CTR
        if results:
            winner = max(results.items(), key=lambda x: x[1]['avg_ctr'])
            
            # Calcular mejora
            ctr_values = [r['avg_ctr'] for r in results.values()]
            min_ctr = min(ctr_values) if ctr_values else 0
            improvement = winner[1]['avg_ctr'] - min_ctr
            
            analysis = {
                'test_id': test_id or 'default',
                'timestamp': datetime.now().isoformat(),
                'results': results,
                'winner': winner[0],
                'winner_name': winner[1]['name'],
                'winner_stats': winner[1]['statistics'],
                'improvement': improvement,
                'improvement_percent': (improvement / min_ctr * 100) if min_ctr > 0 else 0,
                'total_variants': len(results),
                'recommendation': self._generate_recommendation(results, winner)
            }
        else:
            analysis = {
                'test_id': test_id or 'default',
                'timestamp': datetime.now().isoformat(),
                'results': results,
                'recommendation': 'No hay suficientes datos para análisis'
            }
        
        self.logger.info(f"✅ Análisis completado: {len(results)} variantes analizadas")
        
        return analysis
    
    def _generate_recommendation(self, results: Dict, winner: Tuple) -> str:
        """
        Genera recomendación basada en resultados del test.
        
        Args:
            results: Resultados del test
            winner: Tupla (variant_id, variant_data) del ganador
            
        Returns:
            Recomendación textual
        """
        if not results:
            return "No hay suficientes datos para generar recomendación"
        
        winner_id, winner_data = winner
        if 'improvement' in winner_data:
            improvement = winner_data['improvement']
        else:
            min_ctr = min([r['avg_ctr'] for r in results.values()]) if results else 0
            improvement = winner_data.get('avg_ctr', 0) - min_ctr
        
        if improvement > 0.05:  # 5% de mejora
            return f"Recomendamos implementar la variante '{winner_data['name']}' - Mejora del {improvement:.2%} en CTR"
        elif improvement > 0.02:  # 2% de mejora
            return f"La variante '{winner_data['name']}' muestra mejora leve ({improvement:.2%}) - Considerar implementación"
        else:
            return "No hay diferencia significativa entre variantes - Continuar con schema actual"
    
    def generate_schema_code(self, variant_id: str) -> str:
        """
        Genera código HTML/JSON-LD para una variante específica.
        
        Args:
            variant_id: ID de la variante
            
        Returns:
            String con código JSON-LD listo para insertar
        """
        if variant_id not in self.schema_variants:
            self.logger.error(f"❌ Variante {variant_id} no encontrada")
            return ""
        
        schema = self.schema_variants[variant_id]['schema']
        json_ld = json.dumps(schema, indent=2, ensure_ascii=False)
        
        html_code = f'<script type="application/ld+json">\n{json_ld}\n</script>'
        
        return html_code
    
    def conclude_test(self, test_id: str = None, winning_variant_id: str = None):
        """
        Concluye un test A/B y desactiva variantes perdedoras.
        
        Args:
            test_id: ID del test
            winning_variant_id: ID de la variante ganadora (opcional, auto-detecta si None)
        """
        analysis = self.analyze_results(test_id)
        
        if winning_variant_id is None:
            winning_variant_id = analysis.get('winner')
        
        # Desactivar todas las variantes excepto la ganadora
        for variant_id in self.schema_variants:
            if variant_id != winning_variant_id:
                self.schema_variants[variant_id]['is_active'] = False
                self.logger.info(f"🔴 Variante desactivada: {variant_id}")
        
        if winning_variant_id:
            self.logger.info(f"🏆 Test concluido. Variante ganadora: {winning_variant_id}")
    
    def export_test_results(self, test_id: str = None, filename: str = "ab_test_results.json") -> str:
        """
        Exporta resultados del test a archivo JSON.
        
        Args:
            test_id: ID del test
            filename: Nombre del archivo de salida
            
        Returns:
            Ruta del archivo exportado
        """
        analysis = self.analyze_results(test_id)
        
        output_path = self.data_dir / filename
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(analysis, f, indent=2, ensure_ascii=False)
        
        self.logger.info(f"💾 Resultados exportados a {output_path}")
        
        return str(output_path)
    
    def get_variant_by_name(self, variant_name: str) -> Optional[str]:
        """
        Busca variante por nombre.
        
        Args:
            variant_name: Nombre de la variante
            
        Returns:
            ID de la variante o None
        """
        for variant_id, variant_data in self.schema_variants.items():
            if variant_data['name'] == variant_name:
                return variant_id
        return None


# Ejemplo de uso y pruebas
if __name__ == "__main__":
    # Configurar logging
    logging.basicConfig(level=logging.INFO)
    
    # Crear sistema de A/B testing
    ab_system = SchemaABTestSystem()
    
    # Schema base TouristTrip
    base_tourist_trip = {
        "@context": "https://schema.org",
        "@type": "TouristTrip",
        "name": "Plan Eje Cafetero",
        "description": "Tour completo por el Eje Cafetero",
        "provider": {
            "@type": "TravelAgency",
            "name": "Quindío Travel"
        }
    }
    
    print("🚀 Creando variantes de Schema para A/B testing...")
    
    # Variante 1: Con aggregateRating
    variant_1 = ab_system.create_schema_variant(
        base_tourist_trip,
        "Con aggregateRating",
        {"aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "1200"}},
        "Schema con calificaciones agregadas para prueba social"
    )
    
    # Variante 2: Con review array
    variant_2 = ab_system.create_schema_variant(
        base_tourist_trip,
        "Con review array",
        {"review": [{"@type": "Review", "author": {"@type": "Person", "name": "Cliente Satisfecho"}, "reviewRating": {"@type": "Rating", "ratingValue": "5"}}]},
        "Schema con reviews individuales para mayor detalle"
    )
    
    # Variante 3: Con precio urgente
    variant_3 = ab_system.create_schema_variant(
        base_tourist_trip,
        "Con precio urgente",
        {"offers": {"@type": "Offer", "price": "1152000", "priceCurrency": "COP", "availability": "https://schema.org/LimitedAvailability"}},
        "Schema con disponibilidad limitada para urgencia"
    )
    
    # Simular asignación de usuarios
    print("\n🚀 Simulando asignación de usuarios...")
    for i in range(10):
        user_id = f"user_{i}"
        assigned = ab_system.assign_user_to_variant(user_id)
        print(f"   {user_id} → {assigned}")
    
    # Simular métricas de rendimiento
    print("\n🚀 Simulando métricas de rendimiento...")
    import random
    
    for variant_id in ab_system.schema_variants:
        # Simular CTR diferentes
        base_ctr = 0.05 if variant_id == variant_1 else 0.04
        for _ in range(50):
            ctr = base_ctr + random.uniform(-0.01, 0.01)
            ab_system.track_performance(variant_id, "ctr", ctr)
        
        # Simular posiciones
        for _ in range(50):
            position = random.uniform(1, 10)
            ab_system.track_performance(variant_id, "position", position)
        
        # Simular impresiones
        for _ in range(10):
            impressions = random.randint(100, 1000)
            ab_system.track_performance(variant_id, "impressions", impressions)
    
    # Analizar resultados
    print("\n🚀 Analizando resultados del A/B test...")
    analysis = ab_system.analyze_results()
    
    print(f"\n📊 Resultados del A/B Test:")
    print(f"   Variante ganadora: {analysis['winner_name']}")
    print(f"   Mejora en CTR: {analysis['improvement_percent']:.2f}%")
    print(f"   Recomendación: {analysis['recommendation']}")
    
    # Exportar resultados
    print("\n🚀 Exportando resultados...")
    ab_system.export_test_results()
    
    # Generar código para la variante ganadora
    print("\n🚀 Generando código para variante ganadora...")
    winner_code = ab_system.generate_schema_code(analysis['winner'])
    print(f"   Código generado: {len(winner_code)} caracteres")
    
    print(f"\n✅ Sistema SchemaABTestSystem funcionando correctamente")